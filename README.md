# Buffer Overflow for Vulnserver application

Script that performs a buffer overflow on Vulnserver windows application. The script overwrites the SEH handler, to include an arbitrary memory location of our choosing, and lets us execute any code we want(in our case, shellcode that spawns a bind shell)
