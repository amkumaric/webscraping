from urllib.request import urlopen, Request
from bs4 import BeautifulSoup


url = 'https://www.webull.com/quote/crypto'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}

req = Request(url, headers=headers)
webpage = urlopen(req).read()
soup = BeautifulSoup(webpage, 'html.parser')

print(soup.title.text)

stock_data = soup.findAll('div',attrs={'class':'table-cell'})

counter = 0
for x in range(5):
    detail_div = stock_data[counter+1].find('div', class_='detail')
    if detail_div:
        name_tag = detail_div.find('p', class_='tit')
        symbol_tag = detail_div.find('p', class_='txt')

        name = name_tag.text.strip() if name_tag else None
        symbol = symbol_tag.text.strip() if symbol_tag else None

    change = float(stock_data[counter + 4].text.strip('%').strip('+'))

    last_price_text = stock_data[counter + 2].text.replace(',', '')  # Remove commas
    last_price = float(last_price_text.strip())  # Convert to float after stripping whitespace


    percent_change = float(stock_data[counter + 3].text.strip('%').strip('+'))

    print(f'Crypto Name: {name}')
    print(f'Symbol: {symbol}')
    print(f'Price: {last_price}')
    print(f'Percent Change: {percent_change}%')
    print(f'Price Change: {change}')
    print('\n')
		
    counter += 10




#SOME USEFUL FUNCTIONS IN BEAUTIFULSOUP
#-----------------------------------------------#
# find(tag, attributes, recursive, text, keywords)
# findAll(tag, attributes, recursive, text, limit, keywords)

#Tags: find("h1","h2","h3", etc.)
#Attributes: find("span", {"class":{"green","red"}})
#Text: nameList = Objfind(text="the prince")
#Limit = find with limit of 1
#keyword: allText = Obj.find(id="title",class="text")

