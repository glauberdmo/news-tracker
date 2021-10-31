from ScrappingTools.ArticlesScrapper import ArticlesScrapper

g1Extraction = ArticlesScrapper("folha")

a = (g1Extraction.get_articles())
print(end="\n")