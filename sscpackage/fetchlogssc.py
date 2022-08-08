class FetchLogSSC:
    def __init__(self):
        self.fetchlogpath = r'C:\SSC\SimpleStockChecker_REV1\sscpackage\storage\fetchlog.txt'

    def ssc_fetchlogwrite(self, fetchstorename):
        with open(self.fetchlogpath, 'a') as fl:
            fl.seek(0, 2)
            fl.write(fetchstorename + ", ")
            fl.close()

    def ssc_fetchlogclear(self):
        with open(self.fetchlogpath, 'w') as fl2:
            fl2.truncate()
            fl2.close()

    def ssc_logfetch(self):
        logfetch_retval = []
        with open(self.fetchlogpath, 'r') as fl3:
            fl3.seek(0, 0)
            data = fl3.read().split(", ")
            for logentry in data:
                logfetch_retval.append(logentry)
            fl3.close()
        return logfetch_retval

    def ssc_fetchloguniqueid(self):
        logfetchunique_retval = []
        logfetchuniquename_retval = {}
        with open(self.fetchlogpath, 'r') as fl4:
            fl4.seek(0, 0)
            data = fl4.read().split(", ")
            for val in data:
                if len(val) == 0:
                    data.pop(data.index(val))
                else:
                    continue
            for line in data:
                if line.split("__")[3] not in logfetchunique_retval:
                    logfetchunique_retval.append(line.split("__")[3])
                    logfetchuniquename_retval[line.split("__")[3]] = line.split("__")[0]
            fl4.close()
        return logfetchuniquename_retval
