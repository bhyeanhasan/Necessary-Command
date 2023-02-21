
.MODEL SMALL  
.STACK 100H    
.DATA 

.CODE
    MAIN PROC   
        MOV AX, @DATA
        MOV DS , AX  
        
        MOV BL,5
        MOV CX,4  
        MOV AL, BL
        
        FOR:  
        DEC BL
        MUL BL 
        LOOP FOR   
        
        
        MOV AH,2
        MOV DL,AL 
        INT 21H

        MOV AH,4CH
        INT 21H    
    MAIN ENDP        
END MAIN