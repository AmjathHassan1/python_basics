from authentication import Authentication
import constance
import utils

def main():
    try:
        print("\n\nWelcome to Student Management System\n\n")
        print("===================================== LOGIN ======================================")



        # username="mini@gmail.com"
        # password="mini"
        auth_user=False
        while not auth_user:
            username = input("Enter your username: ")
            password = input("Enter your password: ")
            # username = "mini@gmail.com"
            # password="mini"
            auth = Authentication(constance.USER_CSV_LOCATION)
            auth_user=auth.authenticate(username, password)

        if auth_user:
            menu_obj = utils.MenuPicker()
            menu_selected = False
            repeat = False
            while not repeat:
                while not menu_selected:
                    utils.MenuPicker.show_menu()
                    menu_selected = menu_obj.input_menu()

                curd_obj=utils.CrudStudent(constance.STUDENT_CSV_LOCATION)

                if int(menu_selected) == 1:
                    curd_obj.view_student()
                elif int(menu_selected) == 2:
                    curd_obj.add_student()
                elif int(menu_selected) == 3:
                    curd_obj.update_student()
                elif int(menu_selected) == 4:
                    curd_obj.delete_student()
                elif int(menu_selected) == 5:
                    curd_obj.search_student()
                elif int(menu_selected) == 6:
                    curd_obj.view_top_students()
                else:
                    print("Login out.................!\n")
                    break

                repeat_input = input("\nDo you wish to repeat menu? (y/n): ")
                if repeat_input == "y":
                    repeat = False
                    menu_selected = False
                else:
                    print("Login out.................!\n")
                    repeat = True


    except Exception as error:
        print(error)


if __name__ == '__main__':
    main()