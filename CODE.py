import time
repeats = 0
while repeats == 0:
    var = input("What do you think is worse for the environment: BEEF or CHICKEN? ")
    if var[0].lower() == 'c':
        print("It's actually BEEF!")
        time.sleep(0.5)
    elif var[0].lower() == 'b':
        print("It is indeed BEEF!")
        time.sleep(0.5)
        pts=pts+1
    print('')
    var = int(input('How many times worse do you think BEEF is than CHICKEN for carbon emmissions? '))
    if var >= 8 and var <= 12:
        print('Well done! BEEF emits around 10 times more carbon dioxide than CHICKEN.')
        time.sleep(0.5)
        pts=pts+1
    else:
        print("BEEF actually emits closer to 10 times more carbon dioxide than CHICKEN!")
        time.sleep(0.5)
    print('')
    
    var = input("What do you think is worse for the environment: CHICKEN or DARK CHOCOLATE? ")
    if var[0].lower() == 'c':
        print("It's actually DARK CHOCOLATE!")
        time.sleep(0.5)
    elif var[0].lower() == 'd':
        print("It is indeed DARK CHOCOLATE!")
        time.sleep(0.5)
        pts=pts+1
    print('')
    var = int(input('How many times worse do you think DARK CHOCOLATE is than CHICKEN for carbon emmissions? '))
    if var >= 2 and var <= 5:
        print('Well done! DARK CHOCOLATE emits around 3.4 times more carbon dioxide than CHICKEN.')
        time.sleep(0.5)
        pts=pts+1
    else:
        print("DARK CHOCOLATE actually emits closer to 3.4 times more carbon dioxide than CHICKEN!")
        time.sleep(0.5)
    print('')
    
    var = input("What do you think is worse for the environment: DARK CHOCOLATE or TOFU? ")
    if var[0].lower() == 't':
        print("It's actually DARK CHOCOLATE!")
        time.sleep(0.5)
    elif var[0].lower() == 'd':
        print("It is indeed DARK CHOCOLATE!")
        time.sleep(0.5)
        pts=pts+1
    print('')
    var = int(input('How many times worse do you think DARK CHOCOLATE is than TOFU for carbon emmissions? '))
    if var >= 9 and var <= 13:
        print('Well done! DARK CHOCOLATE emits around 11.3 times more carbon dioxide than TOFU.')
        time.sleep(0.5)
        pts=pts+1
    else:
        print("DARK CHOCOLATE actually emits closer to 11.3 times more carbon dioxide than TOFU!")
        time.sleep(0.5)
    print('')
    
    var = input("What do you think is worse for the environment: TOFU or PULSES (eg lentils, chickpeas, beans, peas etc)? ")
    if var[0].lower() == 'p':
        print("It's actually TOFU!")
        time.sleep(0.5)
    elif var[0].lower() == 't':
        print("It is indeed TOFU!")
        time.sleep(0.5)
        pts=pts+1
    print('')
    var = int(input('How many times worse do you think TOFU is than PULSES for carbon emmissions? '))
    if var >= 1.5 and var <= 2.5:
        print('Well done! TOFU emits around 2 times more carbon dioxide then PULSES.')
        time.sleep(0.5)
        pts=pts+1
    else:
        print("TOFU actually emits closer to 2 times more carbon dioxide than PULSES!")
        time.sleep(0.5)
    print('')
    
    var = int(input('How many times worse do you think BEEF is than PULSES for carbon emmissions? '))
    if var >= 50 and var <= 90:
        print('Well done! BEEF emits between 50 and 90 times more carbon dioxide then PULSES.')
        time.sleep(0.5)
        pts=pts+1
    else:
        print("BEEF actually emits between 50 and 90 times more carbon dioxide than PULSES!")
        time.sleep(0.5)
    print('')
    
    
    var = int(input("What percentage of the average person's carbon emmisions is food? "))
    if var >= 20 and var <= 30:
        print("Well done! 20 to 30 percent of the average person's carbon emmisions is food.")
        time.sleep(0.5)
        pts=pts+1
    else:
        print("Food actually makes up 20 to 30 percent of the average person's carbon emmisions!")
        time.sleep(0.5)
    print('')
    
    print('This all means that switching from eating a meat centered diet to one of vegetarianism reduces your total carbon emmisions by roughly 12.5%!')
    time.sleep(2)
    print('That equates to 1.6 tonnes of CO2 for the average UK citizen.')
    time.sleep(1.5)
    print('Your diet makes a huge difference on the environment.')
    time.sleep(1.5)
    print('')
    print('And well done for getting '+str(pts)+'/10 points on the quiz!!')
    check = input('')
    if check == 'no':
        repeats = 1
    else:
        repeats = 0
