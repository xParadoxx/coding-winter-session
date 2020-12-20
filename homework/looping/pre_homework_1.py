"""
Write a program that validates a password for some service (whatever you want). Allow the user to have 5 attempts.
Make good use of functions, loops, and global variables.
"""

PASSWORD = "password"


def get_password_attempt():
    attempt = input("whats your password? ")
    return attempt


def main():
    attempt_count = 0
    attempt = get_password_attempt()
    successful_login = True  # this variable is called a flag --> boolean
    while attempt != PASSWORD:  # the inputted password is incorrect
        attempt_count += 1
        print("that's the wrong password!")
        attempt = get_password_attempt()
        if attempt_count >= 4:
            print("you're out of password attempts chief")
            successful_login = False
            break

    if successful_login:
        print("\ngood job for logging")
    else:
        print("\nnope you're not getting in")


main()
