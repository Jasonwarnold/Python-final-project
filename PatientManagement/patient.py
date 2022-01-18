# ------------------------------------------------------------------
# Class: CIST 2371 Beginning Python Programming
# Term: Spring 2021
# Instructor: Jianmin Wang
# Description: Solution to end of semester project, patient class for patient management system.
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

class Patient:

    def __init__(self, pid, fname, lname, street, city, state, zipcode, phone, emerg_name, emerg_phone):
        self.__pid = pid
        self.__fname = fname
        self.__lname = lname
        self.__street = street
        self.__city = city
        self.__state = state
        self.__zipcode = zipcode
        self.__phone = phone
        self.__emerg_name = emerg_name
        self.__emerg_phone = emerg_phone

    def set_id(self, pid):
        self.__pid = pid

    def get_id(self):
        return self.__pid

    def set_fname(self, fname):
        self.__fname = fname

    def get_fname(self):
        return self.__fname

    def set_lname(self, lname):
        self.__lname = lname

    def get_lname(self):
        return self.__lname

    def set_street(self, street):
        self.__street = street

    def get_street(self):
        return self.__street

    def set_city(self, city):
        self.__city = city

    def get_city(self):
        return self.__city

    def set_state(self, state):
        self.__state = state

    def get_state(self):
        return self.__state

    def set_zipcode(self, zipcode):
        self.__zipcode = zipcode

    def get_zipcode(self):
        return self.__zipcode

    def set_phone(self, phone):
        self.__phone = phone

    def get_phone(self):
        return self.__phone

    def set_emerg_name(self, emerg_name):
        self.__emerg_name = emerg_name

    def get_emerg_name(self):
        return self.__emerg_name

    def set_emerg_phone(self, emerg_phone):
        self.__emerg_phone = emerg_phone

    def get_emerg_phone(self):
        return self.__emerg_phone

    def display_pat(self):
        print('Patient id:        ', self.__pid)
        print('Patient name:      ', self.__lname, ',', self.__fname)
        print('Patient Address:   ', self.__street)
        print('                   ', self.__city, ',', self.__state, self.__zipcode)
        print('Patient phone #:   ', self.__phone)
        print('Emergency contact: ', self.__emerg_name)
        print('Emergency phone#:  ', self.__emerg_phone)