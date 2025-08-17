"""
Copyright (C) 2018-2025 Bryant Moscon - bmoscon@gmail.com

Please see the LICENSE file for the terms and conditions
associated with this software.
"""

from flowfire import FeedHandler
from flowfire.backends.arctic import FundingArctic, TickerArctic, TradeArctic
from flowfire.defines import FUNDING, TICKER, TRADES
from flowfire.exchanges import Bitfinex, Bitmex, Coinbase


def main():
    f = FeedHandler()
    f.add_feed(
        Bitmex(
            channels=[TRADES, FUNDING],
            symbols=["BTC-USD-PERP"],
            callbacks={
                TRADES: TradeArctic("flowfire-test"),
                FUNDING: FundingArctic("flowfire-test"),
            },
        )
    )
    f.add_feed(
        Bitfinex(
            channels=[TRADES],
            symbols=["BTC-USD"],
            callbacks={TRADES: TradeArctic("flowfire-test")},
        )
    )
    f.add_feed(
        Coinbase(
            channels=[TICKER],
            symbols=["BTC-USD"],
            callbacks={TICKER: TickerArctic("flowfire-test")},
        )
    )
    f.run()


if __name__ == "__main__":
    main()
