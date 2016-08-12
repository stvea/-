from bs4 import BeautifulSoup
import requests
import csv,sys
def Name(url):
	html = requests.get(url)
	html = html.text
	soup = BeautifulSoup(html, "html.parser")
	children =  soup.find_all('div','info')
	for child in children:
		for po in child.find_all('div',"star clearfix"):
			print po.select("[class~=rating_nums]")
		if child.a.string != None:
			tump = child.a.string.strip()
			tump = tump.encode("GBK")
			csv_writer.writerow([tump])
			print "Writting books success"
		else:
			i = 0;
			b="";
			name1 = ""
			name2 = ""
			name = ""
			i = 0
			for a in child.a.contents:
				if i == 0:
					name1 = a.string.strip()
					i = 1
				else:
					name2 = a.string.strip()
					name = name1+name2
					name = name.encode("GBK")
					i = 0
					csv_writer.writerow([name])
					print "Writting books success"
					pass
			pass
#csv_file = open("rent.csv","wb") 
#csv_writer = csv.writer(csv_file, delimiter=',')
#curl = "http://www.ygdy8.net"
csv_file = open("rent1.csv","wb") 
csv_writer = csv.writer(csv_file, delimiter=',')
page = 0
url = "https://book.douban.com/tag/%E7%BC%96%E7%A8%8B?start={page}&type=T"
while True:
	page += 20
	Name(url.format(page=page))
	#print li
	if page == 20:
		break
		pass
	#url = url.format(page=page)
#print url
#Name(url)
