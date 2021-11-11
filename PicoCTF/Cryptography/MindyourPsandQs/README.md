# Mind your Ps and Qs
## Description
<br>

In RSA, a small e value can be problematic, but what about N? Can you decrypt this? [values](https://mercury.picoctf.net/static/12d820e355a7775a2c9129b2622a7eb6/values)


## Solve
<br>

Use [factordb](http://factordb.com/index.php?query=1422450808944701344261903748621562998784243662042303391362692043823716783771691667) to calculate the n's factor.

```n =  2159947535959146091116171018558446546179<40> · 658558036833541874645521278345168572231473<42>```

Use the knowledge below to write the Python program to decode this cipher.

```run RSA.py```

> [Crypto.Util.number](https://pycryptodome.readthedocs.io/en/latest/src/util/util.html) 


## Resources
### RSA (Rivest-Shamir-Adleman)
- [explain by geeksforgeeks](https://www.geeksforgeeks.org/rsa-algorithm-cryptography/)
    - asymmetric
        - Works on two different keys.
        - eg. Public Key and Private Key
            1. A client (for example browser) sends its public key to the server and requests for some data.
            2. The server encrypts the data using client’s public key and sends the encrypted data.
            3. Client receives this data and decrypts it.
    - RSA keys can be typically **1024** or **2048** bits long.
        - Experts believe that 1024 bit keys could be broken in the near future. But till now it seems to be an infeasible task.

    - C
        - Value of the cipher message (Integer)
        - ciphertext
    - E
        - Public Key E (Usually E=65537)
    - N
        - Public Key value (Integer)
        - P * Q
        - [factordb](http://factordb.com/index.php)
    - D
        - Private Key value (Integer)
    - P
        - Factor 1 (**prime** number)
    - Q
        - Factor 2 (**prime** number)
    - Φ
        - Intermediate value Phi (Integer)
    - M
        -  M = c^d mod n

- [explain by di-mgt](https://www.di-mgt.com.au/rsa_alg.html)
- [tool: RsaCtfTool](https://github.com/Ganapati/RsaCtfTool)
- [online example](http://www.isg.rhul.ac.uk/static/msc/teaching/ic2/demo/43.htm)
- [Does RSA work for any message M?](https://crypto.stackexchange.com/questions/1004/does-rsa-work-for-any-message-m)

## How to calculate public key and private key under RSA scenario?
1. calculate 'n', n= p * q
2. Calaulate the coprime (relatively prime) that's smaller than 'n'.
> Φ(n)= (p - 1)(q - 1)
3. Choose an integer 'e' (**Public Key**).
> Φ(n) > e > 1

> e and Φ(n) are coprime
4. Calculate 'd' (**Private Key**).
> remainder of e * d / Φ(n) is **1**

> d = e - 1 mod Φ(n)

- explain mod:
    - 4 mod 2 = 0, 5 mod 2 = 1
    - remainder of 4 / 2 is 0, thus 4 mod 2 = 0
    - remainder of 5 / 2 is 0, thus 5 mod 2 = 1


Public Key: KU = {e, n}
Private Key: KR = {d, n}


