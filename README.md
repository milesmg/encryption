# pgp_encryption
 
The two files in this code are meant to complement each other, enabling the user to
run a PGP ("pretty good privacy") encryption program. 

PGP, or public key cryptography, relies on large prime numbers. Equipped with two large primes, a user can generate a public and private key. The user's public key is used by senders to encrypt messages, which the initial user can then decrypt with their private key.

The strength of this encryption lies in the size of the two large primes that generated the key pair. It is very easy to multiply large prime numbers, but very hard to factor the product of two large primes. This 'one-directionality' is the basis for modern cryptography.

The encryptAndDecrypt.py file contains a variable called message. Upon being run, the program encrypts the message using the public key provided. The program then decrypts the message using the accompanying private key. The encryption/decryption segments can be run separately, with a few adjustments.

The lucasTest.py file runs the Lucas Test for Primality on a given list of prime numbers. The Lucas Test, like public key cryptography, relies on modular arithmetic, this time to check whether a number is prime. By plugging the output of this program into itself, you can generate larger and larger primes, and can use these primes to generate key pairs.

Good luck!