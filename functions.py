# def getTitlesAndLinks(tree, isFirstTime):
from lxml import html
import requests

def removeAside(tree):
    aside = tree.xpath('//aside')[0]
    aside.getparent().remove(aside)
    return tree

def getArticlesLinks(tree, isFirstTime):
    headers = []
    links = []
    if isFirstTime:
        focusArticlesLinks = tree.xpath('//a[@class="focus-articles__link"]/@href')
        links.extend(focusArticlesLinks)
        # articlesTitles = [articles[0].getchildren()[0].text.replace("\n", ""), articles[1].getchildren()[0].text.replace("\n", "")]
        # headers.extend(articlesTitles)
    h3 = tree.xpath('.//a[./h3]')
    assert (type(h3) == list) & (len(h3) > 0), "Title scraping didn't work"
    for h in h3:
        header = h.getchildren()
        if (len(header) != 1):
            continue
        # title = header[0].text.replace("\n", "")
        link = h.attrib["href"]
        # headers.append(title)
        links.append(link)
    # return {"headers": headers, "links": links}
    return [*links]

def getAuthors(tree):
    authorNames = tree.xpath('//div[./span][./a]/a/text()')
    return authorNames

def getDates(tree):
    dates = tree.xpath('//*[not(article)]/time/text()')
    # return len(dates)
    return dates

def getArticleData(articleLink):
    rawData = requests.get(articleLink).content
    tree = html.fromstring(rawData)
    tree = removeAside(tree)
    link = articleLink
    title = tree.xpath('//h1/text()')[0]
    date = tree.xpath('//time/text()')[0]
    image = tree.xpath('//figure/img/@data-src')[0]
    rawContent = tree.xpath('//div[@class="content"]')[0]
    contentChildren = rawContent.getchildren()
    for el in contentChildren:
        if el.text != None:
            if el.text.find("More from CyberNews:") != -1:
                continue
            print(el.text)
        for e in el.getchildren():
            if e.text != None:
                if e.text.find("More from CyberNews:") == -1:
                    continue
                print(e)
            

                    # content.
    authorElement = tree.xpath('//div[./span][./a]/a')[0]
    authorName = authorElement.text
    authorLink = authorElement.attrib['href']
    # authorA = tree.xpath('//div[./span][./a]/a/text()')[0]
    # print(content)
