# Countdown app

## About the project
This app is used for Countdown ,and you can start it, stop it and also reset the app.

# Introduction Video of the Website


https://user-images.githubusercontent.com/75939608/232629209-9d05f04e-c0b2-4e1f-badd-c5c5f06a25a8.mov




## Tech stack
- Backend technologies : 
    - Python v3.10.x or higher
    - Libraries
        - tk
        - tkinter.messagebox
        - time
        - playsound

## About application

- I initialized the GUI with the following elements :

    - root
    - heading label
    - start button
    - stop button
    - reset button
    - a frame which shows current time
    - hours,minutes,seconds entries and labels
        
- I used the following functions for the commands: 
    - countdown:
        I used try and except method if there is a value error to show the warning with tkinter.messagebox.
        First I created times variable to get sum of seconds by converting hours and minutes into seconds.
        Then i used if else statement if user adds not input ,then it will show warning message for user to add time.
        I created while loop and  it goes till our times variable is equal to 0. 
        I created minute and second variable by dividing times ,and the remainder is equal to seconds 
        Then I created if statement to check if minute is more than 60 ,then it creates new value for minute and creates variable for hour.
        Then i created 3 if statements for checking if there hour,minute and second is less then 10 then it will be seen with 0 in front of our number
        I set hour,minute and second variables for our entry
        Then I updated root and used time.sleep function to make our while loop to wait 1 second every time
        Then new if statement comes for checking if time is equal to 0 ,it means time is out and it show message ,play sound and set all the entries as default value
        I created an if statement for checking if our global variable do_tick is true or not,if it is true then it stops the countdown.
        I Subtract our times variable every time with value 1 

    - start: 
        if user click to start button it will get global do_tick variable and make it False and call countdown function and our time starts as per added values to our entries

    - stop: 
        If user click stop button then our global do_tick variable be True and then our countdown app stops because in the above i have added if statement that if do_tick is True brake the app

    - reset: 
        First it ask from user if he/she wants to reset or not.
        If it is yes,then it gets global variable do_tick and make it True firstly to stop our countdown and then set all the entries as "00"
    - clock:
        It gets current time by help of time module
        Then it changes label every second by help of after method.

