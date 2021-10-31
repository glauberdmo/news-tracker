from typing import Dict, List, Tuple

class ArticlesScrapper:
    """
    Class ArticlesScrapper
    site_name: str - site to get articles
    possible values for site_name: ["uol","folha","g1"]  
    ISSUES: G1 is not working, html is not being parsed correctly
    
    """
    def __init__(self, site_name:str):
        from pathlib import Path
        self.tags_settings = Path(__file__).absolute().parent / 'TagsSettings.json'  #get path address to tag settings  
        self.site_name = site_name
        self.url = self._get_url()
        self.class_tags = self._get_class_tags()

    def __repr__(self) -> str:
        return f"ArticlesScrapper({self.site_name})"
        
    def _get_url(self)->str:
        import json        
        with open(self.tags_settings) as json_file:
            data = json.load(json_file)
            return data[self.site_name]["url"]
    
    def _get_class_tags(self)->List[str]:
        import json
        with open(self.tags_settings) as json_file:
            data = json.load(json_file)
            return data[self.site_name]["tags"]

    def _get_website_text(self) -> str:    
        #Get the text of a website.
        import requests

        try:
            #Get response from url
            response = requests.get(self.url)
            return response.text
        except Exception as e: 
            print(e)
            return ""       

    def get_articles(self) -> list:   
        #Get articles from website text
        from bs4 import BeautifulSoup

        articles:list = []
        site_content:str = self._get_website_text()
        soup =BeautifulSoup(site_content, 'html.parser')
        results = soup.find_all(class_=self.class_tags[0])  

        #add articles to list    
        for result in results:
            articles.append(BeautifulSoup(str(result), 'html.parser').get_text())
            print(articles[-1])

        #verify if articles were found    
        assert len(articles) > 0, "No articles found"
        return articles
    