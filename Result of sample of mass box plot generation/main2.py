__author__ = 'teo'

import rpy2.robjects as robjects
from rpy2.robjects.packages import importr
import rpy2.robjects.lib.ggplot2 as ggplot2
import os
import re
import numpy
#setting import global r functions
ggplot = importr("ggplot2") #imports ggplot2
grdevices = importr('grDevices') #imports graphical capabilities
r = robjects.r #provides access to the R command line
#This serves as way for you to set the correspondence between R labels and the name you want a particular data set to get on titles and graph labels.
# Any Dict related errors are probably because something is missing from here
name_dict = {'AP.classes':'Number of AP Classes', 'X.drive.yourself':'Drive yourself', 'serial..':'Serial Number','Grade':'Grade','Gender': 'Gender', 'Age':'Age','Diet':'Diet','breakfast.frequency':'Breakfast Frequency', 'food.breakfast':'Food for breakfast','sleep.per.night':'Hours of Sleep per Night on Average','homework.time':'Time Spent on Homework','X.homework.in.school':'Time Spent on Homework in School', 'transportation.time':'Time Spent on Transport', 'get.home.around':'Getting Home at','wake.up.around':'Wake Up at', 'X..homework.alone':'Homework Completed Alone', 'fast.food.frequency':'Frequency of Fastfood Consumption', 'sick.days':'Numer of Sick Days','lunch.detention.workshop':'Number of Days in Lunch Detention', 'part.time.job':'Hours in a Part Time Job', 'GPA':'Grade Point Average','stress':'Stress on a scale of 1 to 7', 'metro.':'% of time commuting on Metro', 'bus.':'Bus', 'walk.':'Walk', 'driven.':'Driven', 'X':'X???', 'subject.good':'Good Subject', 'subject.bad':'Bad Subject', 'know.grade':"I Know my grade", 'respected.by.friends':'On a scale of 1 to 7, I am respect by my friends', 'respected.by.teachers':'respected by teachers', 'like.burke': 'On a Scale of 1 to 7, I like Burke...', 'assembly':'On a scale of 1 to 7, I enjoy assembly', 'bonding.trip':'I enjoyed the bonding trip', 'advising.program':'The Advising Program', 'clubs':'CLUBS!!!!', 'sport.season':'Sports Season', 'pe.credit':'Pe Credits', 'sport.outside':'Sports Outside'}
#This sets the last part of the title for the graphs
titleUni = ' Edmund Burke School 2013 - 2014, 2014-2015 Census'
#gets the directory of the python file so it can put the images there
cwd = os.getcwd()
print(cwd)

def validNumber(names):
    '''This function takes a list of R names, access the current data set and returns all the names with integer/numeric data types'''
    newNames = []
    for x in range(0,(len(names))):
        #print(x)
        classR = robjects.r('class(data$' + names[x] + ')')
        #print(classR[0])
        none1 = re.search('integer|Numeric|numeric',classR[0])
        #print(none1)
        if none1 != None:
            newNames.append(names[x])
    return(newNames)


def range_det(name):
    print(name)

    #print("here")
    #a = robjects.r('seq(0,10,1)')
    #print(a)
    maxR = robjects.r('max(data$' + name + ')')
    minR = robjects.r('min(data$' + name + ')')
    max = int(maxR[0])
    print(max)
    min = int(minR[0])
    print(min)
    if ((max < 10) & (min >= 1)):
        print("a")
        return('stat_bin(breaks=1:7,right = TRUE,origin=0)')
    elif ((max == min)|(max+1 == min)|(max == min -1)):
        return('geom_bar()')
    elif ((max < 100) & (min >= 0)):
        print("b")
        return('stat_bin(breaks=(seq(0,100,10)),right=TRUE,origin=0)')
    else:
        print("c")
        return('geom_bar(aes(y = 100 *(..count..)/sum(..count..)),stat ="bin")')


#robjects.r('data <- read.csv("6.csv")')
#a = robjects.r('max(data$stress')
#print(a)
#range_det('stress')

def Bar_Graph_Gen(dataSetName,groupName):
    '''This function takes the name of the data set (without the .csv) and the group name. It generates all the bar graphs for the valid parts of the data'''
    robjects.r('data <- read.csv(\'' + dataSetName + '.csv' + '\',na.strings = "N/A")')
    data = r['read.csv'](dataSetName + '.csv')
    names = r['names'](data)
    validNames = validNumber(names)
    for x1 in range(0,len(validNames)):
        title = name_dict[validNames[x1]] + ', ' + groupName + ', ' + titleUni
        x = name_dict[validNames[x1]]
        y = 'Percentage of Students'
        plot = robjects.r('ggplot(data, aes(x = (' + validNames[x1] + '), y=100 *(..count..)/sum(..count..) )) +' + range_det(validNames[x1]) +' + labs(title="' + title + '",x = "' + x + '" ,y = "' + y + '")')
        fileName = cwd + '/barPlot' + groupName + x
        grdevices.png(file=fileName,width=800,height=800) #You change file size here
        plot.plot()
        grdevices.dev_off
    return ()

def gradeMake(x):
    '''Generates the grade label for some useful things'''
    a = (str(x)) + "th Grade"
    return(a)
#Required for binary object and box plot generation
def User_bar ():
    '''Takes a userinputed list of files names (without the .csv) in the form [6,11], converts their names to grade names and the runs the bargraph generation on the corresponding files and grade names'''
    x = input('Enter the file designations that you want bar graphs for:')
    fileN = [str(z) for z in x]
    grade = [gradeMake(z) for z in x]
    c = [Bar_Graph_Gen(a,b) for (a,b) in zip(fileN,grade)]
    return()


def mass_r_binary_op(op,verb,dataSetName,cutoff):
    robjects.r('data <- read.csv(\'' + dataSetName + '.csv' + '\',na.strings = "N/A")')
    data = r['read.csv'](dataSetName + '.csv')
    names = r['names'](data)
    validNames = validNumber(names)
    l = len(validNames)
    results = []
    for x in range(0,l):
        xname = validNames[x]
        print(xname)
        #print(xname)
        robjects.r(xname + ' <- data$' + xname)
        for y in range((x+1),l):
            yname = validNames[y]
            print(yname)
            robjects.r(yname+ ' <- data$' + yname)
            #print(yname)
            result = robjects.r(op+'(' + validNames[x] + ',' + validNames[y] + ')')
            if (abs(result[0]) >= cutoff):
                results.append(xname + verb + yname + '=' + str(result[0]) + '\n')
            else:
                pass
    f = open((op+'report'),'w')
    #print(results)
    for z in range(0,len(results)):
        f.write(results[z])
    f.close()

def mass_box_plot_gen(classifier,dataSetName):
    robjects.r('data <- read.csv(\'' + dataSetName + '.csv' + '\',na.strings = "N/A")')
    data = r['read.csv'](dataSetName + '.csv')
    names = r['names'](data)
    validNames = validNumber(names)
    l = len(validNames)
    for x in range(0,l):
        title = 'Comprehensive box plot of'+ name_dict[validNames[x]] + ',' + titleUni
        y = name_dict[validNames[x]]
        x1 = classifier + 's' #You might want to change this to make the titles look reasonable...
        plot = robjects.r('ggplot(data,aes(factor(' + classifier + '),' + validNames[x] + ')) + geom_boxplot() + labs(title="' + title + '",x = "' + x1 + '" ,y = "' + y + '")')
        fileName = cwd + '/boxplot' + title
        grdevices.png(file=fileName,width=800,height=800) #You change file size here
        plot.plot()
        grdevices.dev_off
        return()



#samples:
#mass_r_binary_op('cor',' correlates with ','11',.5)
#User_bar()
mass_box_plot_gen('Grade','total')





