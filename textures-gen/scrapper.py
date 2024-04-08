import urllib.request
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, TimeoutException

# you need to download a chromedriver 2.15 and move it locally

class Scrapper:

    def __init__(self):
        options = webdriver.ChromeOptions()
        options.add_argument('-incognito')
        options.add_argument('--headless')
        options.add_argument('--no-sandbox')


        self._driver = webdriver.Chrome(executable_path='./chromedriver', chrome_options=options)
        self._driver.set_page_load_timeout(30)

    def scrape(self, url, dir):
        self._driver.get(url)

        count = 0
        while True:
            pic = self._driver.find_element_by_id('picture')
            src = pic.get_attribute('src')

            print(count, ' src is ', src)

            urllib.request.urlretrieve(src, f'./{dir}/{count}.jpg')

            print('saved img #', count)

            try:
                next_button = self._driver.find_element_by_xpath('//a[img[@class="img-picture-next"]]')
                print(count, ' found next button')
            except (NoSuchElementException, TimeoutException):
                return

            self._driver.get(next_button.get_attribute('href'))
            count += 1


scrapper = Scrapper()

# you should create corresponding directories

# scrapper.scrape('http://textures.forrest.cz/index.php?spgmGal=metal&spgmPic=0#spgmPicture', 'metal')
# scrapper.scrape('https://textures.forrest.cz/index.php?spgmGal=stone&spgmPic=0#spgmPicture', 'stone')
scrapper.scrape('https://textures.forrest.cz/index.php?spgmGal=marble&spgmPic=0#spgmPicture', 'marble')
scrapper.scrape('https://textures.forrest.cz/index.php?spgmGal=wood&spgmPic=0#spgmPicture', 'wood')
