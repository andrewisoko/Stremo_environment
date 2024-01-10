from urllib.request import urlopen
from bs4 import BeautifulSoup
from winotify import Notification, audio
import schedule
import time as tm


# Notification

url = "https://www.vipstand.st/football-live-sports-stream"

html_code = urlopen(url)

soup = BeautifulSoup(html_code, 'lxml')

column = soup.find_all('div', class_="col-12 col-lg-8")


def Teams():
    toast = Notification(app_id="NeuralNine_Script",
                         title="VPN STAND",
                         msg="Match Live Now! ",
                         duration='long',
                         icon=r"C:\Users\aw11c\OneDrive\Pictures\Camera Roll\football_images.png"
                         )

    toast.add_actions(
        label="Click", launch="https://www.vipstand.st/football-live-sports-stream")

    toast.set_audio(audio.LoopingAlarm, loop=False)

    # Teams searching

    for teams in column:
        football_teams = teams.text
        if 'Manchester City' in football_teams:
            print('Man-City is playing today')
            toast.show()

        if 'Bareclona' in football_teams:
            print('Napoli is playing today')
            toast.show()

        if 'Arsenal' in football_teams:
            print('arsenal is playing today ')
            toast.show()

        if 'Internazionale' in football_teams:
            print("Internazionale is playing today")
            toast.show()

# Scheduling


schedule.every(5).seconds.do(Teams)

while True:
    schedule.run_pending()
    tm.sleep(1)
