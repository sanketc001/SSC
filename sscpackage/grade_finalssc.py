import gradesheetprintssc


class GradeFinalSSC(gradesheetprintssc.GradeSheetPrintSSC):
    def __init__(self):
        super().__init__()
        self.finalgrade = ""

    def grade_final_ssc(self, pointbin):
        totalpoints = 0
        awardedpoints = 0
        for basepoints, currentpoints in pointbin:
            totalpoints += basepoints
            awardedpoints += currentpoints

        ratiores = awardedpoints / totalpoints

        if ratiores >= .94:
            self.finalgrade = "A"
        elif ratiores >= .90:
            self.finalgrade = "AB"
        elif ratiores >= .84:
            self.finalgrade = "B"
        elif ratiores >= .80:
            self.finalgrade = "BC"
        elif ratiores >= .74:
            self.finalgrade = "C"
        elif ratiores >= .70:
            self.finalgrade = "CD"
        elif ratiores >= .64:
            self.finalgrade = "D"
        else:
            self.finalgrade = "F"





