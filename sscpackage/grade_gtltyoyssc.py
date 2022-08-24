"""
Grade the Income Statements
"""

import gradesheetprintssc

class GTLTYoYSSC(gradesheetprintssc.GradeSheetPrintSSC):
    def __init__(self):
        super().__init__()
        self.sectionname = 'GTLT'
        self.increasingsections = ["Total Revenue", "Net Income", "Gross Margin", "Operatng Margin", "Net Margin",
                                   "Gross Profit", "EBIT", "Operating Income", "Net Income From Continuing Ops",
                                   "Income Before Tax", "Research & Development", "Total Assets", "Retained Earnings"]
        self.decreasingsections = ["Selling, General & Administrative", "Other Operating Expenses", "Interest Expense",
                                   "Total Operating Expenses", "Cost Of Revenue", "Total Other Income Expense Net"]

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
                if inlinecount > 2:
                    return False
                else:
                    return True, inlinecount, "incdat"
            elif nameval in localavoidmetricgtltbal.keys():
                inlinecount = len(localavoidmetricgtltbal[nameval])
                if inlinecount > 2:
                    return False
                else:
                    return True, inlinecount, "baldat"
            else:
                return False, False, False

        def increasinggtltssc(nameval, count, statement):
            pointsper, weightind = localawardsectiongtlt[nameval]
            respointrunner = 0
            if statement == "incdat":
                stringerbegin = """
                            {nameval} : Available Years:: {count} ::
                            Category:: {statement}

                            Grade Statements Follow:
                            """.format(nameval=nameval, count=count, statement=statement)
                stringermid = ""
                sourcevalsinc = localincdatssc[nameval]
                for indexno in range(count-1, 0, -1):
                    if sourcevalsinc[indexno-1] > sourcevalsinc[indexno]:
                        stringermid += "\nYear {indexnoplus}: {indexnoplusvalue} is '>' Year {indexnoval}" \
                                             " :: Year {indexno} ---* + {pointsper} Point".format(indexnoplus= indexno-1,
                                                                         indexnoplusvalue=sourcevalsinc[indexno-1],
                                                                         indexnoval=sourcevalsinc[indexno],
                                                                         indexno=indexno,
                                                                         pointsper=pointsper)
                        respointrunner += pointsper
                    else:
                        stringermid += "\nYear {indexnoplus}: {indexnoplusvalue} is '<' Year {indexnoval}" \
                                             " :: Year {indexno} ---* + {pointsper} Point".format(indexnoplus= indexno-1,
                                                                                                  indexnoplusvalue=sourcevalsinc[indexno-1],
                                                                                                  indexnoval=sourcevalsinc[indexno],
                                                                                                  indexno=indexno,
                                                                                                  pointsper=pointsper)
                        continue

                respointrunner *= weightind
                restotpoints = 1 * (count-1)
                restotpoints *= weightind
                stringerend = "End Of Grading Element: {nameval}\nPoints Per Grade Element = {pointsper}\n" \
                              "Total Current Points = {respointrunner} ::: " \
                              "Weight = {weightind}".format(nameval=nameval, pointsper=pointsper, respointrunner=respointrunner, weightind=weightind)
                stringertotal = stringerbegin + stringermid + stringerend
                runningtotalgtlt[nameval] = {"Base Points": restotpoints, "Current Points": respointrunner}
                return stringertotal

            elif statement == "baldat":
                stringerbegin = """
                                            {nameval} : Available Years:: {count} ::
                                            Category:: {statement}

                                            Grade Statements Follow:
                                            """.format(nameval=nameval, count=count, statement=statement)
                stringermid = ""
                sourcevalsbal = localbaldatssc[nameval]
                for indexno in range(count-1, 0, -1):
                    if sourcevalsbal[indexno+1] > sourcevalsbal[indexno]:
                        stringermid += "\nYear {indexnoplus}: {indexnoplusvalue} is '>' Year {indexnoval}" \
                                       " :: Year {indexno} ---* + {pointsper} Point".format(indexnoplus= indexno-1,
                                                                                            indexnoplusvalue=sourcevalsbal[indexno-1],
                                                                                            indexnoval=sourcevalsbal[indexno],
                                                                                            indexno=indexno,
                                                                                            pointsper=pointsper)
                        respointrunner += pointsper
                    else:
                        stringermid += "\nYear {indexnoplus}: {indexnoplusvalue} is '<' Year {indexnoval}" \
                                       " :: Year {indexno} ---* + {pointsper} Point".format(indexnoplus=indexno - 1,
                                                                                            indexnoplusvalue=
                                                                                            sourcevalsbal[indexno - 1],
                                                                                            indexnoval=sourcevalsbal[
                                                                                                indexno],
                                                                                            indexno=indexno,
                                                                                            pointsper=pointsper)
                        continue

                respointrunner *= weightind
                restotpoints = 1 * (count-1)
                restotpoints *= weightind
                stringerend = "End Of Grading Element: {nameval}\nPoints Per Grade Element = {pointsper}\n" \
                              "Total Current Points = {respointrunner} ::: " \
                              "Weight = {weightind}".format(nameval=nameval, pointsper=pointsper, respointrunner=respointrunner, weightind=weightind)
                stringertotal = stringerbegin + stringermid + stringerend
                runningtotalgtlt[nameval] = {"Base Points": restotpoints, "Current Points": respointrunner}
                return stringertotal

        for nameval in self.increasingsections:
            valueholderlist = []
            valueholderlist.append(isenoughdatassc(nameval))
            if len(valueholderlist) == 3:
                increasinggtltssc(*valueholderlist)

