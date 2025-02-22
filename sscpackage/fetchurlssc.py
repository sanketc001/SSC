import os
import shelve


class FetchUrlSSC:
    """
    This class is going to combine variables and pass to FetchCyclerSSC as arguments for 'requests' module
    It will also allow you to add another fetch

    #3
    """
    setpath_fetchurlssc = r'C:\SSC\SimpleStockChecker_REV1\sscpackage\storage'

    def __init__(self, ticker, pathnamefetchurls=
    setpath_fetchurlssc + r"\fetchurlshelfdb",
                 pathbakssc=setpath_fetchurlssc + r"\fetchurlshelfdb.bak",
                 pathdatssc=setpath_fetchurlssc + r"\fetchurlshelfdb.dat",
                 pathdirssc=setpath_fetchurlssc + r"\fetchurlshelfdb.dir",
                 shelfkey="fetchbank", *args, **kwargs):
        self.ticker = ticker
        self.pathbakssc = pathbakssc
        self.pathdatssc = pathdatssc
        self.pathdirssc = pathdirssc
        self.pathnamefetchurls = pathnamefetchurls
        self.shelfkey = shelfkey

    def firstcreate_fetchurlssc(self):
        with shelve.open(self.pathnamefetchurls) as shelvefetch:
            shelvefetch.close()

    def checkpaths(self):
        try:
            fetchpaths = [self.pathbakssc, self.pathdatssc, self.pathdirssc]
            count = 0
            for path in fetchpaths:
                if os.path.exists(path):
                    count += 1

            if count == 3:
                return True
            else:
                self.firstcreate_fetchurlssc()
                self.checkpaths()
        except Exception as er:
            print("Exception in FetchUrlSSC: method 'checkpaths'")
            print(er)

    def purge_fetchurlshelf(self):
        try:
            with shelve.open(self.pathnamefetchurls) as pfs:
                if pfs.keys():
                    for entry in pfs.keys():
                        del pfs[entry]
                    if pfs.keys():
                        return 1
                    else:
                        return 0
        except Exception as er:
            print("Exception in FetchUrlSSC: method 'purge_fetchurlshelf'")

    def fetchshelfinitialize(self):
        try:
            if self.checkpaths():
                self.purge_fetchurlshelf()
                # These are variables holding the API locations for the information calls
                url_income = "https://stock-market-data.p.rapidapi.com/stock/financials/income-statement/annual-historical"
                url_balance = "https://stock-market-data.p.rapidapi.com/stock/financials/balance-sheet/annual-historical"
                url_ar = "https://yh-finance.p.rapidapi.com/stock/v2/get-upgrades-downgrades"
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
                    'x-rapidapi-host': "yh-finance.p.rapidapi.com",
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
        except Exception as er:
            print("Exception in FetchUrlSSC:")
            print(er)

    def addfetchssc(self, addfetchnamessc="DEFAULTNAME", fetchurlssc="DEFAULTURL", fetchqsssc="DEFAULTSSC",
                    fetchheadersssc="DEFAULTHEADER", *args, **kwargs):
        try:
            self.addfetchnamessc = addfetchnamessc
            with shelve.open(self.pathnamefetchurls) as fetchshelf:
                temp_bankadd = dict(fetchshelf[self.shelfkey])
                temp_bankadd.update({addfetchnamessc: {"url": fetchurlssc, "qs": fetchqsssc, "headers": fetchheadersssc}})
                fetchshelf[self.shelfkey] = temp_bankadd
                fetchshelf.close()
        except Exception as er:
            print("Exception in FetchUrlSSC: method 'addfetchssc' ")
            print(er)

    def deletefetchssc(self, delfetchnamessc="DEFAULTNAME", *args, **kwargs):
        try:
            self.delfetchnamessc = delfetchnamessc
            with shelve.open(self.pathnamefetchurls) as fetchshelfdel:
                temp_bankdel = dict(fetchshelfdel[self.shelfkey])
                temp_bankdel.pop(delfetchnamessc)
                fetchshelfdel[self.shelfkey] = temp_bankdel
                fetchshelfdel.close()
        except Exception as er:
            print("Exception in FetchUrlSSC: method 'deletefetchssc' ")
            print(er)

    def pullfetchshelf(self, fetchurlshelfnamessc="fetchurlshelfdb", *args, **kwargs):
        try:
            self.fetchshelfinitialize()
            with shelve.open(self.pathnamefetchurls) as fetchshelfpullssc:
                if dict(fetchshelfpullssc[self.shelfkey]):
                    bank = dict(fetchshelfpullssc[self.shelfkey])
                    fetchshelfpullssc.close()
                    return bank
                else:
                    print("error in pullfetchshelf")
        except Exception as er:
            print("Exception in FetchUrlSSC: method 'pullfetchshelf' ")
            print(er)

    def checkshelfcontent(self):
        try:
            with shelve.open(self.pathnamefetchurls) as fetchshelfcheck:
                if fetchshelfcheck:
                    return True
                else:
                    return False
        except Exception as er:
            print("Exception in FetchUrlSSC: method 'checkshelfcontent' ")
            print(er)

    def clearfetchshelfssc(self) -> None:
        try:
            if self.checkpaths():
                with shelve.open(self.pathnamefetchurls) as fetchshelf:
                    for key in fetchshelf.keys():
                        del fetchshelf[key]
                    fetchshelf.close()
        except Exception as er:
            print("Exception in FetchUrlSSC: method 'clearfetchshelfssc' ")
            print(er)


if __name__ == '__main__':
    FS1 = FetchUrlSSC("MSFT")
    FS1.clearfetchshelfssc()
