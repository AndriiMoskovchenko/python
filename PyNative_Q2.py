def SumNumb(numb):
    prevNum = 0
    for num in range(numb):
        sum = prevNum + num
        print("Current Number", num, "Previous Number ", prevNum," Sum: ", sum)    
    prevNum = num
print("Printing current and previous number sum in a given range")
SumNumb(10)
