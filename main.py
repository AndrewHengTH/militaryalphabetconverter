
# English to Military Alphabet Converter
# I dont know why I made this 

# Stuff to prepare military dictionary
f = open("militarydict.txt", "r")
dict = f.read()
dictList = dict.split("\n")

# Main program

input = input("\nWhat do you want to turn into military alphabet? > ") # Take input from user 
input.upper() # Turn all into uppercase 
inputList = list(input) # Turn input into list

for i in range(len(inputList)):
    for j in range(len(dictList)):
        if inputList[i] == dictList[j][0]:
            inputList[i] = dictList[j]

output = ' '.join(str(index) for index in inputList)

print("\n", output, "\n")