import datetime
import re

def update_dday_in_readme():
    # Define the target date
    target_date = datetime.datetime(2025, 12, 8).date()
    today = datetime.date.today()
    
    # Calculate the difference
    time_remaining = target_date - today
    days = time_remaining.days
    
    # Create the D-day string
    if days > 0:
        dday_string = f"**기말고사 시작까지 D-{days}**"
    elif days == 0:
        dday_string = "**기말고사 D-Day! 행운을 빌어요! 🍀**"
    else:
        dday_string = f"**기말고사가 D+{abs(days)}일 지났습니다.**"

    # Read the README.md file
    try:
        with open("README.md", "r", encoding="utf-8") as f:
            content = f.read()
    except FileNotFoundError:
        print("Error: README.md not found.")
        return

    # Replace the content between the markers
    # Using regex with re.DOTALL to match across newlines
    new_content = re.sub(
        r"(?<=<!-- D-DAY-START -->\n).*(?=\n<!-- D-DAY-END -->)",
        dday_string,
        content,
        flags=re.DOTALL
    )

    # Write the updated content back to the file
    with open("README.md", "w", encoding="utf-8") as f:
        f.write(new_content)
        
    print("README.md 파일에 D-day를 성공적으로 업데이트했습니다!")

if __name__ == "__main__":
    update_dday_in_readme()
