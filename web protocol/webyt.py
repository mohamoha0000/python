import requests,random,re


def generate_user_agent():
    letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    aa = 'Mozilla/5.0 (Linux; Android 9; Nokia C2 Build/PPR1.180610.011; wv)'
    b = random.randint(6, 12)
    c = 'Android 9; Nokia C2 Build/'
    d = random.choice(letters)
    e = random.randint(1, 999)
    f = random.choice(letters)
    g = 'AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/100.0.4896.79'
    h = random.randint(73, 100)
    i = 0
    j = random.randint(4200, 4900)
    k = random.randint(40, 150)
    l = 'Mobile Safari/537.36[FBAN/EMA;FBLC/en_GB;FBAV/297.0.0.13.113;]'
    full_agent = f"{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}"
    return full_agent


headers = {
                'User-Agent': generate_user_agent(),
                "X-Country": "Morocco",
                "X-Language": "Arabic",
                "Accept-Language": "ar-MA",
                "X-Country-Code": "MA",
            }


url="https://youtu.be/GwThngSl9J0?si=KEf19AjDhW5hkv8j"

m=requests.get(url,headers=headers).text

print(m)