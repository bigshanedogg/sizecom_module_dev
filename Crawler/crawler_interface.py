from abc import *


class Crawler(metaclass=ABCMeta) :
    '''
    extends by platform
    e.g. Musinsa_Crawler
    '''
    platform_url = None
    platform_name = None

    def __init(self, platform_name, platform_url):
        self.platform_name = platform_name
        self.platform_url = platform_url

    def showDevInfo(self, date="2019.04.02"):
        '''
        show platform basic info
        :param date: String; the last update date for maintenance, should update manually
        :return: None
        '''
        print("Platform: {platform_name}\n" \
              "Url: {platform_url}\n" \
              "Last update : {date}".format(platform_name=self.platform_name, platform_url=self.platform_url, date=date))


    def getPageHtml(self, page_url):
        '''
        get html string of the page with bs4
        :param page_url: String
        :return: String
        '''
        import requests
        _page_source = requests.get(page_url)
        page_source = _page_source.text
        return page_source

    @abstractmethod
    def getBrandUrlList(self):
        '''
        get all brand urls of the platform
        :return: Dictionary; key: brand_name, value: brand_url
        '''
        pass

    @abstractmethod
    def getProductUrlList(self):
        '''
        get all product urls of the platform
        :return: Dictionary; key: product_name, value: product_url
        '''
        pass

    @abstractmethod
    def getProductHtml(self, product_url):
        '''
        get product Html of given product_url
        :param product_url: String
        :return: String
        '''
        return self.getPageHtml(product_url)

    @abstractmethod
    def getReviewHtml(self, product_url):
        '''
        get review Html of given product_url
        :param product_url: String
        :return: String
        '''
        return self.getPageHtml(product_url)