from Crawler.crawler_interface import PlatformCrawler

class CrawlerMusinsa(PlatformCrawler):
    def __init__(self, name="musinsa_crawler", url="https://store.musinsa.com"):
        super(name, url)

    def showDevInfo(self, date="2019.04.07"):
        super(date)

    def getPageHtml(self, page_url):
        super(page_url)

    def getBrandUrlList(self):
        '''
        get all brand urls of the platform
        :return: Dictionary; key: brand_name, value: brand_url
        '''
        from bs4 import BeautifulSoup
        from selenium import webdriver
        from pyvirtualdisplay import Display
        import requests

        # create virtual display
        display = Display(visible=0, size=(800, 600))
        display.start()

        # call Chromedirver for linux
        path = "../resource/chromedriver_linux_0.73"
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--window-size=1420,1080')
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--disable-gpu')
        driver = webdriver.Chrome(chrome_options=chrome_options, executable_path=path)

        # move to platform main
        driver.get(self.url)
        # click brand box after waiting for page loading
        self.wait_for_class_element("tab-box-brand")
        brand_box = driver.find_element_by_class_name("tab-box-brand")
        brand_box.click()

        brand_dic = dict()
        alphabet_upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        for char in set(alphabet_upper):
            # click brand list per 'alphabet' after waiting for page loading
            char_button_class = "ty" + char
            self.wait_for_class_element(char_button_class)
            char_button = driver.find_element_by_class_name(char_button_class)
            char_button.click()

            # get brand list ul tag after waiting page loading
            self.wait_for_id_element("brand_list_print")
            char_button_page = driver.page_source
            brand_tag_list = BeautifulSoup(char_button_page, "html.parser").find("ul", {"id": "brand_list_print"})

            # crawl brand name & url
            for brand_tag in brand_tag_list:
                try:
                    brand_url = brand_tag.find("a", {"class": {"command-brand-link"}})["href"]
                    brand_name = brand_tag.find("a", {"class": {"command-brand-link"}})["text"]
                    brand_name_eng = brand_tag.find("span", {"class": {"eng"}}).text
                    brand_name_kor = brand_tag.find("span", {"class": {"eng"}}).text
                    brand_dic[brand_name] = {"url": brand_url, "name_eng": brand_name_eng, "name_kor": brand_name_kor}
                except:
                    continue

        return brand_dic


    def getProductUrlList(self):
        '''
        get all product urls of the platform
        :return: Dictionary; key: product_name, value: product_url
        '''
        pass

    def getProductHtml(self, product_url):
        '''
        get product Html of given product_url
        :param product_url: String
        :return: String
        '''
        return self.getPageHtml(product_url)

    def getReviewHtml(self, product_url):
        '''
        get review Html of given product_url
        :param product_url: String
        :return: String
        '''
        return self.getPageHtml(product_url)

        )