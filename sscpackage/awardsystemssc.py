"""
This class is going to house the point award system
"""
import shelverssc

class AwardSystemSSC(shelverssc.ShelverSSC):
    def __init__(self, shelvename: 'str' = "awardsystemssc"):
        super().__init__(shelvename)
        self.permstorpathssc = r'C:\SSC\SimpleStockChecker_REV1\sscpackage\storage\\'
        self.awardsystemcontainerssc = {}

    def deleteawardsystem(self, keynamedel):
        self.del_shelvecoreelementssc(self.shelvename, keynamedel)





    def awardsystemsprimer(self):
        defaultawardnamessc = "DEFAULT"

        if self.fetchpeek(self.permstorpathssc + self.shelvename, defaultawardnamessc):
            return 1
        else:

            temp_sscaward = {}
            awardsystemdict = {}

            #Greater Than Less Than Metrics
            defaultgtltmetrics_ssc = ["Total Revenue", "Net Income", "Gross Margin", "Operating Margin", "Net Margin",
                               "Gross Profit", "EBIT", "Operating Income", "Net Income From Continuing Ops",
                               "Income Before Tax", "Research & Development", "Selling, General & Administrative",
                               "Other Operating Expenses", "Interest Expense", "Total Operating Expenses",
                               "Cost Of Revenue", "Total Other Income Expense Net", "Total Assets", "Retained Earnings"]

            for metric in defaultgtltmetrics_ssc:
                temp_sscaward[metric] = {"points": 1, "weight": 1}

            awardsystemdict["GTLT"] = temp_sscaward

            #FINRATIO METRICS
            temp_sscaward = {}
            defaultfinratiosscmetrics = ["Current Ratio", "Acid Test Ratio", "Cash Ratio", "Debt Ratio", "Debt To Equity Ratio",
                                         "Operating Cash Flow", "Interest Coverage Ratio", "Return On Assets Ratio",
                                         "Book Value Per Share"]

            for metric in defaultfinratiosscmetrics:
                temp_sscaward[metric] = {"pointsgood": 1, "pointsneutral": .5, "pointsbad": 0, "weight": 1}

            awardsystemdict["FINRATIOS"] = temp_sscaward

            #INCASRATIO Metrics
            temp_sscaward = {}
            defincasratiometrics = ["Total Revenue", "Net Income", "Gross Margin", "Operating Margin",
                                              "Net Margin",
                                              "Gross Profit", "EBIT", "Operating Income",
                                              "Net Income From Continuing Ops",
                                              "Income Before Tax", "Research & Development",
                                              "Selling, General & Administrative",
                                              "Other Operating Expenses",
                                              "Interest Expense",
                                              "Total Operating Expenses", "Cost Of Revenue",
                                              "Total Other Income Expense Net"]

            for metric in defincasratiometrics:
                temp_sscaward[metric] = {"points": 1, "weight":1}

            awardsystemdict["INCASRATIO"] = temp_sscaward

            #VALDATA Metrics
            temp_sscaward = {}
            defaultvaldatametrics = ["Market Cap (intraday)", "Enterprise Value", "Trailing P/E", "Forward P/E",
                                     "PEG Ratio (5 yr expected)", "Price/Sales (ttm)", "Price/Book (mrq)",
                                     "Enterprise Value/Revenue", "Enterprise Value/EBITDA"]

            for metric in defaultvaldatametrics:
                temp_sscaward[metric] = {"points": 1, "weight": 1}

            awardsystemdict["VALMETRICS"] = temp_sscaward

            #Analyst Grades
            temp_sscaward = {}
            defaultanalystmetricsssc = ["AR-GREAT", "AR-GOOD", "AR-NEUTRAL", "AR-BAD", "AR-WORST"]

            for metric in defaultanalystmetricsssc:
                temp_sscaward[metric] = {"points": 1, "weight": 1}

            awardsystemdict["ARMETRICS"] = temp_sscaward

            self.add_shelvecoreelementssc(self.shelvename, defaultawardnamessc, awardsystemdict)

    def fetchawardsystem(self, industry, sector):
        combokeyindsec = str(industry) + "__" + str(sector)
        if self.inkeys_shelvercorekeysssc(self.shelvename, combokeyindsec):
            return self.pull_shelverssc(self.shelvename, combokeyindsec)
        else:
            return self.pull_shelverssc(self.shelvename, "DEFAULT")

    def addmetricgroupssc(self, awardsystemname_ssc, metricgroupkeyword, data, *args, **kwargs):
        self.add_shelvesubelement(self.shelvename, systemkeywordssc=awardsystemname_ssc,
                                  coremetricssc=metricgroupkeyword, data=data)

# TODO: create separate unittest for awardsystemssc
if __name__ == "__main__":
    AWssc = AwardSystemSSC()
    print(AWssc.awardsystemsprimer())
    print(AWssc.fetchawardsystem("Aeurnautics", "Infrastructure"))
