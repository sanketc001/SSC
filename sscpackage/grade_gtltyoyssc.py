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

        for nameval in self.increasingsections:
            if nameval in localavoidmetricgtltinc:
                """Write the method of calculating with only available data/years combo"""
                continue
            else:
                for yearnumberchrono in range(len(localincdatssc)):
                    pass