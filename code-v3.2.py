#creating this iteration from v3.1 because I'm actually an idiot   
#my problem with the last code was that in line 32 I overwrote the built in function int, I changed the name int to i to fix my second input not working
#This is a more advanced version of the program I want to make, so I will add the previous versions later

#input from the user to create the plaintext that will be encrypted
plaintext = input('Please type the message you would like to encrypt')
#empty list to store the enciphered message
enciphered_list = []

#loop to encrypt my message and store the values in enciphered_list   NEEDS TO BE SHORTENED LATER ON
for char in plaintext:
  if char == 'a':
    enciphered_list.append('c')
  if char == 'b':
    enciphered_list.append('d')
  if char == 'c':
    enciphered_list.append('e')
    
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
            print()
        print(i, end='')
        k += 1

#Code that will ask the user for an integer input to break the enciphered message into same length word groups
len_split = int(input("Please select how many groups you would like to split your message into.\n" + compounded_list))

#loop to run the split_string function when my input matches an integer in my factors list
for i in factors:
    if len_split == i:
        split_string(enciphered_list, i)
