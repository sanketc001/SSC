"""
Rev. 1.1-a.1
Main control program - SSC
"""
import guistarterssc
import parsessc
import gradestarterssc
import fetchstarterssc
import schedule

GUISSC = guistarterssc.GuiStarterSSC()
def cancel_schedule():
    if GUISSC.__class__.cancel_start:




FSmain_SSC = fetchstarterssc.FetchSSC()
PSmain_SSC = parsessc.ParseStart()
PSmain_SSC.ssc_parselogstart()
GSmain_SSC = gradestarterssc.GradeStartSSC()