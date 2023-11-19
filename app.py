# print('Hello world!')
#
# input_1 = float(input("enter no 1: "))
# input_2 = float(input("enter no 2: "))
# summ = input_1 + input_2
# print("Sum: " + str(summ))

# print(not  3 > 4)
# print (10 > 20 or 10 > 9)
# print (10 > 20 and 10 > 9)

# if 36 < temp < 38:
temp = float(input("Temperature: "))

if temp > 36 and temp < 38:
    print("Normal")
elif temp < 36: # this is a comment, too low temp
    print("Hyperthermia")
else:
    print("Fever")

print("done!")
