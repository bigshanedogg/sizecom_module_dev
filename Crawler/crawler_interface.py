from abc import *


class Crawler(metaclass=ABCMeta) :
    '''
    extends by platform
    e.g. Musinsa_Crawler
    '''
    platform_url = None
    platform_name = None

    @abstractmethod
    def __init__(self, name, url):
        self.name = name
        self.url = url

    @abstractmethod
    def showDevInfo(self, date="2019.04.02"):
        '''
        show platform basic info
        :param date: String; the last update date for maintenance, should update manually
        :return: None
        '''
        print("Name: {name}\n" \
              "Url: {url}\n" \
              "Last update : {date}".format(name=self.name, url=self.url, date=date))

    @abstractmethod
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

class PlatformCrawler(Crawler):
    @abstractmethod
    def __init__(self, name, url):
        super(name, url)

    @abstractmethod
    def showDevInfo(self, date="2019.04.02"):
        super(date)

    def getPageHtml(self, page_url):
        super(page_url)

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


class CommunityCrawler(Crawler):
    @abstractmethod
    def __init__(self, name, url):
        super(name, url)

    @abstractmethod
    def showDevInfo(self, date="2019.04.02"):
        super(date)

    @abstractmethod
    def getPageHtml(self, page_url):
        super(page_url)

    pass