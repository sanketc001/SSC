"""
Grade the Income Statements
"""
import grade_gtltyoyssc
import gradesheetprintssc
import itertools

class GTLTYoYSSC(gradesheetprintssc.GradeSheetPrintSSC):
    def __init__(self):
        super().__init__()
        self.sectionname = 'GTLT'
        self.increasingsections = ["Total Revenue", "Net Income", "Gross Margin", "Operating Margin", "Net Margin",
                                   "Gross Profit", "EBIT", "Operating Income", "Net Income From Continuing Ops",
                                   "Income Before Tax", "Research & Development", "Total Assets", "Retained Earnings"]
        self.printerdictssc = {}
        self.gradestore = {}

    def gtltmetricsgradessc(self, ticker, parsecombossc, uniqueidssc, awardsystemssc):
        runningtotalgtlt = {}
        localawardsectiongtlt = awardsystemssc['GTLT']
        localincdatssc = parsecombossc['incdat']
        localbaldatssc = parsecombossc['baldat']
        localavoidmetricgtltinc = parsecombossc["incdatqual"]
        localavoidmetricgtltbal = parsecombossc["baldatqual"]
        runsectorssc = parsecombossc["Sector"]
        runindustryssc = parsecombossc["Industry"]
        self.printprimer(self.sectionname, ticker, uniqueidssc, runsectorssc, runindustryssc)



        def isenoughdatassc(nameval):
            if nameval in localavoidmetricgtltinc.keys():
                inlinecount = len(localavoidmetricgtltinc[nameval])
                if inlinecount >= 2:
                    return nameval, inlinecount, "incdat"
                else:
                    return False
            elif nameval in localavoidmetricgtltbal.keys():
                inlinecount = len(localavoidmetricgtltbal[nameval])
                if inlinecount >= 2:
                    return nameval, inlinecount, "baldat"
                else:
                    return False
            elif nameval in localincdatssc:
                inlinecount = len(localincdatssc[nameval])
                return nameval, inlinecount, "incdat"
            elif nameval in localbaldatssc.keys():
                inlinecount = len(localbaldatssc[nameval])
                return nameval, inlinecount, "baldat"
            else:
                return False

        def increasinggtltssc(nameval, count, statement):
            pointsper = int(localawardsectiongtlt[nameval]["points"])
            weightind = int(localawardsectiongtlt[nameval]["weight"])
            respointrunner = 0
            if statement == "incdat":
                sourcevalsinc = localincdatssc[nameval]
                for oldyear, newyear in itertools.pairwise(reversed(localincdatssc[nameval])):
                    print(newyear)
                    print(oldyear)
                    keyforprint = [nameval, "Year", str(sourcevalsinc.index(newyear)), "|", "Year",
                                   str(sourcevalsinc.index(oldyear))]

                    if newyear > oldyear:
                        respointrunner += pointsper
                        inlinesymbol = ">"
                    else:
                        inlinesymbol = "<"

                    valueforprint = [newyear, inlinesymbol, oldyear, "POINTS", respointrunner, "POINTVAL",
                                     pointsper]

                    self.printerdictssc[str(keyforprint)] = valueforprint

                respointrunner *= weightind
                restotpoints = 1 * (count-1)
                restotpoints *= weightind
                runningtotalgtlt[nameval] = {"Base Points": restotpoints, "Current Points": respointrunner}

            elif statement == "baldat":
                sourcevalsbal = localbaldatssc[nameval]
                for oldyear, newyear in itertools.pairwise(localbaldatssc[nameval]):
                    keyforprint = [nameval, "Year", str(sourcevalsbal.index(newyear)), "|", "Year",
                                   str(sourcevalsbal.index(oldyear))]

                    if newyear > oldyear:
                        respointrunner += pointsper
                        inlinesymbol = ">"
                    else:
                        inlinesymbol = "<"

                    valueforprint = [newyear, inlinesymbol, oldyear, "POINTS", respointrunner, "POINTVAL",
                                     pointsper]

                    self.printerdictssc[str(keyforprint)] = valueforprint

                respointrunner *= weightind
                restotpoints = 1 * (count-1)
                restotpoints *= weightind
                runningtotalgtlt[nameval] = {"Base Points": restotpoints, "Current Points": respointrunner}

            return runningtotalgtlt

        outputstoressc = {}
        for nameval in self.increasingsections:
            if isenoughdatassc(nameval):
                valueholderlist = [*isenoughdatassc(nameval)]
                if len(valueholderlist) == 3:
                    self.gradestore.update(increasinggtltssc(*valueholderlist))
            else:
                continue

        self.gradeprinterssc(**self.printerdictssc)
        self.sectionprinttoexcel()


        return self.sectionendprinttoexcel(**self.gradestore)



if __name__ == "__main__":
    import gradeparsecombinessc
    import awardsystemssc
    testlogvaridssc = 'NVDA__Y8bdxbfeWiliz3B'
    ticker, uniqueid = testlogvaridssc.split("__")
    AWS = awardsystemssc.AwardSystemSSC()
    awardsystempassin = AWS.fetchawardsystem("Industry", "Sector")

    GPSSC = gradeparsecombinessc.GradeParseCombineSSC()
    gradeparsecombo = GPSSC.gradeparsecombinessc(ticker, uniqueid)['NVDA__Y8bdxbfeWiliz3B']

    GTLT = grade_gtltyoyssc.GTLTYoYSSC()
    GTLT.gtltmetricsgradessc(ticker, gradeparsecombo, uniqueid, awardsystempassin)

    # TODO: add testing
