# ------------------------------------------------------------------
# Class: CIST 2371 Beginning Python Programming
# Term: Spring 2021
# Instructor: Jianmin Wang
# Description: Solution to semester end project patient management application procedure class
# Due: 05/05/2021
# author Jason Arnold
# version 1.0
#
# By turning in this code, I Pledge:
#  1. That I have completed the programming assignment independently.
#  2. I have not copied the code from a student or any source.
#  3. I have not given my code to any student.
#
# ---------------------------------------------------------------------

class Procedure:

    def __init__(self, pid, pname, date, dname, cost):
        self.__pid = pid
        self.__pname = pname
        self.__date = date
        self.__dname = dname
        self.__cost = cost

    def set_pid(self, pid):
        self.__pid = pid

    def get_pid(self):
        return self.__pid

    def set_pname(self, pname):
        self.__pname = pname

    def get_pname(self):
        return self.__pname

    def set_date(self, date):
        self.__date = date

    def get_date(self):
        return self.__date

    def set_dname(self, dname):
        self.__dname = dname

    def get_dname(self):
        return self.__dname

    def set_cost(self, cost):
        self.__cost = cost

    def get_cost(self):
        return self.__cost

    def display_procedure(self):
        print('Patient ID:     ', self.__pid)
        print('Patient name:   ', self.__pname)
        print('Procedure date: ', self.__date)
        print('Doctor name:    ', self.__dname)
        print('Cost:           ', self.__cost)