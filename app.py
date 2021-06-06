import requests
from os import path
import sys
import argparse

#argparse choices 

parser = argparse.ArgumentParser()
parser.add_argument('-t', '--target', help = 'select the domain to search')
parser = parser.parse_args()

#main function

def main():
    # parser + optiont target 
    if parser.target:
        if path.exists('subdominios.txt'):
            # open the file subdominio.txt
            wordlist = open('subdominios.txt', 'r')
            # we read the file and convert the variable in a list , splite in 'jump lines'
            wordlist = wordlist.read().split('\n')
            
            # go through the list when the protocol is http>>
            for s in wordlist:
                url = 'http://'+s+'.'+parser.target
                try:
                    # check the page is working
                    requests.get(url)
                except requests.ConnectionError:
                    pass
                else:
                    #print the subdomain founded
                    print('(+) Subdomain found  '+url)
                    
            # go through the list when the protocol is https>>
            for s in wordlist:
                url = 'https://'+s+'.'+parser.target
                try:
                    # check the page is working
                    requests.get(url)
                except requests.ConnectionError:
                    pass
                else:
                    #print the subdomain founded
                    print('(+) Subdomain found  '+url)
    else:
        # not select a target option
        print('please select a valid subdomain')

        sys.exit()



if __name__ == '__main__':
    try: 
        main()
    except KeyboardInterrupt:
        sys.exit()

