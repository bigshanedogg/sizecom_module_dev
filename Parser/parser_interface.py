from abc import *


class Parser(metaclass=ABCMeta) :
    '''
    extends by 'platform-brand'
    e.g. SSFSHOP_8seconds_Parser
    '''
    name = None

    @abstractmethod
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def showDevInfo(self, date="2019.04.02"):
        '''
        show platform basic info
        :param date: String; the last update date for maintenance, should update manually
        :return: None
        '''
        print("Name: {name}\n" \
              "Last update : {date}".format(name=self.name, url=self.url, date=date))

    @abstractmethod
    def parseHtmlToString(self, html_source):
        '''
        extract text of each tag and return list of texts
        :param html_source: String
        :return: List
        '''
        from bs4 import BeautifulSoup
        soup = BeautifulSoup(html_source, 'html.parser')
        _element_list = soup.findAll(text=True)
        element_list = [element for element in _element_list if element.strip() != ""]
        return element_list


class PlatformParser(Parser):
    @abstractmethod
    def __init__(self, name):
        super(name)

    @abstractmethod
    def showDevInfo(self, date="2019.04.02"):
        super(date)

    @abstractmethod
    def parseHtmlToString(self, html_source):
        super(html_source)

    @abstractmethod
    def getSizeInfo_tag(self, html_source):
        '''
        get size info from html tag
        :param html_source: String
        :return: Dictionary; key: each header, value: list of values of each header
        '''
        pass


    @abstractmethod
    def getSizeInfo_image(self):
        '''
        추후 개발
        :return:
        '''
        # html에서 size info를 담은 이미지 포맷의 사이즈표 찾기
        # OCR로 사이즈표 읽어서 string 추출
        # 추출한 string을 size info의 형태로 정제하여 반환
        pass

    @abstractmethod
    def sizeInfoToDic(self):
        # 각 tag는 따로 저장해서 tag_dictionary에 입력
        # 뽑아낸 tag는 dictionary 기준 standard tag로 변환하여 입력
        pass


class CommunityParser(Parser):
    @abstractmethod
    def __init__(self, name):
        super(name)

    @abstractmethod
    def showDevInfo(self, date="2019.04.02"):
        super(date)

    @abstractmethod
    def parseHtmlToString(self, html_source):
        super(html_source)

    pass
