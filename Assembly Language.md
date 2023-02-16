## Assembly Language

### Basic Syntax:

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