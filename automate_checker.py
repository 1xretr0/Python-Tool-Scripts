def automate():
    time_to_automate = int(input('Time to Automate: '))
    time_to_perform = int(input("Time to perform: "))
    times_done = int(input("Amount of times done: "))

    if time_to_automate < (time_to_perform * times_done):
        return True
    else:
        return False

if automate():
    print('Automate it!')
else:
    print('Do it Manually.')

