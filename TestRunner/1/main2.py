__author__ = 'teo'

import rpy2.robjects as robjects
from rpy2.robjects.packages import importr
import rpy2.robjects.lib.ggplot2 as ggplot2
import os
import re
#setting import global r functions
ggplot = importr("ggplot2") #imports ggplot2
grdevices = importr('grDevices')
r = robjects.r #provides access to the R command line
name_dict = {'AP.classes':'Number of AP Classes', 'X.drive.yourself':'Drive yourself', 'serial..':'Serial Number','Grade':'Grade','Gender': 'Gender', 'Age':'Age','Diet':'Diet','breakfast.frequency':'Breakfast Frequency', 'food.breakfast':'Food for breakfast','sleep.per.night':'Hours of Sleep per Night on Average','homework.time':'Time Spent on Homework','X.homework.in.school':'Time Spent on Homework in School', 'transportation.time':'Time Spent on Transport', 'get.home.around':'Getting Home at','wake.up.around':'Wake Up at', 'X..homework.alone':'Homework Completed Alone', 'fast.food.frequency':'Frequency of Fastfood Consumption', 'sick.days':'Numer of Sick Days','lunch.detention.workshop':'Number of Days in Lunch Detention', 'part.time.job':'Hours in a Part Time Job', 'GPA':'Grade Point Average','stress':'Stress on a scale of 1 to 7', 'metro.':'% of time commuting on Metro', 'bus.':'Bus', 'walk.':'Walk', 'driven.':'Driven', 'X':'X???', 'subject.good':'Good Subject', 'subject.bad':'Bad Subject', 'know.grade':"I Know my grade", 'respected.by.friends':'On a scale of 1 to 7, I am respect by my friends', 'respected.by.teachers':'respected by teachers', 'like.burke': 'On a Scale of 1 to 7, I like Burke...', 'assembly':'On a scale of 1 to 7, I enjoy assembly', 'bonding.trip':'I enjoyed the bonding trip', 'advising.program':'The Advising Program', 'clubs':'CLUBS!!!!', 'sport.season':'Sports Season', 'pe.credit':'Pe Credits', 'sport.outside':'Sports Outside'}
titleUni = 'Edmund Burke School 2013 - 2014, 2014-2015 Census'
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



def Bar_Graph_Gen(dataSetName,groupName):
    robjects.r('data <- read.csv(\'' + dataSetName + '.csv' + '\')')
    data = r['read.csv'](dataSetName + '.csv')
    names = r['names'](data)
    validNames = validNumber(names)
    for x1 in range(0,len(validNames)):
        title = name_dict[validNames[x1]] + groupName + titleUni
        x = name_dict[validNames[x1]]
        y = 'Percentage of Students'
        plot = robjects.r('ggplot(data, aes(factor(' + validNames[x1] + '))) +  geom_bar(aes(y = 100 *(..count..)/sum(..count..))) + labs(title="' + title + '",x = "' + x + '" ,y = "' + y + '")')
        fileName = cwd + '/barPlot' + groupName + x
        grdevices.png(file=fileName,width=512,height=512)
        plot.plot()
        grdevices.dev_off
    return ()

def gradeMake(x):
    a = (str(x)) + "th Grade"
    return(a)

def User_bar ():
    x = input('Enter the file designations that you want bar graphs for:')
    fileN = [str(z) for z in x]
    grade = [gradeMake(z) for z in x]
    c = [Bar_Graph_Gen(a,b) for (a,b) in zip(fileN,grade)]
    return()


User_bar()

#Bar_Graph_Gen('6',"6th Grade")
#Bar_Graph_Gen('11',"11th Grade")
