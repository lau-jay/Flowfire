"""
Copyright (C) 2017-2025 Bryant Moscon - bmoscon@gmail.com

Please see the LICENSE file for the terms and conditions
associated with this software.
"""

from flowfire.defines import *
from flowfire.defines import OKX as OKX_str

from .bequant import Bequant
from .binance import Binance
from .binance_delivery import BinanceDelivery
from .binance_futures import BinanceFutures
from .binance_tr import BinanceTR
from .binance_us import BinanceUS
from .bitdotcom import BitDotCom
from .bitfinex import Bitfinex
from .bitflyer import Bitflyer
from .bitget import Bitget
from .bithumb import Bithumb
from .bitmex import Bitmex
from .bitstamp import Bitstamp
from .blockchain import Blockchain
from .bybit import Bybit
from .coinbase import Coinbase
from .cryptodotcom import CryptoDotCom
from .deribit import Deribit
from .dydx import dYdX
from .gemini import Gemini
from .kraken import Kraken
from .kraken_futures import KrakenFutures
from .kucoin import KuCoin
from .okcoin import OKCoin
from .okx import OKX
from .poloniex import Poloniex
from .probit import Probit
from .upbit import Upbit

# Maps string name to class name for use with config
EXCHANGE_MAP = {
    BEQUANT: Bequant,
    BINANCE_DELIVERY: BinanceDelivery,
    BINANCE_FUTURES: BinanceFutures,
    BINANCE_US: BinanceUS,
    BINANCE_TR: BinanceTR,
    BINANCE: Binance,
    BITDOTCOM: BitDotCom,
    BITFINEX: Bitfinex,
    BITFLYER: Bitflyer,
    BITGET: Bitget,
    BITHUMB: Bithumb,
    BITMEX: Bitmex,
    BITSTAMP: Bitstamp,
    BLOCKCHAIN: Blockchain,
    BYBIT: Bybit,
    COINBASE: Coinbase,
    CRYPTODOTCOM: CryptoDotCom,
    DERIBIT: Deribit,
    DYDX: dYdX,
    GEMINI: Gemini,
    KRAKEN_FUTURES: KrakenFutures,
    KRAKEN: Kraken,
    KUCOIN: KuCoin,
    OKCOIN: OKCoin,
    OKX_str: OKX,
    POLONIEX: Poloniex,
    PROBIT: Probit,
    UPBIT: Upbit,
}
