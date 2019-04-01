from abc import *


class Praser(metaclass=ABCMeta) :
    '''
    extends by 'platform-brand'
    e.g. SSFSHOP_8seconds_Parser
    '''
    platform_name = None
    brand_name = None

    def __init__(self, platform_name, brand_name):
        self.platform_name = platform_name
        self.brand_name = brand_name

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


    def getSizeInfo_tag(self, html_source):
        '''
        get size info from html tag
        :param html_source: String
        :return: Dictionary; key: each header, value: list of values of each header
        '''
        pass

    def getSizeInfo_image(self):
        '''
        추후 개발
        :return:
        '''
        # html에서 size info를 담은 이미지 포맷의 사이즈표 찾기
        # OCR로 사이즈표 읽어서 string 추출
        # 추출한 string을 size info의 형태로 정제하여 반환
        pass

    def sizeInfoToDic(self):
        # 각 tag는 따로 저장해서 tag_dictionary에 입력
        # 뽑아낸 tag는 dictionary 기준 standard tag로 변환하여 입력
        pass