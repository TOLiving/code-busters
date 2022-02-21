#creating this iteration from v3.1 because I'm actually an idiot   
#my problem with the last code was that int used int to define the items in the list[Factors]
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
for john in factors:
  str_factors.append(str(john))
#new list to display str_list more cleanly in the interface/terminal
compounded_list = ', '.join(str_factors)

def grouped_message(string, n):
    div_str=len(string) / n
    k = 0
    for i in string:
        if k % part_size == 0:
            print()
        print(i, end='')
        k += 1

#string that will ask the user for an integer input to break the enciphered message into similar length word groups
input_2 = int(input("Please select how many groups you would like to split your message into.\n" + compounded_list))

