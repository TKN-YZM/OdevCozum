elif "hava durumu tahmini" in gelen_ses or "hava durumu" in gelen_ses:
self.seslendirme("hangi şehrin hava durumunu istersiniz")
cevap = self.ses_kayit()

url = "https://www.ntvhava.com/{}-hava-durumu".format(cevap)
request = requests.get(url)
html_icerigi = request.content
soup = BeautifulSoup(html_icerigi, "html.parser")
gunduz_sicakliklari = soup.find_all("div",
                                    {"class": "daily-report-tab-content-pane-item-box-bottom-degree-big"})
gece_sicakliklari = soup.find_all("div",
                                  {"class": "daily-report-tab-content-pane-item-box-bottom-degree-small"})
hava_durumları = soup.find_all("div", {"class": "daily-report-tab-content-pane-item-text"})

gun_isimleri = soup.find_all("div", {
    "class": "daily-report-tab-content-pane-item-date"})  # Gün isimlerini internetten çekiyoruz

gunler = []
gunduz = []
gece = []
hava = []
for x in gunduz_sicakliklari:
    x = x.text
    gunduz.append(x)
for y in gece_sicakliklari:
    y = y.text
    gece.append(y)
for z in hava_durumları:
    z = z.text
    hava.append(z)

for a in gun_isimleri:  # gün isimlerini düzenlemeliyiz
    a = a.text
    a = a[0:3]
    if (a == "Cmt"):
        a = "Cumartesi"
    elif (a == "Paz"):
        a = "Pazar"
    elif (a == "Pzt"):
        a = "Pazartesi"
    elif (a == "Sal"):
        a = "Salı"
    elif (a == "Çar"):
        a = "Çarşamba"
    elif (a == "Per"):
        a = "Perşembe"
    elif (a == "Cum"):
        a = "Cuma"
    self.gunler.append(a)

self.seslendirme("Günlük mü  yarının mı ya da haftalık raporlarını mı istiyorsunuz?")
cevap2 = self.ses_kayit()

saat = datetime.now().strftime("%H:%M")
anlik_metin = " "  # bugünün metini bu olacak her şeyden önce saat kontrolü yapıyoruz eğer akşam 5 den sonra ise sadece bugünün gece raporlarını veriyoruz
if (saat <= "17:00"):
    alnik_metin = "{} İçin Bugünün Hava Tahmini ŞöyleHava:{}Gündüz Sıcaklığı:{}Gece Sıcaklığı:{}".format(cevap, hava[0],
                                                                                                         gunduz[0],
                                                                                                         gece[0])

    anlik_metin = "{} İçin Bugünün Hava Tahmini Şöyle\nGece Sıcaklığı:{}".format(cevap, gece[0])

yarinki_metin = "{} İçin Yarınki Hava Tahmini ŞöyleHava:{}Gündüz Sıcaklığı:{}Gece Sıcaklığı:{}".format(cevap, hava[1],
                                                                                                       gunduz[1],
                                                                                                       gece[1])
besgunluk_metin = "Bugün İçin  Hava Durumu ŞöyleHava:{} Gündüz Sıcaklığı:{}Gece Sıcaklığı:{} Yarın İçin  Hava Tahmini Şöylen Hava:{}Gündüz Sıcaklığı:{}Gece Sıcaklığı:{} {} Günü İçin  Hava Tahmini Şöyle Hava:{} Gündüz Sıcaklığı:{} Gece Sıcaklığı:{} {} Günü İçin  Hava Tahmini Şöyle\nHava:{}\nGündüz Sıcaklığı:{} Gece Sıcaklığı:{}".format(
    hava[0], gunduz[0], gece[0], hava[1], gunduz[1], gece[1], gunler[2], hava[2], gunduz[2], gece[2], gunler[3],
    hava[3], gunduz[3], gece[3])

if (cevap2 == "günlük"):
    self.seslendirme(anlik_metin)

elif (cevap2 == "yarınki hava" or cevap2 == "yarın" or cevap2 == "yarının durumu"):
    self.seslendirme(yarinki_metin)

elif (cevap2 == "beş günlük" or cevap2 == "beş gün"):
    self.seslendirme(besgunluk_metin)