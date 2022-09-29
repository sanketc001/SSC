import shelve
import fetchlogssc


class FetchShelfSSC:
    """
    Attributes:
        -self.ticker
        -self.fetchstoreshelf
        -self.fetchstorename

    Methods:
        -fetchstore() - stores the fetch data in "fetchfiledb" shelve
        -fetchdbpull() - pulls and returns the shelve "fetchfiledb"
    """
    setpath_fetchshelfssc = r'C:\SSC\SimpleStockChecker_REV1\sscpackage\storage'

    def __init__(self, ticker,
                 fetchstoreshelf=setpath_fetchshelfssc + r"\fetchfiledb"):
        self.ticker = ticker
        self.fetchstoreshelf = fetchstoreshelf
        self.fetchstorename = ""


    def fetchstore(self, key="url_income", idssc="DEFAULTID", fetch_data="DEFAULTDATA", timestampidfs="DEFTSID",
                   *args, **kwargs):
        try:
            filedb = shelve.open(self.fetchstoreshelf)
            fetchstorename = str(self.ticker) + "__" + str(key) + "__" + str(idssc) + "__" + str(timestampidfs)
            filedb[fetchstorename] = fetch_data
            filedb.close()
            self.fetchstorename = fetchstorename
            FS_SSC = fetchlogssc.FetchLogSSC()
            FS_SSC.ssc_fetchlogwrite(self.fetchstorename)
            del FS_SSC
            return fetchstorename
        except Exception as er:
            print("Exception Fetchstore Method:")
            print(er)


    def fetchdbpull(self, *args, **kwargs):
        with shelve.open(self.fetchstoreshelf) as fetchshelf_pull:
            if fetchshelf_pull.keys():
                bank = dict(fetchshelf_pull)
                fetchshelf_pull.close()
                return bank
            else:
                print("Shelf Empty")

    def fetch_shelvepurge(self):
        with shelve.open(self.fetchstoreshelf) as fetchstoreshelf_del:
            if fetchstoreshelf_del.keys():
                for key in fetchstoreshelf_del.keys():
                    del fetchstoreshelf_del[key]
            if fetchstoreshelf_del.keys():
                return 1
            else:
                return 0
