"""
Create 'hand-made' list of ratios from income statements and balance sheet elements, e.g. "Current Ratio"
"""


class ParseRatioCreateSSC:
    def parseratiocreatesssc(self, incomedictssc, balancedictssc, incdatqual, baldatqual):
        try:
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
                "Acid Test Ratio": ["Total Current Assets", "Inventory", "Total Current Liabilities"],
                "Cash Ratio": ["Cash", "Total Current Liabilities"],
                "Debt Ratio": ["Total Liabilities", "Total Assets"],
                "Debt To Equity Ratio": ["Total Stockholder Equity", "Total Liabilities"],
                "Operating Cash Flow": ["Operating Income", "Interest Expense"],
                "Interest Coverage Ratio": ["Net Income", "Total Assets"],
                "Return On Assets Ratio": ["Total Stockholder Equity", "Net Income"],
                "Book Value Per Share": ["Treasury Stock", "Other Stockholder Equity", "Total Stockholder Equity",
                                         "Common Stock"],
            }

            finalratiodictssc = {}
            interimratiodictssc = {}

            varnamepulltemplist = {}
            for key in dictratiossclamb.keys():
                calctemplistforzipper = []
                for varname in dictratiosscverbal[key]:
                    if varname in incomedictssc.keys():
                        datatemplistssc = incomedictssc[varname]
                        if varname in incdatqual.keys():
                            qualtemplistssc = incdatqual[varname]
                            varnamepulltemplist[str(varname)] = [datatemplistssc, qualtemplistssc]
                            calctemplistforzipper.append(varnamepulltemplist[varname])
                            continue
                        else:
                            varnamepulltemplist[str(varname)] = [datatemplistssc]
                            calctemplistforzipper.append(datatemplistssc)
                            continue
                    elif varname in balancedictssc.keys():
                        datatempballistssc = balancedictssc[varname]
                        if varname in baldatqual.keys():
                            qualbaltemplistssc = baldatqual[varname]
                            calctemplistforzipper.append([datatempballistssc, qualbaltemplistssc])
                            varnamepulltemplist[str(varname)] = [datatempballistssc, qualbaltemplistssc]
                            continue
                        else:
                            varnamepulltemplist[str(varname)] = [datatempballistssc]
                            calctemplistforzipper.append(list(datatempballistssc))
                            continue
                interimratiodictssc[key] = calctemplistforzipper

            for ratio in dictratiossclamb.keys():
                resssc = []
                for iteration in list(zip(*interimratiodictssc[ratio])):
                    resssc.append(dictratiossclamb[ratio](*iteration))
                finalratiodictssc[ratio] = resssc

            return finalratiodictssc
        except Exception as er:
            print("Exception in ParseRatioSSC: method 'parseratiocreatessc' ")
            print(er)

if __name__ == "__main__":
    import gradeparsecombinessc

    ticker = 'NVDA'
    logidssc = 'Y8bdxbfeWiliz3B'
    GS = gradeparsecombinessc.GradeParseCombineSSC()
    parsecombo = GS.gradeparsecombinessc(ticker, logidssc)['NVDA__Y8bdxbfeWiliz3B']
    PS = ParseRatioCreateSSC()
    incomedictssc = parsecombo["incdat"]
    balancedictssc = parsecombo["baldat"]
    incqualdat = parsecombo["incdatqual"]
    baldatqual = parsecombo["baldatqual"]
    restestssc = PS.parseratiocreatesssc(incomedictssc=incomedictssc, balancedictssc=balancedictssc,
                                         incdatqual=incqualdat, baldatqual=baldatqual)
