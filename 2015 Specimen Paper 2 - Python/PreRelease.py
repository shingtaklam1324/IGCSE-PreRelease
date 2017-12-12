names = []
test1 = []
test2 = []
test3 = []
total = []
totalMarks = 0
#initializes the arrays and variables

for num in range(30):
  names.append(input("Name: ")) #Appends the name of the student to the array
  score = int(input("Test 1 Score:")) #Inputs a value for test1
  while score > 20 or score < 0: #Validation
    print("Score is out of range") #Outputs error message
    score = int(input("Test 1 Score:")) #Inputs again
  else:
    test1.append(score) #Appends a validated score to the array
  score = int(input("Test 2 Score:")) #Same as above
  while score > 25 or score < 0:
    print("Score is out of range")
    score = int(input("Test 2 Score:"))
  else:
    test2.append(score)
  score = int(input("Test 3 Score:"))#Same as above
  while score > 35 or score < 0:
    print("Score is out of range")
    score = int(input("Test 3 Score:"))
  else:
    test3.append(score)
  total.append(test1[num] + test2[num] + test3[num])
  #Appends the total mark to the array
  totalMarks += total[num] #Adds student total to totalMarks

print("Name | Test 1 | Test 2 | Test 3") #Print column headers
for num in range(30):
  print(names[num],test1[num],test2[num],test3[num],total[num]) #Print each student's name, scores and total

print("Average")
print(totalMarks / 30) #Prints the class average

sortedTotal = sorted(total) #Duplicates and sorts the total score array
maxIndex = total.index(sortedTotal[29])
#Index of the student would be last in the sortedTotal array (29) and finds that student in the unsorted array
#This returns the position in the arrays the student is in

print("Highest Mark Student")
print("Name | Test 1 | Test 2 | Test 3") #Prints column headers
print(names[maxIndex],test1[maxIndex],test2[maxIndex],test3[maxIndex]) #Prints out student name, scores and total