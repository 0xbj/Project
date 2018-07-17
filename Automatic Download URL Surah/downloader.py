import os as s
import urllib.request
import progressbar
import time

t1 = time.time()

class _3_Sekawan:
	
	s.system("cls")
	print("\n\t\t\t == Surah Downloader ==")
	print("\t\t\t      = 3 sekawan =\n")

	print("===================================")
	awal = input("[?] Masukkan Awal Nomer Surat : ").zfill(3)
	akhir = input("[?] Masukkan akhir Nomer Surat : ").zfill(3)
	print("===================================\n\n")

	start = int(awal)
	stop = int(akhir)

	pbar = None
	def show_progress(self,block_num, block_size, total_size):
	    widgets=[
	    ' [', progressbar.AdaptiveTransferSpeed(), '] ',
	    progressbar.Bar(),
	    ' (', progressbar.DataSize(), ') ',"(",progressbar.Percentage(),")",
		]

	    global pbar
	    if (self.pbar is None):
	        self.pbar = progressbar.ProgressBar(maxval=total_size,widgets=widgets)

	    downloaded = block_num * block_size
	    if downloaded < total_size:
	        self.pbar.update(downloaded)
	    else:
	        self.pbar.finish()
	        self.pbar = None
	
	def __init__(self):
		while (self.start <= self.stop):

			print("\n\t\t\t[+] Downloading Surat Nomor {0}".format(str(self.start).zfill(3)))
			url = "https://download.quranicaudio.com/quran/yasser_ad-dussary/{0}.mp3".format(str(self.start).zfill(3))
			urllib.request.urlretrieve(url,'{0}.mp3'.format(str(self.start).zfill(3)),self.show_progress)
			self.start = self.start + 1

aku_ganteng = _3_Sekawan()

print("\n\n\t\t Terima Kasih Sudah Menggunakan Software Kami :D")
print("\n\n Selesai Dalam Waktu {0}".format(time.time()-t1))