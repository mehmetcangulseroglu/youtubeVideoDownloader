#youtube video downloader
#pytube kütüphanesini kullanarak youtube videolarını indireceğiz

import pytube
#kullanıcıdan video linkini al
url = input("Lütfen indirmek istediğiniz YouTube videosunun URL'sini girin: ")

path = ""#videonun indirileceği dizin
#en yüksek çözünürlükteki videoyu indir =highest resolution
pytube.YouTube(url).streams.get_highest_resolution().download(path)