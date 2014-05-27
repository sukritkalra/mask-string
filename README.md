mask-string
==========
> Help masking string. It's usefull, especially for masking credit card number and phone number.

Install
-------

```Bash
$ pip install mask-string
```

Usage
-----

```Python
mask_string('Hello world!', 2, 7)
# 'He****rld!'

mask_string('Hello world!', 2, -1)
# 'He****'

mask_string('Hello world!', 2, 7, mask='...')
# 'He...rld!'

mask_string('Hello world!', 0, 7, mask='...')
# '...rld!'
```

