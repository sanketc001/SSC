"""
Class combines all parsed data into a dictionary for access by all grading classes.  Instantiated as a
GradeCollectionSSC.attribute
"""
import gradeparsecombinessc
import parsearssc
import parsebalancessc
import parseincomessc
import parseindssc
import parsesectorssc
import parsevalssc
import parseratiocreatessc


class GradeParseCombineSSC:
    def gradeparsecombinessc(self, ticker, logfileidssc):
        PAR = parsearssc.ParseAr()
        PBAL = parsebalancessc.ParseBalance()
        PINC = parseincomessc.ParseIncome()
        PIND = parseindssc.ParseIndustry()
        PSEC = parsesectorssc.ParseSector()
        PVAL = parsevalssc.ParseVal()

        ardat = PAR.fetch_parsear(logfileidssc)
        baldat = PBAL.fetch_parsebalance(logfileidssc)
        incdat = PINC.fetch_parseincome(logfileidssc)
        inddat = PIND.fetch_parseindustry(logfileidssc)
        secdat = PSEC.fetch_parsesector(logfileidssc)
        valdat = PVAL.fetchparseval(logfileidssc)

        del PAR, PBAL, PINC, PIND, PSEC, PVAL

        corekeycombo = ticker + "__" + logfileidssc
        parsecombo = {}

        def incbalqualssc(datadictssc):
            returndictqualssc = {}
            for key in datadictssc.keys():
                templist = []
                for val in range(len(datadictssc[key])):
                    if datadictssc[key][val] != 0:
                        continue
                    else:
                        templist.append(val)
                        continue
                if templist:
                    returndictqualssc[key] = templist
                else:
                    continue

            return returndictqualssc

        baldatqual = incbalqualssc(baldat)
        incdatqual = incbalqualssc(incdat)

        def ratiolisterssc(datadictssc):
            returndictratiossc = {}
            for key in datadictssc.keys():
                returndictratiossc[key] = [datadictssc[key][x] / datadictssc["Total Revenue"][x] for x in
                                           list(range(len(datadictssc["Total Revenue"]))) if not
                                           isinstance(datadictssc[key][x], str)]
            return returndictratiossc

        incasratiodict = ratiolisterssc(incdat)

        PRC = parseratiocreatessc.ParseRatioCreateSSC()
        finratiodict = PRC.parseratiocreatesssc(incomedictssc=incdat, balancedictssc=baldat, incdatqual=incdatqual,
                                                baldatqual=baldatqual)


        parsecombo[corekeycombo] = {"AR": ardat, "baldat": baldat, "incdat": incdat,
                                    "Industry": inddat, "Sector": secdat, "valdat": valdat,
                                    "baldatqual": baldatqual, "incdatqual": incdatqual,
                                    "incasratiodict": incasratiodict, "finratiodict": finratiodict}

        return parsecombo


if __name__ == "__main__":
    testlogvaridssc = 'NVDA__Y8bdxbfeWiliz3B'
