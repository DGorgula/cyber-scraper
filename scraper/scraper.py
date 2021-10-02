#   dependencies
from franz.miniclient.request import jsonRequest
import requests
from lxml import html
from functions import getArticlesLinks, getAuthors, getDates, getArticleData

#   Dotenv
from dotenv import dotenv_values
import requests
config = dotenv_values(".env")
locals().update(config)

authors = {}
data = requests.get('https://cybernews.com/news/page/1')
tree = html.fromstring(data.content)
assert type(tree) == html.HtmlElement, "Couldn't get the html content"
aside = tree.xpath('//aside')[0]
aside.getparent().remove(aside)

#   gets the number of pages.
numberOfPages = int(tree.findall('.//*[@class="pagination__number"][last()-1]')[0].text)
assert type(numberOfPages) == int

articlesLinks = getArticlesLinks(tree, True)
for articleLink in articlesLinks:
    articleData = getArticleData(articleLink, authors)
    response = requests.post(f'{DB_SERVER}/post/new', json = articleData)
for author in authors:
    response = requests.post(f'{DB_SERVER}/author/new', json = authors[author])
# titlesAndLinks["authors"] = ["",""]
# focusArticlesLinks = tree.xpath('//a[@class="focus-articles__link"]/@href')
# focusArticle1 = requests.get(focusArticlesLinks[0]).content
# focusArticle1Tree = html.fromstring(focusArticle1)
# print(len(titlesAndLinks["links"]))
# titlesAndLinks["authors"].extend(getAuthors(tree))
# titlesAndLinks["dates"] = getDates(tree)

# for i in range(2, numberOfPages+1):
#     data = requests.get(f'https://cybernews.com/news/page/{i}')
#     tree = html.fromstring(data.content)
#     assert type(tree) == html.HtmlElement, "Couldn't get the html content"

#     aside = tree.xpath('//aside')[0]
#     aside.getparent().remove(aside)

#     newTitlesAndLinks = getArticlesLinks(tree, False)
#     assert len(newTitlesAndLinks["headers"]) == len(newTitlesAndLinks["links"]), "Headers and links length doesn't match"
#     titlesAndLinks["headers"].extend(newTitlesAndLinks["headers"])
#     titlesAndLinks["links"].extend(newTitlesAndLinks["links"])
#     titlesAndLinks["authors"].extend(getAuthors(tree))
#     titlesAndLinks["dates"].extend(getDates(tree))
# assert len(titlesAndLinks["headers"]) == len(titlesAndLinks["links"]) == len(titlesAndLinks["authors"]), "Headers and links length doesn't match"
# #  == len(titlesAndLinks["dates"])
# print(*titlesAndLinks["headers"], sep="\n")
# print(*titlesAndLinks["links"], sep="\n")
# print(*titlesAndLinks["authors"], sep="\n")
# print(*titlesAndLinks["dates"], sep="\n")
# print(len(titlesAndLinks["authors"]))

