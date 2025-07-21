import requests
import time
import json


def save_progress(current_index):
    with open("progress.json", "w") as f:
        json.dump({"last_index": current_index}, f)


def load_progress():
    try:
        with open("progress.json", "r") as f:
            data = json.load(f)
            return data.get("last_index", 0)
    except FileNotFoundError:
        return 0


def load_accounts():
    encodings = ['utf-8', 'latin-1', 'cp1252', 'ascii']
    
    for encoding in encodings:
        try:
            with open("combo.txt", "r", encoding=encoding) as f:
                accounts = []
                for line in f:
                    if ':' in line:
                        username, password = line.strip().split(':', 1)
                        accounts.append({"username": username, "password": password})
                return accounts
        except UnicodeDecodeError:
            continue
        except FileNotFoundError:
            print("[-] dosya bulunamadı!")
            return []
    
    print("[-] Dosya hiçbir encoding ile okunamadı!")
    return []


def roblox():
    r = requests.session()
    accounts = load_accounts()
    
    if not accounts:
        print("[-] Kontrol edilecek hesap bulunamadı!")
        return
        
    i = load_progress()
    total = len(accounts)
    print(f"[*] {total} hesap kontrol edilecek")
    print(f"[*] {i}. indexten devam ediliyor")
    
    while i < total:
        account = accounts[i]
        try:
            print(f"\n[*] Kontrol ediliyor: {account['username']} ({i+1}/{total})")
            user = r.get(f"https://users.roblox.com/v1/users/search?keyword={account['username']}", 
                        headers = {
                            "cookie": "GuestData=UserID=-90915057; RBXSource=rbx_acquisition_time=05/23/2025 15:16:28&rbx_acquisition_referrer=&rbx_medium=Social&rbx_source=&rbx_campaign=&rbx_adgroup=&rbx_keyword=&rbx_matchtype=&rbx_send_info=0; _ga=GA1.1.1127504397.1745154437; _ga_9HRYHVCY79=GS2.1.s1748111605$o3$g1$t1748112218$j0$l0$h0; __utmc=200924205; rbxas=2427cfefcb50a5b6efbfe8be95a7db49dad7802aea42af70d489fc495ae87ff6; RBXEventTrackerV2=CreateDate=05/25/2025 12:33:51&rbxid=4369092034&browserid=1744302207909001; __utmz=200924205.1748271950.41.3.utmcsr=youtube.com|utmccn=(referral)|utmcmd=referral|utmcct=/; _ga_F8VP9T1NT3=GS2.1.s1749075124$o16$g0$t1749075124$j60$l0$h0; .ROBLOSECURITY=_|WARNING:-DO-NOT-SHARE-THIS.--Sharing-this-will-allow-someone-to-log-in-as-you-and-to-steal-your-ROBUX-and-items.|_GgIQAQ.272B5CBE68E084639E93A27C2E7EA1D7F445487B64F18F6EAD56BEA806B380D29A5480FCDE873D3DD2106F4D5368C35298C3C4D896B20D07D6D480358D6430CA69BB649B17A152BCAB2661B0F1CEBBB237A075764F8C928B818D99F317B661759F73A8768B367D9BE373A0C744BDE37BDF4F9C41223A55D9FAEF28CF4033B0DEC8FEEEE9AC7E5BB5B05FFD79975734C90DCE1A9631F06DDCBC06BA2FF6DEFE00C25339262BBF4E9256C29C82D69A91809B844BA5182C089EF495ABE66AA7DD6871CA25836F910FC9569BD40B97315F4A67167A98A11C95B39605DDEC33C09211A30244224FC6606D9306CE58980B7F27C9F50FA280A63C4BC1A671999C36E88728CEFC58A135288C660CFC3AEFC3EF4F875ECB83179FC2C0BB85089A4EF4DAEE5838A48DB8EDD8F867E6C713BDFCBA372444643D67D6579DABB0FC0D06AAFE6C4E63F019464B4E24B9E5A8B300813A8D393EAEC00EA4B0D86C64AF5A8243D7D0BEEB84B66B3D5C403655C01E6F72BAFDAC6FDEA652E04B76C917864697EC62DDC32EF815DE56AFC4C995FECB7C8D232C0A2E51ED7A3523627DD07035E145D30BDF6405F4E0B3D403D9E90169741E8355952B70A30611BF1FBE514B7AF1F2B9AAB8551552F52BCF300E4C9A4BE7F82F2571FD42CFCF901D6B010132BD65230B367092CF2EB7A9ED2098838A0D2B760470266556CA662BA52C65025258A1C468DF6E21BEA9F5D335F47A33533EC8EB8CB04DC211C16D349D75C134EA107B91500ADC8931D28C79815F170D025288255DE27ABFF36A7F800E0F76EF7CE7BFE526558ABDB8BEEB0B82F84C108928041412B7269ADDF1B5F0FCD9C6B889129F9D2ECA95D6FB77D104112A10FF2E3E6811FFEA8CCBEE92E8E697E6588BB82A68C50710C46850A71F0CE0C7663C9E1C947070178A417E47BA863E5E34E036A5BFCFFDC035AF945600EE5B256EE0F9501ACCA5A47EAA7CC733DDC55D83506396EEF5F2F935E65C8CBBDEFD970544D298118FB642F7E56B7EA31053B2D85129BB8BAD4C977C9BB3D6BC5CB448F12D60281D0B609B1F9FEB5B3C3530593BE1D45702903200DE933CEDB51FA55023B66AB2A5C14C323A449430BBBFC192D1DF5594619829D6C13ED1FC",
                            "priority": "u=0, i",
                            "sec-ch-ua": "\"(Not(A:Brand\";v=\"99\", \"Google Chrome\";v=\"135\", \"Chromium\";v=\"135\"",
                            "sec-ch-ua-full-version-list": "\"(Not(A:Brand\";v=\"99.0.0.0\", \"Google Chrome\";v=\"135\", \"Chromium\";v=\"135\"",
                            "sec-ch-ua-mobile": "?0",
                            "sec-ch-ua-platform": "\"macOS\"",
                            "sec-fetch-dest": "document",
                            "sec-fetch-mode": "navigate",
                            "sec-fetch-site": "none",
                            "sec-fetch-user": "?1",
                            "upgrade-insecure-requests": "1",
                            "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 11_11) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.6785.62 Safari/537.36"
                        })
            
            if "Too many requests" in user.text:
                print(f"[-] Ratelimit'e takıldık, {account['username']} için 60 saniye bekleniyor...")
                save_progress(i)  # hesap konumu
                time.sleep(60)
                continue 
                
            if '{"code":0,"message":""}' in user.text:
                print(f"[-] {account['username']} için ratelimit veya hesap bulunamadı, tekrar deneniyor...")
                time.sleep(30)
                continue 
                
            if "previousUsernames" in user.text:
                id = user.json()["data"][0]["id"]
                print(f"[+] User ID: {id}")
                
                date = r.get(f"https://users.roblox.com/v1/users/{id}", 
                           headers={"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 13.6; rv:137.0) Gecko/20110101 Firefox/137.0"})
                crdate = date.json()["created"]
                
                if any(year in crdate for year in ["2008-", "2009-", "2010-"]):
                    print(f"[+] Eski hesap bulundu! Tarih: {crdate}")
                    with open("roblox.txt", "a", encoding="utf-8") as f:
                        f.write(f"{account['username']}:{account['password']} | ID: {id} | Creation Date: {crdate}\n")
                else:
                    print(f"[-] Yeni hesap. Tarih: {crdate}")
                    
                i += 1
                save_progress(i)
            else:
                print(f"[-] {account['username']} için hesap bulunamadı")
                i += 1 
                save_progress(i)
                
        except Exception as e:
            print(f"[-] Hata oluştu: {str(e)}")
            time.sleep(1)
            continue 

    save_progress(0)
    print("\n[+] Tüm hesaplar kontrol edildi!")

if __name__ == "__main__":
    print("[*] Roblox Date Checker Başlatıldı")
    roblox()