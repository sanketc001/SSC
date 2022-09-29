import shelve

import dictpullssc
import fetchshelfssc_mod


class ParseAr:
    """
    Process raw JSON data for upgrades-downgrades for grading algorithm
    """

    def __init__(self):
        self.setpathssc_parsesscar = r"C:\SSC\SimpleStockChecker_REV1\sscpackage\storage\parsearshelf"


    def purge_parsear(self):
        with shelve.open(self.setpathssc_parsesscar) as purge_parse:
            if purge_parse.keys():
                for item in purge_parse.keys():
                    del purge_parse[item]
                if purge_parse.keys():
                    return 1
                else:
                    return 0

    def parsear(self, uniquename, par_rawdata):
        try:
            uniquesplitlist = uniquename.split("__")
            ticker, key, idssc, timestampidar = uniquesplitlist[0], uniquesplitlist[1], uniquesplitlist[2], \
                                                uniquesplitlist[3]
            DPssc = dictpullssc.DictPullSSC()
            ardict = DPssc.dictpullssc(par_rawdata, "history")

            FST_SSC = fetchshelfssc_mod.FetchShelfSSC(ticker=ticker, fetchstoreshelf=self.setpathssc_parsesscar)
            FST_SSC.fetchstore(key=key, idssc=idssc, fetch_data=ardict, timestampidfs=timestampidar)
            del FST_SSC
        except Exception as Er:
            print("Exception in parsearssc.ParseAr.parsear")
            print(Er)

    def fetch_parsear(self, timestampidar):
        try:
            with shelve.open(self.setpathssc_parsesscar) as pibank:
                # TODO: look into this, maybe change looping structure, timestamidar in pibank.keys(), no for loop
                for key in pibank.keys():
                    if timestampidar in key:
                        pushdata = pibank[key]
                    else:
                        continue
                return pushdata

        except Exception as Er:
            print("Exception: 'fetch_parsebalance'\n")
            print(Er)
