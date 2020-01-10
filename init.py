import urllib.request
import platform
from zipfile import ZipFile

urlwin = "https://chromedriver.storage.googleapis.com/79.0.3945.36/chromedriver_win32.zip"
urlmac = "https://chromedriver.storage.googleapis.com/79.0.3945.36/chromedriver_mac64.zip"
urllinux ="https://chromedriver.storage.googleapis.com/79.0.3945.36/chromedriver_linux64.zip"

def download():
	if("Windows" in platform.system()):
		urllib.request.urlretrieve(urlwin, './chromedriver.zip')
	elif("Linux" in platform.system()):
		urllib.request.urlretrieve(urllinux, './chromedriver.zip')
	else:
		urllib.request.urlretrieve(urlwin, './chromedriver.zip')

def unzip():
	with ZipFile('chromedriver.zip', "r") as file:
		file.extractall()

if __name__ == '__main__':
	download()
	print("Downloaded Chromedriver.zip successfully.")
	unzip()
	print("Unzipped successful.")