.MODEL SMALL
.DATA
.CODE
MAIN PROC
    
MOV BX,2
MOV AX ,20

L1: 
MOV DX,0
DIV BX ;M/N
CMP DX,0
JE GCD_FOUND ;BX IS N

MOV AX,BX ;replace M by N
MOV BX,DX ;replace N by R
JMP L1
GCD_FOUND: 

MOV AH,2
mov dl,bl 
add dl,48
int 21h

;-----------------
MOV AH,4CH
INT 21H
MAIN ENDP


END MAIN




