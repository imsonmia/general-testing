# Git VCS linked to GitHub repository
# Last Edited 2021-01-27 15:54:09
import time


def main():  # Main feature of the program
    print("If you see this string, you've successfully logged in")
    return


if __name__ == '__main__':  # Check if the program is used a a module
    try:
        usr_cache = open(file="usr_cache.txt", mode='r', buffering=1)
        password_cache = open(file='pass_cache.txt', mode='r', buffering=1)
        user_current = usr_cache.read()
        pass_current = password_cache.read()

        if user_current != '' and pass_current != '':
            print(f"Logged in as user {user_current}")
            usr_cache.close()
            password_cache.close()
            main()  # Made the main feature a function to make the code more readable

        elif user_current == '' and pass_current != '':
            pass_check = str(input("Type in your password to verify this is you: "))
            tries = 0

            while pass_check != pass_current:
                if tries <= 5:
                    pass_check = str(input(f"Password incorrect, try again, you have {str(5-tries)} tries left: "))
                else:
                    print("Too many tries! You are timed out for 20 seconds before you try again.")
                    time.sleep(20)
                    pass_check = str(input("Try again"))
            new_user = str(input("Your username is EMPTY, put in a username: "))

            new_user_data = open(file="usr_cache.txt", mode='w', buffering=1)
            new_user_data.write(new_user)
            new_user_data.close()
            input('Press ENTER key to continue...')
            main()

        elif pass_current == '' and user_current != '':
            user_check = str(input("Type in your username to verify this is you: "))
            tries = 0
            while user_check != user_current:
                if tries <= 5:
                    pass_check = str(input(f"Username incorrect, try again, you have {str(5 - tries)} tries left: "))
                else:
                    print("Too many tries! You are timed out for 20 seconds before you try again.")
                    time.sleep(20)
                    pass_check = str(input("Try again"))
            new_pass = str(input("Your password is EMPTY, put in a password: "))

            new_pass_data = open(file="pass_cache.txt", mode='w', buffering=1)
            new_pass_data.write(new_pass)
            new_pass_data.close()
            input('Press ENTER key to continue...')
            main()

        elif user_current == ''and pass_current == '':
            print("It seems that you are a new user or your username and password data isn't saved successfully")
            new_user = input("Enter a username: ")
            new_pass = input("Enter a password: ")
            pass_verify = input("Enter your password again to verify it: ")
            while new_pass != pass_verify:
                pass_verify = str(input("Verification failed, please retry: "))
            print("Successful!")
            new_user_write_file = open(file="usr_cache.txt", mode='w', buffering=1)
            new_pass_write_file = open(file="pass_cache.txt", mode='w', buffering=1)
            new_user_write_file.write(new_user)
            new_pass_write_file.write(new_pass)
            new_user_write_file.close()
            new_pass_write_file.close()
        else:
            print('Unknown Error, contact author at imsonmia@outlook.com for support')
    except FileNotFoundError:
        print("Didn't detect files, making new ones...")
        new_file_usr = open(file="usr_cache.txt", mode='x', buffering=1)
        new_file_pass = open(file="pass_cache.txt", mode='x', buffering=1)
        print("Files created successfully, please restart the program.")
