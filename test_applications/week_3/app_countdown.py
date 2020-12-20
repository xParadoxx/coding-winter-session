"""
Write a program that counts backwards using range()
"""

import time


def main():
    print("starting countdown!!")
    for i in range(10, 0, -1):
        time.sleep(1)  # optional
        print(i)
    time.sleep(3600)
    print("yay blastoff!!!")


main()
