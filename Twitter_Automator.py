from the_code import twitter_automator, export_favorite, twitter_blocker, new_clicker, extract_links, msg_checker, cooldown, email_checker, human, sort_links, verify
url_list = ['https://twitter.com/home',
'https://twitter.com/taxdtxme',
'https://twitter.com/thegamingglobal',
'https://twitter.com/FLC_Neoxx',
'https://twitter.com/eikzyy',
'https://twitter.com/failedrender'
]
def RUN_PROGRAM(run_program, the_theme=False, exportbookmarksto=False):
	if run_program == 1:                                                                # 1_export_favorite
		# export_favorite(export_bookmarks_to = 'a', theme = the_theme, auto = 'yes')
		export_favorite(auto = 'full')
	elif run_program == 2:
		# twitter_automator (accountloop = 5, tag3 = "yes")
		twitter_automator (accountloop = 5)
	elif run_program == 3: # 1 account loop
		twitter_automator (auto = 'yes', looptimes=0)

	elif run_program == 4:                                                               # 5_blocker
		twitter_blocker (accountloop = 5)
	elif run_program == 5:		
		twitter_blocker(hyperloop = 1, urls = url_list) #sdfsdfvwervdfs3

	elif run_program == 6:
		new_clicker(hyperloop = 0, accountloop = 5, urls = url_list)

	elif run_program == 7:                                                               # 7_extract links
		extract_links(70, del_duplicates = 'y')
	elif run_program == 8:                                                               # 8_msg checker
		msg_checker(auto = 'y', mentions = 'n', keywords = 'Feb 9') 
	elif run_program ==9:
		email_checker()
	elif run_program ==11:                                                              # 11_sort_links
		sort_links(sort_home_page = 'y', for_list = 'y') #search: thelinks

	elif run_program ==10:
		human(times_to_scroll_down = '15', cycles = '6')
	elif run_program ==12:
		verify()

RUN_PROGRAM(8)

# RUN_PROGRAM(1, 'l')
# <==================> <==================> <==================> <==================> <==================>
# <==================> <==================> <==================> <==================> <==================>
def RUN_OTHER_PROGRAM(run_program, the_theme): 
	if run_program == 5: #1 manual: 1 page
		twitter_automator (twitter_account_number = 1, theme = the_theme, auto = 'no', looptimes=0, reply_only='no', except_reply = 'yes')
	elif run_program ==6: #auto reply only
		twitter_automator (twitter_account_number = 8, theme = the_theme, reply_only = 'yes', tag3 = 'yes') 
	elif run_program ==7: #print reply only
		twitter_automator (twitter_account_number = 8, printreply_eg = 'yes', tag3 = "no")
	elif run_program ==8: #block 1 page only
		twitter_blocker(theme = the_theme)
	elif run_program ==9: # 1 account only
		twitter_blocker(twitter_account_number = 11, theme = the_theme, auto = 'yes', looptimes = 0)
# RUN_OTHER_PROGRAM(5, 'd')
