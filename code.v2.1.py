#second iteration; a lot of what I added I ended up scrapping because I ran into several problems  I found easier ways to write the code anyways lol
# message = input("Please type the message you would like to encrypt\n")
# print(len(message))
# encrypted_letters = []
# for char in message:
#     if char == "a":
#         encrypted_letters.append("j")
#     if char == "b":
#         encrypted_letters.append("k")
#     if char == "c":
#         encrypted_letters.append("l")
#     if char == "d":
#         encrypted_letters.append("m")
#     if char == "e":
#         encrypted_letters.append("n")
#     if char == "f":
#         encrypted_letters.append("o")
#     if char == "g":
#         encrypted_letters.append("p")
#     if char == "h":
#         encrypted_letters.append("q")
#     if char == "i":
#         encrypted_letters.append("r")
#     if char == "j":
#         encrypted_letters.append("s")
#     if char == "k":
#         encrypted_letters.append("t")
#     if char == "l":
#         encrypted_letters.append("u")
#     if char == "m":
#         encrypted_letters.append("v")
#     if char == "n":
#         encrypted_letters.append("w")
#     if char == "o":
#         encrypted_letters.append("x")
#     if char == "p":
#         encrypted_letters.append("y")
#     if char == "q":
#         encrypted_letters.append("z")
#     if char == "r":
#         encrypted_letters.append("a")
#     if char == "s":
#         encrypted_letters.append("b")
#     if char == "t":
#         encrypted_letters.append("c")
#     if char == "u":
#         encrypted_letters.append("d")
#     if char == "v":
#         encrypted_letters.append("e")
#     if char == "w":
#         encrypted_letters.append("f")
#     if char == "x":
#         encrypted_letters.append("g")
#     if char == "y":
#         encrypted_letters.append("h")
#     if char == "z":
#         encrypted_letters.append("i")
#     if char == "A":
#         encrypted_letters.append("J")
#     if char == "B":
#         encrypted_letters.append("K")
#     if char == "C":
#         encrypted_letters.append("L")
#     if char == "D":
#         encrypted_letters.append("M")
#     if char == "E":
#         encrypted_letters.append("N")
#     if char == "F":
#         encrypted_letters.append("O")
#     if char == "G":
#         encrypted_letters.append("P")
#     if char == "H":
#         encrypted_letters.append("Q")
#     if char == "I":
#         encrypted_letters.append("R")
#     if char == "J":
#         encrypted_letters.append("S")
#     if char == "K":
#         encrypted_letters.append("T")
#     if char == "L":
#         encrypted_letters.append("U")
#     if char == "M":
#         encrypted_letters.append("V")
#     if char == "N":
#         encrypted_letters.append("W")
#     if char == "O":
#         encrypted_letters.append("X")
#     if char == "P":
#         encrypted_letters.append("Y")
#     if char == "Q":
#         encrypted_letters.append("Z")
#     if char == "R":
#         encrypted_letters.append("A")
#     if char == "S":
#         encrypted_letters.append("B")
#     if char == "T":
#         encrypted_letters.append("C")
#     if char == "U":
#         encrypted_letters.append("D")
#     if char == "V":
#         encrypted_letters.append("E")
#     if char == "W":
#         encrypted_letters.append("F")
#     if char == "X":
#         encrypted_letters.append("G")
#     if char == "Y":
#         encrypted_letters.append("H")
#     if char == "Z":
#         encrypted_letters.append("I")
# encrypted_code = ''.join(encrypted_letters)
# print(encrypted_code)


#might want to make this whole process a function instead so that I can use it in other code or just to practice making functions
def divisible_string(string, lst):
    str_size = len(string)

    k=0
    for i in string:
        if k % str_size == 0:
            lst.append(k)
            k = k + 1
message = "asdfghjkl"
create = []
divisible_string(message, create)
print(create)

# divisible_numbers = []
# k = 1
# string = encrypted_code
# string_len = len(encrypted_code)
# for i in string:
#     if string_len % k == 0:
#         divisible_numbers.append(k)
#         k += 1
# str_divisible_numbers = str(divisible_numbers)
# print('How many groups would you like your message to be grouped in?\n' + str_divisible_numbers)



