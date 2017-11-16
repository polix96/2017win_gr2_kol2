# Class diary  
#
# Create program for handling lesson scores.
# Use python to handle student (highscool) class scores, and attendance.
# Make it possible to:
# - Get students total average score (average across classes)
# - get students average score in class
# - hold students name and surname
# - Count total attendance of student
# The default interface for interaction should be python interpreter.
# Please, use your imagination and create more functionalities. 
# Your project should be able to handle entire school.
# If you have enough courage and time, try storing (reading/writing) 
# data in text files (YAML, JSON).
# If you have even more courage, try implementing user interface.

#!/usr/bin/env python2.7

class School:
	def __init__(self,name,nb_classes,nb_students):
		self.name_of_school=name
		self.number_of_classes=nb_classes
		self.number_of_students=nb_students

class Class(School):
	def __init__(self,nb_cl,nb_students_cl):
		self.number_of_students_in_class=nb_students_cl
		self.average_across_class=0
		self.number_of_class=nb_cl
	
	@staticmethod
	def get_total_average(self,sum_av):
		self.avearge_across_class=sum_av/self.number_of_students_in_class
		return self.avearge_across_class

class Student(Class):
	def __init__(self,name_st,sname_st,pr_st=0,ab_st=0):
		self.name_of_student=name_st
		self.surname_of_student=sname_st
		self.attendance_of_student=0
		self.presents_of_student=pr_st
		self.absences_of_student=ab_st
	
	def get_total_attendance(self):
		total=self.presents_of_student+absences_of_student
		percent=self.presents_of_student/total
		return percent


school_1=School("Liceum im. Adama Mickiewicza",10,200)
class_1=Class(25,"1a")
student_1=Student("Anna","Kowalska")
