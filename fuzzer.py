''''
Your name:黃靖翔
Student ID:112502515
E-mail:sportsman0170@gmail.com
'''

import args, urllib.request

def fuzz(args):
    """Fuzz a target URL with the command-line arguments specified by ``args``."""
    # your code here...
    text_file = open(args.wordlist, "r")#load file
    lines = text_file.read().splitlines()#split
    text_file.close()
    #print(args)
    for text in lines:
        url = args.url.replace("FUZZ", text)#original url
        try:
            #print(url)
            htmlfile = urllib.request.urlopen(url)#request to server
            code = htmlfile.getcode()#get code
            for match in args.match_codes:#find match in match code
                if code == match:
                    print(str(code) + " " + url)
        except urllib.error.HTTPError as e:#error status code
            for match in args.match_codes:
                if e.code == match:
                    print(str(e.code) + " " + url)
        if len(args.extensions) != 0:#append extension
            for ex in args.extensions:
                try:
                    url2 = url + ex#append
                    htmlfile2 = urllib.request.urlopen(url2)#redo again in original url
                    code2 = htmlfile2.getcode()
                    for match in args.match_codes:
                        if code2 == match:
                            print(str(code2) + " " + url2)
                except urllib.error.HTTPError as e:
                    for match in args.match_codes:
                        if e.code == match:
                            print(str(e.code) + " " + url2)

# do not modify this!
if __name__ == "__main__":
    arguments = args.parse_args()
    fuzz(arguments)
