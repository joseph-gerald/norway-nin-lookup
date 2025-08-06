# norway-nin-lookup
Bruteforce the NIN (National Identity Number) by Full Name and DOB

### National Identity Number Format
```
220676 123 45
│      │   │
│      │   └ Control/Verification Numbers  
│      └ Identification Number (odd = men / even = women)
└ Birthdate (DDMMYY)
```
**Identification Number** / Even numbers are female and odd are males <br>
**Control Number** / Used to verify the validity of the number

### Explanation
The first 6 number is the DOB and leaves us with only needing to guess the last 5 digits (100,000 combinations) due to NINs having the feature of differentiating males against females by the last digit of the **Identification Number** halving the possible number to 50,000. 

> [!NOTE]
> Update: the NIN system has checksums to prevent mistyping similiar to credit cards by using their checksum only 827 of the 100,000 agnostic combinations are valid with 412 combinations being male and 415 being female




### Proof Of Concept
The ***POC*** uses [pid.norid.no](https://pid.norid.no) to verify the NIN but requires you to solve a ReCaptchaV2 challenge for every 3 lookups/checks.

### Cost
Using a popular captcha solving service it would cost 0.8$ per 1k tokens or 0.4$ per 1k image recognitions. Given 50,000 looksups are needed we can divided 50k by 3 due to only needing to solve every 3 lookups. This means around 16k captchas need to solved, meaning the cost would be  `16.6*0.8 = 12.8$` or with image recognition `16.6*0.4 = 6.4$` to scan each DOB and gender range.

> [!NOTE]
> Update: With the new numbers of 412 combinations being male and 415 being female the new numbers are `0.412 / 3 * 0.8 = 0.11$` and `0.412 / 3 * 0.4 = 0.05$` for males.

# Summary
| Conditions | Possible Combinations | Price |
| --------- | ----------- | ----------- |
| Known: DOB | 827 | **0.827 / 3 * 0.8 = 0.22$** |
| Known: DOB & Sex | 412 or 415 | **0.412 / 3 * 0.8 = 0.11$** |
