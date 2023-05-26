"""
 Copyright (c) 2021 Alan Yorinks All rights reserved.

 This program is free software; you can redistribute it and/or
 modify it under the terms of the GNU AFFERO GENERAL PUBLIC LICENSE
 Version 3 as published by the Free Software Foundation; either
 or (at your option) any later version.
 This library is distributed in the hope that it will be useful,f
 but WITHOUT ANY WARRANTY; without even the implied warranty of
 MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
 General Public License for more details.

 You should have received a copy of the GNU AFFERO GENERAL PUBLIC LICENSE
 along with this library; if not, write to the Free Software
 Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301  USA

 DHT support courtesy of Martyn Wheeler
 Based on the DHTNew library - https://github.com/RobTillaart/DHTNew
"""

import sys
import time

from telemetrix_rpi_pico import telemetrix_rpi_pico
TRIGGER = 1
STEPS = 2
TIME_STAMP = 3
def the_callback(data):
    # will only be called when an encoder step is measured
    date = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(data[TIME_STAMP]))

    print(f'{date}\t Encoder Pin::\t{data[TRIGGER]}\t Steps:\t'
          f'{data[STEPS]}')

# some globals
PIN_A = 14
PIN_B = 15


# Create a Telemetrix instance.
board = telemetrix_rpi_pico.TelemetrixRpiPico()
try:
    board.set_pin_mode_encoder(PIN_A, PIN_B, the_callback)
    board.set_scan_delay(100)
    while True:
        try:
            # do nothing but sleep while the reports come in.
            time.sleep(1)
        except KeyboardInterrupt:
            board.shutdown()
            sys.exit(0)
except KeyboardInterrupt:
    board.shutdown()
    sys.exit(0)

board.shutdown()
sys.exit(0)


