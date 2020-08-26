from PyQt5 import QtWidgets
from selenium import webdriver
import os,sys,re
import time
from _radiobutton import Ui_MainWindow


class Modem:
    def __init__(self):
        self.browser = webdriver.Chrome()
        self.girissifresi = 'admin'
        self.girisparolasi = 'admin'

    def Tenda_F3_Resetv1(self):

        self.url = "http://192.168.0.1/"
        self.browser.get(self.url)
        self.browser.find_element_by_xpath(
            '//*[@id="login-password"]').send_keys(self.girissifresi)
        time.sleep(2)
        self.browser.find_element_by_xpath('//*[@id="save"]').click()
        self.browser.find_element_by_xpath('//*[@id="system"]').click()
        time.sleep(1)
        element = self.browser.find_element_by_xpath('//*[@id="restore"]')
        self.browser.execute_script("arguments[0].click();", element)
        time.sleep(2)
        alert = self.browser.switch_to_alert()
        alert.accept()
        time.sleep(20)

    def Tenda_F3_Resetv2(self):

        self.url = "http://192.168.0.1/"
        self.browser.get(self.url)
        time.sleep(4)
        self.browser.find_element_by_xpath('//*[@id="system"]').click()
        time.sleep(4)
        element = self.browser.find_element_by_xpath('//*[@id="restore"]')
        time.sleep(4)
        self.browser.execute_script("arguments[0].click();", element)
        time.sleep(4)
        alert = self.browser.switch_to_alert()
        alert.accept()
        time.sleep(25)

    def Tplink850Rst(self):

        self.url = "http://192.168.0.1/"
        self.browser.get(self.url)
        self.browser.find_element_by_xpath(
            '//*[@id="pc-login-password"]').send_keys(self.girissifresi)
        time.sleep(2)
        self.browser.find_element_by_xpath(
            '//*[@id="pc-login-btn"]').click()
        time.sleep(5)
        self.browser.find_element_by_xpath(
            '/html/body/div[1]/div[1]/div/div[1]/ul/li[3]/span[2]').click()
        time.sleep(4)
        self.browser.find_element_by_xpath(
            '//*[@id="menuTree"]/li[9]/a').click()
        time.sleep(4)
        self.browser.find_element_by_xpath(
            '//*[@id="menuTree"]/li[9]/ul/li[4]/a').click()
        time.sleep(4)
        self.browser.find_element_by_xpath(
            '//*[@id="factoryBtn"]').click()
        time.sleep(2)
        self.browser.find_element_by_xpath(
            '//*[@id="alert-container"]/div/div[4]/div/div[2]/div/div[2]/button').click()
        time.sleep(35)

    def Tplink844Rst(self):

        self.url = "http://192.168.0.1/"
        self.browser.get(self.url)
        time.sleep(4)
        self.browser.find_element_by_xpath(
            '/html/body/div[1]/div/div[1]/div/div[1]/div[2]/div[3]/div[3]/div/div/div[2]/div[2]/div[2]/div[1]/div[2]/div[1]/span[2]/input[1]').send_keys(self.girissifresi)
        time.sleep(2)
        self.browser.find_element_by_xpath(
            '//*[@id="local-login-button"]/div[2]/div[1]/a').click()
        time.sleep(5)
        self.browser.find_element_by_xpath(
            '/html/body/div[1]/div/div[1]/div/div[2]/div[1]/div[3]/div/div[1]/ul/li[4]/a/span[2]').click()
        time.sleep(4)
        self.browser.find_element_by_xpath(
            '/html/body/div[1]/div/div[1]/div/div[2]/div[2]/div/div[1]/div/div[1]/ul/li[10]/a/span[2]').click()
        time.sleep(4)
        self.browser.find_element_by_xpath(
            '//*[@id="navigator"]/div/div[1]/ul/li[10]/ul/li[2]/a/span[2]').click()
        time.sleep(4)
        self.browser.find_element_by_xpath(
            '/html/body/div[1]/div/div[1]/div/div[2]/div[2]/div/div[2]/div[1]/div[3]/div[3]/div[2]/div[2]/div[2]/div[2]/div[2]/div[1]/a').click()
        time.sleep(2)
        self.browser.find_element_by_xpath(
            '//*[@id="factory-confirm-msg-btn-ok"]/div[2]/div[1]/a').click()
        time.sleep(35)

    def TendaBireyselv1(self, kullaniciadi, sifre):

        self.url = 'http://192.168.0.1/'
        self.browser.get(self.url)
        self.browser.find_element_by_xpath(
            '//*[@id="login-password"]').send_keys(self.girissifresi)
        time.sleep(4)
        self.browser.find_element_by_xpath('//*[@id="save"]').click()
        time.sleep(4)
        self.browser.find_element_by_xpath('//*[@id="dhcp"]').click()
        time.sleep(4)
        element = self.browser.find_element_by_xpath(
            '//*[@id="wifiSSID"]')
        element.clear()
        self.browser.find_element_by_xpath(
            '//*[@id="wifiSSID"]').send_keys(kullaniciadi)
        time.sleep(4)
        pw = self.browser.find_element_by_xpath('//*[@id="wifiPwd"]')
        pw.clear()
        self.browser.find_element_by_xpath(
            '//*[@id="wifiPwd"]').send_keys(sifre)
        time.sleep(4)
        self.browser.find_element_by_xpath('//*[@id="save"]').click()
        time.sleep(7)

    def TendaBireyselv2(self, usrnm, sfr):

        self.url = 'http://192.168.0.1/'
        self.browser.get(self.url)
        self.browser.find_element_by_xpath('//*[@id="dhcp"]').click()
        time.sleep(3)
        element = self.browser.find_element_by_xpath(
            '//*[@id="wifiSSID"]')
        time.sleep(3)
        element.clear()
        time.sleep(3)
        self.browser.find_element_by_xpath(
            '//*[@id="wifiSSID"]').send_keys(usrnm)
        time.sleep(3)
        pw = self.browser.find_element_by_xpath('//*[@id="wifiPwd"]')
        pw.clear()
        self.browser.find_element_by_xpath(
            '//*[@id="wifiPwd"]').send_keys(sfr)
        time.sleep(3)
        self.browser.find_element_by_xpath('//*[@id="save"]').click()
        time.sleep(7)

    def TendaF3Merkeziv1(self, name, passwords, rname, rpass):

        self.url = 'http://192.168.0.1/'
        self.browser.get(self.url)
        self.browser.find_element_by_xpath(
            '//*[@id="login-password"]').send_keys(self.girissifresi)
        time.sleep(4)
        self.browser.find_element_by_xpath('//*[@id="save"]').click()
        time.sleep(4)
        self.browser.find_element_by_xpath(
            '//*[@id="wanPPPoEUser"]').send_keys(name)
        time.sleep(4)
        self.browser.find_element_by_xpath(
            '//*[@id="wanPPPoEPwd"]').send_keys(passwords)
        time.sleep(4)
        element = self.browser.find_element_by_xpath(
            '//*[@id="wifiSSID"]')
        element.clear()
        time.sleep(4)
        self.browser.find_element_by_xpath(
            '//*[@id="wifiSSID"]').send_keys(rname)
        time.sleep(4)
        cd = self.browser.find_element_by_xpath('//*[@id="wifiPwd"]')
        cd.clear()
        self.browser.find_element_by_xpath(
            '//*[@id="wifiPwd"]').send_keys(rpass)
        time.sleep(4)
        self.browser.find_element_by_xpath('//*[@id="save"]').click()
        time.sleep(10)

    def TendaF3Merkeziv2(self, name, passwords, rname, rpass):
        self.url = 'http://192.168.0.1/'
        self.browser.get(self.url)
        time.sleep(4)
        self.browser.find_element_by_xpath(
            '//*[@id="wanPPPoEUser"]').send_keys(name)
        time.sleep(4)
        self.browser.find_element_by_xpath(
            '//*[@id="wanPPPoEPwd"]').send_keys(passwords)
        time.sleep(4)
        element = self.browser.find_element_by_xpath(
            '//*[@id="wifiSSID"]')
        element.clear()
        time.sleep(4)
        self.browser.find_element_by_xpath(
            '//*[@id="wifiSSID"]').send_keys(rname)
        time.sleep(4)
        cd = self.browser.find_element_by_xpath('//*[@id="wifiPwd"]')
        cd.clear()
        self.browser.find_element_by_xpath(
            '//*[@id="wifiPwd"]').send_keys(rpass)
        time.sleep(4)
        self.browser.find_element_by_xpath('//*[@id="save"]').click()
        time.sleep(10)

    def Tplink850NBrysl(self, rname, rpass):
        self.url = 'http://192.168.0.1/'
        self.browser.get(self.url)
        self.browser.find_element_by_xpath(
            '//*[@id="pc-setPwd-new"]').send_keys(self.girissifresi)
        time.sleep(4)
        self.browser.find_element_by_xpath(
            '//*[@id="pc-setPwd-confirm"]').send_keys(self.girissifresi)
        time.sleep(4)
        self.browser.find_element_by_xpath(
            '//*[@id="pc-setPwd-btn"]').click()
        time.sleep(4)
        self.browser.find_element_by_xpath('//*[@id="next"]').click()
        time.sleep(5)
        self.browser.find_element_by_xpath('//*[@id="next"]').click()
        time.sleep(5)
        cs = self.browser.find_element_by_xpath('//*[@id="wl24gSSID"]')
        cs.clear()
        self.browser.find_element_by_xpath(
            '//*[@id="wl24gSSID"]').send_keys(rname)
        cz = self.browser.find_element_by_xpath('//*[@id="wl24gPwd"]')
        cz.clear()
        self.browser.find_element_by_xpath(
            '//*[@id="wl24gPwd"]').send_keys(rpass)
        time.sleep(5)
        self.browser.find_element_by_xpath('//*[@id="next"]').click()
        time.sleep(5)
        self.browser.find_element_by_xpath(
            '//*[@id="div_wlanNote"]/form/div[4]/label[1]/span[1]').click()
        time.sleep(5)
        self.browser.find_element_by_xpath('//*[@id="next"]').click()
        time.sleep(5)
        self.browser.find_element_by_xpath('//*[@id="save"]').click()
        time.sleep(30)
        self.browser.find_element_by_xpath(
            '//*[@id="quicksetup-process-content"]/div[3]/div[2]/div/form/button').click()
        time.sleep(5)

    def Tplink844NBrysl(self, rname, rpass):
        self.url = 'http://192.168.0.1/'
        self.browser.get(self.url)
        time.sleep(5)
        self.browser.find_element_by_xpath(
            '/html/body/div[1]/div/div[1]/div/div[1]/div[2]/div[3]/div[1]/div/div/div[2]/div[2]/div[2]/div[1]/div[2]/div[1]/span[2]/input[1]').send_keys(self.girissifresi)
        time.sleep(4)
        self.browser.find_element_by_xpath(
            '/html/body/div[1]/div/div[1]/div/div[1]/div[2]/div[3]/div[1]/div/div/div[2]/div[2]/div[2]/div[2]/div[2]/div[1]/span[2]/input[1]').send_keys(self.girissifresi)
        time.sleep(4)
        self.browser.find_element_by_xpath(
            '//*[@id="local-login-button"]/div[2]/div[1]/a').click()
        time.sleep(4)
        self.browser.find_element_by_xpath(
            '//*[@id="quit-qs-button"]/div[2]/div[1]/a/span[2]').click()
        time.sleep(5)
        self.browser.find_element_by_xpath(
            '//*[@id="global-confirm-btn-ok"]/div[2]/div[1]/a').click()
        time.sleep(5)
        self.browser.find_element_by_xpath(
            '/html/body/div[1]/div/div[1]/div/div[2]/div[1]/div[3]/div/div[1]/ul/li[3]/a/span[2]').click()
        time.sleep(5)
        aff = self.browser.find_element_by_xpath(
            '/html/body/div[1]/div/div[1]/div/div[2]/div[2]/div/div[2]/div[1]/div[3]/div[1]/div[2]/div[2]/div[2]/div[5]/div[2]/div[1]/div[2]/div[1]/span[2]/input')
        aff.clear()
        self.browser.find_element_by_xpath(
            '/html/body/div[1]/div/div[1]/div/div[2]/div[2]/div/div[2]/div[1]/div[3]/div[1]/div[2]/div[2]/div[2]/div[5]/div[2]/div[1]/div[2]/div[1]/span[2]/input').send_keys(rname)
        time.sleep(5)
        cs = self.browser.find_element_by_xpath(
            '/html/body/div[1]/div/div[1]/div/div[2]/div[2]/div/div[2]/div[1]/div[3]/div[1]/div[2]/div[2]/div[2]/div[5]/div[2]/div[4]/div[2]/div/div[2]/div[1]/span[2]/input')
        cs.clear()
        self.browser.find_element_by_xpath(
            '/html/body/div[1]/div/div[1]/div/div[2]/div[2]/div/div[2]/div[1]/div[3]/div[1]/div[2]/div[2]/div[2]/div[5]/div[2]/div[4]/div[2]/div/div[2]/div[1]/span[2]/input').send_keys(rpass)
        time.sleep(5)
        self.browser.find_element_by_xpath(
            '//*[@id="save-data"]/div[2]/div[1]/a').click()
        time.sleep(5)

    def Tplink844NMrkzi(self, name, passwords, rname, rpass):
        self.url = 'http://192.168.0.1/'
        self.browser.get(self.url)
        time.sleep(5)
        self.browser.find_element_by_xpath(
            '/html/body/div[1]/div/div[1]/div/div[1]/div[2]/div[3]/div[1]/div/div/div[2]/div[2]/div[2]/div[1]/div[2]/div[1]/span[2]/input[1]').send_keys(self.girissifresi)
        time.sleep(4)
        self.browser.find_element_by_xpath(
            '/html/body/div[1]/div/div[1]/div/div[1]/div[2]/div[3]/div[1]/div/div/div[2]/div[2]/div[2]/div[2]/div[2]/div[1]/span[2]/input[1]').send_keys(self.girissifresi)
        time.sleep(4)
        self.browser.find_element_by_xpath(
            '//*[@id="local-login-button"]/div[2]/div[1]/a').click()
        time.sleep(4)
        self.browser.find_element_by_xpath(
            '//*[@id="quit-qs-button"]/div[2]/div[1]/a/span[2]').click()
        time.sleep(5)
        self.browser.find_element_by_xpath(
            '//*[@id="global-confirm-btn-ok"]/div[2]/div[1]/a').click()
        time.sleep(5)
        self.browser.find_element_by_xpath(
            '//*[@id="main-menu"]/div/div[1]/ul/li[2]/a/span[2]').click()
        time.sleep(5)
        self.browser.find_element_by_xpath(
            '/html/body/div[1]/div/div[1]/div/div[2]/div[2]/div/div[2]/div[1]/div[3]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[2]/div[1]/div[2]/div[1]/a').click()
        time.sleep(4)
        self.browser.find_element_by_xpath(
            '//*[@id="global-combobox-options"]/div/div[3]/div/div/ul/li[3]/label/span[2]').click()
        time.sleep(5)
        self.browser.find_element_by_xpath(
            '/html/body/div[1]/div/div[1]/div/div[2]/div[2]/div/div[2]/div[1]/div[3]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[2]/div[4]/div/div/div[1]/div[2]/div[1]/span[2]/input').send_keys(name)
        time.sleep(5)
        self.browser.find_element_by_xpath(
            '/html/body/div[1]/div/div[1]/div/div[2]/div[2]/div/div[2]/div[1]/div[3]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[2]/div[4]/div/div/div[2]/div[2]/div[1]/span[2]/input[1]').send_keys(passwords)
        time.sleep(4)
        self.browser.find_element_by_xpath(
            '/html/body/div[1]/div/div[1]/div/div[2]/div[2]/div/div[2]/div[2]/div[2]/div[2]/div[1]/a').click()
        time.sleep(4)
        self.browser.find_element_by_xpath(
            '/html/body/div[1]/div/div[1]/div/div[2]/div[1]/div[3]/div/div[1]/ul/li[3]/a/span[2]').click()
        time.sleep(5)
        aff = self.browser.find_element_by_xpath(
            '/html/body/div[1]/div/div[1]/div/div[2]/div[2]/div/div[2]/div[1]/div[3]/div[1]/div[2]/div[2]/div[2]/div[5]/div[2]/div[1]/div[2]/div[1]/span[2]/input')
        aff.clear()
        self.browser.find_element_by_xpath(
            '/html/body/div[1]/div/div[1]/div/div[2]/div[2]/div/div[2]/div[1]/div[3]/div[1]/div[2]/div[2]/div[2]/div[5]/div[2]/div[1]/div[2]/div[1]/span[2]/input').send_keys(rname)
        time.sleep(5)
        cs = self.browser.find_element_by_xpath(
            '/html/body/div[1]/div/div[1]/div/div[2]/div[2]/div/div[2]/div[1]/div[3]/div[1]/div[2]/div[2]/div[2]/div[5]/div[2]/div[4]/div[2]/div/div[2]/div[1]/span[2]/input')
        cs.clear()
        self.browser.find_element_by_xpath(
            '/html/body/div[1]/div/div[1]/div/div[2]/div[2]/div/div[2]/div[1]/div[3]/div[1]/div[2]/div[2]/div[2]/div[5]/div[2]/div[4]/div[2]/div/div[2]/div[1]/span[2]/input').send_keys(rpass)
        time.sleep(5)
        self.browser.find_element_by_xpath(
            '//*[@id="save-data"]/div[2]/div[1]/a').click()
        time.sleep(5)

    def Tplink850NMrkzi(self, name, passwords, rname, rpass):
        self.url = 'http://192.168.0.1/'
        self.browser.get(self.url)
        self.browser.find_element_by_xpath(
            '//*[@id="pc-setPwd-new"]').send_keys(self.girissifresi)
        time.sleep(4)
        self.browser.find_element_by_xpath(
            '//*[@id="pc-setPwd-confirm"]').send_keys(self.girissifresi)
        time.sleep(4)
        self.browser.find_element_by_xpath(
            '//*[@id="pc-setPwd-btn"]').click()
        time.sleep(4)
        self.browser.find_element_by_xpath(
            '/html/body/div[1]/div[3]/div[3]/div/div[1]/div/div[2]/div[1]/form/div[3]/label/span[1]').click()
        time.sleep(5)
        self.browser.find_element_by_xpath('//*[@id="next"]').click()
        time.sleep(5)
        self.browser.find_element_by_xpath(
            '//*[@id="ppp_username"]').send_keys(name)
        time.sleep(4)
        self.browser.find_element_by_xpath(
            '//*[@id="ppp_password"]').send_keys(passwords)
        time.sleep(4)
        self.browser.find_element_by_xpath('//*[@id="next"]').click()
        time.sleep(4)
        xz = self.browser.find_element_by_xpath('//*[@id="wl24gSSID"]')
        xz.clear()
        self.browser.find_element_by_xpath(
            '//*[@id="wl24gSSID"]').send_keys(rname)
        time.sleep(4)
        xc = self.browser.find_element_by_xpath('//*[@id="wl24gPwd"]')
        xc.clear()
        xc = self.browser.find_element_by_xpath(
            '//*[@id="wl24gPwd"]').send_keys(rpass)
        time.sleep(5)
        self.browser.find_element_by_xpath('//*[@id="next"]').click()
        time.sleep(5)
        self.browser.find_element_by_xpath(
            '//*[@id="div_wlanNote"]/form/div[4]/label[1]/span[1]').click()
        time.sleep(5)
        self.browser.find_element_by_xpath('//*[@id="next"]').click()
        time.sleep(5)
        self.browser.find_element_by_xpath('//*[@id="save"]').click()
        time.sleep(30)
        self.browser.find_element_by_xpath(
            '//*[@id="quicksetup-process-content"]/div[3]/div[2]/div/form/button').click()
        time.sleep(5)


class Window(QtWidgets.QMainWindow, Modem):
    def __init__(self):
        super(Window, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # Reset butonlarini burada entegre ediyoruz.
        self.ui.PushbuttonResetleme.clicked.connect(self.getSelectedBtnReset)
        # Bireysel kurulum butonlarini burada entegre ediyoruz.
        # Brsyl Butonu ile iliskilendirmemiz lazim burada  o islemi yapiyoruz.
        self.ui.btnBrysel.clicked.connect(self.getSelectedBtnBrysel)
        # self.ui.RadioButtonMrkz.clicked.connect(self.onClickMrkz)
        # Merkezi Buton ile iliskilendirmeyi bu metod ile yapiyoruz. burada suan o isleme yapiyoruz.
        self.ui.btnBrysel_3.clicked.connect(self.getSelectedBtnMrkz)
        

    def DonguRstDgr(self):
        try:
            self.Tenda_F3_Resetv1()
        except:
            pass
        try:
            self.Tenda_F3_Resetv2()
        except:
            pass
        try:
            self.Tplink850Rst()
        except:
            pass
        try:
            self.Tplink844Rst()
        except:
            pass

    def DonguBrysl(self):
        try:
            self.TendaBireyselv1(self.txt, self.txt1)
        except:
            pass
        try:
            self.TendaBireyselv2(self.txt, self.txt1)
        except:
            pass
        try:
            self.Tplink850NBrysl(self.txt, self.txt1)
        except:
            pass
        try:
            self.Tplink844NBrysl(self.txt, self.txt1)
        except:
            pass

    def donguMrkz(self):
        try:
            self.Tplink844NMrkzi(self.Rz, self.Sx, self.Az, self.Ez)
        except:
            pass
        try:
            self.TendaF3Merkeziv2(self.Rz, self.Sx, self.Az, self.Ez)
        except:
            pass
        try:
            self.Tplink850NMrkzi(self.Rz, self.Sx, self.Az, self.Ez)
        except:
            pass
        try:
            self.TendaF3Merkeziv1(self.Rz, self.Sx, self.Az, self.Ez)
        except:
            pass

    def getSelectedBtnReset(self):
        self.DonguRstDgr()

    def getSelectedBtnBrysel(self):

        self.txt = self.ui.BryselModemismi.text()
        self.txt1 = self.ui.BryselModemsifresi.text()
        try:
            if len(self.txt1) < 8:
                self.ui.Hatamsg.setText("Hata Sifre En Az 8 Karakter Olmalidir.")
            elif re.search("\s",self.txt1,self.txt):
                self.ui.Hatamsg.setText("Parola bosluk Karakteri Iceremez.")     
            else:
                self.DonguBrysl()
        except Exception as e:
            print('hata',e)
        

    def getSelectedBtnMrkz(self):
        self.Az = self.ui.MerkeziModemismi.text()
        self.Ez = self.ui.MerkeziModemParolasi.text()
        self.Rz = self.ui.MerkeziPpoeIsmi.text()
        self.Sx = self.ui.MerkeziPpoeSifresi.text()
        try:
            if len(self.Ez) < 8:
                self.ui.Hatamsg.setText("Hata Sifre En Az 8 Karakter Olmalidir.")  
            elif re.search("\s",self.Ez):
                self.ui.Hatamsg.setText("Parola bosluk Karakteri Iceremez.")   
            else:
                self.donguMrkz()
        except Exception as e:
            print('hata',e)



app = QtWidgets.QApplication(sys.argv)
win = Window()
win.show()
sys.exit(app.exec_())
