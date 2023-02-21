## Assembly Language

### Basic Syntax:


###### INPUT     =   MOV AH , 1; REG = AL
###### PRINT     =   MOV AH , 2; REG = DL
###### STRING    =   MOV AH, 9; REG = DX


```
key: 27R3VDEFYFX4N0VC3FRTQZX
```
#### Template:
```
    ;MD. BABUL HASAN (NOYON)
    ;CSE 16, PSTU
    
    .MODEL SMALL  
    .STACK 100H    
    .DATA 
        VAR1 DB 'B'
    
    .CODE
        MAIN PROC   
            MOV AX, @DATA
            MOV DS , AX  
    
            MOV AH,4CH
            INT 21H    
        MAIN ENDP        
    END MAIN
```

#### Print:
```
    MOV AH,2
    MOV DL, VAR1
    INT 21H
```
#### Print String:
```
    MOV AH,9
    LEA DX, MESSAGE
    INT 21H
```

#### Input:
```
    MOV AH,1
    INT 21H
```
#### Load Declared Data:
```
    MOV AX, @DATA
    MOV DS , AX
```

#### New Line:
```
    MOV AH,2
    MOV DL, 0AH
    INT 21H
    MOV DL, 0DH
    INT 21H 
```

#### UNCONDITIONAL JUMP:
```
    START:
    PRINTN "JUMP HERE"
    JMP START
```
#### CONDITIONAL JUMP:
```
    MOV AX,0
    MOV BX,5
      
    START:
    CMP AX,BX 
    JE END
    PRINTN "JUMP HERE" 
    INC AX
    JNE START 
    
    END:
```

#### IF ELSE:
```
    MOV AX,5
    MOV BX,5
    
    CMP AX,BX
    
    JL IF
    JG ELSE_IF
    JE ELSE
    
    IF:
    PRINTN "LESS"
    JMP END_IF
    ELSE_IF:
    PRINTN "GREATER"
    JMP END_IF  
    ELSE:
    PRINTN  "EQUAL"
    JMP END_IF
    END_IF:
```

#### LOOP

```
    MOV CX,5
    
    TOP:
        PRINTN "OK"
    LOOP TOP
```
#### REVERSE STRING

```
    XOR CX,CX 
    
    INPUT:
        MOV AH, 1
        INT 21H 
        CMP AL, 0DH
        JE EXIT
        PUSH AX 
        INC CX
        JMP INPUT
    EXIT: 
    
    OUTPUT:
        MOV AH,2
        POP DX
        INT 21H   
    LOOP OUTPUT
```
#### ARRAY

```
    LEA SI, NUMBER 
    MOV CX, 9  
    XOR BX, BX
    
    FOR:    
        MOV DL, NUMBER[BX]
        ADD DL,48  
        MOV AH,2
        INT 21H
        ADD BX,1
    
    LOOP FOR
    
    
    ARR DB 0 DUB(0)


    LEA SI, NUMBER 
    MOV CX, 9
    
    FOR:    
        MOV DL, [SI]
        ADD DL,48  
        MOV AH,2
        INT 21H
        ADD SI,1
    
    LOOP FOR
```