
    
.MODEL SMALL  
.STACK 100H    
.DATA 
    VAR1 DB 2

.CODE
    MAIN PROC   
        MOV AX, @DATA
        MOV DS , AX  
        
        MOV AX,81 
        MOV BX,1 
        MOV CL,0
        
        FOR:
        CMP AX,0
        JE EXIT
            SUB AX ,BX
            ADD BX,2
            INC CL 
        JMP FOR 
        EXIT:
        
        
        MOV AH,2
        MOV DL, CL 
        ADD DL,48
        INT 21H 
        
        
        
       
        
        MOV AH,4CH
        INT 21H    
    MAIN ENDP        
END MAIN