import scrapy

class KartSpider(scrapy.Spider):
    name = "kart"
    start_urls = [
  "https://praga-kart.de/Produkte-Teile/Rotax/",
  "https://praga-kart.de/Produkte-Teile/Rotax/REIFEN/",
  "https://praga-kart.de/Produkte-Teile/Rotax/MOTOREN/",
  "https://praga-kart.de/Produkte-Teile/Rotax/Kurbelgehaeuse-Wasserpumpe-E-Starter-Antrieb/",
  "https://praga-kart.de/Produkte-Teile/Rotax/Antriebsstrang-Getriebe-Ausgleichswelle/",
  "https://praga-kart.de/Produkte-Teile/Rotax/Fliekraftkupplung/",
  "https://praga-kart.de/Produkte-Teile/Rotax/Zylinder/",
  "https://praga-kart.de/Produkte-Teile/Rotax/Kurbelwelle-Kolben/",
  "https://praga-kart.de/Produkte-Teile/Rotax/Vergaser/",
  "https://praga-kart.de/Produkte-Teile/Rotax/Kuehlung/",
  "https://praga-kart.de/Produkte-Teile/Rotax/Elektronische-Komponenten/",
  "https://praga-kart.de/Produkte-Teile/Rotax/Kabelbaum/",
  "https://praga-kart.de/Produkte-Teile/Rotax/E-RAVE-System/",
  "https://praga-kart.de/Produkte-Teile/Rotax/Ansaugschalldaempfer/",
  "https://praga-kart.de/Produkte-Teile/Rotax/Auspuff/",
  "https://praga-kart.de/Produkte-Teile/Rotax/Batterien/",
  "https://praga-kart.de/Produkte-Teile/Rotax/ELEKTRONIK/",
  "https://praga-kart.de/Produkte-Teile/Rotax/Kraftstoffsystem/",
  "https://praga-kart.de/Produkte-Teile/IPK/",
  "https://praga-kart.de/Produkte-Teile/IPK/BREMSSYSTEME/STR-V2-Vorderes-Bremssystem/",
  "https://praga-kart.de/Produkte-Teile/IPK/BREMSSYSTEME/RBS-V2-Hinteres-Bremssystem/",
  "https://praga-kart.de/Produkte-Teile/IPK/BREMSSYSTEME/MKB-V2-Hinteres-Bremssystem/",
  "https://praga-kart.de/Produkte-Teile/IPK/BREMSSYSTEME/RBS-V3-Hinteres-Bremssystem/",
  "https://praga-kart.de/Produkte-Teile/IPK/BREMSSYSTEME/BLACK-LINE-Hinteres-Bremssystem/",
  "https://praga-kart.de/Produkte-Teile/IPK/BREMSSYSTEME/BABY-Kart-Mechanisches-Bremssystem/",
  "https://praga-kart.de/Produkte-Teile/IPK/BREMSSYSTEME/BREMSPUMPE/",
  "https://praga-kart.de/Produkte-Teile/IPK/BREMSSYSTEME/BREMSENZUBEHOER/",
  "https://praga-kart.de/Produkte-Teile/IPK/KUEHLUNG/",
  "https://praga-kart.de/Produkte-Teile/IPK/WASSERPUMPE/",
  "https://praga-kart.de/Produkte-Teile/IPK/KUPPLUNGSGESTAENGE/",
  "https://praga-kart.de/Produkte-Teile/IPK/KETTEN-RITZEL/",
  "https://praga-kart.de/Produkte-Teile/IPK/KETTEN-RITZEL/KETTEN/",
  "https://praga-kart.de/Produkte-Teile/IPK/KETTEN-RITZEL/RITZEL/",
  "https://praga-kart.de/Produkte-Teile/IPK/ACHSEN-NABEN-LENKUNG/Achsen/",
  "https://praga-kart.de/Produkte-Teile/IPK/ACHSEN-NABEN-LENKUNG/Achsschenkel/",
  "https://praga-kart.de/Produkte-Teile/IPK/ACHSEN-NABEN-LENKUNG/Achsenzubehoer/",
  "https://praga-kart.de/Produkte-Teile/IPK/ACHSEN-NABEN-LENKUNG/Naben/",
  "https://praga-kart.de/Produkte-Teile/IPK/ACHSEN-NABEN-LENKUNG/Lenksaeule/",
  "https://praga-kart.de/Produkte-Teile/IPK/AUSPUFF/",
  "https://praga-kart.de/Produkte-Teile/IPK/RAHMEN/",
  "https://praga-kart.de/Produkte-Teile/IPK/STABILISATOREN/",
  "https://praga-kart.de/Produkte-Teile/IPK/LAGER/",
  "https://praga-kart.de/Produkte-Teile/IPK/SITZE/",
  "https://praga-kart.de/Produkte-Teile/IPK/PEDALE/",
  "https://praga-kart.de/Produkte-Teile/IPK/ALU-PEDALE/",
  "https://praga-kart.de/Produkte-Teile/IPK/FELGEN/",
  "https://praga-kart.de/Produkte-Teile/PRAGA-FORMULA-K/",
  "https://praga-kart.de/Produkte-Teile/PRAGA-FORMULA-K/KARTS/",
  "https://praga-kart.de/Produkte-Teile/PRAGA-FORMULA-K/ACCESSOIRES/",
  "https://praga-kart.de/Produkte-Teile/PRAGA-FORMULA-K/KLEIDUNG/",
  "https://praga-kart.de/Produkte-Teile/PRAGA-FORMULA-K/PFLEGEPRODUKTE/",
  "https://praga-kart.de/Produkte-Teile/PRAGA-FORMULA-K/WERKZEUGE/",
  "https://praga-kart.de/Produkte-Teile/PRAGA-FORMULA-K/SCHRAUBEN-KLEINTEILE/",
  "https://praga-kart.de/Produkte-Teile/PRAGA-FORMULA-K/SCHRAUBEN-KLEINTEILE/Schrauben/",
  "https://praga-kart.de/Produkte-Teile/PRAGA-FORMULA-K/SCHRAUBEN-KLEINTEILE/Muttern/",
  "https://praga-kart.de/Produkte-Teile/PRAGA-FORMULA-K/SCHRAUBEN-KLEINTEILE/Scheiben/",
  "https://praga-kart.de/Produkte-Teile/PRAGA-FORMULA-K/SCHRAUBEN-KLEINTEILE/Dichtungen/",
  "https://praga-kart.de/Produkte-Teile/PRAGA-FORMULA-K/SCHRAUBEN-KLEINTEILE/Schellen/",
  "https://praga-kart.de/Produkte-Teile/PRAGA-FORMULA-K/SCHRAUBEN-KLEINTEILE/Ringe/",
  "https://praga-kart.de/Produkte-Teile/PRAGA-FORMULA-K/SCHRAUBEN-KLEINTEILE/Stifte/",
  "https://praga-kart.de/Produkte-Teile/ALFANO/",
  "https://praga-kart.de/Produkte-Teile/ALFANO/KRONOS/",
  "https://praga-kart.de/Produkte-Teile/ALFANO/LAPTIMER/",
  "https://praga-kart.de/Produkte-Teile/ALFANO/TYRECONTROL/",
  "https://praga-kart.de/Produkte-Teile/ALFANO/ZUBEHOER/",
  "https://praga-kart.de/Produkte-Teile/ALFANO/ZUBEHOER/BEWEGUNG/",
  "https://praga-kart.de/Produkte-Teile/ALFANO/ZUBEHOER/SPEED/",
  "https://praga-kart.de/Produkte-Teile/ALFANO/ZUBEHOER/HALTER/",
  "https://praga-kart.de/Produkte-Teile/ALFANO/ZUBEHOER/TYRECONTROLL/",
  "https://praga-kart.de/Produkte-Teile/ALFANO/ZUBEHOER/KABEL-HUBS/",
  "https://praga-kart.de/Produkte-Teile/ALFANO/ZUBEHOER/ZEIT/",
  "https://praga-kart.de/Produkte-Teile/ALFANO/ZUBEHOER/DREHZAHL/",
  "https://praga-kart.de/Produkte-Teile/ALFANO/ZUBEHOER/STROMVERSORGUNG/",
  "https://praga-kart.de/Produkte-Teile/ALFANO/ZUBEHOER/TEMPERATUR/",
  "https://praga-kart.de/Produkte-Teile/ALFANO/ZUBEHOER/MODULE-BOXEN/",
  "https://praga-kart.de/Produkte-Teile/ALFANO/ZUBEHOER/ZUBEHOER/",
  "https://praga-kart.de/Produkte-Teile/ALFANO/ZUBEHOER/DOWNLOADING/"
]

    def parse(self, response):
        if response.css("h1::text").get() is not None:
            yield {
                "title" : response.css("h1::text").get().strip(),
                "category" : " > ".join(response.css("span.breadcrumb-title::text").getall()),
                "price" : response.css("p.product-detail-price::text").get().strip(),
                "part_number": response.css("span.product-detail-ordernumber::text").get().strip(),
                "description": "\n".join(list(filter(lambda y: y != "", map(lambda x: x.strip(), response.css("div.product-detail-description-text ::text").extract())))),
                "url": response.url,
                "img": response.css("img.gallery-slider-image::attr(src)").get()
            }
        else: #if there's no h1 header that means we're on the item list
            next_pages = response.css("a.product-name::attr(href)").getall()

            for page in next_pages:
                yield response.follow(page, callback = self.parse)

        # get numbered pages in case the next page exists and isn't disabled
        if response.css("li.page-item.page-next:not(.disabled)").get() is not None:
            if response.url[-1].isnumeric(): #check if last digit is a number, if it is a number that means we're on page 2 at least
                page_num = response.url[-1]
                yield response.follow(response.url[:-1] + str(int(page_num) + 1), callback = self.parse)
            else:
                yield response.follow(response.url + "?order=name-asc&p=2")
