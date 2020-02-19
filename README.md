## Use `DocHelper` to simplify your docstrings

I have been writing many functions with shared arguments (or to pass through - not a big fan of the implicit `**kwargs`), where documenting or updating these repeated arguments is tedious and error-prone. So how about a centralized place to keep your arguments so you only update once?

`DocHelper` solved this problem by keep the docstring for arguments (or other objects) in the same place and compose the docstring in Google format for your functions/classes when you need them.

## Installation
### Install using `pip`

```bash
pip install doc-helper 
```

### Install from source
```bash
# make sure you have setuptools and wheel installed

git clone https://github.com/ynshen/DocHelper.git
cd DocHelper
python setup.py bdist_wheel
pip install dist/the-wheel-file-of-your-version.whl
```

### Usage

```python
from DocHelper import DocHelper

my_doc = DocHelper(
    arg1='Just an simple argument',
    arg2=('Also an simple argument'),
    arg3=('int', 'This argument is integer')
)


@my_doc.compose("""This is my awesome function
Args:
<<arg1, arg2, arg3>>
""")
def awesome_function(arg1, arg2, arg3):
    # getting your job down


@my_doc.compose("""This is another awesome function only takes arg1, arg3, and I want indent = 8
Args:
<<arg1, arg2, 8>>
""")
def another_awesome_function(arg1, arg3):
    # getting your job down
    return 0


>>> awesome_function.__doc__
This is my awesome function
Args:
    arg1: Just an simple argument
    arg2: Also an simple argument
    arg3 (int): This argument is integer


>>> another_awesome_function.__doc__
This is another awesome function only takes arg1, arg3
Args:
    arg1: Just an simple argument
    arg3 (int): This argument is integer
```

### Caveats
It seems triple quote will not automatic align the indent, so you need to start write from the top of lines. It could be improved by calling the docstring formatting function (TODO).

```python
class YourClass:

    @my_doc.compose("""This is the first line
This is the second line, it does not have indent
    """)
    def good_example(self, arg1):
        # do something
        return 0



    @my_doc.compose("""This is the first line
    This is the second line, it have 4 indents
    """)
    def bad_example(self, arg1):
        # do something
        return 0
```

### TODO
- Add docstring formatting function to subtract extra indents
- Include different formatting (Numpy, reStructuredText)


