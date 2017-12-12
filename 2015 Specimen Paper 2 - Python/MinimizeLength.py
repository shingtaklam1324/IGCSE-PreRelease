names, test1, test2, test3, total, maximum = [''] * 30, [''] * 30, [''] * 30, [''] * 30, [''] * 30, [21,26,36]
for i in range(30):
    student = [input("Input Name \n > ")]
    for x in range(3):
        while True:
            try:
                inputVal = int(input("Test {} score \n > ".format(str(x + 1))))
                if inputVal in range(maximum[x]): break
            except ValueError:
                pass
        student.append(inputVal)
    names[i], test1[i] , test2[i] , test3[i] , total[i] = student[0] , student[1] , student[2] , student[3], student[1] + student[2] + student[3]
for i in range(30): print("Name | Test 1 | Test 2 | Test 3 | Total \n {} | {} | {} | {} | {}".format(names[i], test1[i], test2[i], test3[i], total[i]))
maxIndex = total.index((sorted(total))[29])
print("Average: {} \n \n Top Scoring Student \n Name | Test 1 | Test 2 | Test 3 | Total \n {} | {} | {} | {} | {}".format(sum(total) / 30, names[maxIndex], test1[maxIndex], test2[maxIndex], test3[maxIndex], total[maxIndex]))
