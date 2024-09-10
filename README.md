# norway-nin-lookup
Bruteforce the NiN (National Identity Number) by Full Name and DOB

### National Identity Number Format
```
220676 123 45
│      │   │
│      │   └ Control/Verification Numbers  
│      └ Identification Number
└ Birthdate (DDMMYY)
```
**Identification Number** / Even numbers are female and odd are males
**Control Number** / Used to verify the validity of the number

### Explanation
The first 6 number is the DOB and leaves us with only needing to guess the last 5 digits (100,000 combinations) due to NINs having the feature of differentiating males against females by the last digit of the **Identification Number** halving the possible number to 50,000. 
