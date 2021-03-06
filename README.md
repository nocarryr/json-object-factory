[![Build Status](https://travis-ci.org/nocarryr/json-object-factory.svg?branch=master)](https://travis-ci.org/nocarryr/json-object-factory) [![Coverage Status](https://coveralls.io/repos/github/nocarryr/json-object-factory/badge.svg?branch=master)](https://coveralls.io/github/nocarryr/json-object-factory?branch=master)

# json-object-factory
Simplifies building custom encoders and object-hooks for Python's default JSON implementation.

## Installation
```
$ pip install json-object-factory
```
## Usage
Add encoders and decoders to the registry:
```python
import jsonfactory

class MyJsonHandler(object):
    def encode(self, o):
        if isinstance(o, MyCustomClass):
            return o.serialize()
        return None

    def decode(self, d):
        if 'some_custom_key' in d:
            return MyCustomClass(**d)
        return d

jsonfactory.Registry.register(MyJsonHandler)
```
Or use the included decorators:
```python
@jsonfactory.register
class MyOtherJsonHandler(object):
    ...

@jsonfactory.encoder
def an_encoder_function(o):
    ...

@jsonfactory.decoder
def a_decoder_function(d):
    ...
```
Then use the module's `dumps` and `loads` functions:
```python
json_str = jsonfactory.dumps(obj_dict, indent=2)

new_obj_dict = jsonfactory.loads(json_str)
```

## Notes
* The calling signature for encoder functions follows that of the built-in [JSONEncoder](https://docs.python.org/3.5/library/json.html#json.JSONEncoder) with one exception:
    * If no modifications are needed and the object should be passed to the base encoder's handler, `None` should be returned.  This differs from the normal method of calling `super(MyEncoder, self).default(o)` (that would most likely be an error since subclassing `JSONEncoder` isn't necessary).
* The signature for decoder functions follows the `object_hook` signature in [the built-in implementation](https://docs.python.org/3.5/library/json.html#json.load)
