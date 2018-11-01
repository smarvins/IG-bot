from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random
import sys



def print_same_line(text):
    sys.stdout.write('\r')
    sys.stdout.flush()
    sys.stdout.write(text)
    sys.stdout.flush()


class InstagramBot:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.driver = webdriver.Firefox()

    # this closes the browser if anything goes wrong
    def closeBrowser(self):
        self.driver.close()

    # this will log in to instagram
    def login(self):
        # directing the site the bot to browse in
        driver = self.driver
        driver.get("https://www.instagram.com/")
        time.sleep(2)

        # tells the bot to click the login button
        login_button = driver.find_element_by_xpath("//a[@href='/accounts/login/?source=auth_switcher']")
        login_button.click()
        time.sleep(2)

        # tells the bot to add the the username
        user_name_element = driver.find_element_by_xpath("//input[@name='username']")
        user_name_element.clear()
        user_name_element.send_keys(self.username)

        # tells the bot to add the password
        password_element = driver.find_element_by_xpath("//input[@name='password']")
        password_element.clear()
        password_element.send_keys(self.password)
        password_element.send_keys(Keys.TAB + Keys.TAB + Keys.RETURN)

    # this function will like images from hashtags
    def like_photo(self, hashtag):
        driver = self.driver
        driver.get("https://www.instagram.com/explore/tags/" + hashtag + "/")
        time.sleep(2)

        # used to gather images for the bot
        pic_refs = []
        for i in range(1, 7):
            try:
                driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                time.sleep(2)
                # to get tags
                hrefs_in_view = driver.find_elements_by_tag_name('a')

                #finding relevant hrefs
                hrefs_in_view = [elements.get_attribute('href') for elements in hrefs_in_view if hashtag in elements.get_attribute('href')]


                #building list of unique photos
                [pic_hrefs.append(href) for href in hrefs_in_view if href not in pic_hrefs]

            except Exception:
                continue

        #Liking the images
        unique_photos = len(pic_refs)
        for pic_ref in pic_refs:
            driver.get(pic_ref)
            time.sleep(2)
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            try:
                time.sleep(random.randint(2, 4))
                like_button = lambda: driver.find_element_by_xpath('/html/body/span/section/main/div/div/article/div[2]/section[1]/span[1]/button').click()
                like_button().click
                for second in reversed(range(0, random.randint(18, 28))):
                    print_same_line("#" + hashtag + ': unique photos left: ' + str(unique_photos)+ " | Sleeping " + str(second))
                    time.sleep(1)

            except Exception as e:
                time.sleep(2)
            unique_photos -= 1

# Profile section #
username = "Your username"
password = "Password"

# tester to see if the login function works
bot = InstagramBot(username, password)
bot.login()


# the hashtags section, just place in any hashtags or use the ones below #
hashtags = ['amazing', 'beautiful', 'adventure', 'photography', 'nofilter',
            'newyork', 'artsy', 'alumni', 'lion', 'best', 'fun', 'happy',
            'art', 'funny', 'me', 'followme', 'follow', 'cinematography', 'cinema',
            'love', 'instagood', 'instagood', 'followme', 'fashion', 'sun', 'scruffy',
            'street', 'canon', 'beauty', 'studio', 'pretty', 'vintage', 'fierce']

while True:
    try:
        # Choose a random tag from the list of tags
        tag = random.choice(hashtags)
        bot.like_photo(tag)
    except Exception:
        bot.closeBrowser()
        time.sleep(60)
        bot = InstagramBot(username, password)
        bot.login()