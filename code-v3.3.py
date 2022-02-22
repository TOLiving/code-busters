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
  if char == 'd':
    enciphered_list.append('f')
  if char == 'e':
    enciphered_list.append('g')
  if char == 'f':
    enciphered_list.append('h')
  if char == 'g':
    enciphered_list.append('i')
  if char == 'h':
    enciphered_list.append('j')
  if char == 'i':
    enciphered_list.append('k')
  if char == 'j':
    enciphered_list.append('l')
  if char == 'k':
    enciphered_list.append('m')
  if char == 'l':
    enciphered_list.append('n')
  if char == 'm':
    enciphered_list.append('o')
  if char == 'n':
    enciphered_list.append('p')
  if char == 'o':
    enciphered_list.append('q')
  if char == 'p':
    enciphered_list.append('r')
  if char == 'q':
    enciphered_list.append('s')
  if char == 'r':
    enciphered_list.append('t')
  if char == 's':
    enciphered_list.append('u')
  if char == 't':
    enciphered_list.append('v')
  if char == 'u':
    enciphered_list.append('w')
  if char == 'v':
    enciphered_list.append('x')
  if char == 'w':
    enciphered_list.append('y')
  if char == 'x':
    enciphered_list.append('z')
  if char == 'y':
    enciphered_list.append('a')
  if char == 'z':
    enciphered_list.append('b')
  if char == 'A':
    enciphered_list.append('C')
  if char == 'B':
    enciphered_list.append('D')
  if char == 'C':
    enciphered_list.append('E')
  if char == 'D':
    enciphered_list.append('F')
  if char == 'E':
    enciphered_list.append('G')
  if char == 'F':
    enciphered_list.append('H')
  if char == 'G':
    enciphered_list.append('I')
  if char == 'H':
    enciphered_list.append('J')
  if char == 'I':
    enciphered_list.append('K')
  if char == 'J':
    enciphered_list.append('L')
  if char == 'K':
    enciphered_list.append('M')
  if char == 'L':
    enciphered_list.append('N')
  if char == 'M':
    enciphered_list.append('O')
  if char == 'N':
    enciphered_list.append('P')
  if char == 'O':
    enciphered_list.append('Q')
  if char == 'P':
    enciphered_list.append('R')
  if char == 'Q':
    enciphered_list.append('S')
  if char == 'R':
    enciphered_list.append('T')
  if char == 'S':
    enciphered_list.append('U')
  if char == 'T':
    enciphered_list.append('V')
  if char == 'U':
    enciphered_list.append('W')
  if char == 'V':
    enciphered_list.append('X')
  if char == 'W':
    enciphered_list.append('Y')
  if char == 'X':
    enciphered_list.append('Z')
  if char == 'Y':
    enciphered_list.append('A')
  if char == 'Z':
    enciphered_list.append('B')
    
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
