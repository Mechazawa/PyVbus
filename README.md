Boiler-monitor
==============

## Usage
```python
import Vbus
con = Vbus.VBUSConnection(
    "HOST", password="ILikeCheese"
    # These are optional
#   ,debugmode = Vbus.DEBUG_HEXDUMP | Vbus.DEBUG_COMMAND | DEBUG_PROTOCOL
)
con.connect()

# Use the default pre-defined payloadmap
data = con.data()
print data # Print the datamap

# Use a custom payloadmap
framesize = 60
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

data = con.data(payloadmap, framesize)
print data
```
## Payloadmaps
If you do not know what the source map of your vbus device then enable `DEBUG_PROTOCOL`. This will make it print the source map identifier. You can look up how to implement your source map by just searching for the source map hex in [this document](http://tubifex.nl/wordpress/wp-content/uploads/2013/05/VBus-Protokollspezification_en_270111.pdf).
