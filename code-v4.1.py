#my code is almost done being written I'm storing the almost finished project here, and polishing things up on the online editor as I go
#input from the user that will determine what alphabet the plaintext will be enciphered in
n = input("What alphabet would you like to encrypt your message in? Type one uppercase letter.")
#making the previous input usable(instead of a range of 65-60, I now use a range of 0-25
alphabet_key = ord(n) - 65
#input from the user to create the plaintext that will be encrypted
plaintext = input('Please type the message you would like to encrypt')
#empty list to store the enciphered message
enciphered_list = []

#loop to encrypt my message and store the values in enciphered_list
#lowercase alphabet goes from 97-122
#uppercase letters go from 65- 90
#function to encrypt the plaintext in whatever alphabet I want to encrypt my message in 
def encrypt(str, y):
    for char in plaintext:
        #using the equation x = y + c because it is the easiest equation to use for caesar alphabet encryption
        #c is the plaintext character
        c = ord(char)
        #y is the amount of shifts I want to do on the alphabet
        #x is the encrypted letter
        x = c + y
        if c == 32:
            #tells the code to ignore running the code after the continue statement. I want to use this for spaces so that ! doesn't appear in my list 
            continue
        if (x > 90) and (c >= 65) and (c <= 90):
            x = x - 26
        if (x > 122):
            x = x - 26
        enumber = chr(x)
        enciphered_list.append(enumber)
encrypt(plaintext, alphabet_key)
#recording the length of the enciphered message to use the factorization function
enciphered_len = len(enciphered_list)
#empty list to store the factors
factors = []
#empty list to turn the integer values of the list into strings in a list
str_factors =[]

#function used to find the factors of the cipher's message length
def print_factors(x):
  for i in range(1, x + 1):
    if x % i == 0:
      #storing the values of the factor
      factors.append(i)
      
#using the factorization function on the encrypted message
print_factors(enciphered_len)
#small loop that converts individual integers into string in a list
for i in factors:
  str_factors.append(str(i))
#new list to display str_list more cleanly in the interface/terminal
compounded_list = ', '.join(str_factors)

def split_string(string, n):
    div_str=len(string) / n
    k = 0
    for i in string:
        if k % div_str == 0:
            print(end=' ')
        print(i, end='')
        k += 1

#Code that will ask the user for an integer input to break the enciphered message into same length word groups
len_split = int(input("Please select how many groups you would like to split your message into.\n" + compounded_list))

#loop to run the split_string function when my input matches an integer in my factors list
for i in factors:
    if len_split == i:
        split_string(enciphered_list, i)
