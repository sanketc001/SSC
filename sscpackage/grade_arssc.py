import gradesheetprintssc


"""
            for x in ar_dict_strip:
                if x["epochGradeDate"] > (time.time() - 31536000):
                    if str(x["toGrade"]) == "Buy" or str(x["toGrade"]) == "Strong Buy" or \
                            str(x["toGrade"]) == "Overweight" or str(x["toGrade"]) == "Market Perform" or \
                            str(x["toGrade"]) == "Outperform":
                        f.write(str(x["firm"]) + "  :::::  " + str(x["toGrade"]) + "  ::")
                        ar_graderaw += 2
                        f.write(str("Analyst Grade Points ::::: + 2 POINTS  ::\n"))
                    elif str(x["toGrade"]) == "Neutral" or str(x["toGrade"]) == "Hold" or \
                            str(x["toGrade"]) == "Perform" or str(x["toGrade"]) == "Equal-Weight":
                        f.write(str(x["firm"]) + "  :::::  " + str(x["toGrade"]) + "  ::")
                        ar_graderaw += 1
                        f.write(str("Analyst Grade Points ::::: + 1 POINT  ::\n"))
"""


class GradeArSSC(gradesheetprintssc.GradeSheetPrintSSC):
    def __init__(self):
        super().__init__()

    def grade_arssc(self, ticker, parsecombo, uniqueid, awardsystemssc):
        localardict = parsecombo[ticker + "__" + uniqueid]

        pass
