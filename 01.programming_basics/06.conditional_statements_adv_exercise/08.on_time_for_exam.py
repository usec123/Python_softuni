from math import trunc
exam = int(input()) * 60 + int(input())
arr = int(input()) * 60 + int(input())

if arr <= exam:
    if arr >= exam-30: print('On time')
    else: print('Early')
    if (arr!=exam): 
        if (exam-arr > 59): print(f'{trunc((exam-arr)/60)}:{(exam-arr)%60:02d} hours before the start')
        else: print(f'{exam-arr} minutes before the start')
if arr > exam:
    print('Late')
    if (arr-exam > 59): print(f'{trunc((arr-exam)/60)}:{(arr-exam)%60:02d} hours after the start')
    else: print(f'{arr-exam} minutes after the start')