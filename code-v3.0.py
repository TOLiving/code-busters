#This is a more advanced version of the program I want to make, so I will add the previous versions later

#input from the user to create the plaintext that will be encrypted
message = input('Please type the message you would like to encrypt')
#empty list to store the enciphered message
encrypted_list = []

#loop to encrypt my message and store the values in encrypted_list  NEEDS TO BE SHORTENED LATER ON
for char in message:
  if char == 'a':
    encrypted_list.append('c')
  if char == 'b':
    encrypted_list.append('d')
  if char == 'c':
    encrypted_list.append('e')
    
#recording the length of the enciphered message to use the factorization function
emessage_len = len(encrypted_list)
#empty list to store the factors
factors = []
#empty list to turn the integer values of the list into strings in a list
str_factors =[]

#function used to find the factors of the cipher's message length
def print_factors(x):
  for i in range(1, x + 1):
    if x % i ==0:
      #storing the values of the factor
      factors.append(i)
      
#using the factorization function on the encrypted message
print_factors(emessage_len)
#small loop that converts individual integers into string in a list
for int in factors:
  str_factors.append(str(int))
#new list to display str_list more cleanly in the interface/terminal
compounded_list = ', '.join(str_factors)

#string that will ask the user for an integer input to break the enciphered message into similar length word groups
new_input = input("Please select how many groups you would like to split your message into\n" + compounded_list)
#this loop makes sure that the input number is a number found within the cipher factors
#there is something wrong with the organization of this loop, so I'll have to fix it in a bit
for char in str_factors:
  if char != new_input:
    print("Whoops, that number doesn't seem to be a factor of the cipher length, please run the code again :)")
    #break stops the code from running multiple times and printing the message multiple times
    
  elif char == new_input:
    print('complete')
    break