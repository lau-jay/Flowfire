"""
Copyright (C) 2017-2025 Bryant Moscon - bmoscon@gmail.com

Please see the LICENSE file for the terms and conditions
associated with this software.
Copyright (C) 2025 Jay Lau - cappyclear@gmail.com
"""

import pytest

from flowfire.defines import BEQUANT, EXX
from flowfire.exchanges import EXCHANGE_MAP


@pytest.mark.parametrize("exchange", [e for e in EXCHANGE_MAP.keys() if e not in [EXX]])
def test_symbol_conversion(exchange):
    if exchange == BEQUANT:
        # exchange blocks traffic based on geolocation, so this
        # will fail on build machines in github
        return
    feed = EXCHANGE_MAP[exchange]()
    symbols = feed.symbol_mapping()
    for normalized, original in symbols.items():
        assert feed.std_symbol_to_exchange_symbol(normalized) == original
        assert feed.exchange_symbol_to_std_symbol(original) == normalized
