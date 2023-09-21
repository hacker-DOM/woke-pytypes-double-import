
import woke.development.core
from woke.utils import get_package_version

if get_package_version("woke") != "4.0.0a2":
    raise RuntimeError("Pytypes generated for a different version of woke. Please regenerate.")

woke.development.core.errors = {b'\x08\xc3y\xa0': {'': ('woke.development.transactions', ('Error',))}, b'NH{q': {'': ('woke.development.transactions', ('Panic',))}}
woke.development.core.events = {}
woke.development.core.contracts_by_fqn = {'src/interfaces/IFoo.sol:IFoo': ('pytypes.src.interfaces.IFoo', ('IFoo',)), 'src/Foo.sol:Foo': ('pytypes.src.Foo', ('Foo',)), 'tests/mocks/Foo.sol:Foo': ('pytypes.tests.mocks.Foo', ('Foo',))}
woke.development.core.contracts_by_metadata = {b'\xa2dipfsX"\x12 \xeb\x1f\xce\xe6.\x91\xeb\xc0\x00\xda"2\xb3\x92\xc3\xf3\x0b\xa6\xfaY\x99,\xb6\xf6\x9b\xbd\x97\xba\x05\xfe\x9b\xd7dsolcC\x00\x08\x14\x003': 'src/Foo.sol:Foo', b'\xa2dipfsX"\x12 \xbc\xc5p8\xaf7\xcbQ\x82\x92\xf0\x81\xcfO\xd0\x90\x87We\x03\x90:~\x06\x80\xfa\xeb=\x96\xa44\x80dsolcC\x00\x08\x14\x003': 'tests/mocks/Foo.sol:Foo'}
woke.development.core.contracts_inheritance = {'src/interfaces/IFoo.sol:IFoo': ('src/interfaces/IFoo.sol:IFoo',), 'src/Foo.sol:Foo': ('src/Foo.sol:Foo', 'src/interfaces/IFoo.sol:IFoo'), 'tests/mocks/Foo.sol:Foo': ('tests/mocks/Foo.sol:Foo', 'src/interfaces/IFoo.sol:IFoo')}
woke.development.core.contracts_revert_index = {}
woke.development.core.creation_code_index = [(((88, b'o\xb7 \xcbf\xfb\xc1\x10=\xb8\xe7;\xf3\xfe\xb6Qy\xeee\xa7\x12\x8b\xb1\x11+y^\x80\xe7\x1f\x7f\xee'),), 'src/Foo.sol:Foo'), (((88, b'\xc5Y\xa4\xac\t\xdc;\xb3\xfdK{\xcf\x88\xd1d\xb4\x875@\x1c\xd7I\x04\xfc6\x8d{DZ\xd2\xde2'),), 'tests/mocks/Foo.sol:Foo')]
