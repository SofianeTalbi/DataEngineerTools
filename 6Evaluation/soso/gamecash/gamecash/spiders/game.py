from ast import Yield
from xml.etree.ElementTree import C14NWriterTarget
import scrapy
import urllib.parse



class GameSpider(scrapy.Spider):
    name = 'game'
    #allowed_domains = ['https://www.gamecash.fr/']
    start_urls = ['https://www.gamecash.fr/gaming-3ds-u44.html', 'https://www.gamecash.fr/gaming-ds-u6.html', 'https://www.gamecash.fr/gaming-jeux-pc-u10.html', 'https://www.gamecash.fr/gaming-playstation-3-u1.html', 'https://www.gamecash.fr/gaming-playstation-4-u59.html', 'https://www.gamecash.fr/gaming-playstation-5-u168.html', 'https://www.gamecash.fr/gaming-playstation-portable-u3.html', 'https://www.gamecash.fr/gaming-playstation-vita-u53.html', 'https://www.gamecash.fr/gaming-switch-u60.html', 'https://www.gamecash.fr/gaming-wii-u4.html', 'https://www.gamecash.fr/gaming-wii-u-u57.html', 'https://www.gamecash.fr/gaming-xbox-360-u9.html', 'https://www.gamecash.fr/gaming-xbox-one-u58.html', 'https://www.gamecash.fr/gaming-xbox-series-x-u170.html' ]

    def parse(self, response):
        for link in response.xpath("//a[@class='product']/@href"):
            yield response.follow(link.get(), callback=self.parse_categories)

    def parse_categories(self,response):

        dic = { 'Nom'  : response.xpath("//h1[@itemprop='name']/text()").extract()[0],
                #'Plate-forme' : response.xpath("//span[@class='value']/a/text()").extract()[0],
                #'Genre' : response.xpath("//span[@class='value']/a/text()").extract()[1],
        }

        liste_a = [element for element in response.xpath("//span[@class='value']/a/text()").extract()]
        liste_va = [element for element in response.xpath("//span[@class='value']/text()").extract()]
        liste_variable = liste_a + liste_va
        
        for i in range(len(liste_variable)):
            cle = response.xpath("//span[@class='label']/text()").extract()[i]
            variable = liste_variable[i]
            dic.update({cle : variable}) 

        dic.update({'Prix' : response.xpath("//span[@class='priceUnit']/text()").extract()[0] + response.xpath("//span[@class='priceCent']/text()").extract()[0]})       
        
        yield dic