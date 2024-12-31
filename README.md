# University APP

This is our University Enrollment System App 

## Dependencies Installation
```
pip install -r requriments.txt
```
## Tkinter installation via apt
```
sudo apt install python3-tk
```

To run the CLI App please run the main.py with command 
```
python3 main.py
```

To run the GUI App please run the user_interface.py with command 
```
python3 user_interface.py
```

We have 2 system are **ADMIN** and **STUDENT** system 

## Student System 
We allow student to 
1) Register and login to their account 
2) They can **enroll** to maximum **4** subject
    When they enroll, the random subject will assign to them with the random mark
3) They can remove the subject, 
4) Change their password 
5) View their enrolled subjects 

## Admin System
Admin can do some functionality: 
1) Clear the system database
2) View all the student in system
3) Get student by grade
4) Categories students by PASS/FAIL
5) Remove student by id
