## Use `DocHelper` to simplify your python docstrings

If you have been writing classes or functions with many shared arguments, you
might have going through the tedious and error prone process of copy-pasting,
searching-updating same docstring again and again. Passing through `**kwargs`
might not always be the solution not to say it's implicit and makes user to
look up multiple documents to find available arguments.

So how about one place to store and update them all? `DocHelper` keeps the
docstrings for arguments in the same place and you only need to write the
template for each class or functions - it will compose and fill in the
template in Google format.

Works from Jupyter notebook to Sphinx where docstrings were read by importing.

## Installation
### Install using `pip` (recommended)

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

## Usage

### Initialize a `DocHelper` with argument docstrings

```python
from doc_helper import DocHelper

my_doc = DocHelper(
    arg1='Just an simple argument',           # defined as keyword arguments
    arg2=('Also an simple argument'),         # or a (not really) tuple
    arg3=('int', 'This argument is integer')  # tuple with data type
)
```

### Add arguments when you needed
```python
my_doc.add(
    arg4=('pd.DataFrame', 'Just a new argument')
)
```

### Use decorator `DocHelper.compose` to write template

Simply write a string with comma separated arguments name in `<<` and `>>`.
Default indents is 4, just add a number to change to desired indents.

```python
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
This is another awesome function only takes arg1, arg3, and I wand indent = 8
Args:
        arg1: Just an simple argument
        arg3 (int): This argument is integer
```

## Caveats
It seems triple quote will not automatic align the indent, so you need to start
write from the top of lines. It could be improved by calling the docstring
formatting function (TODO).

```python
class YourClass:

    @my_doc.compose("""This is the first line
This is the second line, it does not have indent
    """)
    def good_example(self, arg1):
        # do something
        return 0



    @my_doc.compose("""This is the first line
    This is the second line, it have indents
    """)
    def bad_example(self, arg1):
        # do something
        return 0

>>> YourClass.good_example.__doc__
This is the first lines
This is the second line, it does not have indent


>>> YourClass.bad_example.__doc__
This is the first line
    This is the second line, it have indents
```

## TODO
- Add docstring formatting function to subtract extra indents
- Include different formatting (Numpy, reStructuredText)
