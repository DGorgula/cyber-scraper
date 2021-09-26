#   dependencies
import requests
from lxml import html
from functions import getTitlesAndLinks, getAuthors, getDates

data = requests.get('https://cybernews.com/news/page/1')
tree = html.fromstring(data.content)
assert type(tree) == html.HtmlElement, "Couldn't get the html content"
aside = tree.xpath('//aside')[0]
aside.getparent().remove(aside)

#   gets the number of pages.
numberOfPages = int(tree.findall('.//*[@class="pagination__number"][last()-1]')[0].text)
assert type(numberOfPages) == int

titlesAndLinks = getTitlesAndLinks(tree, True)
titlesAndLinks["authors"] = ["",""]
titlesAndLinks["authors"].extend(getAuthors(tree))
titlesAndLinks["dates"] = getDates(tree)

# for i in range(2, numberOfPages+1):
#     data = requests.get(f'https://cybernews.com/news/page/{i}')
#     tree = html.fromstring(data.content)
#     assert type(tree) == html.HtmlElement, "Couldn't get the html content"

#     aside = tree.xpath('//aside')[0]
#     aside.getparent().remove(aside)

#     newTitlesAndLinks = getTitlesAndLinks(tree, False)
#     assert len(newTitlesAndLinks["headers"]) == len(newTitlesAndLinks["links"]), "Headers and links length doesn't match"
#     titlesAndLinks["headers"].extend(newTitlesAndLinks["headers"])
#     titlesAndLinks["links"].extend(newTitlesAndLinks["links"])
#     titlesAndLinks["authors"].extend(getAuthors(tree))
#     titlesAndLinks["dates"].extend(getDates(tree))
assert len(titlesAndLinks["headers"]) == len(titlesAndLinks["links"]) == len(titlesAndLinks["authors"]), "Headers and links length doesn't match"
#  == len(titlesAndLinks["dates"])
print(*titlesAndLinks["headers"], sep="\n")
print(*titlesAndLinks["links"], sep="\n")
print(*titlesAndLinks["authors"], sep="\n")
print(*titlesAndLinks["dates"], sep="\n")
# print(len(titlesAndLinks["authors"]))

