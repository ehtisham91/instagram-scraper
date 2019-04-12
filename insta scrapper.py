import os
import shutil
import requests
from time import sleep
from bs4 import BeautifulSoup
from selenium import webdriver
from credentials import Username, Password, Path, target_username, Driver_path


class Insta:
    def __init__(self):
        self.username = Username
        self.password = Password
        self.target_username = target_username
        self.path = Path
        self.driver = webdriver.Chrome(Driver_path)

        self.driver.get('https://www.instagram.com')
        sleep(5)
        self.log_in()

        sleep(5)
        self.open_target_profile()
        self.scroll_down()

        self.downloading_images()
        sleep(5)
        self.driver.close()

    def downloading_images(self):
        if not os.path.exists(self.path):
            os.mkdir(self.path)
        soup = BeautifulSoup(self.driver.page_source, 'lxml')
        all_images = soup.find_all('img')
        print('Length of all images', len(all_images))
        for index, image in enumerate(all_images):
            filename = 'image_' + str(index) + '.jpg'
            image_path = os.path.join(self.path, filename)
            link = image['src']
            print('Downloading image', index)
            response = requests.get(link, stream=True)
            try:
                with open(image_path, 'wb') as file:
                    shutil.copyfileobj(response.raw, file)  # source -  destination
            except Exception as e:
                print(e)
                print('Could not download image number ', index)
                print('Image link -->', link)

    def scroll_down(self):
        try:
            posts_count = self.driver.find_element_by_xpath('//span[text()=" posts"]').text
            posts_count = posts_count.replace(' posts', '')
            posts_count = str(posts_count).replace(',', '')  # 15,483 --> 15483
            posts_count = int(posts_count)
            if posts_count > 12:
                no_of_scrolls = int(self.posts_count/12) + 3
                try:
                    for value in range(no_of_scrolls):
                        self.driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
                        sleep(2)
                except Exception as e:
                    print(e)
                    print('Some error occurred while trying to scroll down')
            sleep(10)
        except Exception:
            print('Could not find no of posts while trying to scroll down')

    def open_target_profile(self):

        try:
            sleep(2)
            close_btn = self.driver.find_element_by_link_text("Not Now")
            sleep(2)
            close_btn.click()
            sleep(1)
        except Exception:
            pass

        try:
            self.driver.find_element_by_xpath('//button[contains(text(), "Not Now")]').click()
        except Exception as e:
            pass

        try:
            target_profile_url = 'https://www.instagram.com' + '/' + self.target_username + '/'
            self.driver.get(target_profile_url)
            sleep(3)
        except Exception:
            print('Link is not correct')

    def log_in(self):
        try:
            log_in_button = self.driver.find_element_by_link_text('Log in')
            log_in_button.click()
            sleep(3)
        except Exception:
            print('Unable to find login button')
        else:
            try:
                user_name_input = self.driver.find_element_by_xpath('//input[@aria-label="Phone number, username, or email"]')
                user_name_input.send_keys(self.username)
                password_input = self.driver.find_element_by_xpath('//input[@aria-label="Password"]')
                password_input.send_keys(self.password)
                user_name_input.submit()
            except Exception:
                print('Some exception occurred while trying to find username or password field')


if __name__ == '__main__':
    insta = Insta()
