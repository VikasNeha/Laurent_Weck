import urllib2
from bs4 import BeautifulSoup
import csv


def make_soup(url):
    html = urllib2.urlopen(url).read()
    return BeautifulSoup(html, "html5lib")

ifile = open('csv_files/jsonURLs.csv', 'rb')
csv_reader = csv.reader(ifile)

ofile = open('csv_files/finalURLs.csv', 'wb')
csv_writer = csv.writer(ofile, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)

for row in csv_reader:
    print row[0]
    soup = make_soup(row[1])
    link_tag = soup.find("a", class_="slb float_left")
    csv_writer.writerow([row[0], row[1], link_tag["href"]])

ifile.close()
ofile.close()