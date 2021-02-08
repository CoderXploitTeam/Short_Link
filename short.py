try:
    import requests, os, json
except ImportError:
    os.system("pip install requests")

logo="""
──────▄▀▄─────▄▀▄   Coder : Tegar Dev
─────▄█░░▀▀▀▀▀░░█▄   [ Dunia Kode ]
─▄▄──█░░░░░░░░░░░█──▄▄
█▄▄█─█░░▀░░┬░░▀░░█─█▄▄█
     [Short Link]
"""
api='http://lolhuman.herokuapp.com/api/shortlink2?url='

req=lambda url: requests.get(url)

if __name__=="__main__":
    os.system("clear")
    print(logo)
    link=input('Enter URL: ')
    rek=req(api+link)
    jeson=json.loads(rek.text)
    print('Hasil ShortLink: '+jeson['result'])