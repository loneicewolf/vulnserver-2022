# vulnserver-2022
My (various and different) latest attempts on the VULNSERVER.

- ### attempt 1: just crashing it
  -  (choosing a random huge number, say `5000`)

- ### attempt 2: overwriting EIP
  -  (a bit less than `1`, say EIP overwrite control)

- ### attempt 3: predicting registers
  - (begin with small value, move up until it crashed, but not overwrote anything, now - predict by **first try** to overwrite EDI, EBP, then EIP)


- ### attempt 4 and onward: modifying the memory of other registers from the previous (now controlled) registers
  - jump, call and go to's
  - assembly
  - shellcode




