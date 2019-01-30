.data
	string: .asciz "Hello World!\n" 
	string_size:
	.set size_of_string, string_size - string
.text
	.global _start

_start:
	mov r0, #1   
	ldr r1, addr_of_string
	mov r2, #size_of_string
	mov r7, #4
	swi #0

_exit:
	mov r7, #1
	swi #0

addr_of_string: .word string 
	
