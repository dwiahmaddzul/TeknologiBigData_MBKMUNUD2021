# Import library SNSCRAPE
#!pip install git+https://github.com/JustAnotherArchivist/snscrape.git

#Dwi Ahmad Dzulhijjah 2105551162

import os

#Scrapping menggunakan kata kunci "rakyat tiktok, akun tiktok, manusia tiktok, asal tiktok, sumber tiktok"

os.system("snscrape --jsonl --max-results 500000 --since 2018-06-01 twitter-search \"rakyat tiktok until:2021-10-31\" > rakyattiktok.json")


# os.system("snscrape --jsonl --max-results 500000 --since 2018-06-01 twitter-search \"akun tiktok until:2021-10-31\" > akuntiktok.json")
# os.system("snscrape --jsonl --max-results 500000 --since 2018-06-01 twitter-search \"manusia tiktok until:2021-10-31\" > manusiatiktok.json")
# os.system("snscrape --jsonl --max-results 500000 --since 2018-06-01 twitter-search \"anak tiktok until:2021-10-31\" > anaktiktok.json")
# os.system("snscrape --jsonl --max-results 500000 --since 2018-06-01 twitter-search \"dari tiktok until:2021-10-31\" > daritiktok.json")
# os.system("snscrape --jsonl --max-results 500000 --since 2018-06-01 twitter-search \"asal tiktok until:2021-10-31\" > asaltiktok.json")
# os.system("snscrape --jsonl --max-results 500000 --since 2018-06-01 twitter-search \"profil tiktok until:2021-10-31\" > profiltiktok.json")
# os.system("snscrape --jsonl --max-results 500000 --since 2018-06-01 twitter-search \"sumber tiktok until:2021-10-31\" > sumbertiktok.json")
# os.system("snscrape --jsonl --max-results 500000 --since 2018-06-01 twitter-search \"rakyat tiktok until:2021-10-31\" > rakyattiktok.json")
# os.system("snscrape --jsonl --max-results 500000 --since 2018-06-01 twitter-search \"orang tiktok until:2021-10-31\" > orangtiktok.json")
# os.system("snscrape --jsonl --max-results 500000 --since 2018-06-01 twitter-search \"kaum tiktok until:2021-10-31\" > kaumtiktok.json")
# os.system("snscrape --jsonl --max-results 500000 --since 2018-06-01 twitter-search \"manusia tiktok until:2021-10-31\" > manusiatiktok.json")
# os.system("snscrape --jsonl --max-results 500000 --since 2018-06-01 twitter-search \"umat tiktok until:2021-10-31\" > umattiktok.json")
# os.system("snscrape --jsonl --max-results 500000 --since 2018-06-01 twitter-search \"penghuni tiktok until:2021-10-31\" > penghunitiktok.json")
