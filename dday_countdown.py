import datetime
import time
import os

def clear_screen():
    # For Windows
    if os.name == 'nt':
        _ = os.system('cls')
    # For macOS and Linux
    else:
        _ = os.system('clear')

def dday_countdown(target_date_str):
    target_date = datetime.datetime.strptime(target_date_str, "%Y-%m-%d").date()

    while True:
        clear_screen()
        today = datetime.date.today()
        time_remaining = target_date - today

        if time_remaining.days > 0:
            print(f"기말고사 D-day: D-{time_remaining.days}")
        elif time_remaining.days == 0:
            print("기말고사 D-day: 오늘이 기말고사 시작일입니다!")
        else:
            print(f"기말고사 D-day: 기말고사가 {abs(time_remaining.days)}일 지났습니다.")
            break # Stop the countdown after the exam date has passed

        time.sleep(1)

if __name__ == "__main__":
    # The target date is 2025-12-08 as confirmed by the user
    target_date = "2025-12-08"
    dday_countdown(target_date)
