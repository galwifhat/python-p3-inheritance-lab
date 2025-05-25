#!/usr/bin/env python

from user import User

class Student(User):
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        self.knowledge = []
    
    def learn(self, know):
        self.knowledge.append(know)
        
my_student = Student("My", "Student")
my_student.learn("New information")