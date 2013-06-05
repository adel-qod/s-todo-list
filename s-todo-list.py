#!/usr/bin/python

#Copyright (c) 2013, Mhd Adel Al Qodmani
#All rights reserved.

#Redistribution and use in source and binary forms, with or without modification, are permitted provided that the following conditions are met:

#Redistributions of source code must retain the above copyright notice, this list of conditions and the following disclaimer.

#Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the following disclaimer in the documentation and/or other materials provided with the distribution.

#THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.


import getpass #to get the username
import os#to delete files
#############################################################
# THIS IS TESTED FOR python 2.7 and not later versions
#############################################################
def printOptionsList():
	print 'Welcome to your task manager, ' + getpass.getuser()
	print 'To add a task, type add'
	print 'To view task list, type list'
	print 'To check tasks as finished, type finish'
	print 'To clear the terminal, type clear'
	print 'To exit, type exit'
	print 'To view this list again, type help'

def clear():
	print "\x1b[2J\x1b[H"#using escape chars to clear the terminal

def add():	
	while True:
		taskName = raw_input("Task name:  ")
		importance = raw_input("Is it important? y or n:  ")
		if importance != 'y' and importance != 'n':
			print"Wrong option"
			continue
		urgency = raw_input("Is it urgent? y or n:  ")
		if urgency != 'y' and urgency != 'n':
			print "Wrong option"
			continue
		fp = open('./tasks','a+')
		fp.write(taskName + ',')
		fp.write(importance + ',')
		fp.write(urgency + '\n')
		fp.close()
		print "Task entered.."
		answer = raw_input("Are you done?")
	       	if answer == 'y':
			clear()
			printOptionsList()
			break

def listTasks():
#the list happens in order, we first present the important and urgent
#then the important and not urgent
#then the unimportant and urgent
#and finally, the unimportant and unurgent
#the first blog has a try-catch statement so that if there are no tasks
#we simply stop the listing process
	try:
		with open('./tasks', 'r') as fp:
			s = fp.readline()
			while s:
				task = s.split(',')
				if task[1] == 'y' and task[2].strip() == 'y':
					print task[0] + "\t\t\t Important" + "\t\t\t urgent"
				s = fp.readline()
		fp.close()
	except IOError as e:
		print "There are no tasks\n"
		printOptionsList()
		return

	with open('./tasks', 'r') as fp:
                s = fp.readline()
                while s:
                        task = s.split(',')
                        if task[1] == 'y' and task[2].strip() == 'n':
                                print task[0] + "\t\t\t Important" + "\t\t\t not urgent"
                        s = fp.readline()
        fp.close()
	with open('./tasks', 'r') as fp:
                s = fp.readline()
                while s:
                        task = s.split(',')
                        if task[1] == 'n' and task[2].strip() == 'y':
                                print task[0] + "\t\t\t Not Important" + "\t\t\t urgent"
                        s = fp.readline()
        fp.close()
	with open('./tasks', 'r') as fp:
                s = fp.readline()
                while s:
                        task = s.split(',')
                        if task[1] == 'n' and task[2].strip() == 'n':
                                print task[0] + "\t\t\t Not Important" + "\t\t\t not urgent"
                        s = fp.readline()
        fp.close()

def finish():
	listTasks()
	while True:	
		taskName = raw_input('Completed task name or type done to finish:  ')
		fp = open('./tasks','r')
		tasks = fp.readlines()
		fp.close()
		os.unlink('./tasks')
		fp = open('./tasks', 'w+')
		for task in tasks:
			array = task.split(',')
			if array[0].strip() != taskName.strip():
				fp.write(task)
		fp.close()
		if taskName == 'done':
			break
###################### MAIN #################################
clear()
printOptionsList()
while True:
        userInput = raw_input()
        if userInput == 'exit' or userInput == 'quit': 
                quit()  
	elif userInput == 'add':
		add()
	elif userInput == 'list' or userInput =='ls' or userInput == 'view':
		listTasks()
	elif userInput == 'finish' or userInput == 'done':
		finish()
        elif userInput == 'help': 
                printOptionsList()
	elif userInput == 'clear':
		clear()
	else:
		print 'Wrong entry'
