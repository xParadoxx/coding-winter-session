"""
we have dealt with while loops so far, but note: there is always danger with while loops that the condition associated
with the while loop will never terminate (aka evaluate to False)

if that happens, the loop will continue running forever --> we call this an infinite loop

if you do end up with an infinite loop, you can force python to break out of it by hitting ctrl-c on your keyboard or
the little stop button on the run console

while True:
    print("okok")
"""

"""
there are two special commands (keywords) called
--> break
--> continue
you can use inside of a while loop to further control the flow of repetition 
these commands can only be used inside of a loop; they won't work anywhere else inside of your program
"""

"""
break command:
    this is used to immediately end the loop
    once a break statement is encountered, the loop immediately stops and python resumes execution on the line directly
    after the end of the loop
"""

# # create a counter variable
# counter = 0
#
# # enter an infinite loop
# while True:
#     # add 1 to our counter variable
#     counter += 1
#     print(f"counter is at {counter}")
#     if counter >= 5:
#         print("breaking the loop!!!")
#         break

"""
continue command:
    this is used to cause the loop to immediately cease its current iteration and re-evaluate its boolean-condition
    the continue command does not end the loop - it simply causes the loop to "jump" to the next iteration
    if the condition evaluates to True, the loop iterates again, but if it evaluates to False, it will not
"""


counter = 0

while counter < 100:
    # add 1 to our counter variable
    counter += 1
    if counter % 2 == 0:
        print("even number!!!")
        continue

    # if counter >= 100:
    #     print("breaking the loop")
    #     break

    print(f"counter is {counter}")


