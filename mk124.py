import os,platform
try:
   import requests
except:
   os.system('pip2 install requests')

import requests
bit = platform.architecture()[0]
if bit == '64bit':
    from mk124 import ___JSX__
    __JSX__()
elif bit == '32bit':
    from mk124 import ___JSX__
    __JSX__()
