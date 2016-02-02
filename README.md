
# What?
A python decorator that will automatically cast inputs into best guess Python data types.

# Install
``` pip install python-autocast ```

# Examples
```python
>>> from autocast import autocast
>>>
>>> @autocast
... def castit(input):
...     print(type(input))
...
>>> castit('3')
<type 'int'>
>>> castit('5.652')
<type 'float'>
>>> castit(5.652)
<type 'float'>
>>> castit('[1,2,3,4]')
<type 'list'>
>>> castit('true')
<type 'bool'>
>>> castit('True')
<type 'bool'>
>>> castit('false')
<type 'bool'>
>>> castit('False')
<type 'bool'>
>>> castit('None')
<type 'NoneType'>
>>> castit('none')
<type 'NoneType'>
>>> castit('ohai')
<type 'str'>
>>>
```

# Requirements
Python versions ```2.6, 2.7, 3.0, 3.1, 3.2, 3.4```

# Issues / Concerns / Comments?
Please let me know or make a pull request.
