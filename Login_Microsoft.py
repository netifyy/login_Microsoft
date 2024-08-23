_ = '''
==============
[×] Name : Netify
[×] https://t.me/nev_bb
[×] country : America
==============
'''; print(_)
import requests
import os
import random
import string
import sys
from random import choice 

class hotmail:
    def __init__(self):
    	self.n = 'tyle type="text/css" nonce="jMUilehw7U5SAoKIlWC4OHTXKCoiQ6gr+IuwzEWAlpg=">body{display:block !important;}</style'
    	    	
    	self.unqi = 'Reload Success",c.Load(null,function(){if(o)throw"Unexpected state. ResourceLoader.Load() failed despite initial load success. ['+self.n+']'    	
    	
    	self.nm = 'iDefaultLoginOptions:3,serverDetails:{"ri":"SN1PEPF0002F16B","ver":"16.0.30324.2"},oGetCredTypeResult:null,fRemoveMinWidthFromLightBox:true,urlResetPasswor['+self.unqi+']'
    	
    	response = requests.get('https://login.live.com/ppsecure/post.srf')    	
    	cookies = response.cookies.get_dict()
    	try:
    		self.MSPOK = cookies.get('MSPOK')    	
    		self.OParams = cookies.get('OParams')
    		self.uaid = cookies.get('uaid')    	
    	except:
    		self.MSPOK = None 
    		self.OParams = None
    		self.uaid = None
    	
    	    	

    def send_request(self):       
        email = input(" Email : ")
        password = input(' Passowrd : ')
        try:
            headers = {
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
                "Accept-Encoding": "gzip, deflate, br",
                "Accept-Language": "ar-IQ,ar;q=0.9,en-US;q=0.8,en;q=0.7",
                "Cache-Control": "max-age=0",
                "Connection": "keep-alive",
                "Content-Length": "621",
                "Content-Type": "application/x-www-form-urlencoded",    
                "Host": "login.live.com",
                "Origin": "https://login.live.com",
                "Referer": "https://login.live.com/login.srf?wa=wsignin1.0&rpsnv="+self.nm+"&id=292841&aadredir=1&CBCXT=out&lw=1&fl=dob%2cflname%2cwld&cobrandid="+self.uaid+"",
                "Sec-Ch-Ua": "\"Not-A.Brand\";v=\"99\", \"Chromium\";v=\"124\"",
                "Sec-Ch-Ua-Mobile": "?1",
                "Sec-Ch-Ua-Platform": "\"Android\"",
                "Sec-Fetch-Dest": "document",
                "Sec-Fetch-Mode": "navigate",
                "Sec-Fetch-Site": "same-origin",
                "Sec-Fetch-User": "?1",
                "Upgrade-Insecure-Requests": "1",
                "User-Agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36",
               "Cookie": ";;;;OParams=11O.Do2OlvbVOR6dJTaCA4t56v2uUnLAHyOIRCo5C0m70hU*G4Mf9lwmiKzs1OeBMhh8IT8jgtjTEFhBvneYPHsgWIlIT5KuOpOiyQ23ZLOD1eoCXr7wuONgh3!AAQ7sEzgrzaRCRkr5b83*L9I88YwR!8*DlWWSFlGYuuDq8xyzugEQd*Vq1VL12q*ZgCDqlZNUL*Hyz!wLMaOOK*bMDzWtOZd1E1yFChk4PtzgwDp8gOgFLXGMF1hSGLiuo9RRRqho*oPs9weKKtQMUrPgwDegLXJqp7OsivtPZLHhjLzGVm*RL2vvO5rcLcxu2bMAFjE2k4smot2v*Twb4jcYpDdKqXGzd9WxidpqVNOOe4s0EDXvRuVCTBaPxv0t0U4AZpwCxl4uI21JaHMVmJj4ZgOU75YT4Ai38K9sG8xXAibVsomSArp5v20qWu9JzDhjwdk08TqXzeRMWJ4ILsfWh*Wz5y7EHTkS2AIEo!njy46Cd0zjeChaO9iepJ9AqoW6q7Fs2pGHxlKRlXuoAH**Zs4U0DC*aqDA8G2KpA5A8mUIwrBYozCYTy3XnOVrxSpeYxsFi6xO86TmRezBfELXAMmSwN3HQGW6CZfLITTX16v9YEsxy!nw9STzi*iwJhxy4lStFJbLn8TPVnygCcGKwcCnwu6EnOgbpr2Y59IVZusv!83zM8PXBxNF4DWsJgCL1XymE1jElHJjo645i3DrlO5AIR4$; ai_session=IV21GCZ30Ka8N2hOEuMuyV|1724409422603|1724409471041; MSPOK="+self.MSPOK+"$"+self.MSPOK+"$"+self.MSPOK+"$"+self.MSPOK+"$uuid-b3ece3c9-cd30-4246-a5c4-c30a7073cd2a$uuid-47caa828-09a2-4219-afa6-cc032a109e12",


            }

            params = "cobrandid=ab0455a0-8d03-46b9-b18b-df2f57b9e44c&id=292841&contextid=98AA1AA62BCD4D2E&opid=B3501D91C4A71F73&bk=1724409468&uaid="+self.uaid+"&pid=0"
            data="ps=2&psRNGCDefaultType=psRNGCEntropy=&psRNGCSLK=&canary=&ctx=&hpgrequestid=&PPFT=-Dv*Wscxw1CcWL0rMrudpAZqkuu0u97DfeQ8Vl%21D%21boc*6DgUFNVF19jh4TggbDTuZdKBa5oCTDpnPGSj7yg42JpZZjHE3iAA4ROHdz1gMv5vYAw%21%21ezRqM*tSufu92wjH*WdC7TyJHFJoLit%21hZkD0TkZwwulJkxj7hVcXzNDz5Nglk0Th0*DNuO4YiaikFWomHhOIcay0Bd4eUvheZRFI9KSk740QWJa1WHHHgAbKQnR0*rHSOzIJaeVCWXuO98eA%24%24&PPSX=Passpo&NewUser=1&FoundMSAs=&fspost=0&i21=0&CookieDisclosure=0&IsFidoSupported=1&isSignupPost=0&isRecoveryAttemptPost=0&i13=0&login="+email+"&loginfmt="+email+"&type=11&LoginOptions=3&lrt=lrtPartition=&hisRegion=&hisScaleUnit=&passwd="+password+""
            
            response = requests.get('https://login.live.com/ppsecure/post.srf', params=params, headers=headers, data=data).text
         
            if "fmHF" in response:            
                print("Done Login")                                                    
            else:
                print('bad Login')

        except Exception as e:
            print(f" {e}")

if __name__ == "__main__":
    while True:
        fb = hotmail()
        fb.send_request()