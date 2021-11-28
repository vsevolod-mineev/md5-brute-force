#usr/bin/python3.9
import time
import itertools, string
import hashlib
import sys
import signal
import re

class md5_cracker(object):

    def __init__(self):
        print("\nWelcome to md5 hash cracker!")

    def signal_handler(self, signal, frame):
        print('You pressed Ctrl+C!')
        self.done=True
        sys.exit(0)

    def _attack(self, chrs, inputt):
        print ("[+] Started at:", time.strftime('%H:%M:%S'))
        start_time = time.time()
        total_pass_try=0
        for n in range(1, 31+1):
            characterstart_time = time.time()
            print("\n[!] Cracking character number", str(n) +str("..."))
        
            for xs in itertools.product(chrs, repeat=n):
                saved = ''.join(xs)
                stringg = saved
                m = hashlib.md5()
                m.update(saved.encode('utf-8'))
                total_pass_try +=1
                if m.hexdigest() == inputt:
                    time.sleep(10)
                    print('[-] Done.')
                    print("\n[!] Found string:", stringg)
                    print("\n[-] Finished at:", time.strftime('%H:%M:%S'))
                    print("\n[-] Total keywords attempted:", total_pass_try)
                    print("\n---Md5 hash cracked in %s seconds---" % (time.time() - start_time))
                    sys.exit("\nThank You!")
            print('[-] Done.')
        print("\n[!]","Character number", n,"has been cracked in %s seconds!" % (time.time() - characterstart_time))

    def main(self):
        inp_usr = input("\nPaste the md5 hash:\n")
        if re.match(r"([a-fA-F\d]{32})", inp_usr):
            print("\nAlphabet:")
            chrs = string.printable.replace(' \t\n\r\x0b\x0c\n', '')
            print(chrs)
            signal.signal(signal.SIGINT, md5_cracker.signal_handler)
            return md5_cracker._attack(self, chrs, inp_usr);
        else:
            print("Error: Input is not an md5 hash.")
            
if __name__ == "__main__":
    md5 = md5_cracker()
    md5.main()
   
   
   
