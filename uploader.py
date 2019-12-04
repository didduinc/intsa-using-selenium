#To use this script all the file names should be stared with word 'meme' and end with a Number. Ex: meme1

from selenium import webdriver
from selenium.webdriver.chrome.options import *
from selenium.webdriver.common.keys import Keys
import autoit
from random import randint
import time
username = "###" #Enter your username
passwd = "###"   #Enter Your password
driverpth = "C:/python/python3.8.0/Scripts/chromedriver.exe" #Path to the chrome driver

options = Options()
options.add_argument("--log-level=3")

options.add_argument("--silent")
#options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument("--disable-logging")
options.add_argument("--mute-audio")
# mobile_emulation = {"deviceName": "Nexus 5"}
# options.add_experimental_option("mobileEmulation", mobile_emulation)
options.add_argument(
    '--user-agent=Mozilla/5.0 (iPhone; CPU iPhone OS 10_3 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) CriOS/56.0.2924.75 Mobile/14E5239e Safari/602.1')
driver = webdriver.Chrome(executable_path="C:\python\\python3.8.0\\Scripts\\chromedriver.exe", options=options)
driver.get("https://www.instagram.com/accounts/login/?hl=en")
time.sleep(3)
driver.find_element_by_xpath(
    "//*[@id='react-root']/section/main/article/div/div/div/form/div[4]/div/label/input").send_keys(username)
time.sleep(0.5)
driver.find_element_by_xpath(
    "//*[@id='react-root']/section/main/article/div/div/div/form/div[5]/div/label/input").send_keys(passwd)
time.sleep(0.5)
driver.find_element_by_xpath("//*[@id='react-root']/section/main/article/div/div/div/form/div[7]/button/div").click()

while 1:
    time.sleep(1)
    try:
        driver.find_element_by_xpath("//*[@id='react-root']/section/main/div/button").click()
        break
    except:
        pass
while 1:
    time.sleep(1)
    try:
        driver.find_element_by_xpath("/html/body/div[3]/div/div/div[3]/button[2]").click()
        break
    except:
        pass

def callrepeat(aa):
    aaa = aa
    if aa == 1:
        photopath = 'D:\memes\meme'+str(aaa)+'.jpg'
    else:
        photopath = 'meme'+str(aaa)+'.jpg'
    tags = ["#meme","#collegememes", "#memeworld", "#stolenmemes", "#memeinoneplace", "#diddumemes", "#diddu", "#maymay",
            "#memebaba", "#behappy", "memelaughter", "#indianmemes", "#memesdaily", "#memestagram", "#memesfordays",
            "#memesindia", "#memesme", "#memesespa", "#memestar", "#memes4ever", "#memesbelike",
            "#memestealer", "#memeslayer", "#memesforlife", "#memesrlife", "#memesindian", "#memes4life",
            "#memesarelife", "#memesdank", "#memes2k19", "#memesloot", "#MemesUniversity", "#memes2good", "#memesftw",
            "#memesandbeauty", "#memesdaily", "#bestmemes", "#memeslivesmatter", "#memesofig", "#memesilikonu",
            "#memesbro", "#memesupreme", "#memesgraciosos", "#memes4days", "#memesexo", "#memesforyou", "#memes4dayz",
            "#memes2019", "#memesforever", "#memesareme", "#memesfunny", "#memesofinstagram",
            "#memesdaily", "#bestmemesdaily", "#memesdaliy", "#memesjunkie", "#memesinstagram", "#memes4you", "#memestgram",
            "#memesonly", "#memesexy", "meandme","#meme", "#memes", "#funny", "#dankmemes", "#memesdaily", "#funnymemes",
            "#lol", "#dank", "#humor", "#like", "#follow", "#lmao", "#dankmeme", "#edgymemes", "#offensivememes",
            "#love", "#fortnite", "#comedy", "#dailymemes", "#edgy", "#fun","#funnymeme"]
    taglength = len(tags)

    phototext = ""
    p = 0
    tagCounter = randint(3, 7)
    while p < tagCounter:
        p = p + 1
        a = randint(0, taglength-1)
        phototext = phototext + tags[a] + " "
    i = 0
    phototext = phototext.rstrip()
    z = randint(4, 8)
    while i < z:
        i = i + 1
        time.sleep(1)
        driver.find_element_by_css_selector('body').send_keys(Keys.PAGE_DOWN)
        try:
            driver.find_element_by_xpath("/html/body/div[3]/div/div/div[3]/button[2]").click()
            break
        except:
            pass
    if aa == 1:
        tim = 4
    else:
        tim = 1
    driver.find_element_by_xpath("//div[@role='menuitem']").click()
    time.sleep(tim)
    autoit.win_active("Open")  # open can change by your os language if not open change that
    time.sleep(tim)
    autoit.control_send("Open", "Edit1", photopath)
    time.sleep(tim)
    autoit.control_send("Open", "Edit1", "{ENTER}")
    time.sleep(1.3)
    try:
        driver.find_element_by_css_selector('button.pHnkA').click()
    except:
        pass
    time.sleep(tim)
    driver.find_element_by_xpath("//*[@id='react-root']/section/div[1]/header/div/div[2]/button").click()
    time.sleep(tim)
    driver.find_element_by_xpath("//*[@id='react-root']/section/div[2]/section[1]/div[1]/textarea").send_keys(phototext)
    time.sleep(tim)
    driver.find_element_by_xpath("//*[@id='react-root']/section/div[1]/header/div/div[2]/button").click()
    time.sleep(tim)
    print(aaa) #just in case if the script stops to know where to start next time
    return;

i = 0
while i < 100000:
    i = i+1
    callrepeat(i)
