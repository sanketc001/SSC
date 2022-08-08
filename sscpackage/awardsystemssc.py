"""
This class is going to house the point award system
"""

class AwardSystemSSC:
    def __init__(self):
        self.awardsystemcontainer = {}
        self.awardsystempath = r'C:\SSC\SimpleStockChecker_REV1\sscpackage\storage\awardsystemssc'

    def primeawardsystemssc(self):
        grade_metricone = ["Total Revenue", "Net Income", "Gross Margin", "Operating Margin", "Net Margin"]
        grade_metrictwo = ["Gross Profit", "EBIT", "Operating Income", "Net Income From Continuing Ops",
                           "Income Before Tax", "Research & Development"]
        grade_metricthree = ["Selling, General & Administrative", "Other Operating Expenses", "Interest Expense",
                             "Total Operating Expenses", "Cost Of Revenue", "Total Other Income Expense Net"]
        grade_metricfour = ["Total Assets", "Retained Earnings"]
    pass