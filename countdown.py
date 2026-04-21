import time 

def countdown(time_sec):
    while True:
        time_sec -= 1
        time.sleep(1)
        print(f"{time_sec}秒")
        if time_sec == 1:
            print("時間です！")
            break

def pomodoro(sessions, focus, rest):
    for count in range(sessions):
        print("集中タイム開始！")
        countdown (focus * 60)
        print("休憩タイム開始！")
        countdown(rest * 60)

pomodoro(3, 25, 5)
