from xml.etree.ElementTree import TreeBuilder
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
import time
import random
import pyautogui
import keyboard
import pyperclip
import pandas as pd
import os
from dateutil import parser
import datetime
import re
import numpy as np
from selenium.webdriver.common.action_chains import ActionChains
boss = [
        ['https://twitter.com/doAmFPS/status/1518546952887193601', # 19, 20 need do again
        'https://twitter.com/KuangTV/status/1519918461492682753',
        'https://twitter.com/Dittozkul/status/1518365748946780166',
        'https://twitter.com/clonezval/status/1519100262840942595',
        'https://twitter.com/Kurokazexx/status/1518544075900997632',
        'https://twitter.com/lmAvenger/status/1518439025312477185',
        'https://twitter.com/marmarpits/status/1518368276929302528'],
        ['https://twitter.com/hellowreckk/status/1518409152292290560',
        'https://twitter.com/emilong21/status/1518798911401766912',
        'https://twitter.com/AceAvenger_/status/1518955753511567361',
        'https://twitter.com/qvGeSports/status/1520705241326526465',
        'https://twitter.com/onscreenlol/status/1518633421362319361',
        'https://twitter.com/KayrosGG/status/1518639516445143040',
        'https://twitter.com/eugenevlr/status/1518454267056726016',
        'https://twitter.com/BowmanOG_/status/1518337972877283330',
        'https://twitter.com/SkuLLyJai/status/1518369499732320257',
        'https://twitter.com/Lear_VAL/status/1518371170093080578',
        'https://twitter.com/emilong21/status/1518798911401766912',
        'https://twitter.com/lmAvenger/status/1518439025312477185',
        'https://twitter.com/marmarpits/status/1518368276929302528',
        'https://twitter.com/hellowreckk/status/1518409152292290560',
        'https://twitter.com/AceAvenger_/status/1518955753511567361',
        'https://twitter.com/qvGeSports/status/1520705241326526465',
        'https://twitter.com/onscreenlol/status/1518633421362319361',
        'https://twitter.com/KayrosGG/status/1518639516445143040',
        'https://twitter.com/eugenevlr/status/1518454267056726016',
        'https://twitter.com/BowmanOG_/status/1518337972877283330',
        'https://twitter.com/SkuLLyJai/status/1518369499732320257',
        'https://twitter.com/Lear_VAL/status/1518371170093080578'],
        ['https://twitter.com/jawgemo/status/1518367820672765953',
        'https://twitter.com/TokkiRue/status/1518350974401851395',
        'https://twitter.com/badcuzpad/status/1518983239481888769',
        'https://twitter.com/facekidval/status/1518602861101273088',
        'https://twitter.com/TTVMadnessMedia/status/1518434001685344257',
        'https://twitter.com/Skillgap/status/1518341245780869120',
        'https://twitter.com/Shiratsuna_/status/1518723398561669124',
        'https://twitter.com/ACTiV_val/status/1518620852899565568',
        'https://twitter.com/juseuaim/status/1518983468230795269',
        'https://twitter.com/KONEQT_VALORANT/status/1518887137223004160',
        'https://twitter.com/VolatileHQ/status/1520339992232439814',
        'https://twitter.com/slushyval/status/1518698930644525057',
        'https://twitter.com/Nexqal/status/1518349705641697282'],
        ['https://twitter.com/Judlei_/status/1520689491090018306',
        'https://twitter.com/XSET/status/1518331324523761664',
        'https://twitter.com/tokibbi/status/1518336627419934720',
        'https://twitter.com/X13GG/status/1518364681252921348',
        'https://twitter.com/tummit_/status/1518368796561575937',
        'https://twitter.com/tussalty/status/1518351976823730184',
        'https://twitter.com/janitrr/status/1518467404434604032',
        'https://twitter.com/Slastt/status/1518430471847223296',
        'https://twitter.com/Duskzi/status/1518398708022272000'],
        ['https://twitter.com/kaytea_xp/status/1518391936255545344',
        'https://twitter.com/ValorantRed/status/1518366670259204098',
        'https://twitter.com/Banjowtf/status/1520820881869574144',
        'https://twitter.com/Wygers/status/1519013469458206721',
        'https://twitter.com/acrethedog/status/1519100133077491712',
        'https://twitter.com/o_alphaa/status/1519099154399694852',
        'https://twitter.com/lykachu_/status/1518625223570034689',
        'https://twitter.com/Uzoies/status/1518330828098613250']
    ]
class web():
    ac_original = []
    pw_original = []
    account_count = 0
    current_tab = 0
    seperator = '-  -  '    
    layer = 0
    post_status = 'default'
    relogin_status = 'n'
    block_status = 66
    main_window = ''
    current_link = ''
    df = pd.DataFrame()
    df_final = pd.DataFrame()
    df_record = pd.DataFrame()
    page_status = None
    done_comment = ['(DONE)liked','(DONE)retweeted','(DONE)retweetConfirmed','(DONE)reply','(DONE)reply sent','(DONE)followed']

    def twitter_account(twitter_account_number):
        account_options = {0: '@KameronW_Stone', 1: '@Andrew_Grime574', 2:'@Mick_j0n',
                       3: '@jacoBstro4', 4: '@S_K32T', 5: '@sambjmf',
                       6: '@SivZon', 7: '@Greenhattt', 8: '@MillerNileOrz',
                       9: '@antoniochorr', 10: '@ernestTTy', 11: '@Aeveweis',
                       12: '@harperjames31', 13: '@JesseliamxX', 14: '@Martin07215',
                       15: '@xav1errr', 16: '@Stephzip', 17: '@RainingTrainn',
                       18: '@issacbrook19', 19: '@BonoLanda'}
        num = twitter_account_number-1
        if num == 0:
            ac1 = account_options[1]
            ac2 = account_options[2]
            ac3 = account_options[4]
        elif num == 1:
            ac1 = account_options[0]
            ac2 = account_options[2]
            ac3 = account_options[3]
        elif num == 2:
            ac1 = account_options[1]
            ac2 = account_options[0]
            ac3 = account_options[5]
        elif num == 3:
            ac1 = account_options[4]
            ac2 = account_options[5] # change to 5
            ac3 = account_options[7]
        elif num == 4:
            ac1 = account_options[3]
            ac2 = account_options[5] # change to 5
            ac3 = account_options[8]
        elif num == 5:
            ac1 = account_options[3]
            ac2 = account_options[4]
            ac3 = account_options[6]
        elif num == 6:
            ac1 = account_options[7]
            ac2 = account_options[8]
            ac3 = account_options[11]
        elif num == 7:
            ac1 = account_options[8]
            ac2 = account_options[6]
            ac3 = account_options[14]
        elif num == 8:
            ac1 = account_options[7]
            ac2 = account_options[6]
            ac3 = account_options[12]
        elif num == 9:
            ac1 = account_options[10]
            ac2 = account_options[13]
            ac3 = account_options[2]
        elif num == 10:
            ac1 = account_options[11]
            ac2 = account_options[9]
            ac3 = account_options[0]
        elif num == 11:
            ac1 = account_options[10]
            ac2 = account_options[9]
            ac3 = account_options[1]
        elif num == 12:
            ac1 = account_options[13]
            ac2 = account_options[14]
            ac3 = account_options[11]
        elif num == 13:
            ac1 = account_options[12]
            ac2 = account_options[14]
            ac3 = account_options[9]
        elif num == 14:
            ac1 = account_options[12]
            ac2 = account_options[13]
            ac3 = account_options[10]
        elif num == 15:
            ac1 = account_options[6]
            ac2 = account_options[13]
            ac3 = account_options[2]
        elif num == 16:
            ac1 = account_options[12]
            ac2 = account_options[7]
            ac3 = account_options[5]
        elif num == 17:
            ac1 = account_options[0]
            ac2 = account_options[10]
            ac3 = account_options[8]
        elif num == 18:
            ac1 = account_options[10]
            ac2 = account_options[5]
            ac3 = account_options[12]
        elif num == 19:
            ac1 = account_options[4]
            ac2 = account_options[2]
            ac3 = account_options[15]
 
        if num <= 2 or num == 9 or num == 14:
            reply_eg = (
            f"I really want this",
            f"Lets go boys, good luck for all",
            f"Please, I want to win this",
            f"good luck to everyone, may the best win",
            f"Been trying to win giveaways but I cannot",
            f"Now if anyone reply to this I’m insane",
            f"Fingers crossed",
            f"My wallet can’t afford these but I want them so bad BRO",
            f"I never won a giveaway in my life... I hope can I get it this time",
            f"I nominate you guys to summon your powers and help me win this giveaway",
            f"Sorry for tagging u guys but I am so desperate to win this giveaway",
            f"All I wanted is to get this awesome giveaway",
            f"I will tell everyone that I win this giveaway",
            f"Hope you pick me coz I really need this",
            f"You will change my life if I win this hahhahahhahaha",
            f"By any chance if I win the giveaway, the next meal is on me",
            f"Hope I can win this giveaway coz I absolutely want this so bad",
            f"Lets go boys",
            f"This giveaway is fire, good luck to all of you",
            f"May the LUCK be with me",
            f"Wish me luck guys",
            f"We are getting it this time boys",
            f"I want this giveaway so bad",
            f"Sorry for bothering you again orz",
            f"We are getting it this time boys",
            f"Can you get me this if I is not picked",
            f"Im tagging you coz you are my friends",
            f"I want this man",
            f"Your names will be remembered if I win this!",
            f"Do you believe I will win this giveaway?",
            f"This will be the first time I ever win a giveaway if I win this",
            f"Me and the boys will never give up",
            f"I hope I still get a chance at winning",
            f"Please!!!!!!",
            f"That will help me a lot thx!",
            f"Hope i win the giveaway or my faith this is gone for good",
            f"Please pick me!",
            f"I am broke in terms of money and friends",
            f"Thanks for the chance",
            f"u guys were my top 2 tags for some reason ur welcome",
            f"done! gl :D",
            f"yo thank you for the chance :D",
            f"In fate, I trust.",
            f"PLZ",
            f"My besties lmao",
            f"you know it",
            f"good luck to all",
            f"check this out",
            f"just a few more times",
            f"I nominate you",
            f"again and again",
            f"sheeeeeeeesh",
            f"you can join too",
            f"thank you",
            f"GL to everyone",
            f"I wish everyone good luck",
            f"I hope I can win this",
            f"cmon help me out",
            f"you should enter this giveaway too ",
            f"thanks a lot for the giveaway",
            f"really hope I get this man",
            f"sorry for the tags love you",
            f"I'm so desperate",
            f"there's a chance",
            f"pray for me plz",
            f"u r my only friends"
 
           )
        elif 3 <= num <= 5 or num == 10 or num == 12:
            reply_eg =(
                f"give me some luck gang",
                f"I know you will be mad if dont tag you for this",
                f"If you are reading this comment, which means I deserve to win this giveaway!",
                f"This is what friends for",
                f"This is the meaning of friends",
                f"Good luck to all of you",
                f"We got this, I have faith in you",
                f"I am determined to win this",
                f"You really should join this giveaway as well",
                f"This is the time where we will win",
                f"I believe you wont mind for helping to win this",
                f"Luckily I still have you guys after all these time",
                f"Check this out. This is legit",
                f"Lets cross fingers for this one",
                f"I need your luck on this one",
                f"Believe me, I will win this time",
                f"Tell me, what is possibility of not winning this",
                f"It is so hard to win these giveaways, sad life",
                f"I am feeling lucky this time",
                f"You really should join this as well",
                f"This the proof of friendship",
                f"Hope one of us can finally win a giveaway FOR ONCE",
                f"This is happening, I cant wait for it",
                f"Check this out, I was saying about this giveaway just now",
                f"You really should join this as well",
                f"This is happening, I cant wait for it",
                f"There is a reason that why I tag you",
                f"For SURE I get this one hahaha",
                f"And it begins once again",
                f"I believe in my luck",
                f"It’s gonna happen in the near future",
                f"We were just talkin about these!!!",
                f"Im sorry for the incoming giveaway spam",
                f"I want this so bad and you wont get it",
                f"I’m down bad for this",
                f"Am I ever gonna win one",
                f"PLEASEEEEEEEEEEEE",
                f"thank you for your contributions",
                f"If you never tried, you never win",
                f"I will win this by the next time we meet ",
                f"I am glad that you are my friends",
                f"I will never give up until I success",
                f"here we go again lmao",
                f"Please, I want this giveaway",
                f"I want it so bad",
                f"lemme win",
                f"haha",
                f"let's goooooo",
                f"I need you now",
                f"plz dont mind",
                f"here we go",
                f"Hope I win this one",
                f"maybe this time",
                f"This is gonna be me",
                f"better late than sorry",
                f"yes sir",
                f"have faith in me",
                f"how to actually win one of these",
                f"Best of luck to everyone",
                f"lets go sir",
                f"I would love to win this"
                )
        elif 15 <= num <= 19:
            reply_eg = (
                f"Lets go",
                f"I never win these ffs",
                f"let me win this so i win these so i can stop tagging yall",
                f"pick me!",
                f"I'm down for it",
                f"It's the time",
                f"Please",
                f"lemme win",
                f"haha",
                f"let's goooooo",
                f"I need you now",
                f"plz dont mind",
                f"here we go",
                f"Hope I win this one",
                f"maybe this time",
                f"This is gonna be me",
                f"better late than sorry",
                f"yes sir",
                f"have faith in me",
                f"how to actually win one of these",
                f"Best of luck to everyone",
                f"lets go sir",
                f"I would love to win this"
                f"PLZ",
                f"My besties lmao",
                f"you know it",
                f"good luck to all",
                f"check this out",
                f"just a few more times",
                f"I nominate you",
                f"again and again",
                f"sheeeeeeeesh",
                f"you can join too",
                f"thank you",
                f"GL to everyone",
                f"I wish everyone good luck",
                f"I hope I can win this",
                f"cmon help me out",
                f"you should enter this giveaway too ",
                f"thanks a lot for the giveaway",
                f"really hope I get this man",
                f"sorry for the tags love you",
                f"I'm so desperate",
                f"there's a chance",
                f"pray for me plz",
                f"u r my only friends"
                )
        else:
            reply_eg =(
                f"You definitely need to check this out lmao",
                f"Good luck to everyone",
                f"Some things are destined to be",
                f"It just takes us a couple of tries to win",
                f"I can see my chances here",
                f"Fate is never fair but Im winning this",
                f"Im telling you Im winning this time",
                f"Dont worry if you think I cant never win",
                f"Im born lucky you know",
                f"When the time comes, it comes",
                f"I need some support from you two",
                f"I know you are backing me up",
                f"Sometimes what we need is hope",
                f"GL to all!!",
                f"I need you both",
                f"never give up",
                f"Have faith in me",
                f"Do you think I can win this",
                f"I got to win once eventually",
                f"How are you doing these days",
                f"I definitely dont tag u frequently",
                f"You know what this is",
                f"yall know the drill",
                f"Gimmie plz",
                f"Sorry for the shameless tag haha",
                f"yall are amazing",
                f"maybe this time omg",
                f"pls universe give me this",
                f"this is the time where we will win one",
                f"I never doubt the possibility of not winning this",
                f"hope ya don’t mind this, but I really want to win this",
                f"I know you love me tagging u in these",
                f"I never win but I'll try and try again",
                f"I am once again tagging you to win a giveaway",
                f"hundreds tries but never win let's see",
                f"plz pray for me again",
                f"didn’t win the last one, so here we go again",
                f"ya both getting tagged because I WANT THIS",
                f"imma prove that giveaways are real to u guys",
                f"these are my only friends",
                f"Lets go",
                f"I never win these ffs",
                f"let me win this so i win these so i can stop tagging yall",
                f"pick me!",
                f"I'm down for it",
                f"It's the time",
                f"Please",
                )

        pickkk = random.randint(4, 5)
        if pickkk == 4:
            numberofaccount = f'{ac2} {ac1}'
        elif pickkk == 5:
            numberofaccount = f'{ac1} {ac2}'
        new = random.choice(reply_eg)
        tag = random.randint(1, 2)
        if tag == 2:
            the_reply_eg = f'{new} {numberofaccount}'
        else:
            the_reply_eg = f'{numberofaccount} {new}'
        return the_reply_eg
    def extract_links(num=False, screenshot=False):
        print(web.seperator*4, 'starting...')
        while True:
            if keyboard.is_pressed('1'):
                while True:
                    pyautogui.hotkey('ctrl', 'l', delay=0.25)
                    time.sleep(0.4)
                    pyautogui.hotkey('ctrl', 'c', delay=0.25)
                    aasd = str(pyperclip.paste())
                    if aasd in web.thelist:
                        return()
                    web.thelist.append(aasd)
                    pyautogui.hotkey('ctrl', 'tab', delay=0.25)
                    time.sleep(0.2)
    def wait():
        time.sleep(random.randint(1, 3))
    def website_type(type, xpath, wait, comment=False):
        while True:
            try:
                a = WebDriverWait(web.driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, xpath))
                )
                if wait == 0:
                    pass
                else:
                    web.wait()
                # a.click()
                a.send_keys(type)
                a.send_keys(Keys.RETURN)
                web.comment(comment)
                break
            except:
                pass
    def comment(comment):
        if comment:
            print(web.seperator*web.layer*4, comment)
            web.df = web.df.append({web.ac[web.account_count]: comment}, ignore_index = True)
    def website_click_by_class(path, comment=False):
        while True:
            try:
                a = WebDriverWait(web.driver, 10).until(
                    EC.presence_of_element_located((By.CLASS_NAME, path))
                )
                web.wait()
                a.click()
                web.comment(comment)
                break
            except:
                pass
    def website_click(xpath, wait=False, comment=False):
        while True:
            try:
                a = WebDriverWait(web.driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, xpath))
                )
                if wait == 0:
                    pass
                else:
                    web.wait()
                a.click()
                web.comment(comment)
                break
            except:
                pass      
    def website_try_click(xpath, target=False,  wait=False, comment=False, relogin=False, hardness=False):
        if (hardness == 0) or (hardness is None):
            try:
                a = web.driver.find_elements(By.XPATH, xpath)
                if target > 1:
                    for i in range(len(a)):
                        if wait == 0:
                            pass
                        else:
                            web.wait()
                        a[i].click()
                else:
                    web.df = web.df.append({web.ac[web.account_count]: '!!! ohno'}, ignore_index = True)
                    if wait == 0:
                        pass
                    else:
                        web.wait()
                    a[0].click()
                web.comment(comment)
            except:
                if relogin:
                    try:
                        a = web.driver.find_element(By.XPATH, "//*[@class='css-901oao css-16my406 r-poiln3 r-bcqeeo r-qvutc0'][text()='Log out']")
                        a.click()
                        web.wait()
                    except:
                        pass
                else:
                    pass
        elif hardness == 1:
            try:
                a = WebDriverWait(web.driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, xpath))
                )
                if target > 1:
                    for i in range(len(a)):
                        a[i].click()
                        web.wait()
                else:
                    a[i].click()
                    web.wait()
                web.comment(comment)
            except:
                pass
    def waitnclick(xpath, comment=False):
        while True:
            try:
                a = WebDriverWait(web.driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, xpath))
                )
                a.click()
                web.comment(comment)
                break
            except:
                web.website_try_click("//*[@class='css-901oao css-16my406 r-poiln3 r-bcqeeo r-qvutc0'][text()='Keep less relevant ads']", 1, 'bug cleared (keep less relevant ads)')
    def website_check_if_done(type):
        if type == 'tweet':
            try:
                a = web.driver.find_element(By.XPATH, './/div[@aria-label="Liked"]')
                web.post_status = 'done'
            except:
                pass
            try:
                a = web.driver.find_element(By.XPATH, './/div[@aria-label="Like"]')
                web.post_status = 'not done'
            except:
                pass
        elif type == 'block':
            attempt = 0
            while True:
                attempt +=1
                try:
                    a = web.driver.find_element(By.XPATH, '//div[starts-with (@aria-label,"Follow @")][@class="css-18t94o4 css-1dbjc4n r-42olwf r-sdzlij r-1phboty r-rs99b7 r-2yi16 r-1qi8awa r-1ny4l3l r-ymttw5 r-o7ynqc r-6416eg r-lrvibr"]')
                    web.block_status = 0
                    break
                except:
                    pass
                try:
                    a = web.driver.find_element(By.XPATH, '//div[starts-with (@aria-label,"Following @")]')
                    web.block_status = 0
                    break
                except:
                    pass
                try:
                    a = web.driver.find_element(By.XPATH, "//div[contains(@data-testid,'unblock')]")
                    web.block_status = 1
                    break
                except:
                    pass
                if attempt>10:
                    web.driver.refresh()
                    print(web.seperator*web.layer*4, '!refreshed')
                    web.df = web.df.append({web.ac[web.account_count]: '!1refreshed'}, ignore_index = True)
                    attempt=0
    def follow():
        bbb_count = 0
        followed_b4 = 0
        followed_now = 0
        for bbb in web.driver.find_elements(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/section/div/div/div[1]/div/div[1]/article/div/div/div/div[3]/div[1]/div/div/div/span/a'):
            bbb_count +=1
            hreftext = str(bbb.get_attribute('href'))[20:] # href e.g. https://twitter.com/lmAvenger
            a = ActionChains(web.driver)
            a.move_to_element(bbb).perform()
            while True:
                try:
                    aria = web.driver.find_element(By.XPATH,'//*[@class="css-1dbjc4n r-xoduu5 r-1r5jyh0 r-1ipicw7"]/div/div[1]/div[2]/div').get_attribute('aria-label')
                    print(hreftext)
                    print(aria)
                    if hreftext in str(aria):
                        break
                except:
                    pass
            n = web.driver.find_element(By.XPATH,'//*[@class="css-1dbjc4n r-xoduu5 r-1r5jyh0 r-1ipicw7"]/div/div[1]/div[2]/div/span/span/span')
            print(n.text)
            if n.text == 'Following':
                followed_b4 +=1
            elif n.text == 'Follow':
                while True:
                    try:
                        b = web.driver.find_element(By.XPATH,'//*[@class="css-1dbjc4n r-xoduu5 r-1r5jyh0 r-1ipicw7"]/div/div[1]/div[2]/div')
                        a.move_to_element(b).click().perform()
                        web.wait()
                        followed_now+=1
                        break
                    except:
                        pass
            elif n.text == 'Blocked':
                print('check3')
            a = ActionChains(web.driver)
            b = web.driver.find_element(By.XPATH,"//*[@aria-label='Twitter']")
            a.move_to_element(b).perform()
            while True:
                try:
                    web.driver.find_element(By.XPATH,'//*[@class="css-1dbjc4n r-xoduu5 r-1r5jyh0 r-1ipicw7"]/div/div[1]/div[2]/div')
                except:
                    break
        web.comment(f'(5){bbb_count}relevant found')
        try:
            bbb
            web.comment(f'(6){followed_now}followed')
        except:
            web.website_try_click("//*[@class='css-901oao css-16my406 r-poiln3 r-bcqeeo r-qvutc0'][text()='Follow']", target=2, wait = 1, comment = f'(?)followed')
        web.comment(f'(7){followed_b4}following')
    def liker():
        #check if page is loaded
        web.if_desired_page_loaded('liker')
        try:
            a = web.driver.find_element(By.XPATH, "//*[text()='Blocked']")
            print(web.seperator*web.layer*4, '!!!!!!!!!!!!!!!!!!!!!!!!!!!!!  \n performing on a BLOCKED ACCOUNT \n !!!!!!!!!!!!!!!!!!!!!!!!!!!!!  ')
            web.df = web.df.append({web.ac[web.account_count]: 'performing on a BLOCKED ACCOUNT'}, ignore_index = True)
        except:
            web.follow()
            web.website_check_if_done('tweet')
            if web.post_status == 'not done':
                web.website_click('.//div[@data-testid="like"]', wait = 0, comment = '(1)liked')
                web.website_click('.//div[@data-testid="retweet"]', wait = 1,comment = '(2)retweeted')
                web.website_click('.//div[@data-testid="retweetConfirm"]', wait = 1,comment = '(3)retweetConfirmed')
                web.website_type(web.twitter_account(1), './/div[@data-testid="tweetTextarea_0"]', wait = None, comment = None)
                web.website_click("//*[@class='css-901oao css-16my406 r-poiln3 r-bcqeeo r-qvutc0'][text()='Reply']", wait = 1, comment = '(4)reply sent')
                # web.follow()
                # web.website_try_click("//*[@class='css-18t94o4 css-1dbjc4n r-1ny4l3l r-ymttw5 r-1f1sjgu r-o7ynqc r-6416eg']/div/div[2]/div[1]/div[2]/div[1]/div[1]/span/span[text()='Following']", target=2, wait = None, comment = '(6)followed')
            else:
                for iii in range(len(web.done_comment)):
                    web.df = web.df.append({web.ac[web.account_count]: web.done_comment[iii]}, ignore_index = True)
    def inside_if_desired_page_loaded(type):
        while True:
            try:
                if type == 'blocker':
                    web.until_found("//*[@class='css-1dbjc4n r-6gpygo r-14gqq1x']")
                elif type == 'liker':
                    web.until_found('.//div[@data-testid="reply"]')
                break
            except:
                pass
            try:
                web.driver.find_element(By.XPATH, "//*[text()='Retry']") #retry
                web.driver.refresh()
            except:
                pass
    def if_desired_page_loaded(type):
        web.page_status = None
        web.inside_if_desired_page_loaded(type)
        try: #if logined in or not (liker same as blocker)
            web.driver.find_element(By.XPATH, "//*[text()='Don’t miss what’s happening']")
            web.driver.refresh()
            print(web.seperator*web.layer*4, '!2refreshed')
            web.df = web.df.append({web.ac[web.account_count]: '!2refreshed'}, ignore_index = True)
            web.inside_if_desired_page_loaded(type)
        except:
            pass
        if type == 'blocker':
            try:
                a = web.driver.find_element(By.XPATH, "//*[text()='This account doesn’t exist']")
                web.df = web.df.append({web.ac[web.account_count]: '!!!!!!!!!!!!! \n This account doesn’t exist \n !!!!!!!!!!!!!'}, ignore_index = True)
                print(web.seperator*web.layer*4, '!!!!!!!!!!!!! \n This account doesn’t exist \n !!!!!!!!!!!!!')
                web.page_status = None
            except:
                web.page_status = 'exist'
        elif type == 'liker':
            try:
                a = web.driver.find_element(By.XPATH, "//*[text()='Hmm...this page doesn’t exist. Try searching for something else.']")
                web.df = web.df.append({web.ac[web.account_count]: '!!!!!!!!!!!!! \n This page doesn’t exist \n !!!!!!!!!!!!!'}, ignore_index = True)
                print(web.seperator*web.layer*4, '!!!!!!!!!!!!! \n This account doesn’t exist \n !!!!!!!!!!!!!')
                web.page_status = None
            except:
                web.page_status = 'exist'
    def blocker():
        web.if_desired_page_loaded('blocker')
        if web.page_status == 'exist':
            web.website_check_if_done('block')
            print('web.block_status: ', web.block_status)
            if web.block_status == 0:
                web.website_click("//*[@data-testid='userActions']")
                web.website_click("//*[@data-testid='block']")
                web.website_click("//*[@data-testid='confirmationSheetConfirm']")
                web.df = web.df.append({web.ac[web.account_count]: 'blocked'}, ignore_index = True)
            else:
                web.df = web.df.append({web.ac[web.account_count]: 'has been blocked'}, ignore_index = True)
        else:
            pass
    def open_in_new_tab(xpath):
        web.target_account = ''
        while True:
            # print('c1')
            try:
                web.target_account = web.driver.find_element(By.XPATH, xpath).get_attribute('href')
                if web.target_account is not None:
                    break
            except:
                pass
        web.main_window = web.driver.current_window_handle
        web.driver.execute_script("window.open('');")
        # web.driver.switch_to.new_window('window')
        web.driver.switch_to.window(web.driver.window_handles[web.current_tab+1])
        web.driver.get(web.target_account)
        basepath = web.driver.find_element(By.XPATH,".//div[starts-with (@aria-label,'Timeline')]/div")
        break_count = 0
        date_count = 0
        pass_count = 0
        pass_count_times = 15
        time.sleep(3)
        while True:
            break_count+=1
            print(break_count)
            try:
                a = basepath.find_element(By.XPATH,f"//div[{break_count}]/div/div/article[@data-testid='tweet']//*[@dir='ltr']/span[@class='css-901oao css-16my406 r-poiln3 r-bcqeeo r-qvutc0']").text
                if a[1:] != web.target_account[20:]:
                    print('not relevant')
                    pass
                else:
                    #time
                    date = basepath.find_element(By.XPATH, f"//div[{break_count}]/div/div/article[@data-testid='tweet']//a[@id]/time").text
                    try:
                        date = parser.parse(date)
                        date = str(date)[2:10]
                        print(date)
                        format_data = "%y-%m-%d"
                        date = datetime.datetime.strptime(date, format_data)
                        # print(f'{date.month}-{date.day}')
                    except:
                        pass
                    #text
                    parts = basepath.find_elements(By.XPATH,f"//div[{break_count}]/div/div/article[@data-testid='tweet']//*[@class='css-1dbjc4n']/div[@dir='auto']")
                    whole_part = ''
                    for part in parts:
                        try:
                            whole_part += part.text
                        except:
                            pass
                    whole_part = whole_part.replace('\n', ' ')
                    print(whole_part)
                    print('.')

                    #href
                    href = basepath.find_element(By.XPATH, f"//div[{break_count}]/div/div/article[@data-testid='tweet']//a[@id]").get_attribute('href')
                    print(href)

                    pass_count_times_once = 'n'
                    pass_count = 0
            except:
                pass_count+=1
            try:
                if (pass_count_times_once == 'y') and (pass_count>=pass_count_times):
                    print('pass_count_times_twice already')
                    break
            except:
                pass
            try:
                print ('pass_count:' ,pass_count, 'pass_count_times_once:', pass_count_times_once)
            except:
                pass
            if pass_count>=pass_count_times:
                # html = web.driver.find_element_by_tag_name('html')
                # html.send_keys(Keys.END)
                web.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                pass_count = 0
                break_count-=pass_count_times-1
                pass_count_times_once = 'y'
                time.sleep(5)
                html = web.driver.find_element_by_tag_name('html')


            # print('date_count: ', date_count)
            print('*'*40)

            target_date = datetime.datetime.strptime("22-01-15", format_data)
            if target_date > date:
                date_count +=1
            if date_count > 10:
                print(f'reached {target_date}')
                break
    def related_extract():
        pass
    def until_found(xpath):
        while True:
            try:
                bbb = web.driver.find_element(By.XPATH, xpath)
                if bbb is not None:
                    break
            except:
                pass
    def check_noti():
        web.waitnclick('//a[@aria-label="Notifications"]')
        web.waitnclick('//*[text()="Mentions"]/../..')
        print(f'checking  {web.ac[web.account_count]}')
        while True:
            if keyboard.is_pressed('1'):
                break
            else:
                pass
# web.extract_links()
    def twitter_automator(action, accountloop1=False, accountloop2=False):
        if accountloop1=='test':
            accountloop1 = random.choice(range(0,len(web.ac)))
            web.ac = web.ac_original[accountloop1-1:accountloop1+3]
            web.pw = web.pw_original[accountloop1-1:accountloop1+3]
        else:
            web.ac = web.ac_original[accountloop1-1:accountloop2-1]
            web.pw = web.pw_original[accountloop1-1:accountloop2-1]
        current_ac_number = accountloop1
        options = Options()
        options.add_argument("start-maximized")
        web.driver = webdriver.Chrome(executable_path='C:/Users/kamka/Documents/chromedriver.exe', options=options) #home
        web.driver.get("https://twitter.com/login")
        for account in range(len(web.ac)):
            web.df = pd.DataFrame()
            web.layer = 1
            web.df[web.ac[web.account_count]] = " "
            web.df = web.df.append({web.ac[web.account_count]: web.ac_original.index(web.ac[web.account_count])+1}, ignore_index = True)
            print('* '*60, f'\nlogining in: [{current_ac_number}] {web.ac[web.account_count]}\n','* '*60 )
            #enter username
            web.website_type(web.ac[web.account_count], '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[5]/label', wait = 0, comment ='ac typed')
            #fill password & log in
            web.website_type(web.pw[web.account_count], '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input', wait = 0, comment ='pw typed')
            print(web.pw[web.account_count])
            # #open new tab for action
            web.wait()
             # check if the home page has loaded
            while True:
                try:
                    bbb = web.driver.find_element(By.XPATH, './/div[@data-testid="retweet"]')
                    if bbb is not None:
                        break
                except:
                    pass
                try:
                    bbb = web.driver.find_element(By.XPATH, '//span[text()="Turn on personalized ads"]/..')
                    if bbb is not None:
                        break
                except:
                    pass
            time.sleep(2)
            web.layer = 2
            if action == 'check_mentions':
                web.check_noti()
            else:
                for i in range(len(what)):
                    web.layer = 3
                    web.df = web.df.append({web.ac[web.account_count]: what[i]}, ignore_index = True)
                    if account == 0:
                        web.driver.execute_script("window.open('');")
                        web.driver.switch_to.window(web.driver.window_handles[i+1])
                        web.driver.get(what[i])
                        web.current_tab = i+1
                    else:
                        web.driver.switch_to.window(web.driver.window_handles[i+1])
                    print(web.seperator*web.layer*4, [i+1], 'automating:', what[i][:30])
                    #main function performed here
                    web.layer = 4 
                    # web.more_than_3("//a[starts-with (text(),'@')]", 'no commment')
                    if action == 'like':
                        web.liker()
                    elif action =='block':
                        web.blocker()
            if accountloop1:
                web.layer = 1
                web.driver.switch_to.window(web.driver.window_handles[0])
                #logout from the home page
                web.website_click('//*[@data-testid="SideNav_AccountSwitcher_Button"]', comment = 'SideNav_AccountSwitcher_Button clicked')
                web.website_click("//*[@class='css-4rbku5 css-18t94o4 css-1dbjc4n r-1loqt21 r-18u37iz r-1ny4l3l r-ymttw5 r-1yzf0co r-o7ynqc r-6416eg r-13qz1uu'][@data-testid='AccountSwitcher_Logout_Button']", comment = 'AccountSwitcher_Logout_Button')
                web.website_click("//*[@class='css-901oao css-16my406 r-poiln3 r-bcqeeo r-qvutc0'][text()='Log out']", comment = 'Logout_Button clicked')
                web.df_final.to_excel("automator_log.xlsx")
                #check situation
                while True:
                    try:
                        web.driver.find_element(By.XPATH, '//*[@data-testid="loginButton"]').click()
                        comment = '(sit1) loginButton clicked'
                        web.df = web.df.append({web.ac[web.account_count]: comment}, ignore_index = True)
                        print (comment)
                        break
                    except:
                        pass
                    # try:
                    #     web.driver.find_element(By.XPATH, '//*[text()="Log in"]/../../..').click()
                    #     comment = '(sit2) loginButton clicked'
                    #     web.df = web.df.append({web.ac[web.account_count]: comment}, ignore_index = True)
                    #     print (comment)
                    #     break
                    # except:
                    #     pass
                    try:
                        web.driver.find_element(By.XPATH, '//*[text()="Log in"]/../../..').click()
                        attempt = 0
                        while True:
                            attempt+=1
                            try:
                                web.driver.find_element(By.XPATH, '//*[text()="Use phone, email or username"]/../../..').click()
                                comment = '(sit3) 2 Buttons clicked'
                                web.df = web.df.append({web.ac[web.account_count]: comment}, ignore_index = True)
                                print (comment)
                                break
                            except:
                                pass
                            try:
                                web.driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[5]/label')
                                comment = '(sit4) login page has loaded'
                                web.df = web.df.append({web.ac[web.account_count]: comment}, ignore_index = True)
                                print (comment)
                                break
                            except:
                                pass
                            if attempt>50:
                                web.df = web.df.append({web.ac[web.account_count]: 'attempt>50'}, ignore_index = True)
                                print('break becoz attempt>50')
                                break
                    except:
                        pass
                    try:
                        web.driver.find_element(By.XPATH, '//*[text()="Sign in"]/..').click()
                        while True:
                            try:
                                # print('gonna fail')
                                web.driver.find_element(By.XPATH, '//*[text()="Use phone, email or username"]/..').click()
                                comment = '(sit5) Already have an account? Sign in'
                                web.df = web.df.append({web.ac[web.account_count]: comment}, ignore_index = True)
                                print(comment)
                                break
                            except:
                                pass
                            try:
                                web.driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[5]/label') #
                                comment = '(sit5.1) login page has loaded'
                                web.df = web.df.append({web.ac[web.account_count]: comment}, ignore_index = True)
                                print (comment)
                                break
                            except:
                                pass
                        break
                    except:
                        pass
                    try:
                        web.driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[5]/label')
                        comment = '(sit6) login page has loaded'
                        web.df = web.df.append({web.ac[web.account_count]: comment}, ignore_index = True)
                        print (comment)
                        break
                    except:
                        pass
                print(f'[{current_ac_number}] {web.ac[web.account_count]} is done')
                web.df_final = pd.concat([web.df_final, web.df], axis=1)
                print(web.df_final)
            web.account_count += 1
            current_ac_number +=1
        web.df_final.to_excel("automator_log.xlsx")
        # os.system('automator_log.xlsx')
    def record_checker(action):
        df = pd.read_excel(r'C:/Users/kamka\Documents/333/tb_processed.xlsx')
        account = random.choice(range(0,len(web.ac_original)))
        #login
        web.driver.get("https://twitter.com/login")
        print('* '*60, f'\nlogining in: [{account+1}] {web.ac[account]}\n','* '*60 )
        #enter username
        web.website_type(web.ac_original[web.account_count], '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[5]/label', wait = 0, comment ='ac typed')
        #fill password & log in
        web.website_type(web.pw_original[web.account_count], '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input', wait = 0, comment ='pw typed')
        # #open new tab for action
        web.wait()
        while True:
            try:
                bbb = web.driver.find_element(By.XPATH, './/div[@data-testid="retweet"]')
                if bbb is not None:
                    break
            except:
                pass
            try:
                bbb = web.driver.find_element(By.XPATH, '//span[text()="Turn on personalized ads"]/..')
                if bbb is not None:
                    break
            except:
                pass
        print('first page has loaded')
        time.sleep(1)
        table_index = 0
        if action == 'check_links_and_related_ac':
            for link in df['link']:
                web.driver.execute_script("window.open('');")
                web.driver.switch_to.window(web.driver.window_handles[table_index+1])
                web.driver.get(link)
                # retrive from the tweet
                web.current_link_stripped = link.replace(re.findall(r".+.com\/", link)[0], '').replace(re.findall(r"\/status.+", link)[0], '')
                web.tag_list = []
                web.until_found("//*[@class='css-901oao r-1nao33i r-37j5jr r-1blvdjr r-16dba41 r-vrz42v r-bcqeeo r-bnwqim r-qvutc0']")
                time.sleep(0.5)
                for bbb in web.driver.find_elements(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/section/div/div/div[1]/div/div[1]/article/div/div/div/div[3]/div[1]/div/div/div/span/a'):
                    a = str(bbb.get_attribute('href'))
                    if web.current_link_stripped not in a:
                        print(a)
                        web.tag_list.append(a)
                x = df.columns.get_loc('-related-')
                if web.tag_list == []:
                    df.iloc[table_index,x] = '/'
                else:
                    web.tag_list.insert(0,'related:')
                    web.tag_list.append('.')
                    # print(web.tag_list)
                    #iterate the retracted list(related)
                    for each_webtag_list in web.tag_list:
                        # print(table_index)
                        df.iloc[table_index,x] = each_webtag_list
                        # print(df.iloc[table_index,x])
                        # print(df.iloc[table_index,0])
                        x+=1
                table_index+=1
                print('*  ' * 30)
            username = df["link"].apply(lambda a: a.replace(re.findall(r".+.com\/", a)[0], '').replace(re.findall(r"\/status.+", a)[0], ''))
            # print(df["Month"])
            df["Month"] = df["Month"].apply(lambda x: str(x)[5:7])
            df["Group"] = df["Group"].astype(str)
            df["Note"] = '.'
            # print(df["Group"])
            df['check links'] = "https://twitter.com/search?q=(from%3A"+ username + f")%20since%3A2022-" + df["Month"].astype(str) + '-' + df["Date"].astype(str) + '&src=typed_query&f=live'
        elif action == 'check_result':
            for link in df['link']:
                web.driver.execute_script("window.open('');")
                web.driver.switch_to.window(web.driver.window_handles[table_index+1])
                web.driver.get(link)
                #if the page (tweet) is load
                while True:
                    try:
                        a = web.driver.find_element(By.XPATH, "//*[@class='css-901oao r-1nao33i r-37j5jr r-1blvdjr r-16dba41 r-vrz42v r-bcqeeo r-bnwqim r-qvutc0']")
                        if a is not None:
                            this_tweet = 'valid'
                            break
                    except:
                        pass
                    try:
                        b = web.driver.find_element(By.XPATH, "//*[text()='Hmm...this page doesn’t exist. Try searching for something else.']")
                        if a is not None:
                            x = df.index.get_loc(link)
                            df[table_index, 'Done'] = 'Fake'
                            this_tweet = 'invalid'
                            break
                    except:
                        pass
                table_index +=1
            table_index = 0
            for link in df['check links']:
                if this_tweet == 'valid':
                    web.driver.execute_script("window.open('');")
                    web.driver.switch_to.window(web.driver.window_handles[table_index+1])
                    web.driver.get(link)
                    SCROLL_PAUSE_TIME = 0.5
                    # Get scroll height
                    last_height = web.driver.execute_script("return document.body.scrollHeight")

                    while True:
                        # Scroll down to bottom
                        web.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

                        # Wait to load page
                        time.sleep(SCROLL_PAUSE_TIME)

                        # Calculate new scroll height and compare with last scroll height
                        new_height = web.driver.execute_script("return document.body.scrollHeight")
                        if new_height == last_height:
                            break
                        last_height = new_height
                else:
                    pass
        df.to_excel("record_checker_processed.xlsx")

for each in range(len(boss)):
    what = boss[each]
    web.twitter_automator('like', 1,21)
    web.df_final.to_excel(f"{each}_automator_log.xlsx")
    for handle in web.driver.window_handles:
        web.driver.switch_to.window(handle)
        web.driver.close()
web.driver = webdriver.Chrome(executable_path='C:/Users/kamka/Documents/chromedriver.exe') #home

# web.twitter_automator('check_mentions', 1,22)
# web.twitter_automator('like', 15,21)
# web.twitter_automator('block',1,22)

# web.record_checker('check_links_and_related_ac')
# web.record_checker('check_result')