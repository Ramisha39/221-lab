file = open("input problem 01.txt")

x = file.read()

temp = x.split("\n")

t = temp[1].split(" ")
print(t)
arr = []
for k in t:
    k = int(k)
    arr.append(k)


def bubblesort(arr):
    for i in range(len(arr)-1):
        #declaring a variable to control the iteration
        swap = 0
        for j in range(len(arr)-i-1):
            if arr[j] > arr[j+1]:
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
                #Entering this if condition, meaning swap is done and the array is not sorted, swap = 1
                #not entering the if condition, meaning swap is not done, swap remains 0
                swap = 1

        #swap remains 0, meaning the array is sorted. So, no need to run the loop anymore.
        if swap == 0:
            break
    output = open("output problem 01.txt", "w")

    string = ""
    count = 0
    for x in arr:
        if count != 0:
            string = string + " " + str(x)
        else:
            string = string + str(x)
        count += 1
    output.write(string)
    # return arr


bubblesort(arr)