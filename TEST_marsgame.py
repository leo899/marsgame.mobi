from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import sys
import threading
import tkinter as tk
import datetime
from PIL import Image, ImageTk
import win32gui
import win32.lib.win32con as win32con
import pickle
import os
import pystray

chromeoptions = webdriver.ChromeOptions()
chromeoptions.add_argument("--headless")
chromeoptions.add_argument("--window-size=300,700")
chromeoptions.add_argument("--window-position=800,1")
browser = webdriver.Chrome(options=chromeoptions)
#browser = webdriver.PhantomJS('phantomjs.exe')

try:
    frgrnd_wndw = win32gui.GetForegroundWindow()
    wndw_title = win32gui.GetWindowText(frgrnd_wndw)
    if wndw_title.endswith("py.exe") or wndw_title.endswith("marsgame.mobi.exe"):
        win32gui.ShowWindow(frgrnd_wndw, win32con.SW_HIDE)
except NoSuchElementException:
    pass

stop = False

def authoriz():
    # ---------------------------    АВТОРИЗАЦИЯ    ---------------------
    canvas3.place(relx=0.735, rely=0.03)
    lbox.insert(0, "{} авторизация".format(datetime.datetime.today().strftime("%d.%m.%Y %H.%M.%S:")))
    time.sleep(0.6)
    lbox.insert(0, "{} открываю сайт".format(datetime.datetime.today().strftime("%d.%m.%Y %H.%M.%S:")))
    browser.get("https://marsgame.mobi/login")  # открываем сайт игры
    time.sleep(1)
    lbox.insert(0, "{} Проверяю файл куки".format(datetime.datetime.today().strftime("%d.%m.%Y %H.%M.%S:")))
    if os.path.exists("cookie"):
        lbox.insert(0, "{} Файл куки найден".format(datetime.datetime.today().strftime("%d.%m.%Y %H.%M.%S:")))
        time.sleep(0.5)
        with open("cookie", 'rb') as cookiesfile:
            lbox.insert(0, "{} Подставляем куки".format(datetime.datetime.today().strftime("%d.%m.%Y %H.%M.%S:")))
            cookies = pickle.load(cookiesfile)
            for cookie in cookies:
                browser.add_cookie(cookie)
                lbox.insert(0, "{} Обновляю страницу".format(datetime.datetime.today().strftime("%d.%m.%Y %H.%M.%S:")))
                browser.refresh()
                time.sleep(1)
        try:
            lbox.insert(0, "{} Проверяю доступ".format(datetime.datetime.today().strftime("%d.%m.%Y %H.%M.%S:")))
            WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "img.fl")))
            lbox.insert(0, "{} ДОСТУП ПОЛУЧЕН".format(datetime.datetime.today().strftime("%d.%m.%Y %H.%M.%S:")))
            time.sleep(1)
            threading.Thread(target=info, name="Основные действия").start()
        except TimeoutException:
            lbox.insert(0, "{} Неверный логин".format(datetime.datetime.today().strftime("%d.%m.%Y %H.%M.%S:")))
            time.sleep(0.5)
            lbox.insert(0, "{} ВВЕДИТЕ ДАННЫЕ ДЛЯ ВХОДА".format(datetime.datetime.today().strftime("%d.%m.%Y %H.%M.%S:")))
            canvas3.place_forget()
            frame1.place(relx=0.718, rely=0.012, relheight=0.336, relwidth=0.278)
    else:
        lbox.insert(0, "{} файл куки не найден".format(datetime.datetime.today().strftime("%d.%m.%Y %H.%M.%S:")))
        time.sleep(1)
        lbox.insert(0, "{} ВВЕДИТЕ ДАННЫЕ ДЛЯ ВХОДА".format(datetime.datetime.today().strftime("%d.%m.%Y %H.%M.%S:")))
        canvas3.place_forget()
        frame1.place(relx=0.718, rely=0.012, relheight=0.336, relwidth=0.278)
        #########################

def authoriz2():
    frame1.place(relx=0.718, rely=0.012, relheight=0.336, relwidth=0.278)
    lbox.insert(0, "{} авторизация".format(datetime.datetime.today().strftime("%d.%m.%Y %H.%M.%S:")))
    time.sleep(0.6)
    lbox.insert(0, "{} открываю сайт".format(datetime.datetime.today().strftime("%d.%m.%Y %H.%M.%S:")))
    browser.get("https://marsgame.mobi/login")  # открываем сайт игры
    time.sleep(1)
    a = login.get()
    b = password.get()
    frame1.place_forget()
    logpas = browser.find_element_by_xpath('/html/body/div[3]')  # ищем элемент для ввода логина
    lbox.insert(0, "{} Вводим логин".format(datetime.datetime.today().strftime("%d.%m.%Y %H.%M.%S:")))
    logpas.find_element_by_name('nick').click()  # ищем дочерний элемент для логина и кликаем для активации
    logpas.find_element_by_name('nick').send_keys(a)  # вводим логин
    lbox.insert(0, "{} Вводим пароль".format(datetime.datetime.today().strftime("%d.%m.%Y %H.%M.%S:")))
    logpas.find_element_by_name('password').click()  # ищем дочерний элемент для пароля и кликаем для активации
    logpas.find_element_by_name('password').send_keys(b)  # вводим пароль
    time.sleep(0.4)
    browser.find_element_by_xpath('//*[@id="id1"]/div[4]/input').click()  # ищем кнопку войти и кликаем
    lbox.insert(0, "{} Входим".format(datetime.datetime.today().strftime("%d.%m.%Y %H.%M.%S:")))
    time.sleep(2)
    lbox.insert(0, "{} Сохраняю файл куки".format(datetime.datetime.today().strftime("%d.%m.%Y %H.%M.%S:")))
    with open("cookie", 'wb') as filehandler:
        pickle.dump(browser.get_cookies(), filehandler)
    try:
        lbox.insert(0, "{} Проверяю доступ".format(datetime.datetime.today().strftime("%d.%m.%Y %H.%M.%S:")))
        WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "img.fl")))
        lbox.insert(0, "{} ДОСТУП ПОЛУЧЕН".format(datetime.datetime.today().strftime("%d.%m.%Y %H.%M.%S:")))
        canvas3.place(relx=0.735, rely=0.03)
        time.sleep(2)
        threading.Thread(target=info, name="Основные действия").start()
    except NoSuchElementException:
        lbox.insert(0, "{} Неверный логин".format(datetime.datetime.today().strftime("%d.%m.%Y %H.%M.%S:")))
        time.sleep(1)
        lbox.insert(0, "{} ВВЕДЕННЫЕ ДАННЫЕ НЕВЕРНЫ".format(datetime.datetime.today().strftime("%d.%m.%Y %H.%M.%S:")))
        canvas3.place_forget()
        frame1.place(relx=0.718, rely=0.012, relheight=0.336, relwidth=0.278)

def info():
    lbox.insert(0, "{} Обновляю данные об аккаунте".format(datetime.datetime.today().strftime("%d.%m.%Y %H.%M.%S:")))
    #browser.get("https://marsgame.mobi/profile/5273552")
    browser.find_element_by_xpath("//img[@alt='Профиль']").click()
    time.sleep(1)
    a = browser.find_element_by_css_selector("a.avatar.user").text
    canvas1.place(relx=0.01, rely=0.09)
    label4.configure(text=a)
    b = browser.find_element_by_xpath("/html/body/div[@class='content']/div[1]/span[2]/span").text
    canvas2.place(relx=0.4, rely=0.09)
    label5.configure(text=b)
    f = browser.find_element_by_xpath("/html/body/div[@class='content']/div[2]").text
    label6.configure(text=f)
    k = browser.find_element_by_xpath("/html/body/div[@class='content']/div[@class='minor'][1]").text
    label7.configure(text=k)
    l = browser.find_element_by_xpath("/html/body/div[@class='content']/div[@class='minor'][2]").text
    label8.configure(text=l)
    p = browser.find_element_by_xpath("/html/body/div[@class='content']/div[6]").text
    label9.configure(text=p)
    time.sleep(1)
    t = browser.find_element_by_xpath("//img[@alt='Корпорация']")
    t.click()
    time.sleep(1)
    corp = browser.find_element_by_xpath("/html/body/div[@class='content'][1]").text
    label10.configure(text=corp)
    balans()

def balans():
    browser.get("http://marsgame.mobi/")
    lbox.insert(0, "{} Собираем прибыль".format(datetime.datetime.today().strftime("%d.%m.%Y %H.%M.%S:")))
    i = 0
    while i < 5:
        i = i + 1
        browser.refresh()
        time.sleep(1)
        g = browser.find_element_by_xpath("//div[@class = 'fr']/div").text
        g2 = browser.find_element_by_xpath("//div[@class = 'small']").text
        k = datetime.datetime.today().strftime("%d.%m.%Y %H.%M.%S:")
        lbox.insert(0, "{}  {}  {}".format(k, g, g2))
        time.sleep(10)
    prokachka()

def prokachka():
    lbox.insert(0, "{} Прокачиваем бизнес".format(datetime.datetime.today().strftime("%d.%m.%Y %H.%M.%S:")))
    i = 0
    while i < 3:
        b = browser.find_element_by_xpath("//a[contains(text(), 'Автопрокачка')]")
        b.click()
        time.sleep(1)
        browser.find_element_by_xpath("//img[@class = 'fl']").click()
        time.sleep(1)
        g2 = browser.find_element_by_xpath("//div[@class = 'small']").text
        g = browser.find_element_by_xpath("//div[@class = 'fr']/div").text
        lbox.insert(0, "{} Прокачал".format(datetime.datetime.today().strftime("%d.%m.%Y %H.%M.%S:")))
        time.sleep(0.6)
        k = datetime.datetime.today().strftime("%d.%m.%Y %H.%M.%S:")
        lbox.insert(0, "{}  {} {}".format(k, g, g2))
        time.sleep(2)
        i = i + 1
    kos_musor()

def kos_musor():
    lbox.insert(0, "{} Открываем косический мусор".format(datetime.datetime.today().strftime("%d.%m.%Y %H.%M.%S:")))
    browser.get("https://marsgame.mobi/garbage")  # открываем косический мусор
    time.sleep(2)
    try:
        browser.find_element_by_xpath("//a[contains(text(), 'Купить весь доступный мусор за ')]").click()
        time.sleep(2)
        lbox.insert(0, "{} Космический мусор куплен".format(datetime.datetime.today().strftime("%d.%m.%Y %H.%M.%S:")))
        time.sleep(2)
        corp()
    except:
        lbox.insert(0, "{} Все куплено, ждем".format(datetime.datetime.today().strftime("%d.%m.%Y %H.%M.%S:")))
        time.sleep(2)
        corp()

def corp():
    lbox.insert(0, "{} Открываем корпу".format(datetime.datetime.today().strftime("%d.%m.%Y %H.%M.%S:")))
    browser.get("https://marsgame.mobi/corp/834")  # открываем корпу
    time.sleep(2)
    q = browser.find_element_by_xpath("//div[@class = 'bordered']").text
    lbox.insert(0, "{} {}".format(datetime.datetime.today().strftime("%d.%m.%Y %H.%M.%S:"), q))
    time.sleep(1)
    while True:
        try:
            browser.find_element_by_css_selector('a.btni.mt4').click()
            lbox.insert(0, "{} Получено".format(datetime.datetime.today().strftime("%d.%m.%Y %H.%M.%S:")))
            time.sleep(1)
        except NoSuchElementException as nee:
            lbox.insert(0, "{} Летим за мусором у космического шлюза".format(datetime.datetime.today().strftime("%d.%m.%Y %H.%M.%S:")))
            kosm_shl()

def kosm_shl():
    while True:
        try:
            browser.find_element_by_xpath("//a[contains(text(), 'Получить мусор')]").click()
            #browser.find_element_by_css_selector('a.btni').click()
            time.sleep(1)
        except NoSuchElementException as nee:
            lbox.insert(0, "{} Космический Шлюз --> мусор получен".format(datetime.datetime.today().strftime("%d.%m.%Y %H.%M.%S:")))
            time.sleep(0.6)
            lbox.insert(0, "{} Переходим качать комнаты".format(datetime.datetime.today().strftime("%d.%m.%Y %H.%M.%S:")))
            komnati()

def komnati():
    lbox.insert(0, "{} Прокачиваем комнаты".format(datetime.datetime.today().strftime("%d.%m.%Y %H.%M.%S:")))
    browser.get("https://marsgame.mobi/sb/9969316")
    time.sleep(2)
    #i = 0
    #while i < 94:
    l = browser.find_element_by_xpath("//div[@class = 'center tdbrown big']").text
    k = ""
    while k != l:
        a = browser.find_element_by_xpath("//div[@class = 'center tdbrown big']").text
        lbox.insert(0, "{} {}".format(datetime.datetime.today().strftime("%d.%m.%Y %H.%M.%S:"), a))
        browser.find_element_by_partial_link_text('Автопрокачка').click()
        time.sleep(1)
        lbox.insert(0, "{} Готово".format(datetime.datetime.today().strftime("%d.%m.%Y %H.%M.%S:")))
        browser.find_element_by_xpath("//a[@class = 'fr']").click()
        time.sleep(1)
        k = browser.find_element_by_xpath("//div[@class = 'center tdbrown big']").text
        label1.configure(text=k)
    gryadki()

def gryadki():
    lbox.insert(0, "{} Смотрим грядки".format(datetime.datetime.today().strftime("%d.%m.%Y %H.%M.%S:")))
    browser.get("https://marsgame.mobi/garden")
    time.sleep(2)
    while True:
        try:
            browser.find_element_by_xpath("//a[contains(text(), 'Сбор ')]").click()
            time.sleep(1)
        except:
            q = browser.find_element_by_xpath("//span[@class = 'btni']").text
            lbox.insert(0, "{} {}".format(datetime.datetime.today().strftime("%d.%m.%Y %H.%M.%S:"), q))
            time.sleep(0.6)
            lbox.insert(0, "{} Все собрано".format(datetime.datetime.today().strftime("%d.%m.%Y %H.%M.%S:")))
            time.sleep(2)
            balans()

def hide_to_tray(_event=None):
    tray_icon = pystray.Icon("marsgame.mobi", title="marsgame.mobi")  # create the tray icon
    tray_icon.icon = Image.open("images/icon.png")  # open the icon using PIL
    tray_icon.menu = pystray.Menu(pystray.MenuItem("Показать", lambda: tray_icon.stop(), default=True),
                                  pystray.MenuItem("Выход", lambda: ex, default=False))  # create the menu
    root.withdraw()  # hide the window
    tray_icon.run()  # run the icon's main loop
    root.deiconify()




def ex():
    browser.quit()
    stop = True
    root.destroy()
    sys.exit()
# *************************************************************************************
root = tk.Tk()
root.title("marsgame.mobi")
root.geometry('500x400')
root.resizable(False, False)
root.iconphoto(True, tk.PhotoImage(file='images/icon.png'))

lbox = tk.Listbox(root)
lbox.place(relx=0.01, rely=0.6, width=350, height=150)

button1 = tk.Button(root)
button1.configure(text="Выход")
button1.place(relx=0.790, rely=0.910)
button1.bind("<Button-1>", lambda e: ex())

frame1 = tk.Frame(root, relief="raised", borderwidth=2)
#frame1.place(relx=0.718, rely=0.012, relheight=0.336, relwidth=0.278)

label1 = tk.Label(frame1)
label1.configure(text="Логин")
label1.place(relx=0.1, rely=0.02)
login = tk.Entry(frame1)
login.place(relx=0.06, rely=0.18)

label2 = tk.Label(frame1)
label2.configure(text="Пароль")
label2.place(relx=0.1, rely=0.34)
password = tk.Entry(frame1)
password.configure(show="*")
password.place(relx=0.06, rely=0.5)
button2 = tk.Button(frame1)
button2.configure(text="Вход")
button2.place(relx=0.3, rely=0.72)
button2.bind("<Button-1>", lambda e: threading.Thread(target=authoriz2, name="Авторизация из frame1").start())

button3 = tk.Button(root)
button3.configure(text="Свернуть в трей")
button3.place(relx=0.740, rely=0.820)
button3.bind("<Button-1>", lambda e: threading.Thread(target=hide_to_tray, name="Свернуть в трей").start())

# инфо об аке
frame2 = tk.Frame(root, relief="raised", borderwidth=1)
frame2.place(relx=0.01, rely=0.01, height=230, width=350)

label3 = tk.Label(frame2)
label3.configure(fg="#C13006", font=("arial", 10, "bold"))
label3.configure(text="Информация об аккаунте")
label3.configure(anchor="center")
label3.place(relx=0.21, rely=0, height=19, width=190)

label4 = tk.Label(frame2) # ник **************************************
label4.configure(text="")
label4.configure(anchor="w")
label4.configure(font=12)
label4.place(relx=0.10, rely=0.113, height=18, width=150)

canvas1 = tk.Canvas(frame2, height=25, width=25) # картинка акк
image1 = Image.open("images/akk.png")
image1 = image1.resize((25, 25), Image.ANTIALIAS)
image1 = ImageTk.PhotoImage(image1)
canvas1.create_image(0, 0, anchor="nw", image=image1)

label5 = tk.Label(frame2) # кристал
label5.configure(text="")
label5.configure(anchor="w")
label5.configure(font=12)
label5.place(relx=0.50, rely=0.113, height=18, width=150)

canvas2 = tk.Canvas(frame2, height=25, width=25) # картинка кристалл
image2 = Image.open("images/ruby.png")
image2 = image2.resize((25, 25), Image.ANTIALIAS)
image2 = ImageTk.PhotoImage(image2)
canvas2.create_image(0, 0, anchor="nw", image=image2)

label6 = tk.Label(frame2)
label6.configure(text="Обновляю данные")
label6.configure(anchor="center")
label6.configure(font=12)
label6.place(relx=0.01, rely=0.220, height=58, width=270)

label7 = tk.Label(frame2)
label7.configure(text="")
label7.configure(anchor="center")
label7.configure(font=12)
label7.place(relx=0.01, rely=0.500, height=18, width=270)

label8 = tk.Label(frame2)
label8.configure(text="")
label8.configure(anchor="center")
label8.configure(font=12)
label8.place(relx=0.01, rely=0.590, height=18, width=270)

label9 = tk.Label(frame2)
label9.configure(text="")
label9.configure(anchor="center")
label9.configure(font=12)
label9.place(relx=0.01, rely=0.680, height=19, width=270)

label10 = tk.Label(frame2)
label10.configure(text="")
label10.configure(anchor="center")
label10.configure(font=12)
label10.place(relx=0.01, rely=0.758, height=50, width=270)

canvas3 = tk.Canvas(root, height=300, width=116) # картинка справа
image3 = Image.open("images/start_logo.png")
#image3 = image3.resize((25, 25), Image.ANTIALIAS)
image3 = ImageTk.PhotoImage(image3)
canvas3.create_image(0, 0, anchor="nw", image=image3)

# запуск авторизации для проверки куки
threading.Thread(target=authoriz, name="Авторизация").start()

root.mainloop()
