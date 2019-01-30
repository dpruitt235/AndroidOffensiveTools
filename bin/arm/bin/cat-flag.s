.data
        _filename:      .string "/system/bin/sh"
        arg0:           .string "/system/bin/sh"
        arg1:           .string "-c"
        arg2:           .string "cat /data/local/tmp/flag.txt"
        args:
                .word arg0
                .word arg1
                .word arg2
.text
        .global  _start

_start:
        mov r7, #11             @ execve syscall
        ldr r0,=_filename
        ldr r1,=args
        swi #0
_exit:
  mov r7, #1
  swi 0
