import asyncio
from sscpackage.fetchssc import FetchSSC


class FetchStarterSSC:
    """
    This class accepts the tickerlist from user input as an arg, then starts parsing with asyncio and a maximum of 5
    concurrent fetches (max simultaneous RapidAPI will allow for my payment level)

    This class and 'fetch_cycle'
    """
    runlist_tickers = []
    fetch_cancel = False
    fetch_header = "FETCH TICKERS: "
    init_once = False



    @staticmethod
    def pull_header():
        return FetchStarterSSC.fetch_header

    @staticmethod
    def update_header(arg_header):
        FetchStarterSSC.fetch_header = str(arg_header)

    @staticmethod
    def update_runlist(args):
        del FetchStarterSSC.runlist_tickers
        FetchStarterSSC.runlist_tickers = [x for x in args]

    @staticmethod
    def pull_runlist():
        return FetchStarterSSC.runlist_tickers

    def __init__(self, tickerlist: list):
        self.tickerlist = tickerlist
        self.fetch_cancel: bool = False
        self.runninglist = []
        FetchStarterSSC.init_once = True

    @staticmethod
    def cancel_fetch():
        print("entered cancel_fetch :: ")
        FetchStarterSSC.fetch_cancel = True
        print(FetchStarterSSC.fetch_cancel)

    async def _fetch_cycle(self, *args, **kwargs):
        tickerlistvar_fetchssc = self.tickerlist[:]
        while tickerlistvar_fetchssc:
            if FetchStarterSSC.fetch_cancel:
                print("Broke Chain - FetchStarter")
                break
            if len(tickerlistvar_fetchssc) >= 5:
                ticker_runlist = []
                for indexno in range(0, 5):
                    if FetchStarterSSC.fetch_cancel:
                        print("Broke Chain - FetchStarter")
                        break
                    ticker_runlist.append(tickerlistvar_fetchssc[indexno])
                    print(ticker_runlist)
                    FetchStarterSSC.update_runlist(ticker_runlist)
                await asyncio.gather(
                    FetchSSC(tickerlistvar_fetchssc.pop(0)).rapid_fetch(),
                    FetchSSC(tickerlistvar_fetchssc.pop(0)).rapid_fetch(),
                    FetchSSC(tickerlistvar_fetchssc.pop(0)).rapid_fetch(),
                    FetchSSC(tickerlistvar_fetchssc.pop(0)).rapid_fetch(),
                    FetchSSC(tickerlistvar_fetchssc.pop(0)).rapid_fetch(),
                )
            else:
                if FetchStarterSSC.fetch_cancel:
                    print("Broke Chain - FetchStarter")
                    break
                for indexno in range(len(tickerlistvar_fetchssc)):
                    if FetchStarterSSC.fetch_cancel:
                        print("Broke Chain - FetchStarter")
                        break
                    await asyncio.gather(FetchSSC(tickerlistvar_fetchssc.pop(0)).rapid_fetch())
            await asyncio.sleep(1)
