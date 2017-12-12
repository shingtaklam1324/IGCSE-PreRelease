names = []
test1 = []
test2 = []
test3 = []
total = []
totalMarks = 0

for num in range(30):
  names.append(input("Name: "))
  score = int(input("Test 1 Score:"))
  while score > 20 or score < 0:
    print("Score is out of range")
    score = int(input("Test 1 Score:"))
  else:
    test1.append(score)
  score = int(input("Test 2 Score:"))
  while score > 25 or score < 0:
    print("Score is out of range")
    score = int(input("Test 2 Score:"))
  else:
    test2.append(score)
  score = int(input("Test 3 Score:"))
  while score > 35 or score < 0:
    print("Score is out of range")
    score = int(input("Test 3 Score:"))
  else:
    test3.append(score)
  total.append(test1[num] + test2[num] + test3[num])
  totalMarks += total[num]
'''
print("Name | Test 1 | Test 2 | Test 3 | Total")
for num in range(30):
  print(names[num],test1[num],test2[num],test3[num],total[num])
print("Average")
print(totalMarks / 30)
sortedTotal = sorted(total)
maxIndex = total.index(sortedTotal[29])
print("Highest Mark Student")
print("Name | Test 1 | Test 2 | Test 3 | Total")
print(names[maxIndex],test1[maxIndex],test2[maxIndex],test3[maxIndex],total[maxIndex])
'''