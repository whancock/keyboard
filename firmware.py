#!/usr/bin/env python3

#import asyncio
import evdev
#from evdev import UInput, ecodes as e


#keybd = evdev.InputDevice('/dev/hidg0')



#print(evdev.list_devices())

# from rmedgar.com
NULL_CHAR = chr(0)

def write_report(report):
	with open('/dev/hidg0', 'rb+') as fd:
		fd.write(report.encode())

# e
write_report(NULL_CHAR*2+chr(8)+NULL_CHAR*5)
write_report(NULL_CHAR*2+chr(128)+NULL_CHAR*5)

# ! (press shift and 1)
# write_report(chr(32)+NULL_CHAR+chr(30)+NULL_CHAR*5)

# Release all keys
write_report(NULL_CHAR*8)



# from cherry pi split keyboard
# can report multiple keys per tick, may need this later
#def report_keyboard(c,k):
#    with open('/dev/hidg0', 'rb+') as fk:
#        fk.write((c).to_bytes(1, byteorder='big')+    \
#                 (0).to_bytes(1, byteorder='big')+    \
#                 (k[0]).to_bytes(1, byteorder='big')+ \
#                 (k[1]).to_bytes(1, byteorder='big')+ \
#                 (k[2]).to_bytes(1, byteorder='big')+ \
#                 (k[3]).to_bytes(1, byteorder='big')+ \
#                 (k[4]).to_bytes(1, byteorder='big')+ \
#                 (k[5]).to_bytes(1, byteorder='big'))




#ui = UInput()


#ui.write(e.EV_KEY, e.KEY_A, 1)  # KEY_A down
#ui.write(e.EV_KEY, e.KEY_A, 0)  # KEY_A up
#ui.syn()


#ui.close()

