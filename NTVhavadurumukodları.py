import time
import requests
from bs4 import BeautifulSoup
from datetime import datetime

class HavaDurumu():
    def HavaRaporlari(self):
        self.sehir=input("Lutfen Hava Raporları İçin Şehir Giriniz: ")
        url = "https://www.ntvhava.com/{}-hava-durumu".format(self.sehir)
        request = requests.get(url)
        html_icerigi = request.content
        soup = BeautifulSoup(html_icerigi, "html.parser")
        gunduz_sicakliklari = soup.find_all("div",
                                            {"class": "daily-report-tab-content-pane-item-box-bottom-degree-big"})
        gece_sicakliklari = soup.find_all("div",
                                          {"class": "daily-report-tab-content-pane-item-box-bottom-degree-small"})
        hava_durumları = soup.find_all("div", {"class": "daily-report-tab-content-pane-item-text"})

        gun_isimleri=soup.find_all("div",{"class":"daily-report-tab-content-pane-item-date"})

        self.gunduz = []
        self.gece = []
        self.hava = []
        self.gunler=[]

        for x in gunduz_sicakliklari:
            x = x.text
            x = x.strip()
            self.gunduz.append(x)

        for y in gece_sicakliklari:
            y = y.text
            y = y.strip()
            y = y.replace("/", " ")
            self.gece.append(y)

        for z in hava_durumları:
            z = z.text
            z = z.strip()
            self.hava.append(z)

        for a in gun_isimleri:
            a=a.text
            a=a[0:3]
            if(a=="Cmt"):
                a="Cumartesi"
            elif(a=="Paz"):
                a="Pazar"
            elif(a=="Pzt"):
                a="Pazartesi"
            elif(a=="Sal"):
                a="Salı"
            elif(a=="Çar"):
                a="Çarşamba"
            elif(a=="Per"):
                a="Perşembe"
            elif(a=="Cum"):
                a="Cuma"
            self.gunler.append(a)


    def gunluk_hava(self):
        saat=datetime.now().strftime("%H:%M")
        if(saat<="17:00"):
            print("--------------------------------------------------\n{} İçin Bugünün Hava Tahmini Şöyle\nHava:{}\nGündüz Sıcaklığı:{}\nGece Sıcaklığı:{}\n--------------------------------------------------".
                  format(self.sehir.upper(),self.hava[0],self.gunduz[0],self.gece[0]))
        else:
            print("--------------------------------------------------\n{} İçin Bugünün Hava Tahmini Şöyle\nGece Sıcaklığı:{}\n--------------------------------------------------".
                  format(self.sehir,self.gece[0]))

    def yarinki_hava(self):
        print("--------------------------------------------------\n{} İçin Yarınki Hava Tahmini Şöyle\nHava:{}\nGündüz Sıcaklığı:{}\nGece Sıcaklığı:{}\n--------------------------------------------------".
                format( self.sehir.upper(), self.hava[1], self.gunduz[1], self.gece[1]))

    def bes_gunluk(self):
        if(time.strftime("%A")=="Sunday"):
            print(
                "--------------------------------------------------\nBugün İçin  Hava Durumu Şöyle\nHava:{}\nGündüz Sıcaklığı:{}\nGece Sıcaklığı:{}\n--------------------------------------------------\nYarın İçin  Hava Tahmini Şöyle\nHava:{}\nGündüz Sıcaklığı:{}\nGece Sıcaklığı:{}\n--------------------------------------------------\n{} Günü İçin  Hava Tahmini Şöyle\nHava:{}\nGündüz Sıcaklığı:{}\nGece Sıcaklığı:{}\n--------------------------------------------------\n{} Günü İçin  Hava Tahmini Şöyle\nHava:{}\nGündüz Sıcaklığı:{}\nGece Sıcaklığı:{}\n--------------------------------------------------\n--------------------------------------------------\n".
                format(self.hava[0], self.gunduz[0], self.gece[0], self.hava[1], self.gunduz[1], self.gece[1],
                       self.gunler[2], self.hava[2], self.gunduz[2], self.gece[2], self.gunler[3], self.hava[3],
                       self.gunduz[3], self.gece[3]))

        else:
            print("--------------------------------------------------\nBugün İçin  Hava Durumu Şöyle\nHava:{}\nGündüz Sıcaklığı:{}\nGece Sıcaklığı:{}\n--------------------------------------------------\nYarın İçin  Hava Tahmini Şöyle\nHava:{}\nGündüz Sıcaklığı:{}\nGece Sıcaklığı:{}\n--------------------------------------------------\n{} Günü İçin  Hava Tahmini Şöyle\nHava:{}\nGündüz Sıcaklığı:{}\nGece Sıcaklığı:{}\n--------------------------------------------------\n{} Günü İçin  Hava Tahmini Şöyle\nHava:{}\nGündüz Sıcaklığı:{}\nGece Sıcaklığı:{}\n--------------------------------------------------\n--------------------------------------------------\n{} Günü İçin  Hava Tahmini Şöyle\nHava:{}\nGündüz Sıcaklığı:{}\nGece Sıcaklığı:{}\n-------------------------------------------------- ".
              format(self.hava[0],self.gunduz[0],self.gece[0],self.hava[1], self.gunduz[1], self.gece[1],self.gunler[2],self.hava[2],self.gunduz[2],self.gece[2],self.gunler[3],self.hava[3],self.gunduz[3],self.gece[3],self.gunler[4],self.hava[4],self.gunduz[4],self.gece[4]))


hava=HavaDurumu()
hava.HavaRaporlari()
hava.bes_gunluk()

