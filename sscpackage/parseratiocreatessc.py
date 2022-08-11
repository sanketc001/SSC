"""
Create 'hand-made' list of ratios from income statements and balance sheet elements, e.g. "Current Ratio"
"""
import gradeparsecombinessc

class ParseRatioCreateSSC:
    def parseratiocreatesssc(self, incomedictssc, balancedictssc, incdatqual, baldatqual):

        dictratiossclamb = {
            "Current Ratio": lambda totalcurrentassetsx, totalcurrentliabilitiesy:
            totalcurrentassetsx / totalcurrentliabilitiesy,
            "Acid Test Ratio": lambda totalcurrentassetsx, inventoryy, totalcurrentliabilitiesz:
            (totalcurrentassetsx - inventoryy) / totalcurrentliabilitiesz,
            "Cash Ratio": lambda cashx, totalcurrentliabilitiesy: cashx / totalcurrentliabilitiesy,
            "Debt Ratio": lambda totalliabilitiesx, totalassetsy: totalliabilitiesx / totalassetsy,
            "Debt To Equity Ratio": lambda totalstockholderequity, totalliabilities:
            totalliabilities / totalstockholderequity,
            "Operating Cash Flow": lambda operatingincome, interestexpense: operatingincome / interestexpense,
            "Interest Coverage Ratio": lambda netincome, totalassets: netincome / totalassets,
            "Return On Assets Ratio": lambda totalstockholderequity, netincome:
            netincome / totalstockholderequity,
            "Book Value Per Share": lambda treasurystock, otherstockholderquity, totalstockholderquity, commonstock:
            (totalstockholderquity - treasurystock - otherstockholderquity) / commonstock,
        }

        dictratiosscverbal = {
            "Current Ratio": ["Total Current Assets", "Total Current Liabilities"],
            "Acid Test Ratio": ["]Total Current Assets", "Inventory", "Total Current Liabilities"],
            "Cash Ratio": ["Cash", "Total Current Liabilities"],
            "Debt Ratio": ["Total Liabilities", "Total Assets"],
            "Debt To Equity Ratio": ["Total Stockholder Equity", "Total Liabilities"],
            "Operating Cash Flow": ["Operating Income", "Interest Expense"],
            "Interest Coverage Ratio": ["Net Income", "Total Assets"],
            "Return On Assets Ratio": ["Total Stockholder Equity", "Net Income"],
            "Book Value Per Share": ["Treasury Stock", "Other Stockholder Equity", "Total Stockholder Equity",
                                     "Common Stock"],
        }

        for key in dictratiossclamb.keys():
            calctempdict = {}
            calctemplist = []
            varnamepulltemplist = {}
            flag = False
            for varname in dictratiosscverbal[key]:
                if varname in incomedictssc.keys():
                    datatemplistssc = incomedictssc[varname]
                    if incdatqual[varname]:
                        qualtemplistssc = incdatqual[varname]
                        varnamepulltemplist[varname]: [datatemplistssc, qualtemplistssc]
                        flag = True
                        continue
                    else:
                        varnamepulltemplist[varname]: [datatemplistssc]
                        continue
                elif varname in balancedictssc.keys():
                    datatempballistssc = balancedictssc[varname]

                    if baldatqual[varname]:
                        qualbaltemplistssc = baldatqual[varname]
                        varnamepulltemplist[varname]: [datatempballistssc, qualbaltemplistssc]
                        flag = True
                        continue
                    else:
                        varnamepulltemplist[varname]: [datatempballistssc]
            for varname in dictratiosscverbal:
                if flag:
                    calctempdict[varname] = list(map(dictratiossclamb[varname], ))


if __name__ == "__main__":
