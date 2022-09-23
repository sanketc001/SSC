import asyncio
from sscpackage.fetchssc import FetchSSC


class FetchStarterSSC:
    """
    This class accepts the tickerlist from user input as an arg, then starts parsing with asyncio and a maximum of 5
    concurrent fetches (max simultaneous RapidAPI will allow for my payment level)

    This class and 'fetch_cycle'
    """

    def __init__(self, tickerlist: list):
        self.tickerlist = tickerlist
        self.fetch_cancel: bool = False

    def fetch_cancel(self):
        self.fetch_cancel = True

    async def _fetch_cycle(self, *args, **kwargs):
        tickerlistvar_fetchssc = self.tickerlist[:]
        while tickerlistvar_fetchssc:
            if self.fetch_cancel:
                break
            if len(tickerlistvar_fetchssc) >= 5:
                await asyncio.gather(
                    FetchSSC(tickerlistvar_fetchssc.pop(0)).rapid_fetch(),
                    FetchSSC(tickerlistvar_fetchssc.pop(0)).rapid_fetch(),
                    FetchSSC(tickerlistvar_fetchssc.pop(0)).rapid_fetch(),
                    FetchSSC(tickerlistvar_fetchssc.pop(0)).rapid_fetch(),
                    FetchSSC(tickerlistvar_fetchssc.pop(0)).rapid_fetch(),
                )
            else:
                for indexno in range(len(tickerlistvar_fetchssc)):
                    await asyncio.gather(FetchSSC(tickerlistvar_fetchssc.pop(0)).rapid_fetch())
            await asyncio.sleep(1)
