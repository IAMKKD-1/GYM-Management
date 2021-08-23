import time


def menu():
    print(" ")
    print("Welcome to Krishna's GYM!")
    print(" ")
    print("Choose your usertype")
    print(" ")
    print("Press 1: SuperUser")
    print("Press 2: Gym Member Portal")
    print("Press 3: Exit")
    print(" ")
    input1 = input("Please enter your response: ")
    if input1 == '1':
        try:
            superuser()
        except:
            print(' ')
            print("You entered wrong input!!")
            print(" ")
            print("Restarting program!")
            time.sleep(1)
            superuser()
    elif input1 == '2':
        try:
            member()
        except:
            print(' ')
            print("You entered wrong input!!")
            print(" ")
            print("Restarting program!")
            time.sleep(1)
            member()
    elif input1 == '3':
        print("Thank you!")
    else:
        print("Please Enter valid option!")
        print(" ")
        menu()


class superuser:

    def __init__(self):
        print(" ")
        print("Welcome SuperUser!")
        print(" ")
        print("Press 1: Create Member")
        print("Press 2: View Members")
        print("Press 3: Delete Member")
        print("Press 4: Update Member")
        print("Press 5: Create Regimen")
        print("Press 6: View Regimen")
        print("Press 7: Delete Regimen")
        print("Press 8: Update Regimen")
        print("Press 9: Exit")
        input2 = input("Please Enter your response: ")
        if input2 == '1':
            self.create_member()
            self.__init__()
        elif input2 == '2':
            self.view_member()
            self.__init__()
        elif input2 == '3':
            self.delete_member()
            self.__init__()
        elif input2 == '4':
            self.update_member()
            self.__init__()
        elif input2 == '5':
            self.create_regimen()
            self.__init__()
        elif input2 == '6':
            self.view_regimen()
            self.__init__()
        elif input2 == '7':
            self.delete_regimen()
            self.__init__()
        elif input2 == '8':
            self.update_regimen()
            self.__init__()
        elif input2 == '9':
            menu()
        else:
            print("Please Enter a valid option")
            self.__init__()

    regimen_table = {
        'Regimen1': {'Mon': 'Chest', 'Tue': 'Biceps', 'Wed': 'Rest', 'Thu': 'Back', 'Fri': 'Triceps', 'Sat': 'Rest',
                     'Sun': 'Rest'},
        'Regimen2': {'Mon': 'Chest', 'Tue': 'Biceps', 'Wed': 'Cardio/Abs', 'Thu': 'Back', 'Fri': 'Triceps',
                     'Sat': 'Legs', 'Sun': 'Rest'},
        'Regimen3': {'Mon': 'Chest', 'Tue': 'Biceps', 'Wed': 'Abs/Cardio', 'Thu': 'Back', 'Fri': 'Triceps',
                     'Sat': 'Legs', 'Sun': 'Cardio'},
        'Regimen4': {'Mon': 'Chest', 'Tue': 'Biceps', 'Wed': 'Cardio', 'Thu': 'Back', 'Fri': 'Triceps',
                     'Sat': 'Cardio',
                     'Sun': 'Cardio'}}

    members_detail = {}

    def create_member(self):
        print(" ")
        print("Let's create a new member!")
        print(" ")
        contact_no = input("Please enter member's contact number: ")
        while contact_no in self.members_detail:
            print("Sorry! User with this contact number exists!")
            break
        else:
            self.members_detail[contact_no] = {}

            name = input("Enter full name of member: ")
            self.members_detail[contact_no]["Full Name"] = name

            age = input("Enter Age of the member: ")
            while not age.isdigit():
                print("Age has to be a number!")
                age = input("Please enter valid input: ")
            self.members_detail[contact_no]["Age"] = age

            gender = input("Enter Gender of the member: ")
            while gender not in ['Male', 'MALE', 'male', 'M', 'm', 'Female', 'FEMALE', 'female', 'F', 'f', 'Others',
                                 'others', 'OTHERS']:
                print("Valid Gender input - Male[M], Female[F], Others")
                gender = input("Please enter a valid Gender: ")
            self.members_detail[contact_no]["Gender"] = gender

            email = input("Enter Email ID of the member: ")
            self.members_detail[contact_no]["Email"] = email

            while True:
                try:
                    bmi = float(input('Enter BMI of the member: '))
                    while not isinstance(bmi, float):
                        bmi = float(input("Please enter valid option for BMI: "))
                    self.members_detail[contact_no]['BMI'] = bmi
                except:
                    print("Please enter valid response!")
                else:
                    break

            duration = int(input("Please enter Membership duration: "))
            while duration not in [1, 3, 6, 12]:
                print("Sorry! We only have membership options for 1, 3, 6 and 12 months")
                duration = int(input("Please enter valid membership duration: "))
            self.members_detail[contact_no]['Membership Duration'] = duration

            self.members_detail[contact_no]["Workout Regimen"] = self.regimen_bmi(bmi)
            print(" ")
            print("Member Successfully Created!")
        time.sleep(1)

    def regimen_bmi(self, bmi):
        if bmi < 18.5:
            member_regimen = self.regimen_table['Regimen1']
        elif bmi < 25:
            member_regimen = self.regimen_table['Regimen2']
        elif bmi < 30:
            member_regimen = self.regimen_table['Regimen3']
        elif bmi >= 30:
            member_regimen = self.regimen_table['Regimen4']

        return member_regimen

    def view_member(self):
        input3 = input("Please enter Contact number of member: ")
        if input3 in self.members_detail:
            print(" ")
            print("Member details :- ")
            for detail in self.members_detail[input3]:
                if type(self.members_detail[input3][detail]) != dict:
                    print(f'{detail} : {self.members_detail[input3][detail]}')
                else:
                    print(" ")
                    print(detail + ":-")
                    for regime in self.members_detail[input3][detail]:
                        print(f'{regime} : {self.members_detail[input3][detail][regime]}')
        else:
            print("Sorry! Member not found.")
        time.sleep(1)

    def delete_member(self):
        input4 = input("Please enter Contact number of member: ")
        if input4 in self.members_detail:
            del self.members_detail[input4]
            print("Member Successfully Deleted!")
        else:
            print("Sorry! Member not found.")

    def update_member(self):
        input5 = input("Please enter Contact number of member: ")
        if input5 in self.members_detail:
            print(" ")
            list_num = 1
            for num in self.members_detail[input5]:
                print(f'Press {list_num}: {num}')
                list_num += 1
            update_var = input("Please enter the corresponding number to update: ")

            if update_var == '1':
                new = input("Please enter the new Full Name: ")
                self.members_detail[input5]['Full Name'] = new
                print("Name is successfully updated!")

            elif update_var == '2':
                new = input("Please enter the new Age: ")
                while not new.isdigit():
                    print("Age has to be a number!")
                    new = input("Please enter valid input: ")
                self.members_detail[input5]['Age'] = new
                print("Age is successfully updated!")

            elif update_var == '3':
                new = input("Please enter the new Gender: ")
                while new not in ['Male', 'MALE', 'male', 'M', 'm', 'Female', 'FEMALE', 'female', 'F', 'f',
                                  'Others', 'others', 'OTHERS']:
                    print("Valid Gender input - Male[M], Female[F], Others")
                    new = input("Please enter a valid Gender: ")
                self.members_detail[input5]['Gender'] = new
                print("Gender is successfully updated!")

            elif update_var == '4':
                new = input("Please enter the new Email ID: ")
                self.members_detail[input5]['Email'] = new
                print("Email ID is successfully updated!")

            elif update_var == '5':
                new = float(input("Please enter the new BMI: "))
                while not isinstance(new, float):
                    new = float(input("Please enter valid option for BMI: "))
                self.members_detail[input5]['BMI'] = new
                self.members_detail[input5]['Workout Regimen'] = self.regimen_bmi(new)
                print("BMI & Workout Regimen has been successfully updated!")

            elif update_var == '6':
                print(" ")
                print("Press 1: To Extend Membership")
                print("Press 2: To Revoke Membership")
                new = input("Please enter your response: ")
                loop_role2 = True
                while loop_role2:
                    if new == '1':
                        print("You can extend 1, 3, 6 and 12 months!")
                        new1 = int(input("Enter number of months to extend: "))
                        while new1 not in [1, 3, 6, 12]:
                            print(" ")
                            print("Sorry! We only have membership options for 1, 3, 6 and 12 months")
                            new1 = int(input("Please enter valid membership duration: "))
                        self.members_detail[input5]["Membership Duration"] += new1
                        print(
                            f'Congrats! Your membership duration is now {self.members_detail[input5]["Membership Duration"]} months!')
                        loop_role2 = False

                    elif new == '2':
                        del self.members_detail[input5]
                        print("Membership revoked and Member Deleted Successfully!")
                        loop_role2 = False

                    else:
                        print("Please enter valid response!")

            elif update_var == '7':
                print("Here are names of all the workout regimens")
                list_num2 = 1
                for names in self.regimen_table:
                    print(f'{list_num2}: {names}')
                    list_num2 += 1
                regimen = input("Please enter name of regimen to update: ")
                if regimen in self.regimen_table:
                    print(f'{self.members_detail[input5]["Full Name"]} has been assigned {regimen}')
                    self.members_detail[input5]["Workout Regimen"] = self.regimen_table[regimen]
                    print(" ")
                    print("Your updated Regimen is :- ")
                    for i in self.members_detail[input5]['Workout Regimen']:
                        print(f'{i}: {self.members_detail[input5]["Workout Regimen"][i]}')
                else:
                    print("Workout Regimen not found!")

    def create_regimen(self):
        temp_regimen = {'Mon': '', 'Tue': '', 'Wed': '', 'Thu': '', 'Fri': '', 'Sat': '', 'Sun': ''}
        print(" ")
        new_regimen = input("Please enter the name of new regimen: ")
        while new_regimen in self.regimen_table:
            print("Regimen name already exists!")
            new_regimen = input("Please enter the name of new regimen: ")
        else:
            self.regimen_table[new_regimen] = temp_regimen
            for i in self.regimen_table[new_regimen]:
                self.regimen_table[new_regimen][i] = input(f"Please enter workout for {i}: ")
            print(" ")
            print("New Workout Regimen Added Successfully!")
            print(" ")
            print(f"Workout for the {new_regimen} :- ")
            for j in self.regimen_table[new_regimen]:
                print(f"{j}:{self.regimen_table[new_regimen][j]}")
        time.sleep(1)

    def view_regimen(self):
        print(" ")
        for i in self.regimen_table:
            print(i)
        print(" ")
        reg_name = input("Please enter name of Regimen: ")
        if reg_name in self.regimen_table:
            print(f'Workout for {reg_name} is: ')
            for reg in self.regimen_table[reg_name]:
                print(f'{reg}: {self.regimen_table[reg_name][reg]}')
        else:
            print("Incorrect Regimen Name entered!")
        time.sleep(1)

    def delete_regimen(self):
        delete_reg = input("Please enter name of Regimen to delete: ")
        if delete_reg in self.regimen_table:
            del self.regimen_table[delete_reg]
            print(f"{delete_reg} Deleted Successfully")
        else:
            print("Sorry! Workout Regimen not found!")
        time.sleep(1)

    def update_regimen(self):
        print("Here are names of all the workout regimens")
        list_num2 = 1
        for names in self.regimen_table:
            print(f'{list_num2}: {names}')
            list_num2 += 1
        regimen_name = input("Please enter the name of regimen to update: ")
        if regimen_name in self.regimen_table:
            print(f"Update Workout for {regimen_name}: ")
            for reg1 in self.regimen_table[regimen_name]:
                self.regimen_table[regimen_name][reg1] = input(f"Update for {reg1}: ")
            print('Updated Regimen is:')
            for reg2 in self.regimen_table[regimen_name]:
                print(f'{reg2}: {self.regimen_table[regimen_name][reg2]}')
        else:
            print("Regimen not found!")
        time.sleep(1)


class member:

    def __init__(self):
        self.contactno = input("Please enter your contact number: ")
        if self.contactno in superuser.members_detail:
            print(f"Hello {superuser.members_detail[self.contactno]['Full Name']}")
            self.membermenu()
        else:
            print("User not found! Please ask GYM Superuser for Member Access!")

    def membermenu(self):
        print(" ")
        print("Press 1: My Profile")
        print("Press 2: My Regimen")
        mem_input = input("Please enter your response: ")
        if mem_input == '1':
            self.member_profile()
            self.membermenu()
        elif mem_input == '2':
            self.member_regimen()
            self.membermenu()
        else:
            print("Please enter valid response: ")
            self.membermenu()

    def member_profile(self):
        print(" ")
        print("Your profile :- ")
        for detail in superuser.members_detail[self.contactno]:
            if detail != 'Workout Regimen':
                print(f"{detail} : {superuser.members_detail[self.contactno][detail]}")

    def member_regimen(self):
        print(" ")
        print("Your Workout Regimen: ")
        for detail in superuser.members_detail[self.contactno]['Workout Regimen']:
            print(f"{detail} : {superuser.members_detail[self.contactno]['Workout Regimen'][detail]}")


menu()
