"""
This starts the grade cycle
"""
import fetchlogssc
import gradecollectionssc
import gradeparsecombinessc


class GradeStartSSC():
    grade_cancel = False
    grade_runitem = ""
    grade_header = "GRADE TICKERS - "

    @staticmethod
    def pull_gradeheader():
        return GradeStartSSC.grade_header

    @staticmethod
    def set_gradeheader(arg_head):
        GradeStartSSC.grade_header = str(arg_head)


    @staticmethod
    def set_runitem(arg):
        GradeStartSSC.grade_runitem = arg

    @staticmethod
    def get_runitem():
        return GradeStartSSC.grade_runitem

    @staticmethod
    def cancel_grade():
        print("Cancel_Grade")
        GradeStartSSC.grade_cancel = True
        print(GradeStartSSC.grade_cancel)

    def gradestartssc(self, fiver: bool = True):
        FS_SSC = fetchlogssc.FetchLogSSC()
        localfetchuniquelogcopyssc = FS_SSC.ssc_fetchloguniqueid()
        local_looplist = {}
        if fiver:
            for indexno in range(0, 5):
                local_looplist[sorted(localfetchuniquelogcopyssc.keys())[indexno]] = \
                localfetchuniquelogcopyssc[sorted(localfetchuniquelogcopyssc.keys())[indexno]]
                localfetchuniquelogcopyssc = local_looplist
        else:
            pass

        for entrysscgs in localfetchuniquelogcopyssc.keys():
            if not GradeStartSSC.grade_cancel:
                ticker = entrysscgs.split("__")[0]
                GradeStartSSC.set_runitem(ticker)
                PCOMBO = gradeparsecombinessc.GradeParseCombineSSC()
                GCOL_SSC = gradecollectionssc.GradeCollectionSSC(ticker=localfetchuniquelogcopyssc[entrysscgs],
                                                                 uniqueidssc=entrysscgs,
                                                                 parsecombossc=PCOMBO.gradeparsecombinessc(
                                                                     ticker=localfetchuniquelogcopyssc[entrysscgs],
                                                                     logfileidssc=entrysscgs
                                                                 ))
                GCOL_SSC.gradecollectionssc()

if __name__ == "__main__":
    GSS = GradeStartSSC()
    GSS.gradestartssc(fiver=True)