import os
import urllib.request
from bs4 import BeautifulSoup as soup


def crawling_to_sub_address(url):																				# function untuk nyari sub url dari parent url
	user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'	# HTTP header biar ga error

	headers={'User-Agent':user_agent,} 																			# assign ke variable buat di satuin

	request=urllib.request.Request(url,None,headers) 															# assemble the request with url and header user agent
	download_the_index = urllib.request.urlopen(request)														# download file html
	the_index = download_the_index.read()																		# buka file html yang telah di download

	begin_parsing = soup(the_index,"lxml")																		# memulai parsing dari variable the_index

	list_url = []																								# declare var list untuk nampung 
	
	count = 1
	for link in begin_parsing.find_all('a', attrs = {'target':'_blank','style':'color:#FFFFFF'}):				# mulai cari tag 'a' dengan pemerjelas(attribut) target dan class

		href = link.get('href')																					# ambil link href nya
		list_url.append("{0} {1}".format(count,href))															# masukin hasil ke array list yang uda di init di atas
		count += 1

	return list_url																								# return nilai array list yang berisi link sub url
	
	# list_url.clear()																							# clear array agar tidak numpuk value





def main(page):

	os.system("clear")			
	
	count = 1																									# init count untuk check dengak argumnent page
	while count <= page:

		url = "https://ganool.im/box-office/page/{0}".format(count)												# URL parent dengan page
		
		init = open("link_page {0}".format(count),'w')															# init untuk buka file sesuai halaman ganoolnya							

		user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'

		headers={'User-Agent':user_agent,} 

		request=urllib.request.Request(url,None,headers)
		download_the_index = urllib.request.urlopen(request)
		the_index = download_the_index.read()

		begin_parsing = soup(the_index,"lxml")


		print("\n============================================")													# ini untuk di tampilin di terminal, engga masuk file
		print("\t\tPAGE {0}\t\t".format(count))
		print("============================================")

		for link in begin_parsing.find_all('a', attrs = {'class':'ml-mask'}):									# nyari parent URL dengan attr class=ml-mask


			href = link.get('href')															
			title = link.get_text()																				# untuk nampilin string judul, pake method 'text' engga bisa

			print("{0} => {1}\n".format(title,href))															# nampilin judul dan url parent
			init.write("{0} => {1}\n".format(title,href))														# nulis judul dan url parent ke file

			returned_link = crawling_to_sub_address(href)														# buat variable baru untuk nampung nilai return dari function crawling....

			for i in range(len(crawling_to_sub_address(href))):													# make foor loop untuk assign dan nampilin var array di atas agar bisa tampil
				print("\t{0}".format(returned_link[i]))															# print ke terminal hasil dari child URL link
				init.write("\n\t{0}".format(returned_link[i]))													# nulis ke file

			
			print("\n\t++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n")
			init.write("\n\t++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n")	
		
		count += 1																								# increment untuk while loop paling awal
		init.close()																							# close setiap file habis uda selesai di tulis


main(5)																											# manggil main function dengan jumlah 2 halaman


