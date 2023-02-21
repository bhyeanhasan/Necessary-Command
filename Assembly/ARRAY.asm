
 INCLUDE 'EMU8086.INC'  
.MODEL SMALL  
.STACK 100H    
.DATA 
    ARR DB 1,2,3,4,5
.CODE
    MAIN PROC   
        MOV AX, @DATA
        MOV DS , AX  
       
        ;------------------------  
        MOV CH,0
        MOV CL, 5 
        ;------------------------ 
         
        XOR BX,BX
        
        FOR:
           MOV AH,2
           MOV DL, ARR[BX]
           ADD DL,48
           INT 21H
           INC BX
        LOOP FOR
           

    MAIN ENDP  
    
END MAIN 


