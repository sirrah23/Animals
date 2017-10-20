from collections import defaultdict
from string import ascii_uppercase
import requests
from bs4 import BeautifulSoup


def animalGroupMap():
    wikiLink = "https://en.wikipedia.org/wiki/List_of_English_terms_of_venery,_by_animal"
    soup = BeautifulSoup(requests.get(wikiLink).content, 'html.parser')
    tableRows = soup.find_all('tr')
    tableRows.pop(0)
    rowSpanCount = 0
    data = defaultdict(list)
    i = 0
    while i < len(tableRows):
        cols = tableRows[i].find_all('td')
        rowspan = cols[0].get('rowspan')
        if rowspan is not None:
            rowSpanCount = int(rowspan)-1
            currKey = cols[0].get_text()
            data[currKey].append(cols[1].get_text())
            while rowSpanCount > 0:
                i += 1
                cols = tableRows[i].find_all('td')
                data[currKey].append(cols[0].get_text())
                rowSpanCount -= 1
        elif cols[0].get_text() in ascii_uppercase:
            i += 1
        else:
            data[cols[0].get_text()].append(cols[1].get_text())
            i += 1
    return dict(data)


if __name__ == "__main__":
    animalGroupMap()

