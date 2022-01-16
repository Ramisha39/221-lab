digit = "0123456789"
file = open('input.txt')
output = open('output.txt', 'w')
record = open('record.txt', 'w')

li = []
pallindrome = []
for line in file:
    temp = line.split()
    li.append(temp)

odd = 0
even = 0
not_parity = 0
p = 0
not_p = 0

for i in li:
    for j in i:
        if "." in str(j):
            not_parity += 1
            output.write(str(j) + " cannot have parity and ")
        elif j in digit and int(j)%2 == 0:
            even += 1
            output.write(str(j) + " has even parity and ")
        elif j in digit and int(j)%2 != 0:
            odd += 1
            output.write(str(j) + " has odd parity and ")
        elif j not in digit and str(j) == str(j[-1::-1]):
            p += 1
            output.write(str(j) + " is a palindrome \n")
        elif j not in digit and str(j) != str(j[-1::-1]):
            not_p += 1
            output.write(str(j) + " is not a palindrome \n")

record.write("Percentage of odd parity: "+ str((odd*100)//len(li)) +"%\n")
record.write("Percentage of even parity: "+ str((even*100)//len(li)) + "%\n")
record.write("Percentage of no parity: "+ str((not_parity*100)//len(li)) + "%\n")
record.write("Percentage of palindrome: "+ str((p*100)//len(li)) + "%\n")
record.write("Percentage of non-palindrome: "+ str((not_p*100)//len(li)) + "%\n")


file.close()
output.close()
record.close()





