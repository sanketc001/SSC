import fetchshelfssc_mod
import fetchlogssc
import parseincomessc
import parsebalancessc
import parsearssc
import parsesectorssc
import parseindssc
import parsevalssc


class ParseStart:
    parse_cancel: bool = False
    parse_runitem: str = ""
    parse_header = "PARSE TICKERS-"

    @staticmethod
    def set_parse_header(arg_head):
        ParseStart.parse_header = str(arg_head)

    @staticmethod
    def pull_parseheader():
        return ParseStart.parse_header

    @staticmethod
    def set_parserun(arg):
        ParseStart.parse_runitem = arg

    @staticmethod
    def parse_canceler():
        print("Parse_Cancel")
        ParseStart.parse_cancel= True
        print(ParseStart.parse_cancel)
    @staticmethod
    def parse_runfetch():
        return ParseStart.parse_runitem

    def ssc_parselogstart(self):
        """
        1. opens log file with stored list of current keys
        2. for loop through list to access fetchstore shelve and pull data
        3. Filter data into respective instance variables for parsing.
        """

        FS_SSC = fetchshelfssc_mod.FetchShelfSSC()
        shelvecopy_fromapi = FS_SSC.fetchdbpull()
        del FS_SSC

        FLOG = fetchlogssc.FetchLogSSC()
        local_logcopy = FLOG.ssc_logfetch()
        del FLOG

        PI_SSC = parseincomessc.ParseIncome()
        PB_SSC = parsebalancessc.ParseBalance()
        PVAL_SSC = parsevalssc.ParseVal()
        PAR_SSC = parsearssc.ParseAr()
        PSEC_SSC = parsesectorssc.ParseSector()
        PIND_SSC = parseindssc.ParseIndustry()


        tag_container = {}
        tag_container["url_income"] = "inctag"
        tag_container["url_balance"] = "baltag"
        tag_container["url_val"] = "valtag"
        tag_container["url_ar"] = "artag"
        tag_container["url_sectordata"] = "sectag"
        def indsec(tag):
            PSEC_SSC.parsesector(tag, shelvecopy_fromapi[tag]),
            PIND_SSC.parseindustry(tag, shelvecopy_fromapi[tag])

        dict_tagswitchboard = {"inctag": lambda logentrylamb:
        PI_SSC.parseincome(logentrylamb, shelvecopy_fromapi[logentrylamb]),

                               "baltag": lambda logentrylamb:
                               PB_SSC.parsebalance(logentrylamb, shelvecopy_fromapi[logentrylamb]),

                               "valtag": lambda logentrylamb:
                               PVAL_SSC.parseval(logentrylamb, shelvecopy_fromapi[logentrylamb]),

                               "artag": lambda logentrylamb:
                               PAR_SSC.parsear(logentrylamb, shelvecopy_fromapi[logentrylamb]),

                               "sectag": lambda logentrylamb: indsec(logentrylamb)
                               }

        for logentry in local_logcopy:
            ticker = logentry.split("__")[0]
            ParseStart.set_parserun(ticker)
            if ParseStart.parse_cancel:
                break
            for tag in tag_container.keys():
                if tag in logentry:
                    (dict_tagswitchboard[tag_container[tag]])(logentry)
                    print("ENTRY: TAG - {tag}::::: LOGENTRY - {logentry}::".format(logentry=logentry, tag=tag))
                    break
                else:
                    continue

        del PI_SSC
        del PB_SSC
        del PSEC_SSC
        del PAR_SSC
        del PVAL_SSC
        del PIND_SSC
