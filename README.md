# vulnserver-2022
# note:
this is intended for beginners. I will leave the very deep details and write obvious comments.
this is also not done yet.


My (various and different) latest attempts on the VULNSERVER.

- **attempt 1: just crashing it**
  -  (choosing a random huge number, say `5000`)

-  **attempt 2: overwriting EIP**
  - (a bit less than `1`, say EIP overwrite control)

- **attempt 3: predicting registers**
  - (begin with small value, move up until it crashed, but not overwrote anything, now - predict by **first try** to overwrite EDI, EBP, then EIP)


- **attempt 4 and onward**
  - modifying the memory of other registers from the previous (now controlled) registers
      - jump, call and go to's
      - assembly
      - shellcode




## Screenshots

---

#### EDI Control
![image](https://user-images.githubusercontent.com/68499986/180654506-233bd0bb-06f2-47bd-8073-ae64e5be7932.png)

##### EDI Call Stack
![image](https://user-images.githubusercontent.com/68499986/180655525-6d1c2c68-667b-42e9-bf4d-c1954db69d77.png)


#### EBP Control
![image](https://user-images.githubusercontent.com/68499986/180654725-bb3f5b95-e034-451e-83bd-63a27fd9f46c.png)

#### EIP Control
![image](https://user-images.githubusercontent.com/68499986/180654860-337a0b86-b4ea-4b77-9ba8-e213300a42ab.png)
> `Note how I also overwrote EBP?`
> `let's change that shall we?`


### Bonus: EBP+EIP control together
![image](https://user-images.githubusercontent.com/68499986/180655178-0aa0729b-80e7-476c-bca2-2dfe3beb2f19.png)


![image](https://user-images.githubusercontent.com/68499986/180656116-5052a3e5-fdea-4931-bc91-4f0a869d2027.png)



---


Given one (assuming no ASLR,DEP,.. is present) registers Position(easy to predict given it's minimal overflowing value) (which, again is easy to predict by itself, given 1 reliable amount of '(say) A's' that crash the app5



## Coming soon:
- Writeup (describing basics of my methodology)
- Bibliography
- More References
- Finally the code and a Proof Of Concept (POC) not using Metasploit's msfvenom. and Not radare2 either :) (why not make shellcode from scratch? so you know what you really launch at your poor target..)


### References
- PY COD,E R2
- vulnserver
- https://www.eecg.utoronto.ca/~amza/www.mindsec.com/files/x86regs.html


### Bibliography
- coming soon

