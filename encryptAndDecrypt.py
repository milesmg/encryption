
print("ENCRYPTING:")
print()

#the following code turns the message into a list of long numbers according to their ASCII numbers
def numDigits(a):
  return(len(str(a)))


#finds gcd of two integers
def gcd(a, b):
    if a < b:
        return (gcd(b, a))
    else:
        # R = remainder
        R = a % b
        if R == 0:
            return (b)
        else:
            return (gcd(b, R))

pieceLength = 12

#two large primes; in modern RSA algorithms, 
# these can be more than 600 digits long
p = 81257823079
q = 9120923689


# m is one half of the public and private keys
m = p*q

# phi(m) is euler's totient fxn = #{n | n < m, gcd(n,m) = 1, n is an integer}
phi = (p-1)*(q-1)

# k is the other half of the public key. 
# Once you've generated it, you're going to want to save it and 
# use the same one so people can send you messages
def findK(m):
    k = random.randint(1, m - 1)
    if k != None and gcd(m, k) == 1 and gcd(phi, k) == 1:
        return(k)
    else:
        return (findK(m))
k = 17024138347492331909

# to encrypt/decrypt, you'll have to break a message 
# up into pieces of a pre-agreed upon length.
pieceLength = numDigits(m)-9



print("public key used (k,m) = (" + str(k) + "," + str(m) + ")")

message = "Four score and seven years ago our fathers brought forth on this continent, a new nation, conceived in Liberty, and dedicated to the proposition that all men are created equal. Now we are engaged in a great civil war, testing whether that nation, or any nation so conceived and so dedicated, can long endure. We are met on a great battle-field of that war. We have come to dedicate a portion of that field, as a final resting place for those who here gave their lives that that nation might live. It is altogether fitting and proper that we should do this. But, in a larger sense, we can not dedicate—we can not consecrate—we can not hallow—this ground. The brave men, living and dead, who struggled here, have consecrated it, far above our poor power to add or detract. The world will little note, nor long remember what we say here, but it can never forget what they did here. It is for us the living, rather, to be dedicated here to the unfinished work which they who fought here have thus far so nobly advanced. It is rather for us to be here dedicated to the great task remaining before us—that from these honored dead we take increased devotion to that cause for which they gave the last full measure of devotion—that we here highly resolve that these dead shall not have died in vain—that this nation, under God, shall have a new birth of freedom—and that government of the people, by the people, for the people, shall not perish from the earth." 


print("message = " + message)
print()
messageLength = len(message)

#first we need to chop the message up into pieces. We can make these
#  pieces of any size, so long as their ASCII integer versions
# are less than m and we've agreed upon that size with our decryptor

# One of the challenge we run into is that some letters have a 
# two digit ascii key, and some have a three digit key. Luckily we can just
# 10x these numbers and solve the problem
def setUpNumMessage():
  # eachCharToNum will take a single character and turn it into a number
  # (though it's stored as a string for convenience)
  eachCharToNum = ''
  for x in message:
    # ord returns Unicode code point
    if numDigits(ord(x)) == 2:
        eachCharToNum += str(ord(x)) + '0'
    else:
        eachCharToNum += str(ord(x))
  whereInArray = 0
  whereInPiece = 0

  # here we make an empty array to hold the pieces of our string.
  numMessage = [''] * (1+(len(eachCharToNum)//(pieceLength)))

  # now we iterate through the whole message, adding individual digits to 
  # the array of strings numMessage. The variable whereInArray keeps track 
  # of which piece of the array we're adding to; the variable whereInPiece
  # keeps track of how many digits each piece is (should be <= pieceLength)
  for y in eachCharToNum:
    if y == '0':
      if whereInPiece == 0:
        if whereInArray == 0:
          print("Please Enter A Message That Does Not Begin With Zero")
        else:
          # rather than add a leading 0 to a piece that will get lost in 
          # translation, we simply tack it on to the end of the previous piece.
          numMessage[whereInArray-1] +=y
      else:
        numMessage[whereInArray] +=y
        whereInPiece+=1
    else:
      numMessage[whereInArray] += y
      whereInPiece+=1
    if whereInPiece == pieceLength :
      whereInPiece=0
      whereInArray+=1
  return(numMessage)

numMessage = setUpNumMessage()
# clean up numMessage for any unwanted junk
while numMessage[len(numMessage)-1] == '':
  numMessage.remove('')

# change each entry in numMessage from a string to an int
indexer = 0
while indexer < len(numMessage) :
    numMessage[indexer] = int(numMessage[indexer])
    indexer+=1


#print out the numbers to be encrypted
combined = ''
for x in numMessage:
   combined += str(x)
#print("numMessage = " + combined)


# now we encrypt the message using modular arithmetic and successive squaring
def successive_squaring(a, b, m):
    result = 1
    base = a % m
    
    while b > 0:
        if b % 2 == 1:  # If the current bit is 1
            result = (result * base) % m
        base = (base * base) % m  # Square the base
        b = b // 2  # Shift right by 1 bit
    
    return result

#builds the final cypher
finalCypher = ''
for piece in numMessage :
   finalCypher += str(successive_squaring(piece,k,m)) + 'gap'


print("Your Encrypted Message Is = " + (finalCypher))

# END ENCRYPTION
#################################################################################3
# BEGIN DECRYPTION

import random

print()
print("DECRYPTING:")
print()


print("public key used (k,m) = (" + str(k) + "," + str(m) + ")")
#print("pieceLength = " + str(pieceLength))

      
#your public key is (m,k). Feel free to publish it so people can encrypt messages for you.

# PUT THE CYPHER HERE
cypher = finalCypher
print()
#print("cypher = " + (cypher))


#now for decryption. We need to solve an exponential congruence using our private key, phi, 
# from earlier. Without phi (i.e. without the prime factors of m, half of our public key) 
# decrypting our message could take hundreds of thousands to billions of years 
# depending on how large our primes were.


#   we need to find integers u,v that solve the equation k*u + phi*v = 1
def kthRoot(a, b):
  dividend = []
  divisor = []
  remainder = []
  quotient = []
  index=0
  if a < b:
      return (kthRoot(b, a))
  else:
    r=None
    while(r!=1):
      dividend.append(a)
      divisor.append(b)
      quotient.append(a//b)
      r = dividend[index] - (divisor[index] * quotient[index])
      remainder.append(r)
      a=divisor[index]
      b=remainder[index]
      index+=1
    index-=1
    x=1
    y=quotient[index]
    jndex = 0
    while index > 0:
      if jndex % 2 == 0:
        x = x + y * quotient[index-1]
      else:
        y = y + x * quotient[index-1]
      index-=1
      jndex+=1
    return [x,y]
    
# reduces
def checkRoots(roots):
  if k > phi:
    print("inequality issue")
  else: 
    first = phi*roots[0]
    second = k*roots[1]
    if first-second == 1:
      n = 1
      while roots[1] > 0:
        roots[0] -= (n*k)
        roots[1] -= (n*phi)
        n+=1
      roots[1]=-1*roots[1]
      return(roots)
    else:
      roots[1]=-1*roots[1]
      return(roots)

# sets u = non-negative of (u,v) 
def findU(roots):
  u=None
  if roots[0] > 0:
    u=roots[0]
  else:
    u=roots[1]
  return(u)

roots=kthRoot(k,phi)
roots = checkRoots(roots)
u = findU(roots)


#compute b^u mod m where b = a piece of encrypted text of the right length and u = the non-negative root
decryptedNumMessage = ''


def successive_squaring(a, b, m):
    result = 1
    base = a % m
    
    while b > 0:
        if b % 2 == 1:  # If the current bit is 1
            result = (result * base) % m
        base = (base * base) % m  # Square the base
        b = b // 2  # Shift right by 1 bit
    
    return result


# used 'gap' to break up chunks
pieceCache = ''
i = 0
while i < len(cypher):
    if cypher[i:i+3] == 'gap':
        decryptedNumMessage += str(successive_squaring(int(pieceCache),u,m))
        i = i + 3
        pieceCache = ''
    if (i < len(cypher)):
        pieceCache += cypher[i]
    i = i + 1
   
print()

decryptedMessage = ''
messageCache = ''
for num in decryptedNumMessage:
  if int(messageCache + num) > 999:
      if int(messageCache) > 130: 
        messageCache = str(int(messageCache) / 10)
      decryptedMessage += chr(int(float(messageCache)))
      messageCache = num
  else:
    messageCache += num

print("decrypted Message = " + decryptedMessage)