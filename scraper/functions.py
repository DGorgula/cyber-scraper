from lxml import html
import requests

def removeAside(tree):
    aside = tree.xpath('//aside')[0]
    aside.getparent().remove(aside)
    return tree

def getArticlesLinks(tree, isFirstTime):
    links = []
    if isFirstTime:
        focusArticlesLinks = tree.xpath('//a[@class="focus-articles__link"]/@href')
        links.extend(focusArticlesLinks)
    h3 = tree.xpath('.//a[./h3]')
    assert (type(h3) == list) & (len(h3) > 0), "Title scraping didn't work"
    for h in h3:
        header = h.getchildren()
        if (len(header) != 1):
            continue
        link = h.attrib["href"]
        links.append(link)
    return [*links]

def getAuthors(tree):
    authorNames = tree.xpath('//div[./span][./a]/a/text()')
    return authorNames

def getDates(tree):
    dates = tree.xpath('//*[not(article)]/time/text()')
    return dates

def getArticleData(articleLink, authors):
    rawData = requests.get(articleLink).content
    tree = html.fromstring(rawData)
    tree = removeAside(tree)
    title = tree.xpath('//h1/text()')[0]
    date = tree.xpath('//time/text()')[0]
    image = tree.xpath('//figure/img/@data-src')[0]
    rawContent = tree.xpath('//div[@class="content"]')[0]
    rawContent = removeIrrelevantElements(rawContent)
    content = rawContent.text_content()

    authorElement = tree.xpath('//div[./span][./a]/a')[0]
    authorName = authorElement.text
    authorLink = authorElement.attrib['href']
    if authorName not in authors:
        authorData = getAuthorData(authorLink)
        authors[authorName] = authorData
    return { "link": articleLink, "title": title, "publishDate": date, "image": image, "content": content, "author": authorName}

def getAuthorData(authorUrl):
    rawData = requests.get(authorUrl).content
    tree = html.fromstring(rawData)
    relevantDivChildren = tree.xpath('//div[./div][./h1]')[0]
    name = relevantDivChildren[0].text.strip()
    about = relevantDivChildren[1].text.strip()
    firstName = '"' + name.split(" ")[0] + '"'
    if firstName == '"CyberNews"':
        img = tree.xpath(f'//img[contains(@data-src, "CNTeam")]/@data-src')
    else:
        img = tree.xpath(f'//img[contains(@data-src, {firstName})]/@data-src')
    if len(img) == 0:
        img = tree.xpath(f'//img[contains(@data-src, "default")]/@data-src')
    return {"image": img[0], "name": name, "about": about}

def removeIrrelevantElements(element):
    elementChildren = element.getchildren()
    hrFlag = False
    for subElement in elementChildren:
        if hrFlag: element.remove(subElement)
        elif subElement.tag == "hr":
            hrFlag = True
            element.remove(subElement)
    return element