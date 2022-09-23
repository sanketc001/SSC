"""
Rev. 1.1-a.1
Main control program - SSC
"""
import guistarterssc
import parsessc
import gradestarterssc
import fetchstarterssc
import schedule
def gui_ssc_instantiate():
    print(guistarterssc.GuiStarterSSC.fetch_instcount())
    if guistarterssc.GuiStarterSSC.fetch_instcount() > 0:
        pass
    else:
        guistarterssc.GuiStarterSSC().start_gui_ssc()


gui_ssc_instantiate()

def cancel_schedule():
    if guistarterssc.GuiStarterSSC.cancel_start:
        pass


class ControlBoardSSC():
    """
    Main Control Flow:
    1. guistarter
    FROM GUI - INPUT CHOSEN
    2.
    """
    main_cancelf = False
    def __init__(self):
        self.gui = guistarterssc.GuiStarterSSC()
        self.fetch = fetchstarterssc.FetchSSC()
        self.parse = parsessc.ParseStart()
        self.grade = gradestarterssc.GradeStartSSC()

        # How methods are called for core application after GUI is instantiated
        self.controlflow = {
            "1": self.gui
        }


    def run_core(self, ticker_list):

        if ControlBoardSSC.main_cancelf:
            pass

