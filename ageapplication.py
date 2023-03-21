#An application that calculates the age of 10 students
date_of_birth = [2015, 2010, 2005, 2018, 1997, 2014, 2012, 2000, 2019, 1948] #int
name_of_student = ["harry", "bruno", "mason", "anthony", "sabitzer", "erik", "fred", "charles", "david","makason"] #str
current_year = 2023 #int
average_age = 18 #int

def age_cal():
    name_of_student = input("enter student name: ")
    age_calculation = int(input("enter student date of birth: "))
    if age_calculation > 2006 :
        final_age = current_year - age_calculation
        print(name_of_student, "hello you are", final_age, "years old")
    else:
        final_age = current_year - age_calculation
        print(name_of_student, "sorry you are", final_age, "years old","expected year is 18 and above")
age_cal()
