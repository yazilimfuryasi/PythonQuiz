"""
13.08.2021
github - instagram: @yazilimfuryasi
yazilimfuryasi.com
#   #  #   ####  #  #     #  #   #        ####  #   #  ####  #   #  #    ##   #
#   # # #     #  #  #     #  ## ##        #     #   #  #   # #   # # #  #  #  #
 # #  # #    #   #  #     #  ## ##        #     #   #  #   #  # #  # #  #     #
  #   # #   #    #  #     #  ## ##        ####  #   #  ####    #   # #   ##   #
  #   ###   #    #  #     #  # # #        #     #   #  #  #    #   ###     #  #
  #  #   # #     #  #     #  # # #        #     #   #  #  #    #  #   # #  #  #
  #  #   # ####  #  ####  #  # # #        #      ###   #   #   #  #   #  ##   #
"""

import beautifultable
from sorular import dy, secmeli
from random import choice
from beautifultable import BeautifulTable
from dashtable import data2rst
import colorama
from colorama import init, Fore, Back
init(convert=True)
colorama.init(autoreset=True)

table = BeautifulTable()

class Quiz:
    def __init__(self):
        print(Fore.YELLOW + """
        +----------- Python Sınav Uygulaması -----------+
        |                                               |
        |    Doğru Yanlış için           | 1            |
        |    Çoktan Seçmeli Sorular için | 2            |
        |    Çıkmak için                 | 3 veya exit  |
        |    Yazınız.                                   |
        +-----------------------------------------------+
""")
        while True:
            giris = input(Fore.BLUE+"Seçenek: ")

            if giris == "1":
                return self.dogruYanlis()
            elif giris == "2":
                return self.secmeliSorular()
            elif giris == "exit" or giris == "3":
                exit()
            else:
                print(Fore.RED+"HATALI SEÇİM")

    def kontrol(self, soru, cvp, skor):
        if soru['cevap'].upper() == cvp.upper():
            # print(Fore.GREEN + f"Doğru Cevap! \nPuan {skor + 10}!")
            print(Fore.GREEN + f"Doğru Cevap!\n")
            print(Fore.CYAN + "*"*30)
            self.d += 1
            self.skor += 10
        else:
            print(Fore.RED + f"\nYanlış Cevap :( \nDoğru cevap {Fore.GREEN + soru['cevap'].upper()+ Fore.RED} olacaktı.\n")
            print(Fore.CYAN + "*"*30)
            self.y += 1

    def dogruYanlis(self):
        print(Fore.YELLOW+"- Gelen sorulara cevap vermek için, D/Y tuşlarını kullanın."+ Fore.RED +"\n- Büyük küçük duyarlı değildir."+ Fore.YELLOW +"\n- Soruyu geçmek için 'pas' yazmanız yeterlidir."+ Fore.RED +"\n- Her Soru 10 Puan'dır."+ Fore.YELLOW +"\n- Sorular rastgele sorulmaktadır.\n\n")
        self.d = 0
        self.y = 0
        self.pas = 0
        self.skor = 0
        skor = 0
        soru_sayisi = 1
        liste = []
        for _ in range(100):
            try:
                rast = choice(dy)
            except:
                pass

            if rast['soru'] in liste:
                continue
            else:
                liste.append(rast['soru'])

            if soru_sayisi >= 11:
                break

            table.columns.header = [Fore.RED + "Soru: "+str(soru_sayisi)]
            soru_sayisi += 1
            table.rows.append([Fore.YELLOW + rast['soru']])
            print(table)
            table.rows.clear()

            cevap = input(Fore.YELLOW + "Cevap: ")
            if cevap == "pas":
                print("Soru Geçildi.")
                self.pas += 1
                continue
            self.kontrol(rast, cevap, skor)

        tablae = [
        ["Test Bitti", ""],
        [Fore.GREEN+"Doğru", str(self.d)],
        [Fore.LIGHTRED_EX+"Yanlış", str(self.y)],
        [Fore.LIGHTBLUE_EX+"Boş", str(self.pas)],
        [Fore.LIGHTYELLOW_EX+"Toplam Puan", str(self.skor)]
                ]

        print(Fore.BLUE + data2rst(tablae, use_headers=True))
#         print(Back.LIGHTCYAN_EX + Fore.RED + f"""
# +--------------------------Test Bitti----------------------+
# |    .                                                     |
# |                    {Fore.GREEN}Doğru: {Fore.GREEN+ str(self.d)}                              |
# |                    {Fore.LIGHTRED_EX}Yanlış: {str(self.y)}                             |
# |                    {Fore.LIGHTBLUE_EX}Boş: {str(self.pas)}                                |
# |                    {Fore.LIGHTYELLOW_EX}Toplam Puan: {str(self.skor)}                       |
# +----------------------------------------------------------+
# """)

    def secmeliSorular(self):
        print(Fore.YELLOW+"- Gelen sorulara cevap vermek için, şıkları ekrana yazın. Örn: 'A'"+ Fore.RED +"\n- Büyük küçük duyarlı değildir."+ Fore.YELLOW +"\n- Soruyu geçmek için 'pas' yazmanız yeterlidir."+ Fore.RED +"\n- Her Soru 10 Puan'dır."+ Fore.YELLOW +"\n- Sorular rastgele sorulmaktadır.\n\n")
        self.d = 0
        self.y = 0
        self.pas = 0
        self.skor = 0
        skor = 0
        soru_sayisi = 1

        # print(secmeli[1]["soru"])
        liste = []
        for _ in range(100):
            try:
                rast = choice(secmeli)
            except:
                pass

            if rast['soru'] in liste:
                continue
            else:
                liste.append(rast['soru'])

            if soru_sayisi >= 11:
                break

            table.columns.header = [Fore.RED + "Soru: "+str(soru_sayisi)]
            soru_sayisi += 1
            table.rows.append([Fore.YELLOW + rast['soru']])
            table.column_alignments = beautifultable.ALIGN_LEFT
            print(table)
            table.rows.clear()

            cevap = input("Cevap: ")
            if cevap == "pas":
                print("Soru Geçildi.")
                self.pas += 1
                continue
            self.kontrol(rast, cevap, skor)

        tablae = [
        ["Test Bitti", ""],
        [Fore.GREEN+"Doğru", str(self.d)],
        [Fore.LIGHTRED_EX+"Yanlış", str(self.y)],
        [Fore.LIGHTBLUE_EX+"Boş", str(self.pas)],
        [Fore.LIGHTYELLOW_EX+"Toplam Puan", str(self.skor)]
                ]
        print(Fore.BLUE + data2rst(tablae, use_headers=True))

Quiz()