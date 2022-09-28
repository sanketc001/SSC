"""
Core fetching logic - with Requests
"""

import asyncio
import datetime
import json
import math
import random
import string
import time

import requests

import sscpackage.fetchshelfssc_mod
import sscpackage.fetchurlssc


def theshuffler(basket, countage):
    while countage > 0:
        random.shuffle(basket)
        countage -= 1


def myownrandom(keylength=10):
    place = 0
    startbasket = string.digits + string.ascii_letters
    binbasket = [str(x) for x in startbasket]
    random.shuffle(binbasket)
    keyresult = ""
    while len(keyresult) < keylength:
        random.shuffle(binbasket)
        if place == 4:
            timestamp = int(math.floor(time.time() * 2000))
            while math.floor(timestamp) > 61:
                today = datetime.date.today()
                timestamp /= int(random.randint(1, int(today.strftime("%d"))))
            keyresult += binbasket[int(math.floor(timestamp))]
            place += 1
            theshuffler(binbasket, timestamp)
        elif place == 7:
            seeder = "GroverDaniellePotterShoeDonlonPennPantsMom"
            add = seeder[random.randint(1, 34)]
            keyresult += add
            place += 1
        else:
            keyresult += binbasket[random.randint(1, 61)]
            place += 1

    return keyresult


class FetchSSC:
    ticker_successlist = ""

    def __init__(self, ticker, *args, **kwargs):
        self.ticker = ticker

    async def rapid_fetch(self, *args, **kwargs):
        timestampidrf = myownrandom(15)
        FetchRF = sscpackage.fetchurlssc.FetchUrlSSC()
        self.url_bank = FetchRF.pullfetchshelf()
        for key in self.url_bank.keys():
            url = self.url_bank[key]["url"]
            qs = self.url_bank[key]["qs"]
            head = self.url_bank[key]["headers"]
            response = requests.request("GET", url=url, headers=head, params=qs)  # Request data
            self.response = response
            if response.status_code == 200:  # If received 'all good' response from API for first request, continue
                print(f'{self.ticker} - fetch success')
                textcast_ssc = response.text
                self.fetch_data = dict(json.loads(textcast_ssc))
                FSSC = sscpackage.fetchshelfssc_mod.FetchShelfSSC(ticker=self.ticker)
                FSSC.fetchstore(key, id(self), self.fetch_data, timestampidfs=timestampidrf)
                self.statusfetch = True
                if key == list(self.url_bank.keys())[-1:]:
                    FetchSSC.ticker_successlist += str(self.ticker)
                FetchSSC.ticker_successlist += str(self.ticker) + ", "
            elif response.status_code == 401:
                print("Invalid API Key - Check User Information")
                self.statusfetch = False
            else:
                print(f'{self.ticker} - failed fetch')
                self.statusfetch = False
            await asyncio.sleep(1)
