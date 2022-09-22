import time
import datetime as dt
import json
import grade_arssc
import grade_finratiossc
import grade_gtltyoyssc
import grade_gtltratioyoyssc
import awardsystemssc
import storessc
import grade_valratiossc
import grade_finalssc


class GradeCollectionSSC:
    """
    Grade Process
        *Note: Work In Progress
        Different Grading Algorithms
    """

    def __init__(self, ticker, parsecombossc, uniqueidssc):
        self.totalpointsssc = 0
        self.pointsssc = 0
        self.storeclass = storessc.StoreSSC()
        self.ticker = ticker
        self.uniqueidssc = uniqueidssc
        self.parsecombossc = parsecombossc[ticker + "__" + uniqueidssc]
        self.gradesectionone = grade_gtltyoyssc.GTLTYoYSSC()
        self.gradesectiontwo = grade_gtltratioyoyssc.GTLTYoYRatioSSC()
        self.gradesectionthree = grade_valratiossc.GradeValRatioSSC()
        self.gradesectionfour = grade_arssc.GradeArSSC()
        self.gradesectionfive = grade_finratiossc.GradeFinRatioSSC()
        self.finalgrade = grade_finalssc.GradeFinalSSC()
        self.awardsystem = awardsystemssc.AwardSystemSSC().fetchawardsystem(industry=self.parsecombossc["Industry"],
                                                                            sector=self.parsecombossc["Sector"])

    def gradecollectionssc(self):
        pointbin = []
        pointbin.append(self.gradesectionone.gtltmetricsgradessc(self.ticker, self.parsecombossc, self.uniqueidssc,
                                                                 self.awardsystem))

        pointbin.append(self.gradesectionfive.grade_finratiossc(self.ticker, self.parsecombossc, self.uniqueidssc,
                                                                self.awardsystem))

        pointbin.append(self.gradesectiontwo.grade_gtltyoyratiossc(self.ticker, self.parsecombossc, self.uniqueidssc,
                                                                   self.awardsystem))

        pointbin.append(self.gradesectionthree.grade_valratiossc(self.ticker, self.parsecombossc, self.uniqueidssc,
                                                                 self.awardsystem))

        pointbin.append(self.gradesectionfour.grade_arssc(self.ticker, self.parsecombossc, self.uniqueidssc,
                                                          self.awardsystem))

        self.finalgrade.grade_final_ssc(pointbin)
        self.storeclass.db_chksetup()
        pscombo_tojson = json.dumps(self.parsecombossc, skipkeys=False)
        self.storeclass.log_entry(parsecombo=pscombo_tojson,
                                  grade_ssc=str(self.finalgrade.final_grade_ssc), ticker_entry=str(self.ticker))

        return pointbin


if __name__ == "__main__":
    import gradeparsecombinessc

    testbin_tickers = [
        "AAPL__iUQNePAoVeFQIPV",
        "NVDA__HH12TPwnMth9Tet",
        "GME__AlabRmFaJP9IXEH",
        "GE__DRLihsPscNaTz0Q",
        "FORD__VyjP8walEhZzDRh"
    ]

    def mini_collectiontest(testlogvaridssc):
        ticker, uniqueid = testlogvaridssc.split("__")
        GS = gradeparsecombinessc.GradeParseCombineSSC()
        passindict = GS.gradeparsecombinessc(ticker, uniqueid)
        Gcollect = GradeCollectionSSC(ticker, passindict, uniqueid)
        pointvarbinssc = Gcollect.gradecollectionssc()
        print(pointvarbinssc)

    for uniquekey in testbin_tickers:
        mini_collectiontest(uniquekey)
        import gradeparsecombinessc
