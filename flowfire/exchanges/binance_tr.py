"""
Copyright (C) 2017-2025 Bryant Moscon - bmoscon@gmail.com

Please see the LICENSE file for the terms and conditions
associated with this software.
Copyright (C) 2025 Jay Lau - cappyclear@gmail.com
"""

import logging

from flowfire.connection import RestEndpoint, WebsocketEndpoint, Routes
from flowfire.defines import BINANCE_TR
from flowfire.exchanges.binance import Binance
from flowfire.exchanges.mixins.binance_rest import BinanceTRRestMixin


LOG = logging.getLogger("feedhandler")


class BinanceTR(Binance, BinanceTRRestMixin):
    id = BINANCE_TR
    websocket_endpoints = [WebsocketEndpoint("wss://stream-cloud.trbinance.com")]
    rest_endpoints = [
        RestEndpoint(
            "https://api.binance.me",
            routes=Routes(
                "/api/v3/exchangeInfo", l2book="/api/v3/depth?symbol={}&limit={}"
            ),
        )
    ]
