INCLUDE "EMU8086.INC"
.MODEL SMALL
.STACK 200H
.DATA
.CODE  
    MAIN PROC
        MOV AX,@DATA
        MOV DS,AX
        
        XOR BL,BL
        
        FOR:
        MOV AH,1
        INT 21H    
        
        CMP AL, 0DH   
        
        JE EXIT  
        
        SUB AL,48
         
        SHL BL,1
        OR BL,AL 
        
        JMP FOR   
        EXIT:
        
        PRINTN 
        
        MOV CX,8
        
        START:
            RCL BL ,1
            JC PRINT_ONE
                MOV AH,2
                MOV DL,'0' 
                
                INT 21H 
                JMP LAST
            PRINT_ONE:  
                MOV AH,2
                MOV DL,'1' 
        
                INT 21H
            lAST:
        LOOP START 
        
       
        
    
        MOV AH,4CH
        INT 21H
    MAIN ENDP
END MAIN
