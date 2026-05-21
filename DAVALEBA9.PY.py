
#TASK 1


def sum_of_digits(n):
    n = abs(n)  # handle negative numbers
    if n < 10:
        return n
    return n % 10 + sum_of_digits(n // 10)

print("=== TASK 1: sum_of_digits ===")
print(f"sum_of_digits(1234) = {sum_of_digits(1234)}")   # 10
print(f"sum_of_digits(999)  = {sum_of_digits(999)}")    # 27
print(f"sum_of_digits(0)    = {sum_of_digits(0)}")      # 0



#TASK 2


is_even = lambda n: n % 2 == 0

print("\n=== TASK 2: is_even ===")
print(f"is_even(4)  = {is_even(4)}")   # True
print(f"is_even(7)  = {is_even(7)}")   # False
print(f"is_even(0)  = {is_even(0)}")   # True



#TASK 3


students = [
    ("Luka",   15, 85),
    ("Ana",    14, 92),
    ("Giorgi", 16, 78),
    ("Nino",   15, 95),
]

sorted_students = sorted(students, key=lambda s: (s[1], -s[2]))

print("\n=== TASK 3: Students sorted by age, then score (desc) ===")
for name, age, score in sorted_students:
    print(f"  {name:8s} | age: {age} | score: {score}")



#TASK 4


words = ["banana", "apple", "kiwi", "watermelon", "cherry"]

sorted_words = sorted(words, key=lambda w: len(w), reverse=True)

print("\n=== TASK 4: Words sorted by length (descending) ===")
print(sorted_words)



#TASK 5


capitalized = list(map(lambda w: w.capitalize(), sorted_words))

print("\n=== TASK 5: First letter capitalized (from Task 4 list) ===")
print(capitalized)



#TASK 6


numbers = [5, 12, 7, 18, 3, 24, 9]

filtered = list(filter(lambda n: n > 10 and n % 3 == 0, numbers))

print("\n=== TASK 6: Numbers > 10 and divisible by 3 ===")
print(filtered)  # [12, 18, 24]



#TASK 7


from functools import reduce

students_data = [
    ("Alice",   88, 79, 95),
    ("Bob",     60, 72, 68),
    ("Charlie", 90, 85, 92),
    ("Diana",   75, 80, 70),
    ("Eve",     95, 91, 89),
]


students_with_avg = list(map(
    lambda s: (s[0], reduce(lambda acc, x: acc + x, s[1:]) / len(s[1:])),
    students_data
))


passed = list(filter(lambda s: s[1] >= 85, students_with_avg))


passed_sorted = sorted(passed, key=lambda s: s[1], reverse=True)

print("\n=== OPTIONAL TASK: Students with average >= 85 (sorted desc) ===")
for name, avg in passed_sorted:
    print(f"  {name:10s} | average: {avg:.2f}")