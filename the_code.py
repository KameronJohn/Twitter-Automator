from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con
import webbrowser
import os
import pyperclip

def pause():
    try:
        if keyboard.is_pressed('1'):
            print('paused')
            while True:
                try:
                    if keyboard.is_pressed('del'):
                        print('resumed')
                        break
                except:
                    time.sleep(0.1)
        else:
            pass
    except:
        pass
def chrome_open():
    pyautogui.press('win')
    time.sleep(0.2)
    pyautogui.write('chrome')
    time.sleep(0.2)
    pyautogui.press('enter')
    time.sleep(0.2)
    pyautogui.hotkey('win', 'up', delay=0.25)       
    time.sleep(0.4)
def edge_open():
    pyautogui.press('win')
    time.sleep(0.2)
    pyautogui.write('edge')
    time.sleep(0.2)
    pyautogui.press('enter')
    time.sleep(0.2)
    pyautogui.hotkey('win', 'up', delay=0.25)   
    time.sleep(0.4)  
def brave_open():
    pyautogui.press('win')
    time.sleep(0.2)
    pyautogui.write('brave')
    time.sleep(0.2)
    pyautogui.press('enter')
    time.sleep(0.2)
    pyautogui.hotkey('win', 'up', delay=0.25)
    time.sleep(0.4)
def opera_open():
    pyautogui.press('win')
    time.sleep(0.2)
    pyautogui.write('avast Secure Browser')
    time.sleep(0.2)
    pyautogui.press('enter')
    time.sleep(0.2)
    pyautogui.hotkey('win', 'up', delay=0.25)
    time.sleep(1)
def click():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(0.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)


def twitter_automator(twitter_account_number=False, theme=False, auto=False, looptimes=False, reply_only=False, accountloop=False, printreply_eg=False, tag3=False, except_reply=False):    
    CONFIDENCE = 0.7
    LIGHT_CONFIDENCE = 0.75

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
            f"Lets go boys This giveaway is fire, good luck to all of you",
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
            f"That will help me alot thx!",
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
        if tag3 == 'yes':
            pick = random.randint(1, 3)
            if pick == 1:
                numberofaccount = f'{ac2} {ac1} {ac3}'
            elif pick == 2:
                numberofaccount = f'{ac3} {ac2} {ac1}'
            elif pick == 3:
                numberofaccount = f'{ac1} {ac2} {ac3}'
        else:
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


        # the_reply_eg = f'{numberofaccount} Done'
        # return the_reply_eg

    if theme == 'l':
        twitter_home = 'twitter_home.png'
        follow_button = 'light_Follow.png'
        four_buttons = 'light_4_buttons.png'
        reply_pop_up = 'light_reply_pop_up.png'
        liked_retweeted = 'liked_retweeted.png'
        unfollow = "unfollow.png"
        retweet_quoate_tweet = "retweet_quoate_tweet.png"
        twitter_comment_box = "twitter_comment_box.png"

        account1 = 'ac1.png'
        account2 = 'ac2.png'
        account3 = 'ac3.png'
        account4 = 'ac4.png'
        account5 = 'ac5.png'
        account6 = 'ac6.png'
        account7 = 'ac7.png'
        account8 = 'ac8.png'
        account9 = 'ac9.png'
        account10 = 'ac10.png'
        account11 = 'ac11.png'
        account12 = 'ac12.png'
        account13 = 'ac13.png'
        account14 = 'ac14.png'
        account15 = 'ac15.png'


    elif theme =='d':
        twitter_home = 'dtwitter_home.png'
        follow_button = 'Follow.png'
        four_buttons = 'dark_4_buttons.png'
        reply_pop_up = 'dark_reply_pop_up.png'
        liked_retweeted = 'dliked_retweeted.png'
        unfollow = "dunfollow.png"
        retweet_quoate_tweet = "d_retweet_quoate_tweet.png"
        twitter_comment_box = "d_twitter_comment_box.png"

        account1 = 'dac1.png'
        account2 = 'dac2.png'
        account3 = 'dac3.png'
        account4 = 'dac4.png'
        account5 = 'dac5.png'
        account6 = 'dac6.png'
        account7 = 'dac7.png'
        account8 = 'dac8.png'
        account9 = 'dac9.png'
        account10 = 'dac10.png'
        account11 = 'dac11.png'
        account12 = 'dac12.png'
        account13 = 'dac13.png'
        account14 = 'dac14.png'
        account15 = 'dac15.png'

    def twitter_bot():
        if theme == 'l':
            twitter_home = 'twitter_home.png'
            follow_button = 'light_Follow.png'
            four_buttons = 'light_4_buttons.png'
            reply_pop_up = 'light_reply_pop_up.png'
            liked_retweeted = 'liked_retweeted.png'
            unfollow = "unfollow.png"
            retweet_quoate_tweet = "retweet_quoate_tweet.png"
            twitter_comment_box = "twitter_comment_box.png"

        elif theme =='d':
            twitter_home = 'dtwitter_home.png'
            follow_button = 'Follow.png'
            four_buttons = 'dark_4_buttons.png'
            reply_pop_up = 'dark_reply_pop_up.png'
            liked_retweeted = 'dliked_retweeted.png'
            unfollow = "dunfollow.png"
            retweet_quoate_tweet = "d_retweet_quoate_tweet.png"
            twitter_comment_box = "d_twitter_comment_box.png"

        try:
            start22 = pyautogui.locateCenterOnScreen(follow_button, region = (0,0,2500,1450), grayscale=True, confidence=0.85)
            try:
                x, y = pyautogui.locateCenterOnScreen(follow_button,  region=(1400,100,600,900), confidence=0.85)
            except:
                pass
            while start22 is not None:
                pyautogui.moveTo(start22)  # Moves the mouse to the coordinates of the image
                click()
                time.sleep(0.1)
                pyautogui.moveTo(x+230, y+130)
                time.sleep(0.15)
                start22 = pyautogui.locateCenterOnScreen(follow_button, region = (0,0,2500,1450), grayscale=True, confidence=0.85)
            else:
                pass
        except:
            pass

        try:
            x, y = pyautogui.locateCenterOnScreen(unfollow, region = (0,0,2500,1450), grayscale=True, confidence=0.85)
            pyautogui.moveTo(x+230, y+130)  # Moves the mouse to the coordinates of the image
            click()
            time.sleep(0.15)
            print('"unfollow bug" cleared')
        except:
            pass

        pause()
        liked_retweeted_check = ''
        try:
            asfdfdf = pyautogui.locateCenterOnScreen(liked_retweeted, region = (0,0,2500,1450), grayscale=True, confidence=0.85)
            if asfdfdf is not None:
                liked_retweeted_check = 'yes'
        except:
            pass

        four_buttons_clear = ''
        if liked_retweeted_check == 'yes':
            print('has been done')
        else:
            for i in range(3):
                try:
                    x, y = pyautogui.locateCenterOnScreen(four_buttons, region = (0,0,2500,1200), confidence=0.7)
                    if (x, y) is not None:
                        pyautogui.moveTo(x+68, y) #like
                        click()
                        pyautogui.moveTo(x-75, y) #retweet
                        click()
                        while True:
                            try:
                                checkcheck = pyautogui.locateCenterOnScreen(retweet_quoate_tweet, region = (0,0,2500,1200), confidence=0.7)
                                if checkcheck is not None:
                                    pyautogui.moveTo(x-200, y) #retweet2
                                    click()
                                    break
                            except:
                                print('?????????')
                                time.sleep(0.1)
                        pause()
                        if except_reply:
                            pass
                        else:
                            click()
                            while True:
                                try:
                                    time.sleep(0.5)
                                    start3 = pyautogui.locateCenterOnScreen('got_it.png', region = (0,0,2500,1200), grayscale=True, confidence=LIGHT_CONFIDENCE)
                                    if start3 is not None:
                                        pyautogui.moveTo(start3)
                                        click()
                                        break
                                    else:
                                        break
                                except:
                                    print('halosdsd')
                            while True:
                                try:    
                                    checkcheckss = pyautogui.locateCenterOnScreen(twitter_comment_box, region = (0,0,2500,1200), confidence=LIGHT_CONFIDENCE)
                                    if checkcheckss is not None:     
                                        pyautogui.write(twitter_account(twitter_account_number))
                                        time.sleep(1)
                                        pyautogui.hotkey('ctrl', 'enter', delay=0.25)
                                        time.sleep(0.25)
                                        pyautogui.hotkey('ctrl', 'enter', delay=0.25)
                                        time.sleep(0.25)
                                        # print ('liked, retweet, replied')
                                        break
                                except:
                                    time.sleep(0.2)
                                    # click()
                                    print('clicked')
                        four_buttons_clear = 'done'
                        break
                except:
                    time.sleep(2)
            if four_buttons_clear == '':
                if twitter_account_number == 2 or twitter_account_number == 5 or twitter_account_number == 8 or twitter_account_number == 11 or twitter_account_number == 14:
                    # print ('scrolled')
                    pyautogui.moveTo(2224, 264)
                    click()
                    time.sleep(0.2)
                    click()
                    pyautogui.scroll(-500)
                    time.sleep(1)
                else:
                    # print ('scrolled')
                    pyautogui.moveTo(2224, 264)
                    click()
                    time.sleep(0.2)
                    click()
                    pyautogui.scroll(-1000)
                    time.sleep(1)
                try:
                    x, y = pyautogui.locateCenterOnScreen(four_buttons, region = (0,0,2500,1200), confidence=0.65)
                    if (x, y) is not None:
                        pyautogui.moveTo(x+68, y) #like
                        click()
                        pyautogui.moveTo(x-75, y) #retweet
                        click()
                        while True:
                            try:
                                checkcheck = pyautogui.locateCenterOnScreen(retweet_quoate_tweet, region = (0,0,2500,1200), confidence=LIGHT_CONFIDENCE)
                                if checkcheck is not None:
                                    pyautogui.moveTo(x-200, y) #retweet2
                                    click()
                                    break
                            except:
                                time.sleep(0.1)
                                print('check3')
                        if except_reply:
                            pass
                        else:
                            click()
                            while True:
                                try:    
                                    checkcheckss = pyautogui.locateCenterOnScreen(twitter_comment_box, region = (0,0,2500,1200), confidence=LIGHT_CONFIDENCE)
                                    if checkcheckss is not None:     
                                        pyautogui.write(twitter_account(twitter_account_number))
                                        time.sleep(1.25) 
                                        pyautogui.hotkey('ctrl', 'enter', delay=0.25)
                                        time.sleep(0.25)
                                        pyautogui.hotkey('ctrl', 'enter', delay=0.25)                

                                        # print ('liked, retweet, replied')
                                        break
                                except:
                                    time.sleep(0.2)
                                    click()
                                    print('check4')
                            # print ('check2')
                except:
                    pass
            else:
                pass


        try:
            start22 = pyautogui.locateCenterOnScreen(follow_button, region = (0,0,2500,1450), grayscale=True, confidence=0.8)
            try:
                x, y = pyautogui.locateCenterOnScreen(follow_button,  region=(1400,100,600,900), confidence=0.85)
            except:
                pass
            while start22 is not None:
                pyautogui.moveTo(start22)  # Moves the mouse to the coordinates of the image
                click()
                time.sleep(0.1)
                pyautogui.moveTo(x+230, y+130)
                time.sleep(0.15)
                start22 = pyautogui.locateCenterOnScreen(follow_button, region = (0,0,2500,1450), grayscale=True, confidence=0.8)
                print ('followed (second attempt)')
            else:
                pass
        except:
            pass

    def trytry():
        try:
            start = pyautogui.locateCenterOnScreen('trytry.png', region = (0,0,2500,1450), confidence=LIGHT_CONFIDENCE)
            if start is not None:
                pyautogui.moveTo(start)
                click()
                time.sleep(0.5)
                print(twitter_account(twitter_account_number))
                time.sleep(0.25)
                click()
        except:
            pass

    count = 0
    count2 = 0
    run_time = 0
    check_count = 0
    theme = ''
    print ('twitter_automator initiated')

    def get_key(val):
        for key,value in aclist.items():
            if val == value:
                return key

    def tabtabtab():
        # print('reloading pages...')
        times = count+1
        for i in range(times):
            pyautogui.hotkey('ctrl', 'tab', delay=0.25)
            time.sleep(0.5)
        pyautogui.hotkey('ctrl', 'tab', delay=0.25)
        time.sleep(1)
        pyautogui.hotkey('ctrl', 'tab', delay=0.25)
        time.sleep(1)

    accountloopcount = 0
    while True: #twitter_bot
        if printreply_eg:
            try:
                if keyboard.is_pressed('shift'):
                    # print(twitter_account(twitter_account_number))
                    pyautogui.write(twitter_account(twitter_account_number))
                elif keyboard.is_pressed('['):
                    twitter_bot()
            except:
                pass
        elif keyboard.is_pressed('1'):
            print ('running...')
            while True:
                if keyboard.is_pressed('shift'):
                    print ('THE PROGRAM IS ENDING......')
                    return
                if accountloop:
                    if run_time == 0:
                        print ('accountloop is initiated')
                        run_time += 1
                        # time.sleep(2)
                        pyautogui.screenshot('my_screenshot.png', region=(1000,100,1000,1200))
                        pyautogui.hotkey('ctrl', 'tab', delay=0.25)

                        #O o O o O o O o THEME FINDER o O o O o O o O#
                        start11 = pyautogui.locateCenterOnScreen('light_twitter.png', region = (400,0,500,200), confidence=0.8)
                        if start11 is not None:
                            theme = 'l'
                            print ('in light theme')
                        else:
                            start21 = pyautogui.locateCenterOnScreen('dark_twitter.png', region = (400,0,500,200), confidence=0.8)
                            if start21 is not None:
                                theme = 'd'
                                print ('in dark theme')
                            else:
                                print('theme cannot be determined')
                                return
                        #O o O o O o O o THEME FINDER o O o O o O o O#

                        ############account_number_finder############
                        for i in range(1, 21):
                            if theme =='l':
                                accountlist = f'un_ac{i}.png'
                            elif theme =='d':
                                accountlist = f'un_dac{i}.png'
                            twitter_account_number = i
                            start323 = pyautogui.locateCenterOnScreen(accountlist, region = (500,1340,500,100), confidence=0.8) #identify the account
                            if start323 is not None:
                                twitter_account_number = i
                                break 
                            else:
                                pass
                        if start323 is None: 
                            print('UNABLE TO LOCATE ACCOUNT')
                            return
                        else:
                            name = f'automating account {twitter_account_number}'
                            s = name.center(60, "=")
                            print (s)
                        ############account_number_finder############
                        pyautogui.hotkey('ctrl', 'tab', delay=0.25)
                    elif run_time >= 1:
                        # print ()
                        count += 1
                        twitter_bot()
                        if theme == 'l':
                            liked_retweeted = 'liked_retweeted.png'

                        elif theme =='d':
                            liked_retweeted = 'dliked_retweeted.png'

                        start322 = pyautogui.locateCenterOnScreen(liked_retweeted, region = (0,0,2500,1450), confidence=LIGHT_CONFIDENCE)
                        if start322 is None:
                            check_count += 1
                            print(f'DOUBLE CHECK IS NEEDED x{check_count}')
                        else:
                            print (f'.')

                        # trytry()
                        time.sleep(0.15)
                        pyautogui.hotkey('ctrl', 'tab', delay=0.25)
                        # print ('twitter_bot ran for',count, 'times')
                        start = pyautogui.locateCenterOnScreen('my_screenshot.png', region = (0,0,2500,1450), confidence=0.9)
                        # time.sleep(4) # --------------------------------------------------------------------------------------------------------------------------------------> extra sleep time
                    try:    # - - - - - - - - - - - - - - - - - -> when to stop 
                        if start is not None:
                            accountloopcount += 1
                            if accountloopcount == accountloop:
                                print('E.N.D')
                                return
                            elif twitter_account_number == 13 or twitter_account_number == 14 or twitter_account_number == 15 or twitter_account_number == 20:
                                print('the last account has reached')
                                print('E.N.D')
                                return
                            else:
                                print('a cycle has completed')
                                pyautogui.hotkey('ctrl', 'tab', delay=0.25)
                                aclist= {1:'1', 2:'4', 3:'7', 4:'10', 5:'13', 6:'2', 7:'5', 8:'8', 9:'11', 10:'14', 11:'3', 12:'6', 13:'9', 14:'12', 15:'15', 16:'16', 17:'17', 18:'18', 19:'19', 20:'20'}
                                count_acw = int(get_key(str(twitter_account_number))) #turn t.ac.no to str to get the key and turn back to int
                                next_num = count_acw+1
                                valueofpos = aclist.get(next_num)
                                if theme =='l':
                                    accounttosearch = f'ac{valueofpos}.png'
                                elif theme =='d':
                                    accounttosearch = f'dac{valueofpos}.png'
                                pyautogui.moveTo(x=741, y=1395)
                                click()
                                while True:
                                    try:
                                        start2 = pyautogui.locateCenterOnScreen(accounttosearch, region = (0,0,2500,1450), confidence=0.85)
                                        if start2 is not None:
                                            pyautogui.moveTo(start2)
                                            click()
                                            time.sleep(0.2)
                                            break
                                    except:
                                        time.sleep(0.1)
                                tabtabtab()
                                count = 0
                                check_count = 0
                                twitter_account_number = int(valueofpos)
                                name = f'automating account {twitter_account_number}'
                                s = name.center(60, "=")
                                print (s)                                
                    except:
                        pass


                if (auto == 'yes') and (looptimes > 0): #----------------------------------------------> limited loop
                    check_count = 0
                    if count <= looptimes:
                        count += 1
                        twitter_bot()
                        
                        start322 = pyautogui.locateCenterOnScreen(liked_retweeted, region = (0,0,2500,1450), confidence=LIGHT_CONFIDENCE)
                        if start322 is None:
                            check_count += 1
                            print(f'DOUBLE CHECK IS NEEDED x{check_count}')
                        else:
                            print (f'.')

                        pyautogui.hotkey('ctrl', 'tab', delay=0.25)
                        # print ('twitter_bot ran for',count, 'times')
                    else:
                        pass
                elif (auto == 'yes') and (looptimes == 0): #----------------------------------------------> unlimited loop    

                    check_count = 0
                    if run_time == 0:
                        #O o O o O o O o THEME FINDER o O o O o O o O#
                        start11 = pyautogui.locateCenterOnScreen('light_twitter.png', region = (400,0,500,200), confidence=0.8)
                        if start11 is not None:
                            theme = 'l'
                            print ('in light theme')
                        else:
                            start21 = pyautogui.locateCenterOnScreen('dark_twitter.png', region = (400,0,500,200), confidence=0.8)
                            if start21 is not None:
                                theme = 'd'
                                print ('in dark theme')
                            else:
                                print('theme cannot be determined')
                                return
                        #O o O o O o O o THEME FINDER o O o O o O o O#

                        ############account_number_finder############
                        for i in range(1, 21):
                            if theme =='l':
                                accountlist = f'un_ac{i}.png'
                            elif theme =='d':
                                accountlist = f'un_dac{i}.png'
                            twitter_account_number = i
                            start323 = pyautogui.locateCenterOnScreen(accountlist, region = (500,1340,500,100), confidence=0.8) #identify the account
                            if start323 is not None:
                                twitter_account_number = i
                                break 
                            else:
                                pass
                        if start323 is None: 
                            print('UNABLE TO LOCATE ACCOUNT')
                            return
                        else:
                            name = f'automating account {twitter_account_number}'
                            s = name.center(60, "=")
                            print (s)
                        ############account_number_finder############
                        run_time += 1
                        time.sleep(1)
                        pyautogui.screenshot('my_screenshot.png', region=(1000,100,1000,1200))
                        pyautogui.hotkey('ctrl', 'tab', delay=0.25)
                    else:
                        count += 1
                        if theme == 'l':
                            twitter_home = 'twitter_home.png'
                            follow_button = 'light_Follow.png'
                            four_buttons = 'light_4_buttons.png'
                            reply_pop_up = 'light_reply_pop_up.png'
                            liked_retweeted = 'liked_retweeted.png'
                            unfollow = "unfollow.png"

                        elif theme =='d':
                            twitter_home = 'dtwitter_home.png'
                            follow_button = 'Follow.png'
                            four_buttons = 'dark_4_buttons.png'
                            reply_pop_up = 'dark_reply_pop_up.png'
                            liked_retweeted = 'dliked_retweeted.png'
                            unfollow = "dunfollow.png"
                        try:
                            start22 = pyautogui.locateCenterOnScreen(follow_button, region = (0,0,2500,1450), grayscale=True, confidence=0.85)
                            try:
                                x, y = pyautogui.locateCenterOnScreen(follow_button,  region=(1400,100,600,900), confidence=0.85)
                            except:
                                pass
                            while start22 is not None:
                                pyautogui.moveTo(start22)  # Moves the mouse to the coordinates of the image
                                click()
                                time.sleep(0.1)
                                pyautogui.moveTo(x+230, y+130)
                                time.sleep(0.15)
                                start22 = pyautogui.locateCenterOnScreen(follow_button, region = (0,0,2500,1450), grayscale=True, confidence=0.85)
                            else:
                                pass
                        except:
                            pass

                        try:
                            x, y = pyautogui.locateCenterOnScreen(unfollow, region = (0,0,2500,1450), grayscale=True, confidence=0.85)
                            pyautogui.moveTo(x+230, y+130)  # Moves the mouse to the coordinates of the image
                            click()
                            time.sleep(0.15)
                            print('"unfollow bug" cleared')
                        except:
                            pass

                        try:
                            x, y = pyautogui.locateCenterOnScreen(four_buttons, region = (0,0,2500,1200), confidence=LIGHT_CONFIDENCE)
                            if (x, y) is not None:
                                pyautogui.moveTo(x+68, y) #like
                                click()
                                pyautogui.moveTo(x-75, y) #retweet
                                click()
                                time.sleep(0.3)
                                pyautogui.moveTo(x-155, y) #retweet2
                                click()
                                time.sleep(0.2)

                                if except_reply:
                                    pass
                                else:
                                    pyautogui.moveTo(x-215, y) #reply
                                    time.sleep(0.1)
                                    click()
                                    time.sleep(0.5)
                                    pyautogui.write(twitter_account(twitter_account_number))
                                    pyautogui.moveTo(x=1041, y=1395)
                                    time.sleep(1)
                                    pyautogui.hotkey('ctrl', 'enter', delay=0.25)
                                    time.sleep(0.25)
                                    pyautogui.hotkey('ctrl', 'enter', delay=0.25)                
                                    # print ('liked, retweet, replied')
                        except:
                            # pyautogui.moveTo(2224, 264)
                            # click()
                            # time.sleep(0.2)
                            # click()
                            # pyautogui.scroll(-500)
                            time.sleep(0.2)
                            try:
                                x, y = pyautogui.locateCenterOnScreen(four_buttons, region = (0,0,2500,1450), confidence=0.7)
                                if (x, y) is not None:
                                    pyautogui.moveTo(x+68, y) #like
                                    click()
                                    pyautogui.moveTo(x-75, y) #retweet
                                    click()
                                    time.sleep(0.3)
                                    pyautogui.moveTo(x-155, y) #retweet2
                                    click()
                                    time.sleep(0.2)

                                    if except_reply:
                                        pass
                                    else:
                                        pyautogui.moveTo(x-215, y) #reply
                                        time.sleep(0.1)
                                        click()
                                        time.sleep(0.5)
                                        pyautogui.write(twitter_account(twitter_account_number))
                                        pyautogui.moveTo(x=1041, y=1395)
                                        time.sleep(1)
                                        pyautogui.hotkey('ctrl', 'enter', delay=0.25)                
                                        # print ('liked, retweet, replied')
                            except:
                                print ('four_buttons not found')


                        try:
                            start22 = pyautogui.locateCenterOnScreen(follow_button, region = (0,0,2500,1450), grayscale=True, confidence=0.8)
                            try:
                                x, y = pyautogui.locateCenterOnScreen(follow_button,  region=(1400,100,600,900), confidence=0.85)
                            except:
                                pass
                            while start22 is not None:
                                pyautogui.moveTo(start22)  # Moves the mouse to the coordinates of the image
                                click()
                                time.sleep(0.1)
                                pyautogui.moveTo(x+230, y+130)
                                time.sleep(0.15)
                                start22 = pyautogui.locateCenterOnScreen(follow_button, region = (0,0,2500,1450), grayscale=True, confidence=0.8)
                                print ('followed (second attempt)')
                            else:
                                pass
                        except:
                            pass
                        
                        start322 = pyautogui.locateCenterOnScreen(liked_retweeted, region = (0,0,2500,1450), confidence=LIGHT_CONFIDENCE)
                        if start322 is None:
                            check_count += 1
                            print(f'DOUBLE CHECK IS NEEDED x{check_count}')
                        else:
                            print (f'.')

                        time.sleep(0.15)
                        pyautogui.hotkey('ctrl', 'tab', delay=0.25)
                        # print ('twitter_bot ran for',count, 'times')
                        start = pyautogui.locateCenterOnScreen('my_screenshot.png', region = (0,0,2500,1450), confidence=0.9)
                        # time.sleep(4) # --------------------------------------------------------------------------------------------------------------------------------------> extra sleep time
                    try:
                        if start is not None:
                            print('Stopped (Home page has reached)')
                            return
                    except:
                        pass
                elif keyboard.is_pressed('['):
                    if reply_only == 'yes':
                        starts = pyautogui.locateCenterOnScreen(reply_pop_up, region = (0,0,2500,1450), grayscale=True, confidence=LIGHT_CONFIDENCE)
                        if (starts is not None):
                            pyautogui.moveTo(starts)  # Moves the mouse to the coordinates of the image
                            click()
                            time.sleep(0.3)
                            pyautogui.write(twitter_account(twitter_account_number))
                            time.sleep(1)
                            print ('replied')
                        else:
                            pass
                    else:
                        print('hi')
                        count += 1
                        if theme == 'l':
                            twitter_home = 'twitter_home.png'
                            follow_button = 'light_Follow.png'
                            four_buttons = 'light_4_buttons.png'
                            reply_pop_up = 'light_reply_pop_up.png'
                            liked_retweeted = 'liked_retweeted.png'
                            unfollow = "unfollow.png"

                        elif theme =='d':
                            twitter_home = 'dtwitter_home.png'
                            follow_button = 'Follow.png'
                            four_buttons = 'dark_4_buttons.png'
                            reply_pop_up = 'dark_reply_pop_up.png'
                            liked_retweeted = 'dliked_retweeted.png'
                            unfollow = "dunfollow.png"
                        # try:
                        #     start22 = pyautogui.locateCenterOnScreen(follow_button, region = (0,0,2500,1450), grayscale=True, confidence=0.85)
                        #     try:
                        #         x, y = pyautogui.locateCenterOnScreen(follow_button,  region=(1400,100,600,900), confidence=0.85)
                        #     except:
                        #         pass
                        #     while start22 is not None:
                        #         pyautogui.moveTo(start22)  # Moves the mouse to the coordinates of the image
                        #         click()
                        #         time.sleep(0.1)
                        #         pyautogui.moveTo(x+230, y+130)
                        #         time.sleep(0.15)
                        #         start22 = pyautogui.locateCenterOnScreen(follow_button, region = (0,0,2500,1450), grayscale=True, confidence=0.85)
                        #     else:
                        #         pass
                        # except:
                        #     pass

                        # try:
                        #     x, y = pyautogui.locateCenterOnScreen(unfollow, region = (0,0,2500,1450), grayscale=True, confidence=0.85)
                        #     pyautogui.moveTo(x+230, y+130)  # Moves the mouse to the coordinates of the image
                        #     click()
                        #     time.sleep(0.15)
                        #     print('"unfollow bug" cleared')
                        # except:
                        #     pass

                        try:
                            x, y = pyautogui.locateCenterOnScreen(four_buttons, region = (0,0,2500,1200), confidence=0.7)
                            if (x, y) is not None:
                                pyautogui.moveTo(x+68, y) #like
                                click()
                                pyautogui.moveTo(x-75, y) #retweet
                                click()
                                while True:
                                    try:
                                        checkcheck = pyautogui.locateCenterOnScreen(retweet_quoate_tweet, region = (0,0,2500,1200), confidence=LIGHT_CONFIDENCE)
                                        if checkcheck is not None:
                                            pyautogui.moveTo(x-200, y) #retweet2
                                            click()
                                            break
                                    except:
                                        time.sleep(0.1)

                                if except_reply:
                                    pass
                                else:
                                    pyautogui.moveTo(x-215, y) #reply
                                    time.sleep(0.1)
                                    click()
                                    time.sleep(0.5)
                                    pyautogui.write(twitter_account(twitter_account_number))
                                    pyautogui.moveTo(x=1041, y=1395)
                                    time.sleep(1)
                                    pyautogui.hotkey('ctrl', 'enter', delay=0.25)                
                                    # print ('liked, retweet, replied')
                            else:
                                print ('four_buttons not found')
                        except:
                            pass

                        try:
                            start22 = pyautogui.locateCenterOnScreen(follow_button, region = (0,0,2500,1450), grayscale=True, confidence=0.8)
                            try:
                                x, y = pyautogui.locateCenterOnScreen(follow_button,  region=(1400,100,600,900), confidence=0.85)
                            except:
                                pass
                            while start22 is not None:
                                pyautogui.moveTo(start22)  # Moves the mouse to the coordinates of the image
                                click()
                                time.sleep(0.1)
                                pyautogui.moveTo(x+230, y+130)
                                time.sleep(0.15)
                                start22 = pyautogui.locateCenterOnScreen(follow_button, region = (0,0,2500,1450), grayscale=True, confidence=0.8)
                                print ('followed (second attempt)')
                            else:
                                pass
                        except:
                            pass
                        print ('DONE x', count)
                elif keyboard.is_pressed(']'):
                    if reply_only =='yes':
                        pyautogui.hotkey('ctrl', 'enter', delay=0.25)                
                    pyautogui.hotkey('ctrl', 'tab', delay=0.25)
def export_favorite(theme=False, export_bookmarks_to=False, auto=False):
    CONFIDENCE = 0.85
    LIGHT_CONFIDENCE = 0.9
    print('running....')
    document = 'document.png'
    brave_click = 'brave_click.png'
    brave_open_favorites = 'brave_open_favorites.png'
    if theme == 'l':
        readinglist = 'readinglist.png'
        bookmarkmanager = 'bookmarkmanager.png'
        blank = 'blankspace.png'
        chromedot = 'chromedotdot.png'
        chromeimport = 'chrome_import.png'
        filenameinput = 'filenameinput.png'
        twitter_icon = 'twitter_s_icon.png'
        manage = 'manage.png'
        favoritesbar = 'favoritesbar.png'
        dot_edge = 'dot_edge.png'
        exportfavorites = 'exportfavorites.png'

        edge_delete = 'edge_delete.png'
        edge_import = 'edge_import.png'
        edge_choice = 'edge_choice.png'
        edge_pickchrome = 'edge_pickchrome.png'
        edge_final_import = 'edge_final_import.png'
        edge_done = 'edge_done.png'
        otherfavories = 'otherfavorites.png'

        brave_importbookmarks = 'brave_importbookmarks.png'

        small_win = "small_win.png"

    elif theme == 'd':
        readinglist = 'd_readinglist.png'
        bookmarkmanager = 'd_bookmarkmanager.png'
        blank = 'd_blankspace.png'
        chromedot = 'd_chromedotdot.png'
        chromeimport = 'd_chrome_import.png'
        filenameinput = 'dfilenameinput.png'
        twitter_icon = 'd_twitter_s_icon.png'
        manage = 'd_manage.png'
        favoritesbar = 'd_favoritesbar.png'
        dot_edge = 'd_dot_edge.png'
        exportfavorites = 'd_exportfavorites.png'
        chromeexport = 'd_chromeexport.png'


        edge_delete = 'd_edge_delete.png'
        edge_import = 'd_edge_import.png'
        edge_choice = 'd_edge_choice.png'
        edge_pickchrome = 'd_edge_pickchrome.png'
        edge_final_import = 'd_edge_final_import.png'
        edge_done = 'd_edge_done.png'
        otherfavories = 'd_otherfavories.png'

        brave_importbookmarks = 'dbrave_importbookmarks.png'

        small_win = "dsmall_win.png"
    # if (export_bookmarks_to == 'c'):
    def to_c_1():
        while True:
            try:
                start3 = pyautogui.locateCenterOnScreen(readinglist, region = (0,0,2500,1450), grayscale=True, confidence=LIGHT_CONFIDENCE)
                if start3 is not None:
                    pyautogui.moveTo(start3)
                    pyautogui.click(button='right')
                    time.sleep(0.1)
                    break
            except:
                time.sleep(0.1)

        while True:
            try:
                start3 = pyautogui.locateCenterOnScreen(bookmarkmanager, region = (0,0,2500,1450), grayscale=True, confidence=LIGHT_CONFIDENCE)
                if start3 is not None:
                    pyautogui.moveTo(start3)
                    click()
                    time.sleep(0.1)
                    break
            except:
                time.sleep(0.1)
        while True:
            try:
                start3 = pyautogui.locateCenterOnScreen(blank, region = (0,0,2500,1450), grayscale=True, confidence=LIGHT_CONFIDENCE)
                if start3 is not None:
                    pyautogui.moveTo(start3)
                    click()
                    time.sleep(0.1)
                    pyautogui.hotkey('ctrl', 'a', delay=0.25)
                    pyautogui.press('del')
                    break
            except:
                time.sleep(0.1)
        while True:
            try:
                start3 = pyautogui.locateCenterOnScreen(chromedot, region = (0,0,2500,1450), grayscale=True, confidence=LIGHT_CONFIDENCE)
                if start3 is not None:
                    pyautogui.moveTo(start3)
                    click()
                    time.sleep(0.1)
                    break
            except:
                time.sleep(0.1)
        while True:
            try:
                start3 = pyautogui.locateCenterOnScreen(chromeimport, region = (0,0,2500,1450), grayscale=True, confidence=LIGHT_CONFIDENCE)
                if start3 is not None:
                    pyautogui.moveTo(start3)
                    click()
                    time.sleep(0.1)
                    break
            except:
                time.sleep(0.1)
        while True:
            try:
                start3 = pyautogui.locateCenterOnScreen(document, region = (0,0,2500,1450), grayscale=True, confidence=LIGHT_CONFIDENCE)
                if start3 is not None:
                    pyautogui.moveTo(start3)
                    click()
                    time.sleep(0.1)
                    break
            except:
                time.sleep(0.1)
        while True:
            try:
                start3 = pyautogui.locateCenterOnScreen(filenameinput, region = (0,0,2500,1450), grayscale=True, confidence=LIGHT_CONFIDENCE)
                if start3 is not None:
                    pyautogui.moveTo(start3)
                    click()
                    time.sleep(0.25)
                    break
            except:
                time.sleep(0.1)

        pyautogui.write('exportfromedge.html')
        pyautogui.press('enter')
        time.sleep(0.2)
        
        # start = pyautogui.locateCenterOnScreen(opera_extrafile, region = (700, 150, 700, 1300), grayscale=True, confidence=LIGHT_CONFIDENCE)
        # pyautogui.moveTo(start)  # Moves the mouse to the coordinates of the image
        # click()
        # pyautogui.press('delete')
        print ('Brave -> Chrome imported')

    def to_c_2():
        while True:
            try:
                start3 = pyautogui.locateCenterOnScreen(brave_open_favorites, region = (0,0,2500,1450), grayscale=True, confidence=LIGHT_CONFIDENCE)
                if start3 is not None:
                    pyautogui.moveTo(start3)
                    pyautogui.click(button='right')
                    time.sleep(0.25)
                    break
            except:
                time.sleep(0.1)

        while True:
            try:
                start3 = pyautogui.locateCenterOnScreen(bookmarkmanager, region = (0,0,2500,1450), grayscale=True, confidence=LIGHT_CONFIDENCE)
                if start3 is not None:
                    pyautogui.moveTo(start3)
                    click()
                    time.sleep(0.25)
                    break
            except:
                time.sleep(0.1)

        time.sleep(0.25)
        pyautogui.moveTo(2459, 181)
        click()
        time.sleep(0.3)

        pyautogui.moveTo(2389, 349)
        click()
        time.sleep(0.5)

        pyautogui.write('exportfromedge.html')
        time.sleep(0.1)
        start = pyautogui.locateCenterOnScreen(document, region = (0,0,2500,1450), grayscale=True, confidence=LIGHT_CONFIDENCE)
        pyautogui.moveTo(start)  # Moves the mouse to the coordinates of the image
        click()
        time.sleep(0.9)
        pyautogui.press('tab')
        time.sleep(0.05)
        pyautogui.press('tab')
        time.sleep(0.05)
        pyautogui.press('tab')
        time.sleep(0.05)
        pyautogui.press('tab')
        time.sleep(0.05)
        pyautogui.press('tab')
        time.sleep(0.05)
        pyautogui.press('tab')
        time.sleep(0.05)
        pyautogui.press('tab')
        time.sleep(0.05)
        pyautogui.press('tab')
        time.sleep(0.2)
        pyautogui.press('enter')
        pyautogui.press('tab')
        pyautogui.press('enter')
        print ('Brave -> Chrome exported')
    # elif (export_bookmarks_to == 'e'):
    def to_e():
        while True:
            try:
                start3 = pyautogui.locateCenterOnScreen(twitter_icon, region = (0,0,2500,1450), grayscale=True, confidence=LIGHT_CONFIDENCE)
                if start3 is not None:
                    pyautogui.moveTo(start3)
                    pyautogui.click(button='right')
                    time.sleep(0.1)
                    break
            except:
                time.sleep(0.1)
                print('nope')
        while True:
            try:
                start3 = pyautogui.locateCenterOnScreen(manage, region = (0,0,2500,1450), grayscale=True, confidence=LIGHT_CONFIDENCE)
                if start3 is not None:
                    pyautogui.moveTo(start3)
                    click()
                    time.sleep(0.1)
                    break
            except:
                time.sleep(0.1)
        while True:
            try:
                start3 = pyautogui.locateCenterOnScreen(favoritesbar, region = (0,0,2500,1450), grayscale=True, confidence=LIGHT_CONFIDENCE)
                if start3 is not None:
                    pyautogui.moveTo(start3)
                    click()
                    pyautogui.hotkey('ctrl', 'a', delay=0.1)
                    time.sleep(0.1)
                    break
            except:
                time.sleep(0.1)
        while True:
            try:
                start3 = pyautogui.locateCenterOnScreen(edge_delete, region = (0,0,2500,1450), grayscale=True, confidence=LIGHT_CONFIDENCE)
                if start3 is not None:
                    pyautogui.moveTo(start3)
                    click()
                    time.sleep(0.1)
                    break
            except:
                time.sleep(0.1)
        while True:
            try:
                start3 = pyautogui.locateCenterOnScreen(otherfavories, region = (0,0,2500,1450), grayscale=True, confidence=LIGHT_CONFIDENCE)
                if start3 is not None:
                    pyautogui.moveTo(start3)
                    click()
                    time.sleep(0.1)
                    break
            except:
                time.sleep(0.1)
        while True:
            try:
                start3 = pyautogui.locateCenterOnScreen(favoritesbar, region = (0,0,2500,1450), grayscale=True, confidence=LIGHT_CONFIDENCE)
                if start3 is not None:
                    pyautogui.moveTo(start3)
                    click()
                    time.sleep(0.1)
                    break
            except:
                time.sleep(0.1)
        while True:
            try:
                start3 = pyautogui.locateCenterOnScreen(dot_edge, region = (0,0,2500,1450), grayscale=True, confidence=LIGHT_CONFIDENCE)
                if start3 is not None:
                    pyautogui.moveTo(start3)
                    click()
                    time.sleep(0.1)
                    break
            except:
                time.sleep(0.1)
        while True:
            try:
                start3 = pyautogui.locateCenterOnScreen(edge_import, region = (0,0,2500,1450), grayscale=True, confidence=LIGHT_CONFIDENCE)
                if start3 is not None:
                    pyautogui.moveTo(start3)
                    click()
                    time.sleep(0.1)
                    break
            except:
                time.sleep(0.1)
        while True:
            try:
                start3 = pyautogui.locateCenterOnScreen(edge_choice, region = (0,0,2500,1450), grayscale=True, confidence=LIGHT_CONFIDENCE)
                if start3 is not None:
                    pyautogui.moveTo(start3)
                    click()
                    time.sleep(0.1)
                    break
            except:
                time.sleep(0.1)
        while True:
            try:
                start3 = pyautogui.locateCenterOnScreen(edge_pickchrome, region = (0,0,2500,1450), grayscale=True, confidence=LIGHT_CONFIDENCE)
                if start3 is not None:
                    pyautogui.moveTo(start3)
                    click()
                    time.sleep(0.1)
                    pyautogui.scroll(-40)
                    break
            except:
                time.sleep(0.1)
        while True:
            try:
                start3 = pyautogui.locateCenterOnScreen(edge_final_import, region = (0,0,2500,1450), grayscale=True, confidence=LIGHT_CONFIDENCE)
                if start3 is not None:
                    pyautogui.moveTo(start3)
                    click()
                    time.sleep(0.1)
                    break
            except:
                time.sleep(0.1)
        while True:
            try:
                start3 = pyautogui.locateCenterOnScreen(edge_done, region = (0,0,2500,1450), grayscale=True, confidence=LIGHT_CONFIDENCE)
                if start3 is not None:
                    pyautogui.moveTo(start3)
                    click()
                    time.sleep(0.1)
                    break
            except:
                time.sleep(0.1)
        print ('Step1: Chrome -> Edge imported') 

    # elif (export_bookmarks_to == 'b'):
    def to_b_2(): 
        LIGHT_CONFIDENCE = 0.85
        while True:
            try:
                start3 = pyautogui.locateCenterOnScreen(brave_open_favorites, region = (0,0,2500,1450), grayscale=True, confidence=LIGHT_CONFIDENCE)
                if start3 is not None:
                    pyautogui.moveTo(start3)
                    pyautogui.click(button='right')
                    time.sleep(0.1)
                    break
            except:
                time.sleep(0.1)
        while True:
            try:
                start3 = pyautogui.locateCenterOnScreen(bookmarkmanager, region = (0,0,2500,1450), grayscale=True, confidence=LIGHT_CONFIDENCE)
                if start3 is not None:
                    pyautogui.moveTo(start3)
                    click()
                    time.sleep(0.1)
                    break
            except:
                time.sleep(0.1)
        while True:
            try:
                start3 = pyautogui.locateCenterOnScreen(brave_click, region = (0,0,2500,1450), grayscale=True, confidence=LIGHT_CONFIDENCE)
                if start3 is not None:
                    pyautogui.moveTo(start3)
                    click()
                    time.sleep(0.1)
                    pyautogui.hotkey('ctrl', 'a', delay=0.1)
                    pyautogui.press('delete')
                    time.sleep(0.3)
                    pyautogui.moveTo(2459, 181)
                    click()
                    time.sleep(0.3)
                    break
            except:
                time.sleep(0.1)
        while True:
            try:
                start3 = pyautogui.locateCenterOnScreen(brave_importbookmarks, region = (2300,0,200,500), grayscale=True, confidence=LIGHT_CONFIDENCE)
                if start3 is not None:
                    pyautogui.moveTo(start3)
                    click()
                    time.sleep(0.1)
                    break
            except:
                time.sleep(0.1)
        while True:
            try:
                start3 = pyautogui.locateCenterOnScreen(document, region = (0,0,2500,1450), grayscale=True, confidence=LIGHT_CONFIDENCE)
                if start3 is not None:
                    pyautogui.moveTo(start3)
                    click()
                    time.sleep(0.1)
                    break
            except:
                time.sleep(0.1)
        while True:
            try:
                start3 = pyautogui.locateCenterOnScreen(filenameinput, region = (0,0,2500,1450), grayscale=True, confidence=LIGHT_CONFIDENCE)
                if start3 is not None:
                    pyautogui.moveTo(start3)
                    click()
                    time.sleep(0.3)
                    pyautogui.write('exportfromedge.html')
                    pyautogui.press('enter')
                    break
            except:
                time.sleep(0.1)
        print ('Step2: Edge -> Brave imported')

    def to_b_1():
        LIGHT_CONFIDENCE = 0.85
        while True:
            try:
                start3 = pyautogui.locateCenterOnScreen(twitter_icon, region = (0,0,2500,1450), grayscale=True, confidence=LIGHT_CONFIDENCE)
                if start3 is not None:
                    pyautogui.moveTo(start3)
                    pyautogui.click(button='right')
                    time.sleep(0.1)
                    break
            except:
                time.sleep(0.1)
        while True:
            try:
                start3 = pyautogui.locateCenterOnScreen(manage, region = (0,0,2500,1450), grayscale=True, confidence=LIGHT_CONFIDENCE)
                if start3 is not None:
                    pyautogui.moveTo(start3)
                    click()
                    time.sleep(0.1)
                    break
            except:
                time.sleep(0.1)
        while True:
            try:
                start3 = pyautogui.locateCenterOnScreen(favoritesbar, region = (0,0,2500,1450), grayscale=True, confidence=LIGHT_CONFIDENCE)
                if start3 is not None:
                    pyautogui.moveTo(start3)
                    click()
                    time.sleep(0.1)
                    break
            except:
                time.sleep(0.1)
        while True:
            try:
                start3 = pyautogui.locateCenterOnScreen(dot_edge, region = (0,0,2500,1450), grayscale=True, confidence=LIGHT_CONFIDENCE)
                if start3 is not None:
                    pyautogui.moveTo(start3)
                    click()
                    time.sleep(0.1)
                    break
            except:
                time.sleep(0.1)
        while True:
            try:
                start3 = pyautogui.locateCenterOnScreen(exportfavorites, region = (0,0,2500,1450), grayscale=True, confidence=0.9)
                if start3 is not None:
                    pyautogui.moveTo(start3)
                    click()
                    time.sleep(0.8)
                    pyautogui.write('exportfromedge.html')
                    break
            except:
                time.sleep(0.1)
        while True:
            try:
                start3 = pyautogui.locateCenterOnScreen(document, region = (0,0,2500,1450), grayscale=True, confidence=LIGHT_CONFIDENCE)
                if start3 is not None:
                    pyautogui.moveTo(start3)
                    click()
                time.sleep(0.9)
                pyautogui.press('tab')
                time.sleep(0.1)
                pyautogui.press('tab')
                time.sleep(0.1)
                pyautogui.press('tab')
                time.sleep(0.1)
                pyautogui.press('tab')
                time.sleep(0.1)
                pyautogui.press('tab')
                time.sleep(0.1)
                pyautogui.press('tab')
                time.sleep(0.1)
                pyautogui.press('tab')
                time.sleep(0.1)
                pyautogui.press('tab')
                time.sleep(0.1)
                pyautogui.press('enter')
                pyautogui.press('tab')
                pyautogui.press('enter')
                print ('Step3: Edge -> Brave exported')
                break
            except:
                time.sleep(0.1)

    # elif (export_bookmarks_to == 'a'):
    def to_a():
        while True:
            try:
                start3 = pyautogui.locateCenterOnScreen(brave_open_favorites, region = (0,0,2500,1450), grayscale=True, confidence=LIGHT_CONFIDENCE)
                if start3 is not None:
                    pyautogui.moveTo(start3)
                    pyautogui.click(button='right')
                    time.sleep(0.1)
                    break
            except:
                time.sleep(0.1)
        while True:
            try:
                start3 = pyautogui.locateCenterOnScreen('d_bookmarkmanager.png', region = (0,0,2500,1450), grayscale=True, confidence=LIGHT_CONFIDENCE)
                if start3 is not None:
                    pyautogui.moveTo(start3)
                    click()
                    time.sleep(0.1)
                    break
            except:
                time.sleep(0.1)
        while True:
            try:
                start3 = pyautogui.locateCenterOnScreen('blankspace.png', region = (0,0,2500,1450), grayscale=True, confidence=LIGHT_CONFIDENCE)
                if start3 is not None:
                    pyautogui.moveTo(start3)
                    click()
                    time.sleep(0.1)
                    pyautogui.hotkey('ctrl', 'a', delay=0.1)
                    pyautogui.press('delete')
                    time.sleep(0.3)
                    pyautogui.moveTo(2445, 128)
                    click()
                    time.sleep(0.3)
                    break
            except:
                time.sleep(0.1)
        while True:
            try:
                start3 = pyautogui.locateCenterOnScreen('avast_import.png', region = (2300,0,200,500), grayscale=True, confidence=0.95)
                if start3 is not None:
                    pyautogui.moveTo(start3)
                    click()
                    time.sleep(0.1)
                    break
            except:
                time.sleep(0.1)
        while True:
            try:
                start3 = pyautogui.locateCenterOnScreen(document, region = (0,0,2500,1450), grayscale=True, confidence=LIGHT_CONFIDENCE)
                if start3 is not None:
                    pyautogui.moveTo(start3)
                    # time.sleep(0.2)
                    click()
                    time.sleep(0.2)
                    break
            except:
                time.sleep(1)
        while True:
            try:
                start3 = pyautogui.locateCenterOnScreen(filenameinput, region = (0,0,2500,1450), grayscale=True, confidence=LIGHT_CONFIDENCE)
                if start3 is not None:
                    pyautogui.moveTo(start3)
                    click()
                    time.sleep(0.3)
                    pyautogui.write('exportfromedge.html')
                    pyautogui.press('enter')
                    break
            except:
                time.sleep(0.1)
        print ('Step4: Brave -> Avast imported')

    if auto == 'yes':
        if (export_bookmarks_to == 'c'):
            brave_open()
            time.sleep(0.5)
            to_c_1()
            time.sleep(0.5)
            pyautogui.hotkey('alt', 'f4', delay=0.25)
            chrome_open()
            time.sleep(0.5)
            to_c_2()
            exit()

        elif (export_bookmarks_to == 'e'):
            edge_open()
            time.sleep(0.5)
            to_e()
            exit()

        elif (export_bookmarks_to == 'b'):
            edge_open()
            time.sleep(0.5)
            to_b_1()
            time.sleep(2)
            pyautogui.hotkey('alt', 'f4', delay=0.25)
            brave_open()
            time.sleep(0.5)
            to_b_2()
            exit()
        elif (export_bookmarks_to == 'a'):
            opera_open()
            time.sleep(0.5)
            to_a()
            time.sleep(2)
            pyautogui.hotkey('alt', 'f4', delay=0.25)
            exit()
    elif auto == 'full':
        edge_open()
        LIGHT_CONFIDENCE = 0.75
        while True:
            try:
                start3 = pyautogui.locateCenterOnScreen('edge_light.png', region = (0,0,2500,1450), confidence=LIGHT_CONFIDENCE)
                if start3 is not None:
                    theme = 'l'
                    print ('in light theme')
                    break
            except:
                time.sleep(0.4)
                print('nope')
            try:
                start3 = pyautogui.locateCenterOnScreen('edge_dark.png', region = (0,0,2500,1450), confidence=LIGHT_CONFIDENCE)
                if start3 is not None:
                    theme = 'd'
                    print ('in dark theme')
                    break
            except:
                time.sleep(0.2)
                print('nope')
        document = 'document.png'
        brave_click = 'brave_click.png'
        brave_open_favorites = 'brave_open_favorites.png'
        if theme == 'l':
            readinglist = 'readinglist.png'
            bookmarkmanager = 'bookmarkmanager.png'
            blank = 'blankspace.png'
            chromedot = 'chromedotdot.png'
            chromeimport = 'chrome_import.png'
            filenameinput = 'filenameinput.png'
            twitter_icon = 'twitter_s_icon.png'
            manage = 'manage.png'
            favoritesbar = 'favoritesbar.png'
            dot_edge = 'dot_edge.png'
            exportfavorites = 'exportfavorites.png'

            edge_delete = 'edge_delete.png'
            edge_import = 'edge_import.png'
            edge_choice = 'edge_choice.png'
            edge_pickchrome = 'edge_pickchrome.png'
            edge_final_import = 'edge_final_import.png'
            edge_done = 'edge_done.png'
            otherfavories = 'otherfavorites.png'

            brave_importbookmarks = 'brave_importbookmarks.png'

            small_win = "small_win.png"

        elif theme == 'd':
            readinglist = 'd_readinglist.png'
            bookmarkmanager = 'd_bookmarkmanager.png'
            blank = 'd_blankspace.png'
            chromedot = 'd_chromedotdot.png'
            chromeimport = 'd_chrome_import.png'
            filenameinput = 'dfilenameinput.png'
            twitter_icon = 'd_twitter_s_icon.png'
            manage = 'd_manage.png'
            favoritesbar = 'd_favoritesbar.png'
            dot_edge = 'd_dot_edge.png'
            exportfavorites = 'd_exportfavorites.png'
            chromeexport = 'd_chromeexport.png'


            edge_delete = 'd_edge_delete.png'
            edge_import = 'd_edge_import.png'
            edge_choice = 'd_edge_choice.png'
            edge_pickchrome = 'd_edge_pickchrome.png'
            edge_final_import = 'd_edge_final_import.png'
            edge_done = 'd_edge_done.png'
            otherfavories = 'd_otherfavories.png'

            brave_importbookmarks = 'dbrave_importbookmarks.png'

            small_win = "dsmall_win.png"
        brave_open()
        opera_open()
        print('press 1 to continue...')
        while True:
            try:
                if keyboard.is_pressed('1'):
                    break
            except:
                time.sleep(0.1)

        edge_open()
        time.sleep(0.5)
        to_e()
        to_b_1()
        time.sleep(2)
        pyautogui.hotkey('alt', 'f4', delay=0.25)
        brave_open()
        time.sleep(0.5)
        to_b_2()

        opera_open()
        time.sleep(0.5)
        to_a()
        time.sleep(0.2)
        pyautogui.hotkey('alt', 'f4', delay=0.25)
        time.sleep(0.2)
        pyautogui.hotkey('alt', 'f4', delay=0.25)
        time.sleep(0.2)
        pyautogui.hotkey('alt', 'f4', delay=0.25)
        time.sleep(0.2)
        pyautogui.hotkey('alt', 'f4', delay=0.25)
        time.sleep(0.2)
        pyautogui.hotkey('alt', 'f4', delay=0.25)


    # else:            
    #     if keyboard.is_pressed('1'):
    #         edge_fn()
    #     elif keyboard.is_pressed('2'):
    #         chrome_fn()
    #     elif keyboard.is_pressed('shift'):
    #         print ('THE PROGRAM IS ENDING......')
    #         return
def twitter_blocker(theme=False, twitter_account_number=False, auto=False, looptimes=False, accountloop=False, hyperloop=False, urls=False):
    CONFIDENCE = 0.7
    LIGHT_CONFIDENCE = 0.7
    print('twitter_blocker initiated')
    new_conf = 0.85
    def blocker():
        new_conf = 0.75
        twitter_block = 'block.png'
        if theme == 'l':        
            twitter_home = 'twitter_home.png'
            follow_button = 'light_Follow.png'
            four_buttons = 'light_4_buttons.png'
            twitter_dotdotdot = 'dotdotdot.png'
            twitter_report = 'report.png'
            twitter_spam = 'spam.png'
            twitter_fake = 'fake.png'
            twitter_done = 'done.png'
            twitter_following = 'following.png'
            twitter_block0 = 'twitter_block0.png'

        elif theme =='d':
            twitter_home = 'dtwitter_home.png'
            follow_button = 'Follow.png'
            four_buttons = 'dark_4_buttons.png'
            twitter_dotdotdot = 'ddotdotdot.png'
            twitter_report = 'dreport.png'
            twitter_spam = 'spam.png'
            twitter_fake = 'fake.png'
            twitter_done = 'ddone.png'
            twitter_following = 'dfollowing.png'
            twitter_block0 = 'dtwitter_block0.png'

        pause()

        while True:
            try:
                start2 = pyautogui.locateCenterOnScreen(twitter_dotdotdot, region = (800,0,700,1450), confidence=new_conf)
                if start2 is not None:
                    pyautogui.moveTo(start2)
                    click()
                    time.sleep(0.1)
                    break
            except:
                time.sleep(0.1)
        while True:
            try:
                start2 = pyautogui.locateCenterOnScreen(twitter_block0, region = (0,0,2500,1450), confidence=new_conf)
                if start2 is not None:
                    pyautogui.moveTo(start2)
                    click()
                    time.sleep(0.1)
                    break
            except:
                time.sleep(0.1)
        while True:
            try:
                start2 = pyautogui.locateCenterOnScreen('twitter_block.png', region = (0,0,2500,1450), confidence=new_conf)
                if start2 is not None:
                    pyautogui.moveTo(start2)
                    click()
                    time.sleep(0.1)
                    break
            except:
                time.sleep(0.1)

    def blocker_checker():
        blocked = 'blocked.png'
        starrrrt = pyautogui.locateCenterOnScreen(blocked, region = (1100,0,500,1000), grayscale=True, confidence=LIGHT_CONFIDENCE)
        if starrrrt is not None:
            print(f'.')
            # return
        else:
            print (f'DOUBLE CHECK IS NEEDED')

    def get_key(val):
        for key,value in aclist.items():
            if val == value:
                return key

    def tabtabtab():
        times = count+1
        for i in range(times):
            pyautogui.hotkey('ctrl', 'tab', delay=0.25)
            time.sleep(0.5)
        pyautogui.hotkey('ctrl', 'tab', delay=0.25)
        time.sleep(1)
        pyautogui.hotkey('ctrl', 'tab', delay=0.25)
        print ('all pages are reloaded')
        time.sleep(1)
    accountloopcount = 0
    run_time = 0
    count= 0

    while True:
        if keyboard.is_pressed('`'):
            blocker()
        elif keyboard.is_pressed('shift'):
            print ('THE PROGRAM IS ENDING......')
            return
        elif keyboard.is_pressed('1'): #BLOCKER
            print ('running...')
            while True:
                if accountloop:
                    if run_time == 0:
                        print ('accountloop is initiated')
                        run_time += 1
                        # time.sleep(2)
                        pyautogui.screenshot('my_screenshot.png', region=(1000,100,1000,1200))
                        pyautogui.hotkey('ctrl', 'tab', delay=0.25)

                        #O o O o O o O o THEME FINDER o O o O o O o O#
                        start11 = pyautogui.locateCenterOnScreen('light_twitter.png', region = (400,0,500,200), confidence=0.8)
                        if start11 is not None:
                            theme = 'l'
                            print ('in light theme')
                        else:
                            start21 = pyautogui.locateCenterOnScreen('dark_twitter.png', region = (400,0,500,200), confidence=0.8)
                            if start21 is not None:
                                theme = 'd'
                                print ('in dark theme')
                            else:
                                print('theme cannot be determined')
                                return
                        #O o O o O o O o THEME FINDER o O o O o O o O#

                        ############account_number_finder############
                        for i in range(1, 21):
                            if theme =='l':
                                accountlist = f'un_ac{i}.png'
                            elif theme =='d':
                                accountlist = f'un_dac{i}.png'
                            twitter_account_number = i
                            start323 = pyautogui.locateCenterOnScreen(accountlist, region = (500,1340,500,100), confidence=0.8) #identify the account
                            if start323 is not None:
                                twitter_account_number = i
                                break 
                            else:
                                pass
                        if start323 is None: 
                            print('UNABLE TO LOCATE ACCOUNT')
                            return
                        else:
                            name = f'automating account {twitter_account_number}'
                            s = name.center(60, "=")
                            print (s)
                        ############account_number_finder############
                        pyautogui.hotkey('ctrl', 'tab', delay=0.25)
                    elif run_time >= 1:
                        count += 1
                        starrrrt = pyautogui.locateCenterOnScreen('blocked.png', region = (1100,0,500,1000), grayscale=True, confidence=0.75)
                        if starrrrt is None:
                            blocker()
                            blocker_checker()
                        else:
                            print('blocked already')
                            blocker_checker()
                        # trytry()
                        pyautogui.hotkey('ctrl', 'tab', delay=0.25)
                        start = pyautogui.locateCenterOnScreen('my_screenshot.png', region = (0,0,2500,1450), confidence=0.9)
                    try:
                        if start is not None:
                            accountloopcount += 1
                            if accountloopcount == accountloop:
                                print('E.N.D')
                                return
                            elif twitter_account_number == 13 or twitter_account_number == 14 or twitter_account_number == 15 or twitter_account_number == 20:
                                print('the last account has reached')
                                print('E.N.D')
                                return
                            else:
                                print('a cycle has completed')
                                pyautogui.hotkey('ctrl', 'tab', delay=0.25)
                                aclist= {1:'1', 2:'4', 3:'7', 4:'10', 5:'13', 6:'2', 7:'5', 8:'8', 9:'11', 10:'14', 11:'3', 12:'6', 13:'9', 14:'12', 15:'15', 16:'16', 17:'17', 18:'18', 19:'19', 20:'20'}

                                count_acw = int(get_key(str(twitter_account_number))) #turn t.ac.no to str to get the key and turn back to int
                                next_num = count_acw+1
                                valueofpos = aclist.get(next_num)
                                if theme =='l':
                                    accounttosearch = f'ac{valueofpos}.png'
                                elif theme =='d':
                                    accounttosearch = f'dac{valueofpos}.png'
                                pyautogui.moveTo(x=741, y=1395)
                                click()
                                while True:
                                    try:
                                        start2 = pyautogui.locateCenterOnScreen(accounttosearch, region = (0,0,2500,1450), confidence=0.85)
                                        if start2 is not None:
                                            pyautogui.moveTo(start2)
                                            click()
                                            time.sleep(0.2)
                                            break
                                    except:
                                        time.sleep(0.1)        
                                tabtabtab()
                                twitter_account_number = int(valueofpos)
                                name = f'automating account {twitter_account_number}'
                                s = name.center(60, "=")
                                print (s)
                                count=0 
                    except:
                        pass
                elif hyperloop == 1:
                    chrome_open()
                    edge_open()
                    brave_open()
                    opera_open()
                    print('press 1 to continue')
                    while True:
                        try:
                            if keyboard.is_pressed('1'):
                                break
                        except:
                            time.sleep(0.1)
                    for i in range(4):
                        url_count = 0
                        run_time = 0
                        count = 0
                        accountloopcount = 0
                        print ('preparing browser...') # ---------------------------------------> blocker
                        browser_list = [chrome_open, edge_open, brave_open, opera_open] #sdfsdfvwervdfs 
                        # browser_list = [brave_open, opera_open]
                        browser_list[i]()
                        time.sleep(0.5)
                        pyautogui.hotkey('ctrl', 'n', delay=0.25)
                        pyautogui.write("https://www.websiteplanet.com/webtools/multiple-url/")
                        pyautogui.press('enter')
                        while True:
                            # print('?????')
                            try:
                                start2 = pyautogui.locateCenterOnScreen('urlopener.png', region = (0,0,2500,1450), confidence=0.85)
                                if start2 is not None:
                                    pyautogui.moveTo(start2)
                                    click()
                                    time.sleep(0.2)
                                    break
                            except:
                                time.sleep(0.1)
                                # print('nope?????')        
                        for url in urls:
                            url_count +=1
                            if len(urls) == url_count:
                                pyautogui.write(url)
                                while True:
                                    try:
                                        start2 = pyautogui.locateCenterOnScreen('openmultipleurls.png', region = (0,0,2500,1450), confidence=0.85)
                                        if start2 is not None:
                                            pyautogui.moveTo(start2)
                                            click()
                                            time.sleep(0.2)
                                            break
                                    except:
                                        time.sleep(0.1)
                            else:
                                pyautogui.write(url)
                                pyautogui.press('enter')
                        time.sleep(2)
                        pyautogui.hotkey('ctrl', 'tab', delay=0.25)
                        while True:
                            if run_time == 0:
                                print ('hyperloop is initiated')
                                run_time += 1
                                pyautogui.screenshot('my_screenshot.png', region=(1000,100,1000,1200))
                                time.sleep(0.2)
                                pyautogui.hotkey('ctrl', 'tab', delay=0.25)
                                time.sleep(0.2)
                                pyautogui.hotkey('ctrl', 'r', delay=0.25)
                                #O o O o O o O o THEME FINDER o O o O o O o O#
                                while True:
                                    try:
                                        start3 = pyautogui.locateCenterOnScreen('light_twitter.png', region = (400,0,500,200), grayscale=True, confidence=0.8)
                                        if start3 is not None:
                                            theme = 'l'
                                            print ('in light theme')
                                            break
                                        elif start3 is None:
                                            start21 = pyautogui.locateCenterOnScreen('dark_twitter.png', region = (400,0,500,200), confidence=0.8)
                                            if start21 is not None:
                                                theme = 'd'
                                                print ('in dark theme')
                                                break
                                            else:
                                                print('theme cannot be determined')
                                                pass
                                    except:
                                        time.sleep(0.1)
                                #O o O o O o O o THEME FINDER o O o O o O o O#
                                time.sleep(1)
                                # - - - - - - - FIRST AC LOCATER - - - - - - - 
                                firstaccountlist = ['1', '2', '3', '16']
                                for i in firstaccountlist:
                                    if theme =='l':
                                        accountlist = f'un_ac{i}.png'
                                    elif theme =='d':
                                        accountlist = f'un_dac{i}.png'
                                    twitter_account_number = i
                                    start323 = pyautogui.locateCenterOnScreen(accountlist, region = (500,1340,500,100), confidence=0.8) #identify the account
                                    if start323 is not None:                                      
                                        print('The first account has been selected')
                                        break
                                if start323 is None:
                                    pyautogui.moveTo(x=741, y=1395)
                                    click()
                                    time.sleep(1)
                                    firstaccountlist = ['1', '2', '3', '16']
                                    for i in firstaccountlist:
                                        if theme =='l':
                                            accountlist = f'ac{i}.png'
                                        elif theme =='d':
                                            accountlist = f'dac{i}.png'
                                        twitter_account_number = i
                                        start3223 = pyautogui.locateCenterOnScreen(accountlist, region = (500,650,500,700), confidence=0.75) #identify the account
                                        if start3223 is not None:
                                            pyautogui.moveTo(start3223)
                                            click()
                                            print('The first account has been selected')
                                            break
                                    if start3223 is None:
                                        print('The first account cant be found')
                                        return


                                # - - - - - - - FIRST AC LOCATER - - - - - - - 
                                # ^ ^ ^ ^ ^ ^ ^ Taber ^ ^ ^ ^ ^ ^ ^ #
                                for i in range(len(urls)):
                                    pyautogui.hotkey('ctrl', 'tab', delay=0.25)
                                    time.sleep(0.5)
                                pyautogui.hotkey('ctrl', 'tab', delay=0.25)
                                time.sleep(1)
                                pyautogui.hotkey('ctrl', 'tab', delay=0.25)
                                print('all pages are reloaded (1st account)')
                                # ^ ^ ^ ^ ^ ^ ^ Taber ^ ^ ^ ^ ^ ^ ^ #
                                time.sleep(0.5)


                                name = f'automating account {twitter_account_number}'
                                s = name.center(60, "=")
                                print (s)
                                # - - - - - - - FIRST AC LOCATER - - - - - - -  
                            

                            elif run_time >= 1:
                                count += 1 #< - - - - - - - -  - - - -  - - - -  - - - -  - - - -  - - - -  - - - -  - - - -  - - - - - - - -  - - - -  - - - -   - - - -  - - - - MAIN FUNCTION
                                starrrrt = pyautogui.locateCenterOnScreen('blocked.png', region = (1100,0,500,1000), grayscale=True, confidence=LIGHT_CONFIDENCE)
                                if starrrrt is None:
                                    blocker()
                                    blocker_checker()
                                else:
                                   blocker_checker() 
                                time.sleep(0.3)
                                pyautogui.hotkey('ctrl', 'tab', delay=0.25)
                                start = pyautogui.locateCenterOnScreen('my_screenshot.png', region = (0,0,2500,1450), confidence=0.9)
                                valueofpos = ''
                                try:
                                    if start is not None:
                                        accountloopcount += 1
                                        if accountloopcount == accountloop:
                                            print('E.N.D')
                                            return
                                        elif twitter_account_number == 13 or twitter_account_number == 14 or twitter_account_number == 15:
                                            print('This batch of account is completed')
                                            break
                                        elif twitter_account_number == 20:
                                            print('the hyerloop is done')
                                            print('E.N.D')
                                            return
                                        else:
                                            print('a cycle has completed')
                                            time.sleep(0.17)
                                            pyautogui.hotkey('ctrl', 'tab', delay=0.25)
                                            aclist= {1:'1', 2:'4', 3:'7', 4:'10', 5:'13', 6:'2', 7:'5', 8:'8', 9:'11', 10:'14', 11:'3', 12:'6', 13:'9', 14:'12', 15:'15', 16:'16', 17:'17', 18:'18', 19:'19', 20:'20'}
                                            count_acw = int(get_key(str(twitter_account_number))) #turn t.ac.no to str to get the key and turn back to int
                                            next_num = count_acw+1
                                            valueofpos = aclist.get(next_num)
                                            if theme =='l':
                                                accounttosearch = f'ac{valueofpos}.png'
                                            elif theme =='d':
                                                accounttosearch = f'dac{valueofpos}.png'    
                                            pyautogui.moveTo(x=741, y=1395)
                                            click()
                                            while True:
                                                try:
                                                    start2 = pyautogui.locateCenterOnScreen(accounttosearch, region=(500,800, 500, 650), confidence=0.85)
                                                    if start2 is not None:
                                                        pyautogui.moveTo(start2)
                                                        click()
                                                        time.sleep(0.1)
                                                        break
                                                except:
                                                    time.sleep(0.1)
                                            tabtabtab()
                                            twitter_account_number = int(valueofpos)
                                            name = f'automating account {twitter_account_number}'
                                            s = name.center(60, "=")
                                            print (s)
                                            count=0 
                                except:
                                    pass
                elif (auto == 'yes') and (looptimes > 0): #----------------------------------------------> limited loop
                    if count <= looptimes:
                        count += 1
                        blocker()
                        pyautogui.hotkey('ctrl', 'tab', delay=0.25)
                        print ('blocker ran for',count, 'times')
                    else:
                        pass
                elif (auto == 'yes') and (looptimes == 0): #----------------------------------------------> limited loop
                    if run_time == 0:
                        run_time += 1
                        time.sleep(2)
                        pyautogui.screenshot('my_screenshot.png', region=(1000,100,1000,1200))
                        pyautogui.hotkey('ctrl', 'tab', delay=0.25)
                    else:
                        count += 1
                        blocker()
                        time.sleep(1)
                        blocker_checker()
                        pyautogui.hotkey('ctrl', 'tab', delay=0.25)
                        print ('blocker ran for',count, 'times')
                        start = pyautogui.locateCenterOnScreen('my_screenshot.png', region = (0,0,2500,1450), confidence=0.9)
                    try:
                        if start is not None:
                            print('Home page has reached')
                            return
                    except:
                        pass

        elif keyboard.is_pressed('shift'):
            print ('THE PROGRAM IS ENDING......')
            return
def new_clicker(theme=False, accountloop=False, hyperloop=False, urls=False):
    new_conf = 0.8
    def the_click1():
        while True:
            try:
                start = pyautogui.locateCenterOnScreen('logout.png', region = (0,0,2500,1450), confidence=new_conf)
                if start is not None:
                    pyautogui.moveTo(start)
                    click()
                    time.sleep(0.1)                    
                    break
                else:
                    print('cant logout')
            except:
                time.sleep(0.1)
        while True:
            try:
                start2 = pyautogui.locateCenterOnScreen('ifthisisfound.png', region = (0,0,2500,1450), confidence=new_conf)
                if start2 is not None:
                    start3 = pyautogui.locateCenterOnScreen('twitterlogo.png', region = (0,0,2500,1450), confidence=new_conf)
                    pyautogui.moveTo(start3)
                    click()
                    time.sleep(0.1)
                    break
                else:
                    print('twitterlogo not found222')
            except:
                print('twitterlogo not found')
                time.sleep(0.1)
        while True:
            try:
                start2 = pyautogui.locateCenterOnScreen('login_ed.png', region = (0,0,2500,1450), confidence=new_conf)
                if start2 is not None:
                    break
            except:
                print ('not login_ed')
                time.sleep(0.1)
        print('done')
    def the_click2():
        while True:
            try:
                start3 = pyautogui.locateCenterOnScreen('step1.png', region = (0,0,2500,1450), confidence=new_conf)
                if start3 is not None:
                    pyautogui.moveTo(start3)
                    click()
                    time.sleep(0.5)
                    break
            except:
                time.sleep(0.25)



        while True:
            try:
                start3 = pyautogui.locateCenterOnScreen('step2.png', region = (0,0,2500,1450), confidence=new_conf)
                if start3 is not None:
                    pyautogui.moveTo(start3)
                    click()
                    time.sleep(0.25)
                    pyautogui.scroll(-10000)
                    break
            except:
                time.sleep(0.25)
        while True:
            pyautogui.press('esc')
            try:
                start3 = pyautogui.locateCenterOnScreen('step21.png', region = (0,0,2500,1450), confidence=new_conf)
                if start3 is not None:
                    pyautogui.moveTo(start3)
                    click()
                    time.sleep(0.25)
                    break
            except:
                time.sleep(0.25)
        while True:
            try:
                start3 = pyautogui.locateCenterOnScreen('gleam_twitter_retweet.png', region = (0,0,2500,1450), confidence=new_conf)
                if start3 is not None:
                    pyautogui.moveTo(start3)
                    click()
                    time.sleep(0.25)
                    pyautogui.hotkey('ctrl', 'w', delay=0.25)
                    break
            except:
                time.sleep(0.25)

        while True:
            try:
                start3 = pyautogui.locateCenterOnScreen('gleam_continue.png', region = (0,0,2500,1450), confidence=new_conf)
                if start3 is not None:
                    pyautogui.moveTo(start3)
                    click()
                    time.sleep(0.25)
                    break
            except:
                time.sleep(0.25)

        while True:
            try:
                start3 = pyautogui.locateCenterOnScreen('step3.png', region = (0,0,2500,1450), confidence=new_conf)
                if start3 is not None:
                    pyautogui.moveTo(start3)
                    click()
                    time.sleep(5) #########################################################################################################################
                    break
            except:
                time.sleep(0.25)
        while True:
            try:
                start3 = pyautogui.locateCenterOnScreen('step0.png', region = (0,0,2500,1450), confidence=0.85)
                if start3 is not None:
                    break
            except:
                time.sleep(0.25)

        while True:
            try:
                start3 = pyautogui.locateCenterOnScreen('step4.png', region = (0,0,2500,1450), confidence=new_conf)
                if start3 is not None:
                    pyautogui.moveTo(start3)
                    click()
                    time.sleep(0.25)
                    break
            except:
                time.sleep(0.25)
        while True:
            try:
                start3 = pyautogui.locateCenterOnScreen('gleam_continue.png', region = (0,0,2500,1450), confidence=new_conf)
                if start3 is not None:
                    pyautogui.moveTo(start3)
                    click()
                    time.sleep(0.25)
                    break
            except:
                time.sleep(0.25)

        while True:
            try:
                start3 = pyautogui.locateCenterOnScreen('step5.png', region = (0,0,2500,1450), confidence=new_conf)
                if start3 is not None:
                    pyautogui.moveTo(start3)
                    click()
                    time.sleep(0.25)
                    break
            except:
                time.sleep(0.25)
        while True:
            pyautogui.scroll(-10000)
            try:
                start3 = pyautogui.locateCenterOnScreen('gleam_continue.png', region = (0,0,2500,1450), confidence=new_conf)
                if start3 is not None:
                    pyautogui.moveTo(start3)
                    click()
                    time.sleep(0.25)
                    break
            except:
                time.sleep(0.25)
        while True:
            click()
            try:
                start3 = pyautogui.locateCenterOnScreen('step00.png', region = (0,0,2500,1450), confidence=new_conf)
                if start3 is not None:
                    break
            except:
                time.sleep(1)


        while True:
            try:
                start3 = pyautogui.locateCenterOnScreen('step6.png', region = (0,0,2500,1450), confidence=0.85)
                if start3 is not None:
                    pyautogui.moveTo(start3)
                    click()
                    time.sleep(0.25)
                    break
            except:
                time.sleep(0.25)
        while True:
            try:
                start3 = pyautogui.locateCenterOnScreen('gleam_continue.png', region = (0,0,2500,1450), confidence=new_conf)
                if start3 is not None:
                    pyautogui.moveTo(start3)
                    click()
                    time.sleep(0.25)
                    break
            except:
                time.sleep(0.25)


        while True:
            try:
                start32 = pyautogui.locateCenterOnScreen('step7.png', region = (0,0,2500,1450), confidence=0.85)
                if start32 is not None:
                    pyautogui.moveTo(start32)
                    click()
                    time.sleep(0.25)
                    break
            except:
                time.sleep(0.25)
        while True:
            try:
                start3 = pyautogui.locateCenterOnScreen('gleam_continue.png', region = (0,0,2500,1450), confidence=new_conf)
                if start3 is not None:
                    pyautogui.moveTo(start3)
                    click()
                    time.sleep(0.25)
                    break
            except:
                time.sleep(0.25)
    def the_click3():
        pass
        #####################
    def the_click4():
        while True:
            try:
                start3 = pyautogui.locateCenterOnScreen('gleam_edit.png', region = (0,0,2500,1450), confidence=new_conf)
                if start3 is not None:
                    pyautogui.moveTo(start3)
                    click()
                    time.sleep(0.25)
                    break
            except:
                time.sleep(0.25)
        while True:
            try:
                x, y = pyautogui.locateCenterOnScreen('twitchlogo.png', region = (0,0,2500,1450), confidence=0.8)
                if x is not None:
                    pyautogui.moveTo(x+450, y)
                    click()
                    time.sleep(0.25)
                    break
            except:
                time.sleep(0.25)
        # while True:
        #     try:
        #         x, y = pyautogui.locateCenterOnScreen('discordlogo.png', region = (0,0,2500,1450), confidence=0.8)
        #         if x is not None:
        #             pyautogui.moveTo(x+450, y)
        #             click()
        #             time.sleep(0.25)
        #             break
        #     except:
        #         time.sleep(0.25)
        # while True:
        #     try:
        #         x, y = pyautogui.locateCenterOnScreen('steam.png', region = (0,0,2500,1450), confidence=0.8)
        #         if x is not None:
        #             pyautogui.moveTo(x+450, y)
        #             click()
        #             time.sleep(0.25)
        #             break
        #     except:
        #         time.sleep(0.25)
        while True:
            try:
                start3 = pyautogui.locateCenterOnScreen('gleam_save.png', region = (0,0,2500,1450), confidence=new_conf)
                if start3 is not None:
                    pyautogui.moveTo(start3)
                    click()
                    time.sleep(0.25)
                    break
            except:
                time.sleep(0.25)

    def click4():
        pass
    def tabtabtab():
        print('reloading pages...')
        times = count+1
        for i in range(times):
            pyautogui.hotkey('ctrl', 'tab', delay=0.25)
            time.sleep(0.5)
        pyautogui.hotkey('ctrl', 'tab', delay=0.25)
        time.sleep(1)
        pyautogui.hotkey('ctrl', 'tab', delay=0.25)
        print ('all pages are reloaded')
        time.sleep(1)
    def get_key(val):
        for key,value in aclist.items():
            if val == value:
                return key

    if theme == 'l':

        account1 = 'ac1.png'
        account2 = 'ac2.png'
        account3 = 'ac3.png'
        account4 = 'ac4.png'
        account5 = 'ac5.png'
        account6 = 'ac6.png'
        account7 = 'ac7.png'
        account8 = 'ac8.png'
        account9 = 'ac9.png'
        account10 = 'ac10.png'
        account11 = 'ac11.png'
        account12 = 'ac12.png'
        account13 = 'ac13.png'
        account14 = 'ac14.png'
        account15 = 'ac15.png'

    elif theme =='d':

        account1 = 'dac1.png'
        account2 = 'dac2.png'
        account3 = 'dac3.png'
        account4 = 'dac4.png'
        account5 = 'dac5.png'
        account6 = 'dac6.png'
        account7 = 'dac7.png'
        account8 = 'dac8.png'
        account9 = 'dac9.png'
        account10 = 'dac10.png'
        account11 = 'dac11.png'
        account12 = 'dac12.png'
        account13 = 'dac13.png'
        account14 = 'dac14.png'
        account15 = 'dac15.png'

    run_time = 0
    count = 0
    accountloopcount = 0
    print ('new_clicker is initiated')
    while True:  #new_clicker
        if keyboard.is_pressed('2'):
            the_click1()
            # the_click2()
            # the_click3()
        elif keyboard.is_pressed('3'):
            the_click2()
            pass
        elif keyboard.is_pressed('4'):
            the_click4()
            pass  
        elif keyboard.is_pressed('shift'):
            print ('THE PROGRAM IS ENDING......')
            quit()
        elif keyboard.is_pressed('1'): #new_clicker
            print ('running...')
            if accountloop > 0:
                while True:
                    if run_time == 0:
                        print ('accountloop is initiated')
                        run_time += 1
                        # time.sleep(2)

                        pyautogui.screenshot('my_screenshot.png', region=(1000,100,1000,1200))
                        pyautogui.hotkey('ctrl', 'tab', delay=0.25)

                        #O o O o O o O o THEME FINDER o O o O o O o O#
                        start11 = pyautogui.locateCenterOnScreen('light_twitter.png', region = (400,0,500,200), confidence=0.8)
                        if start11 is not None:
                            theme = 'l'
                            print ('in light theme')
                        else:
                            start21 = pyautogui.locateCenterOnScreen('dark_twitter.png', region = (400,0,500,200), confidence=0.8)
                            if start21 is not None:
                                theme = 'd'
                                print ('in dark theme')
                            else:
                                print('theme cannot be determined')
                                return
                        #O o O o O o O o THEME FINDER o O o O o O o O#

                        ############account_number_finder############
                        for i in range(1, 21):
                            if theme =='l':
                                accountlist = f'un_ac{i}.png'
                            elif theme =='d':
                                accountlist = f'un_dac{i}.png'
                            twitter_account_number = i
                            start323 = pyautogui.locateCenterOnScreen(accountlist, region = (500,1340,500,100), confidence=0.8) #identify the account
                            if start323 is not None:
                                twitter_account_number = i
                                break 
                            else:
                                pass
                        if start323 is None: 
                            print('UNABLE TO LOCATE ACCOUNT')
                            return
                        else:
                            name = f'automating account {twitter_account_number}'
                            s = name.center(60, "=")
                            print (s)
                        ############account_number_finder############
                        pyautogui.hotkey('ctrl', 'tab', delay=0.25)
                    elif run_time >= 1:
                        count += 1
                        the_click1()
                        the_click2()
                        the_click4()
                        time.sleep(0.3)
                        pyautogui.hotkey('ctrl', 'tab', delay=0.25)
                        start = pyautogui.locateCenterOnScreen('my_screenshot.png', region = (0,0,2500,1450), confidence=0.9)
                    valueofpos = ''
                    try:
                        if start is not None:
                            accountloopcount += 1
                            if accountloopcount == accountloop:
                                print('E.N.D')
                                return
                            elif twitter_account_number == 13 or twitter_account_number == 14 or twitter_account_number == 15 or twitter_account_number == 20:
                                print('the last account has reached')
                                print('E.N.D')
                                return
                            else:
                                print('a cycle has completed')
                                pyautogui.hotkey('ctrl', 'tab', delay=0.25)
                                aclist= {1:'1', 2:'4', 3:'7', 4:'10', 5:'13', 6:'2', 7:'5', 8:'8', 9:'11', 10:'14', 11:'3', 12:'6', 13:'9', 14:'12', 15:'15', 16:'16', 17:'17', 18:'18', 19:'19', 20:'20'}
                                count_acw = int(get_key(str(twitter_account_number))) #turn t.ac.no to str to get the key and turn back to int
                                next_num = count_acw+1
                                valueofpos = aclist.get(next_num)
                                if theme =='l':
                                    accounttosearch = f'ac{valueofpos}.png'
                                elif theme =='d':
                                    accounttosearch = f'dac{valueofpos}.png'    
                                pyautogui.moveTo(x=741, y=1395)
                                click()
                                while True:
                                    try:
                                        start2 = pyautogui.locateCenterOnScreen(accounttosearch, region=(500,800, 500, 650), confidence=0.85)
                                        if start2 is not None:
                                            pyautogui.moveTo(start2)
                                            click()
                                            time.sleep(0.1)
                                            break
                                    except:
                                        time.sleep(0.1)
                                tabtabtab()
                                twitter_account_number = int(valueofpos)
                                name = f'automating account {twitter_account_number}'
                                s = name.center(60, "=")
                                print (s)
                                count=0 
                    except:
                        pass   
            elif hyperloop == 1:
                for i in range(0,3):
                    url_count = 0
                    run_time = 0
                    count = 0
                    accountloopcount = 0
                    print ('preparing browser...')
                    browser_list = [chrome_open, edge_open, brave_open, opera_open]
                    # browser_list = [edge_open, brave_open, opera_open]
                    browser_list[i]()
                    time.sleep(0.5)
                    pyautogui.hotkey('ctrl', 'n', delay=0.25)
                    pyautogui.write("https://www.websiteplanet.com/webtools/multiple-url/")
                    pyautogui.press('enter')
                    while True:
                        try:
                            start2 = pyautogui.locateCenterOnScreen('urlopener.png', region = (0,0,2500,1450), confidence=0.85)
                            if start2 is not None:
                                pyautogui.moveTo(start2)
                                click()
                                time.sleep(0.2)
                                break
                        except:
                            time.sleep(0.1)        
                    for url in urls:
                        url_count +=1
                        if len(urls) == url_count:
                            pyautogui.write(url)
                            while True:
                                try:
                                    start2 = pyautogui.locateCenterOnScreen('openmultipleurls.png', region = (0,0,2500,1450), confidence=0.85)
                                    if start2 is not None:
                                        pyautogui.moveTo(start2)
                                        click()
                                        time.sleep(0.2)
                                        break
                                except:
                                    time.sleep(0.1)
                        else:
                            pyautogui.write(url)
                            pyautogui.press('enter')
                    time.sleep(2)
                    pyautogui.hotkey('ctrl', 'tab', delay=0.25)
                    while True:
                        if run_time == 0:
                            print ('hyperloop is initiated')
                            run_time += 1
                            pyautogui.screenshot('my_screenshot.png', region=(1000,100,1000,1200))
                            time.sleep(0.2)
                            pyautogui.hotkey('ctrl', 'tab', delay=0.25)
                            #O o O o O o O o THEME FINDER o O o O o O o O#
                            while True:
                                try:
                                    start3 = pyautogui.locateCenterOnScreen('light_twitter.png', region = (400,0,500,200), grayscale=True, confidence=0.8)
                                    if start3 is not None:
                                        theme = 'l'
                                        print ('in light theme')
                                        break
                                    elif start3 is None:
                                        start21 = pyautogui.locateCenterOnScreen('dark_twitter.png', region = (400,0,500,200), confidence=0.8)
                                        if start21 is not None:
                                            theme = 'd'
                                            print ('in dark theme')
                                            break
                                        else:
                                            print('theme cannot be determined')
                                            pass
                                except:
                                    time.sleep(0.1)
                            #O o O o O o O o THEME FINDER o O o O o O o O#
                            time.sleep(1)
                            # - - - - - - - FIRST AC LOCATER - - - - - - - 
                            firstaccountlist = ['1', '2', '3', '16']
                            for i in firstaccountlist:
                                if theme =='l':
                                    accountlist = f'un_ac{i}.png'
                                elif theme =='d':
                                    accountlist = f'un_dac{i}.png'
                                twitter_account_number = i
                                start323 = pyautogui.locateCenterOnScreen(accountlist, region = (500,1340,500,100), confidence=0.8) #identify the account
                                if start323 is not None:
                                    twitter_account_number = i
                                    print('The first account has been selected')
                                    break
                            if start323 is None:
                                pyautogui.moveTo(x=741, y=1395)
                                click()
                                time.sleep(1)
                                firstaccountlist = ['1', '2', '3', '16']
                                for i in firstaccountlist:
                                    if theme =='l':
                                        accountlist = f'ac{i}.png'
                                    elif theme =='d':
                                        accountlist = f'dac{i}.png'
                                    twitter_account_number = i
                                    start323 = pyautogui.locateCenterOnScreen(accountlist, region = (500,650,500,700), confidence=0.75) #identify the account
                                    if start323 is not None:
                                        pyautogui.moveTo(start323)
                                        click()
                                        print('The first account has been selected')
                                        break
                            # - - - - - - - FIRST AC LOCATER - - - - - - - 

                            # ^ ^ ^ ^ ^ ^ ^ Taber ^ ^ ^ ^ ^ ^ ^ #
                            for i in range(len(urls)):
                                pyautogui.hotkey('ctrl', 'tab', delay=0.25)
                                time.sleep(0.5)
                            time.sleep(1)
                            pyautogui.hotkey('ctrl', 'tab', delay=0.25)
                            time.sleep(0.2)
                            pyautogui.hotkey('ctrl', 'tab', delay=0.25)
                            print('all pages are reloaded (1st account)')
                            # ^ ^ ^ ^ ^ ^ ^ Taber ^ ^ ^ ^ ^ ^ ^ #
                            time.sleep(0.5)



                            name = f'automating account {twitter_account_number}'
                            s = name.center(60, "=")
                            print (s)
                            # - - - - - - - FIRST AC LOCATER - - - - - - -  
                        

                        elif run_time >= 1:
                            count += 1 #< - - - - - - - -  - - - -  - - - -  - - - -  - - - -  - - - -  - - - -  - - - -  - - - - - - - -  - - - -  - - - -   - - - -  - - - - newcliker hyperloop MAIN FUNCTION
                            the_click1()
                            the_click2()
                            the_click4()
                            # backup ()
                            time.sleep(2)
                            pyautogui.hotkey('ctrl', 'tab', delay=0.25)
                            start = pyautogui.locateCenterOnScreen('my_screenshot.png', region = (0,0,2500,1450), confidence=0.9)
                            valueofpos = ''
                            try:
                                if start is not None:
                                    accountloopcount += 1
                                    if accountloopcount == accountloop:
                                        print('E.N.D')
                                        return
                                    elif twitter_account_number == 13 or twitter_account_number == 14 or twitter_account_number == 20:
                                        print('This batch of account is completed')
                                        break
                                    elif twitter_account_number == 15:
                                        print('the hyerloop is done')
                                        print('E.N.D')
                                        return
                                    else:
                                        print('a cycle has completed')
                                        time.sleep(0.17)
                                        pyautogui.hotkey('ctrl', 'tab', delay=0.25)
                                        aclist= {1:'1', 2:'4', 3:'7', 4:'10', 5:'13', 6:'2', 7:'5', 8:'8', 9:'11', 10:'14', 11:'3', 12:'6', 13:'9', 14:'12', 15:'15', 16:'16', 17:'17', 18:'18', 19:'19', 20:'20'}
                                        count_acw = int(get_key(str(twitter_account_number))) #turn t.ac.no to str to get the key and turn back to int
                                        next_num = count_acw+1
                                        valueofpos = aclist.get(next_num)
                                        if theme =='l':
                                            accounttosearch = f'ac{valueofpos}.png'
                                        elif theme =='d':
                                            accounttosearch = f'dac{valueofpos}.png'    
                                        pyautogui.moveTo(x=741, y=1395)
                                        click()
                                        while True:
                                            try:
                                                start2 = pyautogui.locateCenterOnScreen(accounttosearch, region=(500,800, 500, 650), confidence=0.85)
                                                if start2 is not None:
                                                    pyautogui.moveTo(start2)
                                                    click()
                                                    time.sleep(0.1)
                                                    break
                                            except:
                                                time.sleep(0.1)
                                        tabtabtab()
                                        twitter_account_number = int(valueofpos)
                                        name = f'automating account {twitter_account_number}'
                                        s = name.center(60, "=")
                                        print (s)
                                        count=0 
                            except:
                                pass
                            time.sleep(0.5)

def extract_links(times, del_duplicates):
    url_listtt = []
    print ('extract_links is initiated')
    while True:
        try:
            if keyboard.is_pressed('shift'):
                break
                return
        except:
            pass
        if keyboard.is_pressed('1'): #new_clicker
            print ('running...')
            for i in range(times):
                pyautogui.hotkey('ctrl', 'l', delay=0.25)
                time.sleep(0.15)
                pyautogui.hotkey('ctrl', 'c', delay=0.25)
                if del_duplicates == 'y':
                    a = pyperclip.paste()
                    if a not in url_listtt:
                        url_listtt.append(a)
                    else:
                        print('done')
                        quit()
                else:
                    pass
                pyautogui.hotkey('alt', 'tab', delay=0.25)
                pyautogui.hotkey('ctrl', 'v', delay=0.25)
                pyautogui.press('enter')
                pyautogui.hotkey('alt', 'tab', delay=0.25)
                pyautogui.hotkey('ctrl', 'tab', delay=0.25)
                time.sleep(0.15)
            print('reached designated times')
            print(url_listtt)
            return
def msg_checker(auto, mentions=False, keywords=False):
    def get_key(val):
        for key,value in aclist.items():
            if val == value:
                return key
    def checker():
        LIGHT_CONFIDENCE = 0.8
        if theme == 'l':
            msg_checker = "notification.png"
            mentions = "mentions.png"
        elif theme == 'd':
            msg_checker = "dnotification.png"
            mentions = "dmentions.png"
        while True:
            try:
                start3 = pyautogui.locateCenterOnScreen(msg_checker, region = (0,0,2500,1450), grayscale=True, confidence=LIGHT_CONFIDENCE)
                if start3 is not None:
                    pyautogui.moveTo(start3)
                    click()
                    time.sleep(0.1)
                    break
            except:
                print('cant find')
                time.sleep(0.1)
        if mentions == 'y':
            while True:
                try:
                    start3 = pyautogui.locateCenterOnScreen(mentions, region = (0,0,2500,1450), grayscale=True, confidence=LIGHT_CONFIDENCE)
                    if start3 is not None:
                        pyautogui.moveTo(start3)
                        click()
                        time.sleep(0.1)
                        break
                except:
                    time.sleep(0.1)
        if keywords is not None:
            pyautogui.hotkey('ctrl', 'f', delay=0.25)
            time.sleep(0.4)
            pyautogui.write(keywords)
            # pyautogui.press('tab')

        if auto == 'n':
            pass
        else:
            while True:
                if keyboard.is_pressed('1'):
                    break
                if keyboard.is_pressed('2'):
                    print('PAUSED')
                    while True:
                        if keyboard.is_pressed('del'):
                            break
                    else:
                        time.sleep(0.01)
                else:
                    time.sleep(0.01)

    print ('msg_checker is initiated')
    while True:
        if keyboard.is_pressed('1'):
            chrome_open()
            edge_open()
            brave_open()
            opera_open()
            while True:
                if keyboard.is_pressed('1'):
                    for i in range(0,4):
                        url_count = 0
                        run_time = 0
                        count = 0
                        accountloopcount = 0
                        print ('preparing browser...') # ---------------------------------------> msg checker
                        browser_list = [chrome_open, edge_open, brave_open, opera_open]
                        # browser_list = [brave_open, opera_open]
                        browser_list[i]()
                        time.sleep(0.25)
                        pyautogui.hotkey('ctrl', 'n', delay=0.25)
                        pyautogui.write('https://twitter.com/home')
                        time.sleep(0.25)
                        pyautogui.press('enter')
                        while True:
                            if auto == 'y':
                                if run_time == 0:
                                    print ('hyperloop is initiated')
                                    run_time += 1
                                    #O o O o O o O o THEME FINDER o O o O o O o O#
                                    while True:
                                        try:
                                            start3 = pyautogui.locateCenterOnScreen('light_twitter.png', region = (400,0,500,200), grayscale=True, confidence=0.8)
                                            if start3 is not None:
                                                theme = 'l'
                                                print ('in light theme')
                                                break
                                            elif start3 is None:
                                                start21 = pyautogui.locateCenterOnScreen('dark_twitter.png', region = (400,0,500,200), confidence=0.8)
                                                if start21 is not None:
                                                    theme = 'd'
                                                    print ('in dark theme')
                                                    break
                                                else:
                                                    print('theme cannot be determined')
                                                    pass
                                        except:
                                            time.sleep(0.1)
                                    #O o O o O o O o THEME FINDER o O o O o O o O#
                                    time.sleep(1)
                                    # - - - - - - - FIRST AC LOCATER - - - - - - - 
                                    first_ac_locater = 'run'
                                    while first_ac_locater == 'run':
                                        firstaccountlist = ['1', '2', '3', '16']
                                        for i in firstaccountlist:
                                            if theme =='l':
                                                accountlist = f'un_ac{i}.png'
                                            elif theme =='d':
                                                accountlist = f'un_dac{i}.png'
                                            twitter_account_number = i
                                            start323 = pyautogui.locateCenterOnScreen(accountlist, region = (500,1340,500,100), grayscale=True, confidence=0.85) #identify the account
                                            if start323 is not None:
                                                twitter_account_number = i
                                                print('The first account has been selected')
                                                first_ac_locater = 'false'
                                                break
                                        if start323 is None:
                                            pyautogui.moveTo(x=741, y=1395)
                                            click()
                                            time.sleep(1)
                                            firstaccountlist = ['1', '2', '3', '16']
                                            for i in firstaccountlist:
                                                if theme =='l':
                                                    accountlist = f'ac{i}.png'
                                                elif theme =='d':
                                                    accountlist = f'dac{i}.png'
                                                twitter_account_number = i
                                                start323 = pyautogui.locateCenterOnScreen(accountlist, region = (500,650,500,700), confidence=0.85) #identify the account
                                                print(accountlist)
                                                if start323 is not None:
                                                    pyautogui.moveTo(start323)
                                                    click()
                                                    print('The first account has been selected')
                                                    first_ac_locater = 'false'
                                                    break
                                        if start323 is None:
                                            pyautogui.moveTo(331, 716) 
                                            click()
                                            print('happens when the first run cant find the first_ac')
                                    # - - - - - - - FIRST AC LOCATER - - - - - - - 
                                    name = f'automating account {twitter_account_number}'
                                    s = name.center(60, "=")
                                    print (s)
                                    time.sleep(1)

                                elif run_time >= 1:
                                    checker()
                                    valueofpos = ''
                                    try:
                                        if twitter_account_number == 13 or twitter_account_number == 14 or twitter_account_number == 15:
                                            print('This batch of account is completed')
                                            break
                                        elif twitter_account_number == 20:
                                            print('the hyerloop is done')
                                            print('E.N.D')
                                            return
                                        else:
                                            print('a cycle has completed')
                                            time.sleep(0.17)
                                            pyautogui.hotkey('ctrl', 'tab', delay=0.25)
                                            aclist= {1:'1', 2:'4', 3:'7', 4:'10', 5:'13', 6:'2', 7:'5', 8:'8', 9:'11', 10:'14', 11:'3', 12:'6', 13:'9', 14:'12', 15:'15', 16:'16', 17:'17', 18:'18', 19:'19', 20:'20'}
                                            count_acw = int(get_key(str(twitter_account_number))) #turn t.ac.no to str to get the key and turn back to int
                                            next_num = count_acw+1
                                            valueofpos = aclist.get(next_num)
                                            if theme =='l':
                                                accounttosearch = f'ac{valueofpos}.png'
                                            elif theme =='d':
                                                accounttosearch = f'dac{valueofpos}.png'    
                                            pyautogui.moveTo(x=741, y=1395)
                                            click()
                                            while True:
                                                try:
                                                    start2 = pyautogui.locateCenterOnScreen(accounttosearch, region=(500,800, 500, 650), confidence=0.85)
                                                    if start2 is not None:
                                                        pyautogui.moveTo(start2)
                                                        click()
                                                        time.sleep(0.1)
                                                        break
                                                except:
                                                    time.sleep(0.1)
                                            twitter_account_number = int(valueofpos)
                                            name = f'automating account {twitter_account_number}'
                                            s = name.center(60, "=")
                                            print (s)
                                            count=0 
                                    except:
                                        pass
                                    time.sleep(0.5)
                            elif auto == 'n':
                                if run_time == 0:
                                    run_time +=1
                                    #O o O o O o O o THEME FINDER o O o O o O o O#
                                    while True:
                                        try:
                                            start3 = pyautogui.locateCenterOnScreen('light_twitter.png', region = (400,0,500,200), grayscale=True, confidence=0.8)
                                            if start3 is not None:
                                                theme = 'l'
                                                print ('in light theme')
                                                break
                                            elif start3 is None:
                                                start21 = pyautogui.locateCenterOnScreen('dark_twitter.png', region = (400,0,500,200), confidence=0.8)
                                                if start21 is not None:
                                                    theme = 'd'
                                                    print ('in dark theme')
                                                    break
                                                else:
                                                    print('theme cannot be determined')
                                                    pass
                                        except:
                                            time.sleep(0.1)
                                    #O o O o O o O o THEME FINDER o O o O o O o O#
                                    pyautogui.moveTo(x=741, y=1395)
                                    click()
                                elif run_time >= 1:
                                    run_time +=1
                                    aa = '0'
                                    while True:
                                        try:
                                            if keyboard.is_pressed('1'):
                                                checker()
                                                break
                                            elif keyboard.is_pressed('2'):
                                                aa = 'stop'
                                                break
                                        except:
                                            time.sleep(0.2)
                                    while True:
                                        try:
                                            if keyboard.is_pressed('1'):
                                                pyautogui.moveTo(x=741, y=1395)
                                                click()
                                                break
                                            elif keyboard.is_pressed('2'):
                                                aa = 'stop'
                                                break
                                        except:
                                            time.sleep(0.2)
                                    if aa == 'stop':
                                        break
                                    else:
                                        pass
                    break
            print('?')
            break
            print('??')
            return
            print('???')

def cooldown():
    new_conf = 0.8
    print ('running...')
    while True:
        if keyboard.is_pressed('1'):
            print ('cooldown is initiated')
            while True:
                while True:
                    try:
                        x, y = pyautogui.locateCenterOnScreen('move1.png', region = (0,0,2500,1450), grayscale=True, confidence=0.8)
                        if x is not None:
                            pyautogui.moveTo(x, y)
                            click()
                            time.sleep(0.25)
                            break
                    except:
                        print('check1')
                        time.sleep(0.25)
                while True:
                    try:
                        start3 = pyautogui.locateCenterOnScreen('move2.png', region = (0,0,2500,1450), confidence=new_conf)
                        if start3 is not None:
                            pyautogui.moveTo(start3)
                            click()
                            time.sleep(0.25)
                            break
                    except:
                        time.sleep(0.25)

                while True:
                    try:
                        start3 = pyautogui.locateCenterOnScreen('move3.png', region = (0,0,2500,1450), confidence=new_conf)
                        if start3 is not None:
                            pyautogui.moveTo(start3)
                            click()
                            time.sleep(0.25)
                            while True:
                                try:
                                    start3 = pyautogui.locateCenterOnScreen('move3_7.png', region = (0,0,2500,1450), confidence=new_conf)
                                    if start3 is not None:
                                        pyautogui.moveTo(start3)
                                        click()
                                        time.sleep(1)
                                        break
                                except:
                                    time.sleep(0.25)
                            break
                    except:
                        pass

                    try:
                        start3 = pyautogui.locateCenterOnScreen('move3_5.png', region = (0,0,2500,1450), confidence=new_conf)
                        if start3 is not None:
                            pyautogui.moveTo(start3)
                            click()
                            time.sleep(0.25)
                            while True:
                                try:
                                    start3 = pyautogui.locateCenterOnScreen('move3_7.png', region = (0,0,2500,1450), confidence=new_conf)
                                    if start3 is not None:
                                        pyautogui.moveTo(start3)
                                        click()
                                        time.sleep(1)
                                        break
                                except:
                                    time.sleep(0.25)
                            break
                    except:
                        pass

                    try:
                        start3 = pyautogui.locateCenterOnScreen('move3_7.png', region = (0,0,2500,1450), confidence=new_conf)
                        if start3 is not None:
                            pyautogui.moveTo(start3)
                            click()
                            time.sleep(1)
                            break
                    except:
                        pass

                while True:
                    try:
                        start3 = pyautogui.locateCenterOnScreen('move4.png', region = (0,0,2500,1450), confidence=new_conf)
                        if start3 is not None:
                            pyautogui.moveTo(start3)
                            click()
                            time.sleep(0.25)
                            break
                    except:
                        time.sleep(0.25)
                while True:
                    try:
                        start3 = pyautogui.locateCenterOnScreen('move5.png', region = (0,0,2500,1450), confidence=new_conf)
                        if start3 is not None:
                            pyautogui.moveTo(start3)
                            click()
                            time.sleep(0.25)
                            break
                    except:
                        time.sleep(0.25)
                pyautogui.hotkey('alt', 'left', delay=0.25)
                time.sleep(0.25)
                pyautogui.hotkey('alt', 'left', delay=0.25)
                pyautogui.scroll(-10000)
                time.sleep(0.2)
                if keyboard.is_pressed('shift'):
                    return

def email_checker():
    print('running...')
    while True:
        if keyboard.is_pressed('1'):
            chrome_open()
            time.sleep(0.2)
            pyautogui.hotkey('ctrl', 'n', delay=0.25)
            for i in range(10):
                pyautogui.hotkey('ctrl', 't', delay=0.25)
                email = (f'https://mail.google.com/mail/u/{i}/#inbox')
                pyautogui.write(email)
                pyautogui.press('enter')
            pyautogui.hotkey('ctrl', 'tab', delay=0.25)
            pyautogui.hotkey('ctrl', 'tab', delay=0.25)
        if keyboard.is_pressed('2'):
            edge_open()
            time.sleep(0.5)
            pyautogui.hotkey('ctrl', 'n', delay=0.25)
            for i in range(10):
                pyautogui.hotkey('ctrl', 't', delay=0.25)
                email = (f'https://mail.google.com/mail/u/{i}/#inbox')
                pyautogui.write(email)
                pyautogui.press('enter')
                time.sleep(0.1)
            pyautogui.hotkey('ctrl', 'tab', delay=0.25)
            pyautogui.hotkey('ctrl', 'tab', delay=0.25)
        if keyboard.is_pressed('4'):
            pyautogui.hotkey('alt', 'f4', delay=0.25)
            time.sleep(1)
            pyautogui.hotkey('alt', 'f4', delay=0.25)
            break
        if keyboard.is_pressed('3'):
            pyautogui.moveTo(x=379, y=189)
            click()
            sleep(0.2)
            pyautogui.moveTo(x=489, y=220)
            click()
            # sleep(0.4)
            # pyautogui.moveTo(x=1413, y=133)
            # click()
            # sleep(0.2)
            # pyautogui.hotkey('ctr', 'tab', delay=0.25)


def human(times_to_scroll_down, cycles):

    def pause():
        try:
            if keyboard.is_pressed('1'):
                print('paused')
                while True:
                    try:
                        if keyboard.is_pressed('del'):
                            print('resumed')
                            break
                    except:
                        time.sleep(0.1)
            else:
                pass
        except:
            pass

    def next_window():
        time.sleep(0.2)
        pyautogui.keyDown('alt')
        time.sleep(0.1)
        pyautogui.press('tab')    
        pyautogui.press('tab')
        pyautogui.press('tab')
        time.sleep(0.1)
        pyautogui.keyUp('alt')
        time.sleep(0.2)

    def pgdn():
        pyautogui.press('pgdn')
        pyautogui.press('pgdn')
        time.sleep(0.1)
        pyautogui.press('pgdn')
        pyautogui.press('pgdn')
        time.sleep(0.1)
        pyautogui.press('pgdn')
        pyautogui.press('pgdn')
        time.sleep(0.1)
        pyautogui.press('pgdn')
        pyautogui.press('pgdn')
        time.sleep(0.1)
        pyautogui.press('pgdn')

    def error_checker():
        for i in range(21):
            try:
                if theme == 'l':
                    x,y = pyautogui.locateCenterOnScreen(f'ac{i}.png', region = (0,0,2100,1450), confidence=0.8)
                elif theme == 'd':
                    print(i)
                    x,y = pyautogui.locateCenterOnScreen(f'dac{i}.png', region = (0,0,2100,1450), confidence=0.8)
                if x is not None:
                    pyautogui.moveTo(x-100, y)
                    click()
            except:
                pass

    chrome_ac = [1,4,7,10,13]
    edge_ac = [2,5,8,11,14]
    brave_ac = [3,6,9,12,15]
    opera_ac = [16,17,18,19,20]
    browser_list = [chrome_ac, edge_ac, brave_ac, opera_ac]
    new_conf=0.85

    # O o O o O o O o THEME FINDER o O o O o O o O#
    start11 = pyautogui.locateCenterOnScreen('light_twitter.png', region = (0,0,2500,1450), confidence=0.7)
    if start11 is not None:
        theme = 'l'
        print ('in light theme')
    else:
        start21 = pyautogui.locateCenterOnScreen('dark_twitter.png', region = (0,0,2500,1450), confidence=0.7)
        if start21 is not None:
            theme = 'd'
            print ('in dark theme')
        else:
            print('theme cannot be determined')
    # O o O o O o O o THEME FINDER o O o O o O o O#
    cycles_ran = 0
    for cycle in range(cycles):
        print (f'---------------cycles_ran = {cycles_ran+1}-------------------')
        passes_four_windows=0
        for looping_order in range(5): #looping on account order 1-5:
            firstaccountlist = ['1', '2', '3', '16']
            b=-1
            cdn_t=-1
            browser_list_num=-1
            for four in range(4): #pick the first ac
                # error_checker()
                cdn_t+=1
                b+=1
                browser_list_num+=1
                if cdn_t%2 == 0:
                    cdn = (0,0,200,1450)
                else:
                    cdn = (1225,0,200,1450)
                            # if looping_order = 0: #if its in the first run: 
                while True:
                    if theme =='l':
                        accounttosearch = f'ac{browser_list[browser_list_num][passes_four_windows]}.png'
                    elif theme =='d':
                        accounttosearch = f'dac{browser_list[browser_list_num][passes_four_windows]}.png'
                    try:
                        start3 = pyautogui.locateCenterOnScreen(f'mini_ac{browser_list[browser_list_num][passes_four_windows]}.png', region = cdn, confidence=new_conf)
                        if start3 is not None:
                            pyautogui.moveTo(start3)
                            click()
                            time.sleep(0.25)
                            click()
                            break
                        elif start3 is None:
                            while True:
                                for i in browser_list[browser_list_num]:
                                    try:
                                        start3 = pyautogui.locateCenterOnScreen(f'mini_ac{i}.png', region = cdn, confidence=new_conf)
                                        if start3 is not None:
                                            pyautogui.moveTo(start3)
                                            click()
                                            while True:
                                                try:
                                                    start3 = pyautogui.locateCenterOnScreen(accounttosearch, region = (0,0,2500,1450), confidence=new_conf)
                                                    if start3 is not None:
                                                        pyautogui.moveTo(start3)
                                                        click()
                                                        time.sleep(0.25)
                                                        break
                                                except:
                                                    time.sleep(0.25)
                                            break
                                    except:
                                        time.sleep(0.1)
                                break   
                            while True:
                                try:
                                    x, y = pyautogui.locateCenterOnScreen(accounttosearch, region = (0,0,2500,1450), confidence=new_conf)
                                    if start3 is not None:
                                        pyautogui.moveTo(x-100, y)
                                        click()
                                        time.sleep(0.25)
                                        break
                                except:
                                    break
                            break
                    except:
                        time.sleep(0.1)

            for four in range(4):
                next_window()
                for i in range(times_to_scroll_down): #start scrolling
                    pause()
                    scroll_interval = round(random.uniform(0.5, 2), 2)
                    pgdn()
                    time.sleep(scroll_interval)
            print(f'{looping_order+1}/5 done')

            passes_four_windows +=1
        cycles_ran += 1
def sort_links(sort_home_page, for_list):
    with open('thelinks.txt', 'r', encoding='utf-8') as f:
        contents2 = f.read().rstrip().lstrip()
        thelist = contents2.split("\n")
        thelist = list(dict.fromkeys(thelist)) #delete duplicate
        newlist = []
        if sort_home_page == 'y':
            for ini_str in thelist:
                sub_str = "/"
                occurrence = 4
                count_o = 0
                for i in ini_str:
                    if i == "/":
                        count_o +=1
                    else:
                        pass
                if count_o <= 3:
                    newlist.append(ini_str)
                else:    
                    val = -1
                    # Finding nth occurrence of substring
                    for i in range(0, occurrence):
                        if len(ini_str) >= val:
                            val = ini_str.find(sub_str, val + 1)
                        else:
                            print('???')
                    newlist.append(ini_str[:val:])

            # delete = '/status/' #sort to profile
            # for i in thelist:   
            #     pos = i.find(delete)
            #     if pos == -1:
            #         pass
            #     else:
            #         i = i[:pos:]
            #     newlist.append(i)
            if for_list == 'y':
                a = ' '.join(newlist)
                a = a.replace(' ',"',\n")
                # a = a.replace(' ',"\n")
                a = a.replace('https',"'https")
                print(a+"'")
            else:
                a = ' '.join(newlist)
                a = a.replace(' ',"\n")
                print(a)
        else:
            if for_list == 'y':
                a = ' '.join(thelist)
                a = a.replace(' ',"',\n")
                a = a.replace('https',"'https")
                print(a+"'")
            else:
                a = ' '.join(thelist)
                a = a.replace(' ',"\n")
                print(a)
def verify():
    print('verify is running...')
    while True:
        if keyboard.is_pressed('1'):
            while True:
                try:
                    # print('verify_continue_to_twitter')
                    x, y = pyautogui.locateCenterOnScreen('verify_continue_to_twitter.png', region = (0,0,2500,700), grayscale=True, confidence=0.8)
                    if x is not None:
                        pyautogui.moveTo(x, y)
                        time.sleep(0.2)
                        click()
                    else:
                        pass
                except:
                    pass
                try:
                    # print('verify_start')
                    x, y = pyautogui.locateCenterOnScreen('verify_start.png', region = (0,0,2500,700), grayscale=True, confidence=0.8)
                    if x is not None:
                        pyautogui.moveTo(x, y)
                        time.sleep(0.2)
                        click()
                    else:
                        pass
                except:
                    pass
                try:
                    # print('verify_bot')
                    x, y = pyautogui.locateCenterOnScreen('verify_bot.png', region = (0,0,2500,700), grayscale=True, confidence=0.9)
                    if x is not None:
                        pyautogui.moveTo(x-50, y)
                        time.sleep(0.2)
                        click()
                    else:
                        pass
                except:
                  pass
                try:
                    # print('verify_send_code')
                    x, y = pyautogui.locateCenterOnScreen('verify_send_code.png', region = (0,0,2500,700), grayscale=True, confidence=0.8)
                    if x is not None:
                        pyautogui.moveTo(x, y)
                        time.sleep(0.2)
                        click()
                    else:
                        pass
                except:
                    pass
                try:
                    # print('verify_continue')
                    x, y = pyautogui.locateCenterOnScreen('verify_continue.png', region = (0,0,2500,700), grayscale=True, confidence=0.8)
                    if x is not None:
                        pyautogui.moveTo(x, y)
                        time.sleep(0.2)
                        click()
                    else:
                        pass
                except:
                    pass