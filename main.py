import time
import os
from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = webdriver.ChromeOptions()
options.add_argument("--log-level=3")
options.add_argument("user-data-dir=C:\\Users\\User\\AppData\\Local\\Google\\Chrome\\User Data\\")
options.binary_location = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"


def wait_and_click(driver, xpath):
    element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, xpath)))
    element.click()


def upload_video(video_path):
    bot = webdriver.Chrome(executable_path="chromedriver.exe", chrome_options=options)
    bot.get("https://studio.youtube.com")

    wait_and_click(bot, '//*[@id="upload-icon"]')

    file_input = bot.find_element(By.XPATH, '//*[@id="content"]/input')
    file_input.send_keys(video_path)

    for _ in range(3):
        wait_and_click(bot, '//*[@id="next-button"]')

    wait_and_click(bot, '//*[@name="VIDEO_MADE_FOR_KIDS_NOT_MFK"]')
    for _ in range(3):
        wait_and_click(bot, '//*[@id="next-button"]')

    wait_and_click(bot, '//*[@name="PUBLIC"]')
    wait_and_click(bot, '//*[@id="next-button"]')

    for _ in range(3):
        wait_and_click(bot, '//*[@id="done-button"]')

    with bot:
        pass

def main():
    print("\033[1;31;40m IMPORTANT: Put one or more videos in the *videos* folder in the bot directory. Please make sure to name the video files like this --> Ex: vid1.mp4 vid2.mp4 vid3.mp4 etc..")
    time.sleep(6)
    
    # answer = input("\033[1;32;40m Press 1 if you want to spam the same video or Press 2 if you want to upload multiple videos: ")
    answer = 2

    if int(answer) == 1:
        nameofvid = input("\033[1;33;40m Put the name of the video you want to upload (Ex: vid.mp4 or myshort.mp4 etc..) ---> ")
        howmany = input("\033[1;33;40m How many times you want to upload this video ---> ")

        for i in range(int(howmany)):
            video_path = os.path.abspath(os.path.join('videos', nameofvid))
            upload_video(video_path)

    elif int(answer) == 2:
        print("\033[1;31;40m IMPORTANT: Please make sure the name of the videos is like this: vid1.mp4, vid2.mp4, vid3.mp4 ...  etc")
        dir_path = '.\\videos'
        count = len([path for path in os.listdir(dir_path) if os.path.isfile(os.path.join(dir_path, path))])

        print("   ", count, " Videos found in the videos folder, ready to upload...")
        time.sleep(6)

        for i in range(count):
            video_path = os.path.abspath(os.path.join('videos', 'vid{}.mp4'.format(i+1)))
            upload_video(video_path)

if __name__ == "__main__":
    main()
