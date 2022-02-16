#first iteration of my code; very simple but kinda boring to use
encrypted_letters = []
message = input('Type the message you want to encrypt.\n')
for char in message:
    if char == "a":
        encrypted_letters.append("j")
    if char == "b":
        encrypted_letters.append("k")
    if char == "c":
        encrypted_letters.append("l")
    if char == "d":
        encrypted_letters.append("m")
    if char == "e":
        encrypted_letters.append("n")
    if char == "f":
        encrypted_letters.append("o")
    if char == "g":
        encrypted_letters.append("p")
    if char == "h":
        encrypted_letters.append("q")
    if char == "i":
        encrypted_letters.append("r")
    if char == "j":
        encrypted_letters.append("s")
    if char == "k":
        encrypted_letters.append("t")
    if char == "l":
        encrypted_letters.append("u")
    if char == "m":
        encrypted_letters.append("v")
    if char == "n":
        encrypted_letters.append("w")
    if char == "o":
        encrypted_letters.append("x")
    if char == "p":
        encrypted_letters.append("y")
    if char == "q":
        encrypted_letters.append("z")
    if char == "r":
        encrypted_letters.append("a")
    if char == "s":
        encrypted_letters.append("b")
    if char == "t":
        encrypted_letters.append("c")
    if char == "u":
        encrypted_letters.append("d")
    if char == "v":
        encrypted_letters.append("e")
    if char == "w":
        encrypted_letters.append("f")
    if char == "x":
        encrypted_letters.append("g")
    if char == "y":
        encrypted_letters.append("h")
    if char == "z":
        encrypted_letters.append("i")
    if char == "A":
        encrypted_letters.append("J")
    if char == "B":
        encrypted_letters.append("K")
    if char == "C":
        encrypted_letters.append("L")
    if char == "D":
        encrypted_letters.append("M")
    if char == "E":
        encrypted_letters.append("N")
    if char == "F":
        encrypted_letters.append("O")
    if char == "G":
        encrypted_letters.append("P")
    if char == "H":
        encrypted_letters.append("Q")
    if char == "I":
        encrypted_letters.append("R")
    if char == "J":
        encrypted_letters.append("S")
    if char == "K":
        encrypted_letters.append("T")
    if char == "L":
        encrypted_letters.append("U")
    if char == "M":
        encrypted_letters.append("V")
    if char == "N":
        encrypted_letters.append("W")
    if char == "O":
        encrypted_letters.append("X")
    if char == "P":
        encrypted_letters.append("Y")
    if char == "Q":
        encrypted_letters.append("Z")
    if char == "R":
        encrypted_letters.append("A")
    if char == "S":
        encrypted_letters.append("B")
    if char == "T":
        encrypted_letters.append("C")
    if char == "U":
        encrypted_letters.append("D")
    if char == "V":
        encrypted_letters.append("E")
    if char == "W":
        encrypted_letters.append("F")
    if char == "X":
        encrypted_letters.append("G")
    if char == "Y":
        encrypted_letters.append("H")
    if char == "Z":
        encrypted_letters.append("I")
encrypted_code = ''.join(encrypted_letters)
print(encrypted_code)
