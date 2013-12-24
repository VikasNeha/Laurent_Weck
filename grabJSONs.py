import urllib2
import json
import csv


ofile = open('csv_files\jsonURLs.csv', 'wb')
csv_writer = csv.writer(ofile, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)

for siteID in range(774, 11):
    print siteID
    sitePath = "http://www.trustedshops.de/b2c_int/getdata.php?module=shopData&format=json&shops[]=" + str(siteID)
    jsonURL = ""
    req = urllib2.Request(sitePath)
    page = urllib2.urlopen(req).read()
    pageJson = json.loads(page)
    pageJson = pageJson['data']
    pageJson = pageJson['shops']
    if type(pageJson) == dict:
        pageJson = pageJson[str(siteID)]
        jsonURL = "http://www.trustedshops.de/profil/" + pageJson['url']
        csv_writer.writerow([str(siteID), jsonURL])

ofile.close()