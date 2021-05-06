# # first_assignment
random_n = int(input('Students, n ='))
random_k = int(input('Apples, k ='))
print()
print("Apples per person", f'{random_k} // {random_n} = {random_k // random_n}')
print("Apples left in basket", f'{random_k} % {random_n} = {random_k % random_n}')
print("---------------------")
# # second_assignment
class1 = int(input('First class ='))
class2 = int(input('Second class ='))
class3 = int(input('Third class ='))
print()
amount1 = class1 // 2
amount2 = class2 // 2
amount3 = class3 // 2
print("Desks needed if even number: ", amount1 + amount2 + amount3)
students1 = class1 % amount1
students2 = class2 % amount2
students3 = class3 % amount3
more_desks = (students1 + students2 + students3)/2
print("Additional desks needed: ", more_desks)
print("Desks needed= ", f'{amount1} + {amount2} + {amount3} + {more_desks} = {amount1 + amount2 + amount3 + more_desks}')
print("---------------------")
# # third_assignment
n = int(input("Enter your number: "))
if n % 2 == 0:
    print("yes")
else:
    print("no")
print("---------------------")
# #fourth_assignment
m = int(input("Enter your number: "))
if m % 2 == 0:
    print("Even number: ", n)
elif m % 2 != 0:
    print("Closest even number", m + 1)
print("---------------------")
# fifth_assignment
k = input("Enter your number: ")
r = str(k)[::-1]
r = int(r)
print("Reverse number", r)
