import shelve
import os

class FetchUrlSSC:
    """
    This class is going to combine variables and pass to FetchCyclerSSC as arguments for 'requests' module
    It will also allow you to add another fetch

    #3
    """
    def __init__(self, ticker="MSFT", pathnamefetchurls="fetchurlshelfdb", pathbakssc="fetchurlshelfdb.bak", pathdatssc="fetchurlshelfdb.dat",
                 pathdirssc="fetchurlshelfdb.dir", shelfkey="fetchbank", *args, **kwargs):
        self.ticker = ticker
        self.pathbakssc = pathbakssc
        self.pathdatssc = pathdatssc
        self.pathdirssc = pathdirssc
        self.pathnamefetchurls = pathnamefetchurls
        self.shelfkey = shelfkey


    def checkpaths(self):
        fetchpaths = [self.pathbakssc, self.pathdatssc, self.pathdirssc]
        count = 0
        for path in fetchpaths:
            if os.path.exists(path):
                count += 1

        if count == 3:
            return True
        else:
            return False

    def fetchshelfinitialize(self, ticker="MSFT"):
        self.ticker = ticker
        if self.checkpaths():
            # These are variables holding the API locations for the information calls
            url_income = "https://stock-market-data.p.rapidapi.com/stock/financials/income-statement/annual-historical"
            url_balance = "https://stock-market-data.p.rapidapi.com/stock/financials/balance-sheet/annual-historical"
            url_ar = "https://apidojo-yahoo-finance-v1.p.rapidapi.com/stock/v2/get-upgrades-downgrades"
            url_val = "https://stock-market-data.p.rapidapi.com/stock/valuation/historical-valuation-measures"
            url_sectordata = "https://stock-market-data.p.rapidapi.com/stock/company-info"


            # These are the two variables necessary to ping the API's, first two take qs, url_ar takes 2
            qs_inc_bal = {"ticker_symbol": self.ticker, "format": "json"}
            qs_ar = {"symbol": self.ticker, "region": "US"}
            qs_val = {"ticker_symbol": self.ticker, "format": "json"}
            qs_sector = {"ticker_symbol": self.ticker}

            # header information including RAPI_key environment variable, necessary for API data fetch
            headers = {
                'x-rapidapi-host': "stock-market-data.p.rapidapi.com",
                'x-rapidapi-key': os.getenv("RAPI_key")
            }

            # Header for the _ar request
            headers_ar = {
                'x-rapidapi-host': "apidojo-yahoo-finance-v1.p.rapidapi.com",
                'x-rapidapi-key': os.getenv("RAPI_key")
            }

            # Create and prime shelf with core necessary fetches
            fetchshelf = shelve.open(self.pathnamefetchurls)
            self.fetch_apidict = {"url_income": {"url": url_income, "qs": qs_inc_bal, "headers": headers},
                                  "url_balance": {"url": url_balance, "qs": qs_inc_bal, "headers": headers},
                                  "url_ar": {"url": url_ar, "qs": qs_ar, "headers": headers_ar},
                                  "url_val": {"url": url_val, "qs": qs_val, "headers": headers},
                                  "url_sectordata": {"url": url_sectordata, "qs": qs_sector, "headers": headers}}
            fetchshelf[self.shelfkey] = self.fetch_apidict
            self.fetchbank = fetchshelf[self.shelfkey]
            fetchshelf.close()
        else:
            return 1

    def addfetchssc(self, addfetchnamessc="DEFAULTNAME", fetchurlssc="DEFAULTURL", fetchqsssc="DEFAULTSSC",
                    fetchheadersssc="DEFAULTHEADER", *args, **kwargs):
        self.addfetchnamessc = addfetchnamessc
        with shelve.open(self.pathnamefetchurls) as fetchshelf:
            temp_bankadd = dict(fetchshelf[self.shelfkey])
            temp_bankadd.update({addfetchnamessc: {"url": fetchurlssc, "qs": fetchqsssc, "headers": fetchheadersssc}})
            fetchshelf[self.shelfkey] = temp_bankadd
            fetchshelf.close()

    def deletefetchssc(self, delfetchnamessc="DEFAULTNAME", *args, **kwargs):
        self.delfetchnamessc = delfetchnamessc
        with shelve.open(self.pathnamefetchurls) as fetchshelfdel:
            temp_bankdel = dict(fetchshelfdel[self.shelfkey])
            temp_bankdel.pop(delfetchnamessc)
            fetchshelfdel[self.shelfkey] = temp_bankdel
            fetchshelfdel.close()

    def pullfetchshelf(self, fetchurlshelfnamessc = "fetchurlshelfdb", *args, **kwargs):
        self.fetchshelfinitialize()
        with shelve.open(fetchurlshelfnamessc) as fetchshelfpullssc:
            if fetchshelfpullssc[self.shelfkey]:
                bank = dict(fetchshelfpullssc[self.shelfkey])
                fetchshelfpullssc.close()
                return bank
            else:
                print("error in pullfetchshelf")
                fetchshelfpullssc.close()

    def checkshelfcontent(self, shelfname="fetchurlshelfdb"):
        if self.checkpaths():
            with shelve.open(shelfname) as fetchshelfcheck:
                res = bool(dict(fetchshelfcheck))
                fetchshelfcheck.close()
                if res:
                    return True
                else:
                    return False

    def clearfetchshelfssc(self, path="fetchurlshelfdb"):
        if self.checkpaths():
            with shelve.open(path) as fetchshelf:
                for key in fetchshelf.keys():
                    del fetchshelf[str(key)]
                fetchshelf.close()
