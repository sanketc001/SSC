"""
Class combines all parsed data into a dictionary for access by all grading classes.  Instatiated as a
GradeCollectionSSC.attribute
"""
import parsearssc
import parsebalancessc
import parseincomessc
import parseindssc
import parsesectorssc
import parsevalssc

class GradeParseCombineSSC():
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
            returndictqualssc = []
            for key in datadictssc.keys():
                for val in datadictssc[key]:
                    if val != 0:
                        continue
                    else:
                        returndictqualssc.append({str(key) + " " + str(datadictssc[key].index(val)):
                                                  str(datadictssc[key].index(val))})
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


        parsecombo[corekeycombo] = {"AR": ardat, "baldat": baldat, "incdat": incdat,
                                    "Industry": inddat, "Sector": secdat, "valdat": valdat,
                                    "baldatqual": baldatqual, "incdatqual": incdatqual,
                                    "incasratiodict": incasratiodict}

        return parsecombo





