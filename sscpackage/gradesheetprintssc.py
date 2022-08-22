"""
Superclass - adding data to Grade Sheet method
"""
import pandas
import datetime

class GradeSheetPrintSSC():
    def __init__(self):
        self.gradesheetprinterprimer = {}
        self.gradesheetprinter = {}
        self.permpathtoexcelssc = r'C:\SSC\SimpleStockChecker_REV1\sscpackage\storage\excelstorage\\'

    def printprimer(self, sectionname, ticker, uniquerunid, sectorssc, industryssc):
        curdatessc = datetime.datetime.today().strftime("%d_%m_%y")
        self.gradesheetprinterprimer.update({"Ticker": str(ticker), "Unique Run ID": uniquerunid,
                                             "Sector": sectorssc, "Industry": industryssc,
                                             "Date / Time": datetime.datetime.today().strftime("%d-%m%y  %H:%M:%S"),
                                             "Section": str(sectionname)})
        localdfssc = pandas.DataFrame(self.gradesheetprinterprimer)
        gradeprimepathssc = self.permpathtoexcelssc + '__' + str(ticker) + '__' + str(uniquerunid)
        with pandas.ExcelWriter(path=gradeprimepathssc, mode='w') as exwssc:
            localdfssc.to_excel(exwssc, sheet_name=str(ticker) + '__' + str(curdatessc))


    def gradeprinterssc(self, **kwargs):
        self.gradesheetprinter.update(kwargs)

