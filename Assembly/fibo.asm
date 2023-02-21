;MD. BABUL HASAN (NOYON)
    ;CSE 16, PSTU
    
.MODEL SMALL  
.STACK 100H    
.DATA 
    ARR DB 100 DOB(0)  
    NUM DB 0

.CODE
    MAIN PROC   
        MOV AX, @DATA
        MOV DS , AX
        
        XOR BX,BX 
        MOV CX,10
        
        MOV ARR[BX], 0
        INC BX
        MOV ARR[BX],1 
        
        FOR2: 
        
            XOR DH,DH
            ADD DH, ARR[BX]
            ADD DH, ARR[BX-1]  
            INC BX
            MOV ARR[BX],DH
            
        
        LOOP FOR2  
        
        MOV CX,10
        
        XOR BX,BX
        FOR:
           MOV AH,2
           MOV DL,ARR[BX]  
           ADD DL,48
           INT 21H
           INC BX
        LOOP FOR

        MOV AH,4CH
        INT 21H    
    MAIN ENDP        
END MAIN