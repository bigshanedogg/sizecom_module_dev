class PlatformParser(Parser):
    def __init__(self, name="musinsa_crawler"):
        super(name)

    def showDevInfo(self, date="2019.04.07"):
        super(date)

    def parseHtmlToString(self, html_source):
        super(html_source)

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
