#!/usr/bin/env python3

import asyncio, evdev

encoder = evdev.InputDevice('/dev/input/by-path/platform-soc:master-event')
button = evdev.InputDevice('/dev/input/by-path/platform-soc:mute-event-joystick')

# from rmedgar.com
NULL_CHAR = chr(0)

def write_report(report):
	with open('/dev/hidg0', 'rb+') as fd:
		fd.write(report.encode())

# e
#write_report(NULL_CHAR*2+chr(8)+NULL_CHAR*5)
#write_report(NULL_CHAR*2+chr(128)+NULL_CHAR*5)

# ! (press shift and 1)
# write_report(chr(32)+NULL_CHAR+chr(30)+NULL_CHAR*5)

# Release all keys
#write_report(NULL_CHAR*8)


async def print_events(device):
	async for event in device.async_read_loop():
		# print(evdev.categorize(event), event.type, event.code, event.value, sep=': ')
		if event.type == evdev.ecodes.EV_REL and event.code == evdev.ecodes.REL_X:
			# print('Rel event')
			if event.value == 1:
				write_report(NULL_CHAR * 2 + chr(1) + NULL_CHAR * 5)
			elif event.value == -1:
				# print('Negative event')
				write_report(NULL_CHAR * 2 + chr(2) + NULL_CHAR * 5)
		# print(device.path, evdev.categorize(event), sep=': ')

for device in encoder, button:
	asyncio.ensure_future(print_events(device))

loop = asyncio.get_event_loop()
loop.run_forever()
