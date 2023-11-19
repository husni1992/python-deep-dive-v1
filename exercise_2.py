# for loop
# fruits = ["apple", "grapes", "mango"]
# for fruit in fruits:
#     print(fruit)

# while loop
# count = 1
# while count <= 5:
#     print(count)
#     count += 1

# break and continue inside for loops
# for num in range(1, 10):
#     if num > 8:
#         break
#     if num % 2 == 0:
#         continue
#     print(num)

# Using else with a for loop
# Here, the else block is executed after the for loop completes its iteration over the range.
for number in range(1, 10):
    print(number * "*")
else:
    print("Loop is finished")

print('-------------\n')

# the 3rd parameter of the range function is step, it is how much you increment each number in the sequence.
for number in range(0, 100, 5):
    print(number)
