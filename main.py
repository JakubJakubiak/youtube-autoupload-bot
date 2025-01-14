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
    bot = webdriver.Chrome(executable_path="chromedriver.exe", options=options)
    bot.get("https://studio.youtube.com")

    wait_and_click(bot, '//*[@id="upload-icon"]')

    file_input = bot.find_element(By.XPATH, '//*[@id="content"]/input')
    file_input.send_keys(video_path)

    wait_and_click(bot, '//*[@name="VIDEO_MADE_FOR_KIDS_NOT_MFK"]')
    
    description_input = bot.find_element(By.XPATH, '//*[@id="textbox"]')
    description_input.clear()
    description_input.send_keys("Film title")

    for _ in range(3):
        wait_and_click(bot, '//*[@id="next-button"]')
        print("1  ///// wait_and_click(bot, '//*[@idnext-button]')")
    
    wait_and_click(bot, '//*[@name="PUBLIC"]')
    print("2 ///// //*[@id=PUBLIC]')")

    wait_and_click(bot, '//*[@id="enable-premiere-checkbox"]')
    print("3 ///// //*[@id=enable-premiere-checkbox]')")
    
    wait_and_click(bot, '//*[@id="done-button"]')
    print("4 ///////[@id=done-button]")

    time.sleep(2)
    bot.quit()
    time.sleep(2)

def main():
    print("\033[1;31;40m IMPORTANT: Put one or more videos in the *videos* folder in the bot directory.")
    dir_path = '.\\videos'
    videos = [path for path in os.listdir(dir_path) if os.path.isfile(os.path.join(dir_path, path))]  
    
    if not videos:
        print("No videos found in the videos folder.")
        return  
    
    print("   ", len(videos), " Videos found in the videos folder, ready to upload...")
    time.sleep(1)   
    
    for video in videos:
            video_path = os.path.abspath(os.path.join('videos', video))
            upload_video(video_path)

if __name__ == "__main__":
    main()
