# -*- coding: utf-8 -*-
from ..items import City 
from scrapy.spiders import CSVFeedSpider

        '''
        row is a dictioary like the following : {'header1': value , 'header2: value ....'}
        row.keys() will extract all the keys and form a list 
        '''


class WeatherSpider(CSVFeedSpider):
    name = 'weather'
    """
    If there are more csv to crawl , write the following code :
    start_urls = gen_urls()

    def gen_urls:
        urls = []
        ......
        return urls 
    """
    start_urls = ['http://beijingair.sinaapp.com/data/china/cities/20171220/csv'] 

    '''
    row in the first coding line of parse_rows(note that it is different from the one in
    the folowing dictionary pairs ) represents  the dictionary elements of ( headers , row ) pair 
    generator from cdviter method 
    
    '''
     

    def parse_row(self, response,row):

        headers = list( row.keys())

        for name in headers[3:len(headers)]:
          
            city = City()
            city ['name'] = name
            city ['norm'] = row['type']
            city ['value'] = row[name]
            city ['date'] = "%s-%s-%s"%(row['date'][0:3],row['date'][4:5],row['date'][6:7])

            yield city 



