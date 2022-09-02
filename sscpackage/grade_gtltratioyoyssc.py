import gradesheetprintssc
import itertools


class GTLTYoYRatioSSC(gradesheetprintssc.GradeSheetPrintSSC):
    def __init__(self):
        super().__init__()
        self.asratioincreasingsections = ["Total Revenue", "Net Income", "Gross Margin", "Operating Margin", "Net Margin",
                                          "Gross Profit", "EBIT", "Operating Income", "Net Income From Continuing Ops",
                                          "Income Before Tax", "Research & Development", "Total Assets", "Retained Earnings"]
        self.asratiodecreasingsections = ["Selling, General & Administrative", "Other Operating Expenses", "Interest Expense",
                                         "Total Operating Expenses", "Cost Of Revenue", "Total Other Income Expense Net"]

    def grade_gtltyoyratiossc(self, ticker, parsecombo, uniqueid, awardsystem):
        runningtotalgtlt = {}
        localawardsectiongtlt = awardsystem['GTLT']
        localratiodict = parsecombo['incasratiodict']


        for rationame in self.asratioincreasingsections:
            pointsper = localawardsectiongtlt[rationame]["Points"]
            for recenty, oldyear in itertools.pairwise(reversed(localratiodict[rationame])):
                respointrunner = 0

                if recenty > oldyear:
                    respointrunner += pointsper
                    inlinesymbol = ">"
                else:
                    inlinesymbol = "<"

                    valueforprint = [str(recenty), inlinesymbol, str(oldyear), "POINTS", str(respointrunner), "POINTVAL",
                                     str(pointsper)]





if __name__ == "__main__":
    pass