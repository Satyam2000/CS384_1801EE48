import tutorial01 as A1

actual_answers = [9, 12, 80, 5, 0.826, [10, 20, 40, 80, 160], [100, 90, 80, 70, 60],[0.2, 0.1, 0.067, 0.05, 0.04]]
student_answers = []

test_case_1 = A1.add(4, 5)
student_answers.append(test_case_1)

test_case_2 = A1.subtract(14, 2)
student_answers.append(test_case_2)


test_case_3 = A1.multiply(10, 8)
student_answers.append(test_case_3)

test_case_4 = A1.divide(10, 2)
student_answers.append(test_case_4)

test_case_5 = A1.power(1.1, -2)
student_answers.append(test_case_5)

# Driver code 

a = 10  # starting number 
r = 2 # Common ratio 
n = 5 # N th term to be find 

gp = A1.printGP(a, r, n) 
gp = list(gp) 
student_answers.append(gp)

print("G.P: ",gp)

ap =A1.printAP(100,-10,5)
ap =list(ap)
student_answers.append(ap)

print("A.P: ",ap)

hp =A1.printHP(5,5,5)
hp =list(hp)
student_answers.append(hp)

print("H.P: ",hp)

print(actual_answers)
print(student_answers)

total_test_cases = len(actual_answers)
count_of_correct_test_cases = 0

for x, y in zip(actual_answers, student_answers):
    if x == y:
        count_of_correct_test_cases += 1

print(f"Test Cases Passed = '{count_of_correct_test_cases}'  / '{total_test_cases}'")
