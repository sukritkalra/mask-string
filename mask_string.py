import sys

def mask_string(string, start, stop, mask='****'):
	length = len(string)
	start = start % length
	stop = stop % length
	return string[:start] + mask + string[stop+1:]

sys.modules[__name__] = mask_string
