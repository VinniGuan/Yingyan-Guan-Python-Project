# Yingyan Guan
# In this project, you will write code that (1) reads data from files about students, courses,
# and registrations (2) processes the data in Lists to answer related questions. Moreover, you’ll create plots that show statistics about the data.

# create three functions that read data from 3 files and append the data into lists.
# This task is often called data preprocessing.

import matplotlib.pyplot as pyplot

def readStudentsData(filename):
    infile = open(filename,'r')
    content = infile.read() 
    infile.close()
    
    Biglist = content.split("\n") # split the list by \n
    
    new = [] # initialize the list 
    
    # i indicate the rows in the file, those rows are sublist in the the big list 
    for i in Biglist:
        sublist = i.split(",")
        new.append(sublist)
    return new


def readRegistrationData(filename):
    infileR = open(filename,'r')
    contentR = infileR.read() 
    infileR.close()
    
    BiglistR = contentR.split("\n")
    
    newR = [] # initialize the list 
    
    # i indicate the rows in the file, those rows are sublist in the the big list 
    for i in BiglistR:
        sublistR = i.split(",")  #we want to split line/small list in the biglist 
        list1 = sublistR[0:-1] # we create list 1 to store the index0 and index1 data except the numbers
        list2 = eval(sublistR[-1]) # convert the last element in small list to float
        list1.append(list2) # add the float to list 1 
        newR.append(list1) # add all the list 1 to big list 
        
    return newR

def readCoursesData(filename):
    infileC = open(filename,'r')
    contentC = infileC.read() 
    infileC.close()
    
    BiglistC = contentC.split("\n")# split the list by \n
    
    newC = [] # initialize the list 
    
    # i indicate the rows in the file, those rows are sublist in the the big list 
    for i in BiglistC:
        sublistC = i.split(",")
        newC.append(sublistC)
    return newC

############################################################### task 2
# create a function that count the number of student that meet the criteria based on gender and state. 
def countStudents(studentsList, gender, state):
    # i is the sublist of stdudentsList 
    for i in range(len(studentsList)): 
        count = 0 
        # we want to extract the element from the sublist
        for studentsublist in studentsList:
            # if gender and state both meet the criteria, we add it in the count
            if (studentsublist[2]==gender) and (studentsublist[3]==state) :
                count += 1
        return count
    
############################################################### task 3
# The studentsPassedCourse function returns a list of students’ names who 
# passed the given course as a parameter. The passing criterion is a grade of 50 or more.
def studentsPassedCourse(studentsList, coursesList, registrationList, courseName):
    # subcoursesList is the row in the file 
    for subcoursesList in coursesList:
        # if the courseName is euqal to the name in the sublist in course list
        # then its course number is the first element in the sublist in the course list 
        if(courseName == subcoursesList[1]):
            coursesNum = subcoursesList[0]
            break
    
    # initialize a list 
    studentNumList = []
    # subregistrationList is the row of the file
    for subregistrationList in registrationList:
        # if the score(index 2 in subregistration list) is greater than 50
        # and the course number(index 1) is euqal to coursesNum
        if((subregistrationList[2] >= 50) and (subregistrationList[1] == coursesNum)):
            # we will append that student ID in the studentNumList
            studentNumList.append(subregistrationList[0])
                
    studentList = [] # initialize a list 
    
    for substudentList in studentsList:
            # if the ID number in studentList in the studentNum List
            # we will know that is the student we want to add in the student list 
            if substudentList[0] in studentNumList:  
                studentList.append(substudentList[1])
                        
    return sorted(studentList)

############################################################### task 4
# we want to know how many students are in one of those courses 
def studentsTakingOneCourse(studentsList, registrationList, courseNum):
    studentNumList = [] # initialize a list 
    
    for subregistrationList in registrationList:
        # if the course we enter in the program is index 1 of subregistration 
        if subregistrationList[1]==courseNum:
            # we will append that student name on the list 
            studentNumList.append(subregistrationList[0])
    
    # initialize a list 
    studentList = []
    for substudentList in studentsList:
        # if that student ID in substudentList is in the studentNUMlist 
         if substudentList[0] in studentNumList:
            # we will append that student name to the studentList 
            studentList.append(substudentList[1])
            
    # we want to return the studentList and the number of student in that list 
    return sorted(studentList), len(studentList)
        
# we want to find how many students are in two different class at the same time 
def studentsTakingTwoCourses(studentsList, registrationList, courseNum1, courseNum2):
    list1,num1 = studentsTakingOneCourse(studentsList, registrationList, courseNum1)
    list2,num2 = studentsTakingOneCourse(studentsList, registrationList, courseNum2)
    studentList = []
    for i in list1: # for those student in list 1
        for j in list2: # for those students in list 2
            if i == j: # if that student are in both course 
                studentList.append(i) # append it to the list
                
    return sorted(studentList), len(studentList)

############################################################### task 5
# The stateCourseStatistics function collects geographical statistics about the students 
# who are registered to a given course.
def stateCourseStatistics(studentsList, registrationList, courseNum):
    # initialize a list
    studentNumList = []
    # subregistrationList is each row in the registration file
    for subregistrationList in registrationList:
        # if the course number in the row in registration file is equal to courseNum, append that student ID
        if subregistrationList[1]==courseNum:
            studentNumList.append(subregistrationList[0])
    
    studentstateList = []
    for substudentList in studentsList:
         if substudentList[0] in studentNumList:
            studentstateList.append(substudentList[3]) # students in different state that in a specific class
    
    # initialize a list
    finallist = [] 
    # create a for loop to import different conditions
    # if the state is appear on the finallist, we don't need to append that 
    for state in studentstateList:
        samestateOff = 0 
        for subfinallist in finallist:
            if(state == subfinallist[0]):
                samestateOff = 1
                subfinallist[1] += 1
        if(samestateOff == 0):
            finallist.append([state,1])
    myList = sorted(finallist, key=lambda x:x[0])         
    return myList
    
############################################################### task 6
# implement the plotPieChart, plotBarChart functions
def plotPieChart(courseNum1, courseNum1Count, courseNum2, courseNum2Count, bothCoursesCount):
    size = [bothCoursesCount, courseNum1Count,courseNum2Count]
    labels = ['Both' + ' '+ courseNum1 + ' ' + 'and' + ' ' + courseNum2, courseNum1, courseNum2]
    colors = ['tomato','lightgreen', 'gold']
   
    # add percentages to the pie chart sections, add shadow, startangle
    pyplot.pie(size, colors = colors, autopct='%1.1f%%',startangle=90)
    
    #To add Legend on the lower left position:
    pyplot.legend(labels = labels, loc = 'lower left')
   
    # To set equal scaling (i.e., make circles circular)
    pyplot.axis('equal')
    shadow=True
    pyplot.savefig("plotPieChart.pdf")
    pyplot.show()
    # save the chart
    

def plotBarChart(statesCountList):
    # initialize the list 
    x = []
    y = []
    
    # create an for loop to append the list of states, the count 
    for i in statesCountList:
        x.append(i[0])
        y.append(i[1])
    # add color and other values 
    pyplot.bar(x, y,color='tomato', width=0.5)
    # add title of the bar charts
    pyplot.title('State Statistics')
    # add y label
    pyplot.ylabel('# of students')
    # rotate the x label 
    pyplot.xticks(rotation=-20)
    pyplot.savefig("plotBarChart.pdf")
    pyplot.show()
    


############################################################### task 7
if __name__ == "__main__":
    
    studentsList = readStudentsData('studentsdata.txt')
    print(studentsList)
    
    registrationList = readRegistrationData('registrationdata.txt')
    print(registrationList)
    
    coursesList = readCoursesData('coursesdata.txt')
    print(coursesList)
    
    students = studentsList
    print (countStudents(students, 'Female', 'Indiana'))
    print (countStudents(students, 'Male', 'Minnesota'))
    
    passedList = studentsPassedCourse(studentsList, coursesList, registrationList, 'Python Programming Language')
    print(passedList)
    
    oneList, oneCount = studentsTakingOneCourse(studentsList, registrationList, 'CS177')
    print(oneList)
    print(oneCount)
    
    twoList, twoCount = studentsTakingTwoCourses(studentsList, registrationList, 'CS177', 'CS180')
    print(twoList)
    print(twoCount)
    
    statesCount = stateCourseStatistics(studentsList, registrationList, 'CS177')
    print(statesCount)
    
    ###task 6 PlotPieChart
    course1Count = studentsTakingOneCourse(studentsList, registrationList, 'CS177')[1]
    course2Count = studentsTakingOneCourse(studentsList, registrationList, 'CS180')[1]
    bothCoursesCount = studentsTakingTwoCourses(studentsList, registrationList, 'CS177', 'CS180')[1]
    plotPieChart('CS177', course1Count, 'CS180', course2Count, bothCoursesCount)
    
    ###task 6 bar chart
    statesCountList = stateCourseStatistics(studentsList, registrationList, 'CS177')
    plotBarChart(statesCountList)



