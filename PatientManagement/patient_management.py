# ------------------------------------------------------------------
# Class: CIST 2371 Beginning Python Programming
# Term: Spring 2021
# Instructor: Jianmin Wang
# Description: Solution to semester project patient management system
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
import json
import pickle
from os import path
import patient
import procedure

patients = dict()
procedures = dict()


# load patients from preset dat file
def load_patients():
    global patients
    try:
        # unpickle specified file to dictionary
        file = open('patients.dat', 'rb')
        patients = pickle.load(file)
        file.close()
        print('Successfully loaded patients from \'patients.dat\'.')
    except IOError:
        print('Patient file not found. Empty patient list loaded.')


# load procedures from preset dat file
def load_procedures():
    global procedures
    try:
        # unpickle specified file to dictionary
        file = open('procedures.dat', 'rb')
        procedures = pickle.load(file)
        file.close()
        print('Successfully loaded procedures from \'procedures.dat\'.')
    except IOError:
        print('Procedure file not found. Empty procedure list loaded')
    return procedures


# import patients from txt file
def import_patients_txt():
    # loop boolean
    run = True
    file_name = input('Please enter the file to import patients from: ')
    while run:
        try:
            # open file and read first line
            file = open(file_name, 'r')
            line = file.readline()
            # check for blank line
            while line != "":
                # split line
                record = line.split(',')
                # create new patient from split record
                pat = patient.Patient(record[0], record[1], record[2], record[3], record[4], record[5], record[6],
                                      record[7], record[8], record[9])
                # add patient to dictionary with key equal to the pid value
                patients[record[0]] = pat
                # get next line
                line = file.readline()
            # close file when done iterating and set loop boolean to false
            file.close()
            print('Records successfully added from', file_name)
            run = False
        # exception handling for file not found with option to re-enter file name
        except IOError:
            choice = input('File not found. Enter 1 to re-enter file name, or any other key to return to main menu')
            if choice == "1":
                file_name = input('Enter file name.')
            else:
                run = False


# import procedures from text file
def import_procedures_txt():
    global procedures
    # loop boolean
    run = True
    file_name = input('Please enter the file to input procedure from: ')
    while run:
        try:
            # open file and read first line
            file = open(file_name, 'r')
            procedures = dict()
            line = file.readline()
            # check for empty line
            while line != "":
                # split line
                record = line.split(',')
                # new procedure from split line
                proc = procedure.Procedure(record[0], record[1], record[2], record[3], record[4])
                # add to  list of procedures for each patient if procedure exists for patient
                if record[0] in procedures:
                    proclist = procedures[record[0]]
                    proclist.append(proc)
                    procedures[record[0]] = proclist
                # or create new list if not already present
                else:
                    proclist = [proc]
                    procedures[record[0]] = proclist
                # get next line
                line = file.readline()
            # close file and set loop boolean false
            file.close()
            print('Records successfully added from', file_name)
            run = False
        # IO exception handling with option to correct file name
        except IOError:
            choice = input('File not found. Enter 1 to re-enter file name, or any other key to return to main menu')
            if choice == "1":
                file_name = input('Enter file name.')
            else:
                run = False


# load patients from dat file
def import_patients_dat():
    # loop boolean
    global patients
    run = True
    file_name = input('Please enter filename to retrieve patients from: ')
    while run:
        try:
            # unpickle specified file to dictionary
            file = open(file_name, 'rb')
            patients = pickle.load(file)
            file.close()
            print('Records successfully added from', file_name)
            input('Press Enter to Continue to main menu.')
            run = False
        # exception handling with option to re-enter file name
        except IOError:
            choice = input('File not found. Enter 1 to re-enter file name, or any other key to return to main menu')
            if choice == "1":
                file_name = input('Enter file name.')
            else:
                run = False


# load procedures from dat file
def import_procedures_dat():
    global procedures
    # loop boolean
    run = True
    file_name = input('Please enter the filename to retrieve procedures from: ')
    while run:
        try:
            # unpickle file
            file = open(file_name, 'rb')
            procedures = pickle.load(file)
            file.close()
            print('Records successfully added from', file_name)
            input('Press Enter to return to main menu. ')
            run = False
        # exception handling for IOError with option to re-enter file name
        except IOError:
            choice = input('File not found. Enter 1 to re-enter file name, or any other key to return to main menu')
            if choice == "1":
                file_name = input('Enter file name.')
            else:
                run = False


# add procedure
def add_procedure():
    global procedures
    pid = ''
    run = True
    found = False
    while run:
        # get pid
        pid = input('Please enter the ID of the patient having the procedure: ')
        # validate pid is from existing patient
        if pid not in patients:
            choice = input('Patient ID not found, please re-enter patient ID, or type \'x\' to return to main menu. ')
            if choice == 'x' or choice == 'X':
                run = False
        if pid in patients:
            run = False
            found = True
    if found:
        # get remaining attributes
        pname = input("Please enter the name of the procedure: ")
        date = input('Please enter the date of the procedure: ')
        dname = input('Please enter the name of the practitioner: ')
        cost = input('Please enter the cost of the procedure: ') + '\n'
        # new procedure and add to dictionary
        proc = procedure.Procedure(pid, pname, date, dname, cost)
        if pid in procedures:
            proclist = [procedures[pid], proc]
            procedures[pid] = proclist
            # display of record added
            print('The following procedure was added: ')
            proc.display_procedure()
            input('Press Enter to return to main menu')
        else:
            proclist = [proc]
            procedures[pid] = proclist
            # display of record added
            print('The following procedure was added: ')
            proc.display_procedure()
            input('Press Enter to return to main menu')


# add procedure with already validated pid from new patient creation
def add_procedure_newpat(pid):
    global procedures
    pid = pid
    # get attributes
    pname = input("Please enter the name of the procedure: ")
    date = input('Please enter the date of the procedure')
    dname = input('Please enter the name of the practitioner: ')
    cost = input('Please enter the cost of the procedure: ') + '\n'
    # new procedure and add to dictionary
    proc = procedure.Procedure(pid, pname, date, dname, cost)
    procedures[pid] = proc
    # display of procedure added
    print('The following procedure was added: ')
    proc.display_procedure()
    input('Press Enter to return to main menu')


# add new patient
def add_patient():
    global patients
    pid = ''
    # cycle through patient keys to set last one as pid
    for pat in patients:
        pat = patients[pat]
        pid = pat.get_id()
    # convert pid to int, then add 1 to set new patient pid
    pidint = int(pid) + 1
    # convert pid back to string and zero fill up to 6 char
    pid = str(pidint).zfill(6)
    # get remaining attributes
    fname = input('Please enter patient\'s first name: ')
    lname = input('Please enter patient\'s last name: ')
    street = input('Please enter patient\'s street address: ')
    city = input('Please enter patient\'s city: ')
    state = input('Please enter patient\'s state: ')
    zipcode = input('Please enter patient\'s zip code: ')
    phone = input('Please enter patient\'s phone number: ')
    emerg_name = input('Please enter emergency contact name: ')
    emerg_phone = input('Please enter emergency contact phone number: ')
    emerg_phone += '\n'
    # new patient  and add to dictionary
    pat = patient.Patient(pid, fname, lname, street, city, state, zipcode, phone, emerg_name, emerg_phone)
    patients[pid] = pat
    # print patient added
    print('The following patient record added: ')
    pat.display_pat()
    # option to add procedure for new patient
    choice = input('Would you like to add a procedure for this new patient? Y to add, or any other key to return ')
    if choice == 'Y' or choice == 'y':
        add_procedure_newpat(pid)


# save patients to preset file on exit
def save_patients():
    global patients
    try:
        # pickle and dump dictionary
        file = open('patients.dat', 'wb')
        pickle.dump(patients, file)
        file.close()
        print('Patients saved to file \'patients.dat\'')
    except IOError:
        print('IO Error')


# save procedures to preset file on exit
def save_procedures():
    global procedures
    try:
        # pickle and dump dictionary
        file = open('procedures.dat', 'wb')
        pickle.dump(procedures, file)
        file.close()
        print('Procedures saved to file \'procedures.dat\'')
    except IOError:
        print('IO Error')


# display all patient records with d2 at main menu
def display_all_patient_records():
    global patients
    for pat in patients:
        pat = patients[pat]
        pat.display_pat()


# display all procedures with d1 at main menu
def display_all_procedure_records():
    global procedures
    for pat in procedures:
        proclist = procedures[pat]
        for proc in proclist:
            proc.display_procedure()


# import patients from JSON file
def import_patient_json():
    global patients
    file_name = input('Enter JSON file name to import patient from: ')
    try:
        with open(file_name, 'r') as file:
            patients_dict = json.load(file)
        for p in patients_dict['patients']:
            pid = p['pid']
            fname = p['fname']
            lname = p['lname']
            street = p['street']
            city = p['city']
            state = p['state']
            zipcode = p['zipcode']
            phone = p['phone']
            emerg_name = p['emerg_name']
            emerg_phone = p['emerg_phone']
            pat = patient.Patient(pid, fname, lname, street, city, state, zipcode, phone, emerg_name, emerg_phone)
            patients[pid] = pat
        print('Records successfully imported from \'' + file_name + '\'')
        input('Press Enter to continue.')
    except IOError:
        print('File not found.')
        input('Press Enter to continue to main menu.')


# export patients list to JSON file
def export_patient_json():
    global patients
    run = True
    patients_dict = {'patients': []}
    file_name = input('Enter .JSON file name to export patients to: ')
    while run:
        # check for existing file
        if path.exists(file_name):
            print('FILE ALREADY EXISTS! PROCEEDING WILL OVERWRITE CURRENT FILE!')
            # option to choose new file name or overwrite existing.
            choice = input('Press 1 to enter a new filename, any other key to continue and overwrite: ')
            if choice == '1':
                file_name = input('Please enter the filename to save patient records to: ')
                run = True
            else:
                run = False
        else:
            run = False
    for pat in patients:
        p = patients[pat]
        pid = p.get_id()
        fname = p.get_fname()
        lname = p.get_lname()
        street = p.get_street()
        city = p.get_city()
        state = p.get_state()
        zipcode = p.get_zipcode()
        phone = p.get_phone()
        emerg_name = p.get_emerg_name()
        emerg_phone = p.get_emerg_phone()
        patients_dict['patients'].append({'pid': pid, 'fname': fname, 'lname': lname, 'street': street, 'city': city,
                                          'state': state, 'zipcode': zipcode, 'phone': phone, 'emerg_name': emerg_name,
                                          'emerg_phone': emerg_phone})
    with open(file_name, 'w') as file:
        json.dump(patients_dict, file, indent=4)
    print('Records successfully exported to \'' + file_name + '\'')
    input('Press Enter to continue.')


# import procedures from JSON file
def import_procedure_json():
    global procedures
    file_name = input('Enter JSON file name to import procedures from: ')
    try:
        with open(file_name, 'r') as file:
            procedures_json = json.load(file)
            for p in procedures_json['procedures']:
                pid = p['pid']
                pname = p['pname']
                date = p['date']
                dname = p['dname']
                cost = p['cost']
                proc = procedure.Procedure(pid, pname, date, dname, cost)
                if pid in procedures:
                    proclist = procedures[pid]
                    proclist.append(proc)
                    procedures[pid] = proclist
                else:
                    proclist = [proc]
                    procedures[pid] = proclist
        print('Records successfully imported from \'' + file_name + '\'')
        input('Press Enter to continue.')
    except IOError:
        print('File not found.')
        input('Press Enter to return to main menu')


# export procedures to JSON file
def export_procedure_json():
    global procedures
    run = True
    procedures_json = {'procedures': []}
    file_name = input('Enter JSON file name to export procedures to: ')
    while run:
        # check for existing file
        if path.exists(file_name):
            print('FILE ALREADY EXISTS! PROCEEDING WILL OVERWRITE CURRENT FILE!')
            # option to choose new file name or overwrite existing.
            choice = input('Press 1 to enter a new filename, any other key to continue and overwrite: ')
            if choice == '1':
                file_name = input('Please enter the filename to save patient records to: ')
                run = True
            else:
                run = False
        else:
            run = False
    for p in procedures:
        plist = procedures[p]
        for proc in plist:
            procedures_json['procedures'].append({'pid': proc.get_pid(),
                                                  'pname': proc.get_pname(),
                                                  'date': proc.get_date(),
                                                  'dname': proc.get_dname(),
                                                  'cost': proc.get_cost()})
    with open(file_name, 'w') as file:
        json.dump(procedures_json, file, indent=4)
    print('Records successfully exported to  \'' + file_name + '\'')
    input('Press Enter to continue.')


# save patients dictionary to dat file
def export_patients_dat():
    global patients
    # loop boolean
    run = True
    run2 = True
    file_name = input('Please enter the filename to save patient records to: ')
    while run:
        # check for existing file to warn of overwrite
        if path.exists(file_name):
            print('FILE ALREADY EXISTS! PROCEEDING WILL OVERWRITE CURRENT FILE!')
            # option to choose new file name or overwrite existing.
            choice = input('Press 1 to enter a new filename, any other key to continue and overwrite: ')
            if choice == '1':
                file_name = input('Please enter the filename to save patient records to: ')
                run = True
            else:
                run = False
        else:
            run = False
    while run2:
        try:
            # pickle and dump dictionary
            file = open(file_name, 'wb')
            pickle.dump(patients, file)
            file.close()
            run2 = False
            print('Records successfully exported to', file_name)
            input('Press Enter to return to main menu. ')
        except IOError:
            choice = input('File not found. Enter 1 to re-enter file name, or any other key to return to main menu')
            if choice == "1":
                file_name = input('Enter file name.')
            else:
                run2 = False


# save procedures to dat file
def export_procedures_dat():
    global procedures
    # loop boolean
    run = True
    run2 = True
    file_name = input('Please enter the filename to save procedure records to')
    while run:
        # check for existing file
        if path.exists(file_name):
            print('FILE ALREADY EXISTS! PROCEEDING WILL OVERWRITE CURRENT FILE!')
            # option to choose new file name or overwrite existing.
            choice = input('Press 1 to enter a new filename, any other key to continue and overwrite: ')
            if choice == '1':
                file_name = input('Please enter the filename to save patient records to: ')
                run = True
            else:
                run = False
        else:
            run = False
    while run2:
        try:
            # pickle and dump
            file = open(file_name, 'wb')
            pickle.dump(patients, file)
            file.close()
            run2 = False
            print('Records successfully exported to', file_name)
            input('Press Enter to return to main menu. ')
        except IOError:
            choice = input('File not found. Enter 1 to re-enter file name, or any other key to return to main menu')
            if choice == "1":
                file_name = input('Enter file name.')
            else:
                run2 = False


# search and display patient records, including procedures, and total charges
def display_patient():
    global patients
    # choose search method
    print('Search for patient by:')
    print('1. Patient ID')
    print('2. First and last name')
    choice = input('Selection')
    charges = 0
    # search by patient ID
    if choice == '1':
        pid = input('Enter ID of patient to display: ')
        # check if patient ID in patients dictionary, and get patient info
        if pid in patients:
            pat = patients[pid]
            # display patient information
            pat.display_pat()
            # check for patient in procedure dictionary, and get procedure(s)
            if pid in procedures:
                proclist = procedures[pid]
                for proc in proclist:
                    # display procedure(s)
                    proc.display_procedure()
                    # compute total charges
                    charges += int(proc.get_cost())
            # display total charges
            print('Total charges due: ', '${:,.2f}'.format(charges))
            input('Press enter to return to menu')
        else:
            print('Patient not found')
            input('Press Enter to continue.')
    # search by first and last name
    elif choice == '2':
        found = False
        first = input('Enter patient first name: ')
        last = input('Enter patient last name: ')
        # iterate through patients dictionary
        for p in patients:
            pat = patients[p]
            # check for both first and last name converted to lowercase to avoid case mismatch
            if pat.get_fname().lower() == first.lower() and pat.get_lname().lower() == last.lower():
                found = True
                # display patient
                pat.display_pat()
                # check for patient in procedures dictionary
                if pat.get_id() in procedures:
                    # get procedures(s)
                    proclist = procedures[pat.get_id()]
                    for proc in proclist:
                        # display procedure(s)
                        proc.display_procedure()
                        # compute cost
                        charges += int(proc.get_cost())
                # display total charges
                print('Total charges due: ', '${:,.2f}'.format(charges))
                input('Press enter to return to menu')
        if not found:
            print('Patient not found.')
            input('Press Enter to continue.')


# edit patient attributes
def edit_patient():
    global patients
    run = True
    pid = input('Please enter the ID of the patient you would like to edit: ')
    if pid in patients:
        # pull existing patient from dictionary
        pat = patients[pid]
        # loop to allow for multiple changes
        while run:
            print('Select an attribute to change or x to quit:')
            print('1. First Name: ', pat.get_fname())
            print('2. Last Name: ', pat.get_lname())
            print('3. Street Address: ', pat.get_street())
            print('4. City: ', pat.get_city())
            print('5. State: ', pat.get_state())
            print('6. Zip Code: ', pat.get_zipcode())
            print('7. Phone Number: ', pat.get_phone())
            print('8. Emergency Contact: ', pat.get_emerg_name())
            print('9. Emergency Contact Phone: ', pat.get_emerg_phone())
            choice = input('Selection: ')
            # change first name
            if choice == '1':
                new = input('Enter new First Name: ')
                pat.set_fname(new)
                print('Patient updated.')
                choice2 = input('Would you like to edit another attribute? Y to change, any other key to exit ')
                if choice2 == 'Y' or choice2 == 'y':
                    run = True
                else:
                    run = False
            # change last name
            elif choice == '2':
                new = input('Enter new Last Name: ')
                pat.set_lname(new)
                print('Patient updated.')
                choice2 = input('Would you like to edit another attribute? Y to change, any other key to exit ')
                if choice2 == 'Y' or choice2 == 'y':
                    run = True
                else:
                    run = False
            # change street address
            elif choice == '3':
                new = input('Enter new Street Address: ')
                pat.set_street(new)
                print('Patient updated.')
                choice2 = input('Would you like to edit another attribute? Y to change, any other key to exit ')
                if choice2 == 'Y' or choice2 == 'y':
                    run = True
                else:
                    run = False
            # change city
            elif choice == '4':
                new = input('Enter new city: ')
                pat.set_city(new)
                print('Patient updated.')
                choice2 = input('Would you like to edit another attribute? Y to change, any other key to exit ')
                if choice2 == 'Y' or choice2 == 'y':
                    run = True
                else:
                    run = False
            # change state
            elif choice == '5':
                new = input('Enter new State: ')
                pat.set_state(new)
                print('Patient updated.')
                choice2 = input('Would you like to edit another attribute? Y to change, any other key to exit ')
                if choice2 == 'Y' or choice2 == 'y':
                    run = True
                else:
                    run = False
            # change zip code
            elif choice == '6':
                new = input('Enter new Zip Code: ')
                pat.set_zipcode(new)
                print('Patient updated.')
                choice2 = input('Would you like to edit another attribute? Y to change, any other key to exit ')
                if choice2 == 'Y' or choice2 == 'y':
                    run = True
                else:
                    run = False
            # change phone number
            elif choice == '7':
                new = input('Enter new Phone Number: ')
                pat.set_phone(new)
                print('Patient updated.')
                choice2 = input('Would you like to edit another attribute? Y to change, any other key to exit ')
                if choice2 == 'Y' or choice2 == 'y':
                    run = True
                else:
                    run = False
            # change emergency contact
            elif choice == '8':
                new = input('Enter new Emergency Contact: ')
                pat.set_emerg_name(new)
                print('Patient updated.')
                choice2 = input('Would you like to edit another attribute? Y to change, any other key to exit ')
                if choice2 == 'Y' or choice2 == 'y':
                    run = True
                else:
                    run = False
            # change emergency contact phone number
            elif choice == '9':
                new = input('Enter new Emergency Contact Phone: ')
                pat.set_emerg_phone(new)
                print('Patient updated.')
                choice2 = input('Would you like to edit another attribute? Y to change, any other key to exit ')
                if choice2 == 'Y' or choice2 == 'y':
                    run = True
                else:
                    run = False
            # exit
            elif choice == 'x' or choice == 'X':
                run = False
            else:
                print('Invalid Selection')
        # reassign updated patient back to dictionary
        patients[pid] = pat
        print('Patient records successfully updated.')
        input('Press Enter to return to main menu.')
    else:
        print('Patient not found')
        input('Press Enter to return to main menu.')


# remove patient from dictionary
def delete_patient():
    global patients
    pid = input('Please enter the ID of the patient you would like to remove: ')
    # check for patient
    if pid in patients:
        # show info for patient and procedures to be deleted for verification
        print('Patient Info:')
        pat = patients[pid]
        pat.display_pat()
        if pid in procedures:
            proclist = procedures[pid]
            for p in proclist:
                p.display_procedure()
        # confirmation of deletion
        choice = input('Are you sure you would like to delete this record? Y/N')
        if choice == 'Y' or choice == 'y':
            # delete patient and procedures for specified patient
            del patients[pid]
            del procedures[pid]
            input('Patient record deleted, press enter to return to main menu')
    else:
        print('Patient ID not found')
        input('Press Enter to return to main menu.')


def main():
    global patients
    global procedures
    run = True
    load_patients()
    load_procedures()
    while run:
        print('Main Menu - choose option from the following:')
        print('1. Add a new patient')
        print('2. Add a new procedure for an existing patient')
        print('3. Display patient information')
        print('4. Change patient information')
        print('5. Delete patient and procedures')
        print('6. Import/export patient data from txt, dat, or json file')
        print('7. import/export procedure data from txt, dat, or json file')
        print('8. Exit')
        choice = input('Selection: ')
        if choice == '1':
            add_patient()
        elif choice == '2':
            add_procedure()
        elif choice == '3':
            display_patient()
        elif choice == '4':
            edit_patient()
        elif choice == '5':
            delete_patient()
        elif choice == '6':
            print('1. Import patients')
            print('2. Export patients')
            choice2 = input('Selection')
            if choice2 == '1':
                print('Choose file type:')
                print('1. txt')
                print('2. dat')
                print('3. JSON')
                choice3 = input('Selection')
                if choice3 == '1':
                    import_patients_txt()
                elif choice3 == '2':
                    import_patients_dat()
                elif choice3 == '3':
                    import_patient_json()
                else:
                    print('Invalid Selection')
            elif choice2 == '2':
                print('Choose file type for export:')
                print('1. dat')
                print('2. JSON')
                choice4 = input('Selection')
                if choice4 == '1':
                    export_patients_dat()
                elif choice4 == '2':
                    export_patient_json()
                else:
                    print('Invalid selection')
            else:
                print('Invalid Selection')
        elif choice == '7':
            print('1. Import procedures')
            print('2. Export procedures')
            choice5 = input('Selection')
            if choice5 == '1':
                print('Choose file type for import')
                print('1. txt')
                print('2. dat')
                print('3. JSON')
                choice6 = input('Selection')
                if choice6 == '1':
                    import_procedures_txt()
                elif choice6 == '2':
                    import_procedures_dat()
                elif choice6 == '3':
                    import_procedure_json()
                else:
                    print('Invalid selection')
            elif choice5 == '2':
                print('Choose file type for export')
                print('1. dat')
                print('2. JSON')
                choice7 = input('Selection')
                if choice7 == '1':
                    export_procedures_dat()
                elif choice7 == '2':
                    export_procedure_json()
                else:
                    print('Invalid Selection')
            else:
                print('Invalid Selection')
        elif choice == '8':
            save_patients()
            save_procedures()
            run = False
        elif choice == 'd1':
            display_all_procedure_records()
        elif choice == 'd2':
            display_all_patient_records()
            

main()
