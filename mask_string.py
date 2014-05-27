import sys

def mask_string(str, start, stop, mask='****'):
	length = len(str)
	start = start % length
	stop = stop % length
	return str[:start] + mask + str[stop+1:]

sys.modules[__name__] = mask_string
