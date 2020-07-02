Step 1

Make sure you have Python downloaded first(https://www.python.org/). Extract this folder directly under your C drive. The path to this folder should be 'C:\USCIS_case_status_check'

Step 2

Open Windows Scheduler by looking for it in the windows search bar, and schedule the batch file(already created) in this folder(app.bat) to be run daily. For more details, follow this link: https://datatofish.com/python-script-windows-scheduler.

Alternatively, you can double click on the "app_batch.bat" file to run the python program and see if it is working or not. 

Step 3

Visit the folder and open the file "C:\USCIS_case_status_check\Current_Status.txt" to see your current status refreshed everyday.

Step 4 

If you want you can include mailing yourself with the current status updates using selenium by following this link(https://stackoverflow.com/questions/51756066/python-w-selenium-gmail-email-send-automating-to-field-is-giving-me-trouble)
and entering your information after you include the code in the existing python script.
