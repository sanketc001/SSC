"""
This starts the grade cycle
"""
import fetchlogssc
import gradecollectionssc
import gradeparsecombinessc


class GradeStartSSC():

    def gradestartssc(self):
        FS_SSC = fetchlogssc.FetchLogSSC()
        localfetchuniquelogcopyssc = FS_SSC.ssc_fetchloguniqueid()
        for entrysscgs in localfetchuniquelogcopyssc.keys():
            PCOMBO = gradeparsecombinessc.GradeParseCombineSSC()
            GCOL_SSC = gradecollectionssc.GradeCollectionSSC(ticker=localfetchuniquelogcopyssc[entrysscgs],
                                                             uniqueidssc=entrysscgs,
                                                             parsecombossc=PCOMBO.gradeparsecombinessc(
                                                                 ticker=localfetchuniquelogcopyssc[entrysscgs],
                                                                 logfileidssc=entrysscgs
                                                             ))







    pass