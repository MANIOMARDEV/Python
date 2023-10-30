# Task 1: Print all integers from 0 to 150.
for i in range(0,151):
    print(i)
    # Task 2: Print all the multiples of 5 from 5 to 1,000.
for i in range(5,1001,5):
    print(i)
# Task 3: Print integers 1 to 100. If divisible by 5, print "Coding" instead. If divisible by 10, print "Coding Dojo".
for i in range(1, 101):
    if i % 10 == 0:
        print("Coding Dojo")
    elif i % 5 == 0:
        print("Coding")
    else:
        print(i)
# Task 4: Add odd integers from 0 to 500,000 and print the final sum.
sum_of_odds = 0
for i in range(1, 500001, 2):
    sum_of_odds += i
print("Sum of odd integers from 0 to 500,000:", sum_of_odds)
# Task 5: Print positive numbers starting at 2018, counting down by fours.
for i in range(2018, 0, -4):
    print(i)
# Task 6: Print integers that are a multiple of mult from lowNum to highNum.
lowNum = 2
highNum = 9
mult = 3
for i in range(lowNum, highNum + 1):
    if i % mult == 0:
        print(i)