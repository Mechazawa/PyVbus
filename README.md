PyVbus
==============

## Usage
```python
import Vbus
con = Vbus.VBUSConnection(
    "HOST", password="ILikeCheese"
    # These are optional. This is the same as setting debugmode to DEBUG_ALL
#   ,debugmode = Vbus.DEBUG_HEXDUMP | Vbus.DEBUG_COMMAND | Vbus.DEBUG_PROTOCOL
)
con.connect()

# Use the default pre-defined payloadmap
data = con.data()
print data # Print the datamap

# Use a custom payloadmap
payloadmap = {
    # Offset, size, factor
    'temp1': (0, 2, 0.1),
    'temp2': (2, 2, 0.1),
    'temp3': (4, 2, 0.1),
    'temp4': (6, 2, 0.1),
    'temp5': (8, 2, 0.1),
    'pump1': (24, 1, 1),
    'pump2': (25, 1, 1)
}

data = con.data(payloadmap)
print data
```
## Payloadmaps
If you do not know what the source map of your vbus device then enable `DEBUG_PROTOCOL`. This will make it print the source map identifier. You can look up how to implement your source map by just searching for the source map hex in [this document](http://tubifex.nl/wordpress/wp-content/uploads/2013/05/VBus-Protokollspezification_en_270111.pdf).

## Screenshot
This screenshot was taken with all the debugmodes enabled.
![screenshot](http://i.imgur.com/uEmmzrF.png)

## License

    Boiler-monitor
    Copyright (C) 2014

    This program is free software; you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation; either version 2 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License along
    with this program; if not, write to the Free Software Foundation, Inc.,
    51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.

