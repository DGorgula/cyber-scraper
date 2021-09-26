def getTitlesAndLinks(tree, isFirstTime):
    headers = []
    links = []
    if isFirstTime:
        articles = tree.xpath('//*[@class="focus-articles__info"]/a')
        articlesLinks = [articles[0].attrib['href'], articles[1].attrib['href']]
        links.extend(articlesLinks)
        articlesTitles = [articles[0].getchildren()[0].text.replace("\n", ""), articles[1].getchildren()[0].text.replace("\n", "")]
        headers.extend(articlesTitles)
    h3 = tree.xpath('.//a[./h3]')
    assert (type(h3) == list) & (len(h3) > 0), "Title scraping didn't work"
    for h in h3:
        header = h.getchildren()
        if (len(header) != 1):
            continue
        title = header[0].text.replace("\n", "")
        link = h.attrib["href"]
        headers.append(title)
        links.append(link)
    return {"headers": headers, "links": links}

def getAuthors(tree):
    authorNames = tree.xpath('//div[./span][./a]/a/text()')
    return authorNames

def getDates(tree):
    dates = tree.xpath('//*[not(article)]/time/text()')
    # return len(dates)
    return dates
    # return tree.xpath('.//a:href', namespaces = "author")