from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
import time
import random
# import pyautogui
import keyboard
import pyperclip
import pandas as pd
import os   
# chrome_options = webdriver.ChromeOptions()
# chrome_optionschrome_options.add_arguments('--incognito')
# # create instance of Chrome webdriver
# driver = webdriver.Chrome(chrome_options=chrome_options, executable_path='C:/Users/kamka/Documents/chromedriver.exe')
#   
# 18/04 first batch = ['https://twitter.com/EMUHLEET/status/1515097921842147332', 'https://twitter.com/BeardedHitbox/status/1513929344330129412', 'https://twitter.com/LDNUTD/status/1514619300367126534', 'https://twitter.com/diegotetv/status/1514423641005457408', 'https://twitter.com/luxxz_tv/status/1515124694273331202', 'https://twitter.com/itsrzca/status/1514992833043836930']

class web():
    ac = ['KameronW_Stone','jacoBstro4','SivZon','antoniochorr','harperjames31','Andrew_Grime574','S_K32T','Greenhattt','ernestTTy','JesseliamxX','Mick_J0n','sambjmf','MillerNileOrz','Aeveweis','Martin07215','xav1errr','Stephzip','RainingTrainn','issacbrook19','BonoLanda']
    pw = '12idontknow3'
    options = Options()
    options.add_argument("start-maximized")
    options.add_argument("--incognito")
    driver = webdriver.Chrome(executable_path='C:/Users/John/Downloads/chromedriver.exe', options=options)
    account_count = 0
    current_tab = 0
    seperator = '-  -  '
    layer = 0
    post_status = 'default'
    relogin_status = 'n'
    block_status = 66
    df = pd.DataFrame()
    df_final = pd.DataFrame()
    done_comment = ['(DONE)liked','(DONE)retweeted','(DONE)retweetConfirmed','(DONE)reply','(DONE)reply sent','(DONE)followed']
    what = [
        'https://twitter.com/ValrntGiveaways',
        'https://twitter.com/LeBornJames21  ',
        'https://twitter.com/TheBoyzTwit    ',
        'https://twitter.com/_Lvlupgaming_',
        'https://twitter.com/WaffleVAL_',
        'https://twitter.com/escapistfool',
        'https://twitter.com/VALORANT_L',
        'https://twitter.com/JettGiveaways',
        'https://twitter.com/legitvalgvwys',
        'https://twitter.com/Aike6lgfxV',
        'https://twitter.com/GamesPAP',
        'https://twitter.com/Zeloily',
        'https://twitter.com/LlKEWlSE',
        'https://twitter.com/Iust2love',
        'https://twitter.com/zaithlol',
        'https://twitter.com/EliteRivals',
        'https://twitter.com/FollowChinoxian',
        'https://twitter.com/firefoxvfx',
        'https://twitter.com/Valorant569',
        'https://twitter.com/MastaAU',
    ]
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

        numberofaccount = ''
        # if t.tag3 == 'y':
        #     pick = random.randint(1, 3)
        #     if pick == 1:
        #         numberofaccount = f'{ac2} {ac1} {ac3}'
        #     elif pick == 2:
        #         numberofaccount = f'{ac3} {ac2} {ac1}'
        #     elif pick == 3:
        #         numberofaccount = f'{ac1} {ac2} {ac3}'
        # else:
        #     pickkk = random.randint(4, 5)
        #     if pickkk == 4:
        #         numberofaccount = f'{ac2} {ac1}'
        #     elif pickkk == 5:
        #         numberofaccount = f'{ac1} {ac2}'
        # if len(t.comment) == 0:
        #     new = random.choice(reply_eg)
        # else:
        #     new = t.comment

        # tag = random.randint(1, 2)
        # if tag == 2:
        #     the_reply_eg = f'{new} {numberofaccount}'
        # else:
        #     the_reply_eg = f'{numberofaccount} {new}'
        # return the_reply_eg
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
        return()
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
                if comment:
                    pass
                else:
                    comment = 'done'
                print(web.seperator*web.layer*4, comment)
                web.df = web.df.append({web.ac[web.account_count]: comment}, ignore_index = True)
                a.send_keys(Keys.RETURN)
                break
            except:
                pass
    def website_click_by_class(path, comment=False):
        while True:
            try:
                a = WebDriverWait(web.driver, 10).until(
                    EC.presence_of_element_located((By.CLASS_NAME, path))
                )
                web.wait()
                a.click()
                if comment:
                    pass
                else:
                    comment = 'done'
                print(web.seperator*web.layer*4, comment)
                web.df = web.df.append({web.ac[web.account_count]: comment}, ignore_index = True)
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
                if comment:
                    pass
                else:
                    comment = 'done'
                print(web.seperator*web.layer*4, comment)
                web.df = web.df.append({web.ac[web.account_count]: comment}, ignore_index = True)
                break
            except:
                pass
    def website_try_click(xpath, target=False,  wait=False, comment=False, relogin=False, hardness=False):
        if (hardness == 0) or (hardness is None):
            try:
                a = web.driver.find_elements(By.XPATH, xpath)
                if target > 1:
                    for i in range(len(a)):
                        a[i].click()
                else:
                    a[i].click()
                if comment:
                    pass
                else:
                    comment = 'done'
                print(web.seperator*web.layer*4, comment)
                web.df = web.df.append({web.ac[web.account_count]: comment}, ignore_index = True)
                if wait == 0:
                    pass
                else:
                    web.wait()
            except:
                if relogin:
                    try:
                        a = web.driver.find_elements(By.XPATH, "//*[@class='css-901oao css-16my406 r-poiln3 r-bcqeeo r-qvutc0'][text()='Log out']")
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
                if comment:
                    pass
                else:
                    comment = 'done'
                print(web.seperator*web.layer*4, comment)
                web.df = web.df.append({web.ac[web.account_count]: comment}, ignore_index = True)
            except:
                pass
    def wait_until(xpath, comment=False):
        while True:
            try:
                a = WebDriverWait(web.driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, xpath))
                )
                a.click()
                if comment:
                    pass
                else:
                    comment = 'done'
                web.df = web.df.append({web.ac[web.account_count]: comment}, ignore_index = True)
                print(web.seperator*web.layer*4, comment)
                break
            except:
                web.website_try_click("//*[@class='css-901oao css-16my406 r-poiln3 r-bcqeeo r-qvutc0'][text()='Keep less relevant ads']", 1, 'bug cleared (keep less relevant ads)')
    def website_check_if_done(type):
        if type == 'tweet':
            try:
                a = web.driver.find_elements(By.XPATH, './/div[@aria-label="Liked"]')
                web.post_status = 'done'
            except:
                pass
            try:
                a = web.driver.find_elements(By.XPATH, './/div[@aria-label="Like"]')
                web.post_status = 'not done'
            except:
                pass
        elif type == 'relogin':
            try:
                web.driver.find_elements(By.XPATH, '//*[@data-testid="loginButton"]').click()
                comment = '(situation1) loginButton clicked'
                web.df = web.df.append({web.ac[web.account_count]: comment}, ignore_index = True)
                print (comment)
            except:
                pass
            try:
                a = web.driver.find_elements(By.XPATH, '//a[@data-testid="login"][@href="/login"]').click()
                comment = '(situation2) login clicked'
                web.df = web.df.append({web.ac[web.account_count]: comment}, ignore_index = True)
                print (comment)
            except:
                pass
        elif type == 'block':
            while True:
                try:
                    a = web.driver.find_elements(By.XPATH, '//div[starts-with (@aria-label,"Follow @")][@class="css-18t94o4 css-1dbjc4n r-42olwf r-sdzlij r-1phboty r-rs99b7 r-2yi16 r-1qi8awa r-1ny4l3l r-ymttw5 r-o7ynqc r-6416eg r-lrvibr"]')
                    web.block_status = 0
                    break
                except:
                    pass
                try:
                    a = web.driver.find_elements(By.XPATH, '//div[starts-with (@aria-label,"Following @")][@class="css-18t94o4 css-1dbjc4n r-42olwf r-sdzlij r-1phboty r-rs99b7 r-2yi16 r-1qi8awa r-1ny4l3l r-ymttw5 r-o7ynqc r-6416eg r-lrvibr"]')
                    web.block_status = 0
                    break
                except:
                    pass
                try:
                    a = web.driver.find_elements(By.XPATH, "//div[contains(@data-testid,'unblock')]")
                    web.block_status = 1
                    break
                except:
                    pass


    def more_than_3(xpath, comment):
        a = web.driver.find_elements(By.XPATH, xpath)
        links = [elem.get_attribute('href') for elem in a]
        print(links)
        web.driver.execute_script("window.open()")
        web.driver.switch_to.window(web.driver.window_handles[web.current_tab+1])
        for i in links:
            web.driver.get(i)
            web.website_click('//*[@class="css-1dbjc4n"][@data-testid="placementTracking"]')
            time.sleep(1)
        web.driver.close()
    def liker():
        web.website_check_if_done('tweet')
        if web.post_status == 'not done':
            web.website_click('.//div[@data-testid="like"]', wait = 0, comment = '(1)liked')
            web.website_click('.//div[@data-testid="retweet"]', '(2)retweeted')
            web.website_click('.//div[@data-testid="retweetConfirm"]', '(3)retweetConfirmed')
            web.website_type(web.twitter_account(1), './/div[@data-testid="tweetTextarea_0"]', '(4)reply')
            web.website_click("//*[@class='css-901oao css-16my406 r-poiln3 r-bcqeeo r-qvutc0'][text()='Reply']", '(5)reply sent')
            web.website_try_click("//*[@class='css-901oao css-16my406 r-poiln3 r-bcqeeo r-qvutc0'][text()='Follow']", 2, comment = '(6)followed')                
        else:
            for iii in range(len(web.done_comment)):
                web.df = web.df.append({web.ac[web.account_count]: web.done_comment[iii]}, ignore_index = True)
            # for i in automationTools:
            #     i.click()
    def blocker():
        web.website_check_if_done('block')
        print(web.block_status)
        if web.block_status == 0:
            web.website_click("//*[@data-testid='userActions']")
            web.website_click("//*[@data-testid='block']")
            web.website_click("//*[@data-testid='confirmationSheetConfirm']")
            web.df = web.df.append({web.ac[web.account_count]: 'blocked'}, ignore_index = True)
        else:
            web.df = web.df.append({web.ac[web.account_count]: 'has been blocked'}, ignore_index = True)
# web.extract_links()
    def twitter_automator(action, accountloop1, accountloop2):
        current_ac_number = accountloop1
        web.ac = web.ac[accountloop1-1:accountloop2-1]
        for account in range(len(web.ac)):
            web.df = pd.DataFrame()
            web.layer = 1
            web.df[web.ac[web.account_count]] = " "
            web.driver.get("https://twitter.com/login")
            print('* '*60, f'\nlogining in: [{current_ac_number}] {web.ac[web.account_count]}\n','* '*60 )
            #enter username
            web.website_type(web.ac[web.account_count], '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[5]/label', wait = 0, comment ='ac typed')
            #fill password & log in
            web.website_type(web.pw, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input', wait = 0, comment ='pw typed')
            # #open new tab for action
            web.wait()
            web.wait_until('.//div[@data-testid="retweet"]', 'home page is loaded')
            web.layer = 2
            if account > 0:
                for i in range(len(web.what)):
                    print(web.seperator*web.layer*4, "tabs reloading....")
                    time.sleep(0.25)
                    web.driver.switch_to.window(web.driver.window_handles[i+1])
                    print(web.seperator*web.layer*4, "tabs reloaded....")
            for i in range(len(web.what)):
                web.layer = 3
                web.df = web.df.append({web.ac[web.account_count]: web.what[i]}, ignore_index = True)
                if account == 0:
                    web.driver.execute_script("window.open('');")
                    # web.driver.switch_to.window(web.driver.window_handles[i+1])
                    # web.driver.get(web.what[i])
                    # web.current_tab = i+1
                    print('shd be ok wor')
                else:
                    web.driver.switch_to.window(web.driver.window_handles[i+1])
                print(web.seperator*web.layer*4, [i+1], 'automating:', web.what[i][:30])
                web.wait()
                #main function performed here
                web.layer = 4
                web.more_than_3("//a[starts-with (text(),'@')]", 'no commment')
                # if action == 'like':
                #     web.liker()
                # elif action =='block':
                #     web.blocker()
            if accountloop1:
                web.layer = 1
                web.driver.switch_to.window(web.driver.window_handles[0])
                #logout from the home page
                web.website_click('//*[@data-testid="SideNav_AccountSwitcher_Button"]', comment = 'SideNav_AccountSwitcher_Button clicked')
                web.website_click("//*[@class='css-4rbku5 css-18t94o4 css-1dbjc4n r-1loqt21 r-18u37iz r-1ny4l3l r-ymttw5 r-1yzf0co r-o7ynqc r-6416eg r-13qz1uu'][@data-testid='AccountSwitcher_Logout_Button']", comment = 'AccountSwitcher_Logout_Button')
                web.website_click("//*[@class='css-901oao css-16my406 r-poiln3 r-bcqeeo r-qvutc0'][text()='Log out']", comment = 'Logout_Button clicked')

                #check situation
                web.website_check_if_done('relogin')
                try:
                    web.website_try_click("//*[@class='css-901oao css-16my406 r-poiln3 r-bcqeeo r-qvutc0'][text()='Sign up with phone or email']", 1, comment = '(situation3) 2 sign in clicked', relogin = 'yes')
                    web.website_try_click("//*[@class='css-901oao css-16my406 r-poiln3 r-bcqeeo r-qvutc0'][text()='Log in']", 1, comment = '(situation3) 3 sign in clicked', relogin = 'yes')
                except:
                    pass
                try:
                    #situation2
                    web.website_try_click('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/div[1]/div/div[3]/div[5]/a/div/span/span', 1, comment = '(situation2) logouted (clicked to login_page)', hardness=1)
                    web.website_try_click('//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[2]/div[2]/div[2]', 1, comment = '(situation2) logouted (unexpected)', hardness=1)
                except:
                    pass
                try:
                    #situation3
                    web.website_try_click("//*[@class='css-4rbku5 css-18t94o4 css-1dbjc4n r-1niwhzg r-1ets6dv r-sdzlij r-1phboty r-rs99b7 r-1loqt21 r-peo1c r-1ps3wis r-1ny4l3l r-1guathk r-o7ynqc r-6416eg r-lrvibr'][@data-testid='login']", 1, comment = '(situation3) login', hardness=1)
                except:
                    pass
                
                print(f'[{current_ac_number}] {web.ac[web.account_count]} is done')
                web.df_final = pd.concat([web.df_final, web.df], axis=1)
                print(web.df_final)
            web.account_count += 1
            current_ac_number +=1
        web.df_final.to_excel("output.xlsx")
        os.system('output.xlsx')
web.twitter_automator('block', 1,21)
# web.twitter_automator('like', 20,21)




# {0: '@KameronW_Stone', 1: '@Andrew_Grime574', 2:'@Mick_j0n',
# 3: '@jacoBstro4', 4: '@S_K32T', 5: '@sambjmf',
# 6: '@SivZon', 7: '@Greenhattt', 8: '@MillerNileOrz', 
# 9: '@antoniochorr', 10: '@ernestTTy', 11: '@Aeveweis',
# 12: '@harperjames31', 13: '@JesseliamxX', 14: '@Martin07215',
# 15: '@xav1errr', 16: '@Stephzip', 17: '@RainingTrainn',
# 18: '@issacbrook19', 19: '@BonoLanda'}
# [0:4][5:9][10:14][15:19]
'''
main_url = 'https://www.linkedin.com' # URL A
tab_url = 'https://www.google.com' # URL B
chromedriver = 'DESCTINATION_TO_YOUR_CHROME_DRIVER'# Open main window with URL A
browser= webdriver.Chrome(executable_path='C:/Users/kamka/Documents/chromedriver.exe', options=options)
browser.get(main_url)
print("Current Page Title is : %s" %browser.title)# Open a new window
browser.execute_script("window.open('');")# Switch to the new window and open URL B
browser.switch_to.window(browser.window_handles[1])
browser.get(tab_url)# …Do something here
# browser.switch_to.window(browser.window_handles[2])
# browser.switch_to.window(browser.window_handles[1])
time.sleep(10)
print("Current Page Title is : %s" %browser.title)# Close the tab with URL B
browser.close()# Switch back to the first tab with URL A
browser.switch_to.window(browser.window_handles[0])
print("Current Page Title is : %s" %browser.title)
'''