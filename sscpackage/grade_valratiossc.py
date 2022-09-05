import gradesheetprintssc
import itertools

class GradeValRatioSSC(gradesheetprintssc.GradeSheetPrintSSC):
    def __init__(self):
        super().__init__()
        self.gradeprinterdict = {}

    def grade_valratiossc(self, ticker, parsecombo, uniqueid, awardsystem):
        localvalratiodict = parsecombo['valdat']
        valratiopointbook = {}

        for rationame in localvalratiodict.keys():
            pointsper = awardsystem['VALMETRICS'][rationame]['points']
            weightval = awardsystem['VALMETRICS'][rationame]['weight']
            respointrunner = 0

            for recenty, oldery in itertools.pairwise(reversed(localvalratiodict[rationame])):
                listforkey = [rationame, "YEAR", localvalratiodict[rationame].index(recenty),
                              "|", localvalratiodict[rationame].index(oldery)]
                if recenty > oldery:
                    respointrunner += pointsper
                    inlineGVALvar = ">"
                else:
                    inlineGVALvar = "<"

                valforgrade = [recenty, inlineGVALvar, oldery, "POINTS", pointsper]
                self.gradeprinterdict[str(listforkey)] = valforgrade

            valratiopointbook[rationame] = {'Base Points': (pointsper * (len(localvalratiodict)-1))*weightval,
                                            'Current Points': respointrunner*weightval}

        for key, value in valratiopointbook.items():
            print(f'KEY: {key} VALUE: {value}')


        self.setinstancepath(ticker, uniqueid)
        self.setsheetnamesscgr(ticker)
        self.gradeprinterssc(**self.gradeprinterdict)
        self.sectionprinttoexcel()
        self.sectionendprinttoexcel(**valratiopointbook)

if __name__ == "__main__":
    import gradeparsecombinessc
    import awardsystemssc
    testlogvaridssc = 'NVDA__Y8bdxbfeWiliz3B'
    ticker, uniqueid = testlogvaridssc.split("__")
    AWS = awardsystemssc.AwardSystemSSC()
    awardsystempassin = AWS.fetchawardsystem("Industry", "Sector")

    GPSSC = gradeparsecombinessc.GradeParseCombineSSC()
    gradeparsecombo = GPSSC.gradeparsecombinessc(ticker, uniqueid)['NVDA__Y8bdxbfeWiliz3B']

    GVAL = GradeValRatioSSC()
    GVAL.printprimer("INCASRATIO", ticker, uniqueid, "SECTOR", "INDUSTRY")
    GVAL.grade_valratiossc(ticker, gradeparsecombo, uniqueid, awardsystempassin)









