"""
Copyright (C) 2017-2025 Bryant Moscon - bmoscon@gmail.com

Please see the LICENSE file for the terms and conditions
associated with this software.
"""

from datetime import datetime

from flowfire import FeedHandler
from flowfire.backends.aggregate import RenkoFixed
from flowfire.defines import TRADES
from flowfire.exchanges import Bitmex


async def renko(data=None):
    print(datetime.utcnow(), data)


def main():
    f = FeedHandler()
    f.add_feed(
        Bitmex(
            symbols=["BTC-USD-PERP"],
            channels=[TRADES],
            callbacks={TRADES: RenkoFixed(renko, brick_size=3)},
        )
    )

    f.run()


if __name__ == "__main__":
    main()
