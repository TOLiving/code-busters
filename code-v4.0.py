#input from the user to create the plaintext that will be encrypted
plaintext = input('Please type the message you would like to encrypt')
#empty list to store the enciphered message
enciphered_list = []
#x = y + c
#x equals the cipher letter
#y stands for the amount of shifts the letter should go through
#c stands for the plaintext letter
#remember the values go from 0 - 25 or something like that 
#lowercase alphabet goes from 97-122
#uppercase letters go from 65- 90
#string stands for the plaintext string, and y stands for the amount of shifts you want in your code
# let's sat we have 123  if character is greater than 122, and char is greater than 99
def encrypt(str, y):
    for char in plaintext:
        c = ord(char)
        add = c + y
        if (add > 122) and (add >= 99):
            add = add - 26
        
        if (add >= 65) and (add <96):
            add = add - 26
        x = chr(add)
        enciphered_list.append(x)
encrypt(plaintext, 5)
print(enciphered_list)
