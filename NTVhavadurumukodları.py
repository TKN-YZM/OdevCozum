  elif "hava durumu tahmini" in gelen_ses or "hava durumu" in gelen_ses:
            self.seslendirme("hangi şehrin hava durumunu istersiniz")
            cevap=self.ses_kayit()

            url = "https://www.ntvhava.com/{}-hava-durumu".format(cevap)
            request = requests.get(url)
            html_icerigi = request.content
            soup = BeautifulSoup(html_icerigi, "html.parser")
            gunduz_sicakliklari = soup.find_all("div",
                                          {"class": "daily-report-tab-content-pane-item-box-bottom-degree-big"})
            gece_sicakliklari = soup.find_all("div",
                                              {"class": "daily-report-tab-content-pane-item-box-bottom-degree-small"})
            hava_durumları = soup.find_all("div", {"class": "daily-report-tab-content-pane-item-text"})
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

            self.seslendirme("Günlük yarın ya da haftalık raporları mı istiyorsunuz?")
            cevap2=self.ses_kayit()
            
            if(cevap2=="günlük"):
                gunluk_hava()
                
            else if(cevap2=="yarınki hava" or cevap2=="yarın" or cevap2=="yarının durumu"):
                yarinki_hava()
               
            else if(cevap2=="beş günlük" or cevap2=="beş gün"):
                bes_gunluk()
            
            def gunluk_hava(self):
                saat=datetime.now().strftime("%H:%M")
                if(saat<="17:00"):
                    metin="{} İçin Bugünün Hava Tahmini ŞöyleHava:{}Gündüz Sıcaklığı:{}Gece Sıcaklığı:{}". #Gunluk hava raporu isterse saat 5 den sonra gün içinin bir anlamı olmaz 
                          format(cevap,hava[0],gunduz[0],gece[0]))             #O yüzden akşam 5 sonrası sadece gece raporuna bakmalıyız bakmalıyız
                    self.seslendirme(metin)
                else:
                    metin="{} İçin Bugünün Hava Tahmini Şöyle\nGece Sıcaklığı:{}".
                          format(cevap,gece[0]))
                    self.seslendirme(metin)

            def yarinki_hava(self):
                metin="{} İçin Yarınki Hava Tahmini ŞöyleHava:{}Gündüz Sıcaklığı:{}Gece Sıcaklığı:{}".
                        format( cevap, hava[1], gunduz[1], gece[1]))
                self.seslendirme(metin)

            def bes_gunluk(self):
                    metin="Bugün İçin  Hava Durumu ŞöyleHava:{} Gündüz Sıcaklığı:{}Gece Sıcaklığı:{} Yarın İçin  Hava Tahmini Şöylen Hava:{}Gündüz Sıcaklığı:{}Gece Sıcaklığı:{} {} Günü İçin  Hava Tahmini Şöyle Hava:{} Gündüz Sıcaklığı:{} Gece Sıcaklığı:{} {} Günü İçin  Hava Tahmini Şöyle\nHava:{}\nGündüz Sıcaklığı:{} Gece Sıcaklığı:{}".
                        format(hava[0], gunduz[0], gece[0], hava[1], gunduz[1], gece[1],
                               gunler[2], hava[2], gunduz[2], gece[2], gunler[3], hava[3],
                               gunduz[3], gece[3]))  
                    self.seslendirme(metin)

            

   

        
