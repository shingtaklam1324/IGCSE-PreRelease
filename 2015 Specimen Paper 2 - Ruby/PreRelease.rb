names = []
test1 = []
test2 = []
test3 = []
total = []
maxScores = [20,25,35]
score = 0
#Initializes the variables
30.times do
	print "Name:"
	names.append($stdin.gets.strip) #inputs the name of the student
	studentScore = []
	3.times do |num|
		begin
			print "Test #{num + 1} score:" #Input the test scores
			score = $stdin.gets.strip.to_i
		end while 0..maxScores[num] === score
		studentScore.append[score]
	end
	test1.append[studentScore[0]] #assign the scores to the arrays
	test2.append[studentScore[1]] #appends to the end
	test3.append[studentScore[2]]
	total.append(studentScore.inject(0,:+)) #appends the sum of the array
end
puts "Name | Test 1 | Test 2 | Test 3 | Total"
30.times {|num| puts "#{names[num]} | #{test1[num]} | #{test2[num]} | #{test3[num]} | #{total[num]}"}
#prints each student's name, scores and total
puts "Average = #{(total.inject(0,:+)) / 30}"
#average = sum/30
puts "Highest Scoring Student | Test 1 | Test 2 | Test 3 | Total"
mIndex = total.index((total.sort).last) #finds the index of the student with the highest total
puts "#{names[mIndex]} | #{test1[mIndex]} | #{test2[mIndex]} | #{test3[mIndex]} | #{total[mIndex]}"