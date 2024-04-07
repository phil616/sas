from requests import post,get
from loguru import logger
from conf import BASEURL
class _HTTP:
    def __init__(self,baseurl=BASEURL):
        self.headers = {}
        self.base = baseurl
    def json_post(self,url,data):
        logger.info(f"Posting to {url} with data: {data}")
        return post(self.base+url,json=data,headers=self.headers)
    def data_post(self,url,data):
        logger.info(f"Posting to {url} with data: {data}")
        return post(self.base+url,data=data,headers=self.headers)
    
    def get(self,url):
        logger.info(f"Getting from {url}")
        return get(self.base + url,headers=self.headers)
    
    def update_headers(self,headers:dict):
        logger.info(f"Updating headers to {headers}")
        self.headers.update(headers)