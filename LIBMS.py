Book_list = ['Sanskrit','Hindi','English','Mathematics','Biology','Physics','Chemistry',
             'Economics','Geography','History','Civics']
Student_Book_list = {}
#Issued_Book = []
while True:
    Issued_Book = []
    user_input = int(input('Welcome to the Library\nEnter your choice of service\n1. Book issue\n2. Book Deposit'
                           '\n3. Administration Menu\n4. Exit\n'))
    if user_input==1:
        Student_name = input('Enter the student name\n')
        Book_issue = (input('Enter the Book name\n')).title()
        if Student_name in Student_Book_list:
            if Student_name not in Student_Book_list:
                Student_Book_list.update({Student_name: Issued_Book})
            Student_Book_list[Student_name].append(Book_issue)
            Book_list.remove(Book_issue)
            print(Book_list)
            print(Student_Book_list)

        else:
            print('Student record with name {} is not found!!\nKindly create one using administration menu if you want any Books!'.format(Student_name))
    elif user_input==2:
        Student_name = input('Enter the student name\n')
        Book_deposit = (input('Enter the Book name\n')).title()
        Issued_Book.remove(Book_deposit)
        Student_Book_list.update({Student_name: Issued_Book})
        #Student_Book_list[Student_name].remove(Book_deposit)
        Book_list.append(Book_deposit)

    elif user_input==3:
        user_input1 = int(input('ADMINISTRATION MENU\n1. Create student record\n2. Display all student records\n'
                                '3. Display specific student record\n4. Modify student record\n5. Delete student record\n6. Create Book\n'
                                '7. Display all books\n8. Display specific Book\n9. Modify Book\n10. Delete Book record\n'))
        if user_input1 == 1:
            Student_name1 = input('enter the student name\n')
            Student_Book_list.update({Student_name1: Issued_Book})
            print('created student record for {}'.format(Student_name1))
        elif user_input1 == 2:
            if Student_Book_list is  {}:
                print('No student record exists!')
            else:
                print('This is the existing student record',Student_Book_list)
        elif user_input1 == 3:
            Student_name2 = input('enter the student name to see the list of books he/she have')
            Student_Book_list[Student_name2]
        elif user_input1 == 4:
            # Modifies student record
            pass
        elif user_input1 == 5:
            Student_name4 = input('enter the student name')
            if Student_name4 not in Student_Book_list:
                print('There is no student with name {}'.format(Student_name4))
            else:
                del Student_Book_list[Student_name4]
        elif user_input1 == 6:
            Book_name = input('enter the book name')
            Book_list.append(Book_name)
        elif user_input1 == 7:
            print(Book_list)
        elif user_input1 == 8:
            Book_name = input('enter the book name').title()
            if Book_name in Book_list:
                print('{} is present in Book_list'.format(Book_name))
            else:
                length_ = len(Student_Book_list)
                for i in range(0,length_):
                    if Book_name in Student_Book_list[i]:
                        print('{} is present with {}'.format(Book_name,Student_Book_list[i]))
        elif user_input1 == 9:
            pass
        elif user_input1 == 10:
            Book_name1 = input('enter the book name').title()
            Book_list.remove(Book_name1)
        #Administration menu
        pass
    elif user_input==4:
        print('Thank you!')
        break


