# -*- coding: utf-8 -*-
"""
Created on Wed Jun  3 11:57:02 2020

@author: adhish
"""

# This script will allow you to set a time daily to check your USCIS case status
#https://towardsdatascience.com/controlling-the-web-with-python-6fceb22c5f08
#https://realpython.com/modern-web-automation-with-python-and-selenium/

from selenium import webdriver
import filecmp
import os.path
import time
#from sys import exit

arr = os.listdir()

def main_func():
    driver = webdriver.Chrome(executable_path=r'C:/USCIS_case_status_check/chromedriver_win32/chromedriver.exe')
        
    # Open the website
    driver.get('https://egov.uscis.gov/casestatus/landing.do')
    
    # Select the id box
    id_box = driver.find_element_by_id('receipt_number')
            
    # Send id information

    id_box.send_keys(user_id)
    id_box.submit()
    
    results = driver.find_elements_by_xpath('/html/body/div[2]/form/div/div[1]/div/div/div[2]/div[3]/p')
    
    with open("Current_Status.txt", "w") as file:
        file.write(results[0].text)
    
    #Find the current timestamp
#    timestr = time.strftime("%Y%m%d")
#    even = int(timestr)%2==0
#    
    if 'Old_Status.txt' not in arr and 'New_Status.txt' not in arr:
        with open("Old_Status.txt", "w") as file:
            file.write(results[0].text)
        with open("New_Status.txt", "w") as file:
            file.write(results[0].text)
        if filecmp.cmp('Old_Status.txt', 'New_Status.txt') is True :
            print('\n\nYour USCIS status has not changed, the old status is: \n\n')
            f = open('Old_Status.txt', 'r')
            file_contents = f.read()
            print(file_contents)
        else:
            print('\n\n CONGRATULATIONS! Your USCIS status has changed to : \n\n')
            f = open('New_Status.txt', 'r')
            file_contents = f.read()
            print(file_contents)
            
    elif 'Old_Status.txt' in arr and 'New_Status.txt' in arr:
        with open("New_Status.txt", "w") as file:
            file.write(results[0].text)
        if filecmp.cmp('Old_Status.txt', 'New_Status.txt') is True :
            print('\n\nYour USCIS status has not changed, the old status is: \n\n')
            f = open('Old_Status.txt', 'r')
            file_contents = f.read()
            print(file_contents)
        else:
            print('\n\n CONGRATULATIONS! Your USCIS status has changed to : \n\n')
            f = open('New_Status.txt', 'r')
            file_contents = f.read()
            print(file_contents)
    
    else:
        print("Unknown error, try again!")
    
    driver.quit()
    
    print('\n\nYour current status is: \n\n')
    f = open('Current_Status.txt', 'r')
    file_contents = f.read()
    print(file_contents)
    
    print('\n\nThis screen will close in 10 seconds\n\n')
    time.sleep(10)

    

if 'USCIS_case_number.txt' not in arr:
    # Enter user id
    user_id = input('Enter your USCIS receipt number: ')
    with open("USCIS_case_number.txt", "w") as file:
        file.write(user_id)
    main_func()

else:
    
    f = open('USCIS_case_number.txt', 'r')
    user_id = f.read()

# Using Chrome to access web
    main_func()
