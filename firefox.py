from selenium import webdriver 
from pprint import pprint
from collections import namedtuple

class Cult: 
    def __unit__(self, driver):
        self.driver = driver 
        self.url = 'www.cultcampinas.com.br'
        self.box = 'eventBox'
        self.type = 'typeEventBox'  # class
        self.title_box = 'titleEventBox'  # class
        self.date = 'dateEvent'  # class
        self.place = 'placeEvent'  # class
        self.hour = 'hourEvent'  # class
        self.descr = 'descEventBox'  # class
        self.event = namedtuple('Event',
                                'title type date place hour descr')

    def navigate(self):
        self.driver.get(self.url)

    def _get_boxes(self):
        return self.driver.find_elements_by_class_name(
            self.box
        )

    def _get_title(self, box):
        

