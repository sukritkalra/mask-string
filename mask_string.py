import sys

def mask_string(str, start, stop, mask='****'):
	length = len(str)
	start = start if start >= 0 else start % length
	stop = stop if stop >=0 else stop % length
	return str[:start] + mask + str[stop+1:]

sys.modules[__name__] = mask_string
