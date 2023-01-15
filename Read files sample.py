# CS 177 – lab07.py
# {Yingyan Guan}
# reads data from a file about companies and their monthly investments 
# compute the average of investments while applying the following criteria:
# stop the average computation when encountering the first negative investment value

def readCompaniesData(filename):
    infile = open(filename, 'r')
    lines = infile.readlines()
    
    # First define how many indexes he has in a big list. There are 6 rows in it, 
    # and each row is a separate list, all of which have 6
    # A index is 6 lines, len(lines) has 6 lines
    listoflist = [0] * len(lines) 
    
    for i in range(len(lines)):
        stripline = lines[i].rstrip('\n') # strip the \n from each element
        eachline = stripline.split(',') #After removing the \n, separate each line with a comma, that is, each small list
        listoflist[i] = eachline # We want to separate each line as a small list, i refers to each line, 
                                 # the above each line has separated each line with a comma
                                 # Now we want to turn each line (eachline) into a small list in the big list (listoflist)
    infile.close()
    return listoflist

def computeAverageInvestment(lst):
    fin_list = []
    # j is the small list in the big list
    for j in range(len(lst)):
        smalllist = lst[j]
        total = 0
        counter = 0
        i = 1
        
        # if I wnat to touch the sublists of the list we need another loop
        # use the while loop break when it met the negative number
        while(i <= len(smalllist)): 
            if(float(smalllist[i]) >= 0):
                total += float(smalllist[i])
                i += 1
                counter += 1
            else:
                break
        avg = total / counter
        fin_list.append([smalllist[0],avg])
    # sort a list of lists
    fin_list = sorted(fin_list, key = lambda x:x[0])
    return fin_list
    
# the definition of main
def main():
    listoflist = readCompaniesData('companies.txt')
    x = computeAverageInvestment(listoflist)
    print(listoflist)
    print("averagesList = computeAverageInvestment(companyInvestmentList)")
    print(x)
# call main function 
main()
    
