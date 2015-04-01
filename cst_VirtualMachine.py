#
#  Crazy Smart Tanks Game 2011

#
#   description:    Virtual Machine - Interpreter Program                
#   author:         Vlad Palos
#   date:           23.03.2011
#

        

import re

class cst_VirtualMachine:

    def __init__ (self, bF):

        print "VM: Loading brain file : " + bF

        self.brain = bF
        brainFile = open('TankBrains/' + bF , 'r')
        self.brainList = brainFile.readlines()
        brainFile.close()
    
        ## Strips from whitespaces
        x = len( self.brainList ) 
        while ( x > 0 ):
            x -= 1           
            self.brainList[ x ] = self.brainList[ x ].replace ( ' ', '' ) 
            self.brainList[ x ] = self.brainList[ x ].replace ( '\t', '' )                       
            if ( self.brainList[ x ] == '\n' ): 
                self.brainList.pop(x)
    
        ## Dictionary: Code Variables
        self.code_vars = {}

        ## Execution pointer in file
        self.code_ep = -1
        self.code_lines = len( self.brainList )
        self.code_while_p = []

        ## Check actual brain code exists
        if ( len ( self.brainList ) == 0):
            self.yell ( "No brain code here !!!" )

        ## Check closed statements
        self.check_closed()        
        
        ## Patterns
        self.cs_is_funct = re.compile( r'(\w+)\(' )
        self.cs_is_var = re.compile( r'\$(\w+)' )
        self.cs_if = re.compile( r'if\((.+)\)do' )
        self.cs_while = re.compile( r'while\((.+)\)do' )

        ## Debugging : Output precomiled Code
###        print "\n\n\nPrecompiled"
###        print self.code_vars
###        for brainLine in self.brainList:
###            print brainLine,

#####################################################################################################         

    ## Main Panda3d task for tank instance

    def run(self, task):
        if ( self.code_ep < self.code_lines - 1 ):
            self.code_ep+=1
                        
            brainLine = self.brainList[self.code_ep]            
        #    print brainLine
            
            if ( self.exe_if_line( brainLine ) ):
                return task.cont

            if ( self.exe_while_line( brainLine ) ):
                return task.cont

            if ( self.exe_attrib_line( brainLine ) ):
                return task.cont

            if ( self.exe_funct_line( brainLine ) ):        
                return task.cont

        else :
            print "Terminating Brain Script ..."
            return task.done
        

#####################################################################################################         

    ## Check if statements if / while closed correctly

    def check_closed(self):
        pointer = -1
        whilecount = 0
        ifcount = 0
        while ( pointer < self.code_lines -1 ):           
            pointer += 1
            if ( self.brainList[pointer][0:6] == "while(" ):
                whilecount += 1
            if ( self.brainList[pointer][0:8] == "endwhile" ):
                whilecount -= 1
            if ( self.brainList[pointer][0:3] == "if(" ):
                ifcount += 1
            if ( self.brainList[pointer][0:5] == "endif" ):
                ifcount -= 1

        if ( whilecount > 0 ):
            self.yell( "Should close another " + str ( whilecount ) + " \"while\" statements !!!" )
        if ( ifcount > 0 ):
            self.yell( "Should close another " + str ( ifcount ) + " \"if\" statements !!!" )
            

#####################################################################################################         

    ## Execute simple function lines
    ## eg: drive ( 234 )

    def exe_funct_line(self, string):
        m = self.cs_is_funct.match( string )
        if ( m ):
            eval ( self.sub_fv( string ) ) 
            return True
        else:
            return False
            


#####################################################################################################         

    ## Execute while statement lines
    ## eg: while ( ... )    { } 

    def exe_while_line(self, string):

        m = self.cs_while.match( string )
        if ( m != None ):           
            self.code_while_p.append(self.code_ep)
            condition = self.sub_fv ( m.group(1) )
            check = eval( condition )
            if ( check == False ):
                self.code_ep = self.code_while_p.pop()                
                whilecount = 1
                while ( whilecount > 0 ):
                    self.code_ep += 1
                    if ( self.code_ep >= self.code_lines ):                        
                        self.yell ("Unexpected end of file, should close " + str( whilecount ) + " while statements !!!")
                    elif ( self.brainList[self.code_ep][0:6] == "while(" ):
                        whilecount += 1
                    elif ( self.brainList[self.code_ep][0:8] == "endwhile" ):
                        whilecount -= 1
            return True

        else:
            if ( string[0:8] == "endwhile" ):
                if ( len ( self.code_while_p ) == 0 ):
                    self.yell ("endwhile used to early!!!")
                else:
                    self.code_ep = self.code_while_p.pop() - 1 
                return True
            else :  
                return False
                  

#####################################################################################################         

    ## Execute if statement lines
    ## eg: if ( ... )    { } 

    def exe_if_line(self, string):
        if (string[0:5] == "endif" ):
            return True
        m = self.cs_if.match( string )
        if ( m == None ):
            return False
        else:
            condition = self.sub_fv ( m.group(1) )
            check = eval( condition )
            if ( check == False ):
                ifcount = 1
                while ( ifcount > 0 ):
                    self.code_ep += 1
                    if ( self.code_ep >= self.code_lines ):                        
                        self.yell ("Unexpected end of file, should close " + str( ifcount ) + " if statements !!!")
                    elif ( self.brainList[self.code_ep][0:3] == "if(" ):
                        ifcount+=1
                    elif ( self.brainList[self.code_ep][0:5] == "endif" ):
                        ifcount-=1
            return True
    
                
            
#####################################################################################################         

    ## Execute Attrib Lines
    ## eg: var = ...

    def exe_attrib_line(self, string):

        eqpos = string.find('=')

        if ( eqpos == -1 ):
            return False 
        else: 
            rpart = string[ eqpos+1:len(string) ]
            lpart = string[ 0:eqpos ]
            value = 0
            
            # Is left part var ?
            if ( self.cs_is_var.match( lpart ) ):        
               
                # Strips the dollar sign 
                avar = lpart[1:len(lpart)]

                # Declare var if it does't exist ...
                # Not needed ...

#                if ( lpart not in self.code_vars ):
#                    print "doneit" + str ( lpart )
#                    self.code_vars [ avar ] = 0 

                # Replace Functions and Variables
                rpart = self.sub_fv( rpart )

                # Execute Line
                self.code_vars[ avar ] = eval( rpart )
                
                # Replace compiled code, speed-up
                self.brainList[ self.code_ep ] = lpart + '=' + rpart

            else : 
                self.yell ( "Does not compute! Left Part not variable ??? " ) 

            return True

#####################################################################################################

    ## Replace Functions and Variables in string


    def sub_fv (self, string):

        # Replace vars with self.code_vars
        if ( self.cs_is_var.search( string ) ):
            string = self.cs_is_var.sub( 'self.code_vars[\'\g<1>\']', string )

        # Replace functions 
        if ( self.cs_is_funct.search( string ) ):
            # Is allowed ?
            it = self.cs_is_funct.finditer(string)
            for match in it :
                self.is_funct_allowed( match.group()[ 0:-1 ] )
            string = self.cs_is_funct.sub( 'self.\g<1>(', string )
        return string

#####################################################################################################    

    def is_funct_allowed(self, string):
        if (string not in self.code_funct):
            self.yell ( "Cannot find function " + string )

#####################################################################################################         

    def yell(self, string):
        print "Error at line " + str ( self.code_ep ) + " : " + string
        exit (1)


