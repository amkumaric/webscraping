
from urllib.request import urlopen
from bs4 import BeautifulSoup
import openpyxl as xl
from openpyxl.styles import Font





#webpage = 'https://www.boxofficemojo.com/weekend/chart/'
webpage = 'https://www.boxofficemojo.com/year/2024/'

page = urlopen(webpage)			

soup = BeautifulSoup(page, 'html.parser')

title = soup.title

movie_name = soup.findAll('td',attrs={'class':'a-text-left mojo-field-type-release mojo-cell-wide'})

movie_gross = soup.findAll('td',attrs={'class':'a-text-right mojo-field-type-money mojo-estimatable'})

movie_release= soup.findAll('td',attrs={'class':'a-text-left mojo-field-type-date a-nowrap'})

movie_theaters = soup.findAll('td',attrs={'class':'a-text-right mojo-field-type-positive_integer'})

movie_number = soup.findAll('td',attrs={'class':'a-text-right mojo-header-column mojo-truncate mojo-field-type-rank mojo-sort-column'})

# Creating WB
wb = xl.Workbook()

ws = wb.active

ws.title = 'Box Office Report'

headerfont= Font(name='Times New Roman', size = 24, bold = True)

counter = 0
for x in range(0,5):
    number = movie_number[counter].text
    name = movie_name[counter].text
    release_date = movie_release[counter].text
    number_of_theaters = float(movie_theaters[counter].text.replace(',','').strip())
    total_gross = float(movie_gross[counter].text.strip('$').replace(',','').strip())
    avg_gross = round(total_gross / number_of_theaters,2)

    counter += 1



wb.save('BoxOfficeReport.xlsx')


##
##
##
##

