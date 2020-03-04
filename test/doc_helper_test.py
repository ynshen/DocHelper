from doc_helper import DocHelper


def test_DocHelper_stores_doc():
    doc = DocHelper(
        arg1='Docstring for arg1',
        arg2=('Docstring for arg2'),
        arg3=('type for arg3', 'Docstring for arg3')
    )
    assert doc.var_lib.shape == (3, 2)


def test_DocHelper_compose_correctly():
    doc = DocHelper(
        arg1='Docstring for arg1',
        arg2=('Docstring for arg2'),
        arg3=('type for arg3', 'Docstring for arg3')
    )
    output = doc.get(['arg1'])
    assert output == "arg1: Docstring for arg1"
    output = doc.get(['arg1', 'arg3'])
    assert output == "arg1: Docstring for arg1\n    arg3 (type for arg3): Docstring for arg3"


def test_string_strip_func_works():
    docstring = ('This is docstring\n'
                 '    with multiple lines of args:\n'
                 '<< arg1,arg2,  arg3 >>\n'
                 '<<arg1, arg3>>\n')

    doc = DocHelper(
        arg1='Docstring for arg1',
        arg2=('Docstring for arg2'),
        arg3=('type for arg3', 'Docstring for arg3')
    )

    split = doc.split_string(docstring)
    assert split[0] == "This is docstring\n    with multiple lines of args:\n"
    assert split[1] == ('arg1', 'arg2', 'arg3')
    assert split[2] == '\n'
    assert split[3] == ('arg1', 'arg3')


def test_DocHelper_compose_doc_decorator_works():
    doc = DocHelper(
        arg1='Docstring for arg1',
        arg2=('Docstring for arg2'),
        arg3=('type for arg3', 'Docstring for arg3')
    )

    @doc.compose("""Here is an example
        <<arg1, arg2>>
    Args:
            <<arg2, arg3, 8>>
    """)
    def target_func(arg1):
        pass

    assert target_func.__doc__ == "Here is an example\n" \
                                  "    arg1: Docstring for arg1\n" \
                                  "    arg2: Docstring for arg2\n" \
                                  "Args:\n" \
                                  "        arg2: Docstring for arg2\n" \
                                  "        arg3 (type for arg3): Docstring for arg3"


def test_DocHelper_compose_doc_decorator_works_with_beginning_indent_turned_on():
    doc = DocHelper(
        arg1='Docstring for arg1',
        arg2=('Docstring for arg2'),
        arg3=('type for arg3', 'Docstring for arg3')
    )

    @doc.compose("""Here is an example
    <<arg1, arg2>>
    Args:
    <<arg2, arg3, 8>>
    """, indent_at_top=True)
    def target_func(arg1):
        pass

    assert target_func.__doc__ == "Here is an example\n" \
                                  "    arg1: Docstring for arg1\n" \
                                  "    arg2: Docstring for arg2\n" \
                                  "Args:\n" \
                                  "        arg2: Docstring for arg2\n" \
                                  "        arg3 (type for arg3): Docstring for arg3"


def test_DocHelper_compose_doc_decorator_no_effect_works():
    doc = DocHelper(
        arg1='Docstring for arg1',
        arg2=('Docstring for arg2'),
        arg3=('type for arg3', 'Docstring for arg3')
    )

    @doc.compose("""Here is an example of simple docstring with no argument substitution
    Args:
        args1
    """)
    def target_func(arg1):
        pass

    assert target_func.__doc__ == "Here is an example of simple docstring with no argument substitution\n" \
                                  "Args:\n" \
                                  "    args1"


def test_DocHelper_compose_doc_decorator_func_works():
    doc = DocHelper(
        arg1='Docstring for arg1',
        arg2=('Docstring for arg2'),
        arg3=('type for arg3', 'Docstring for arg3')
    )

    @doc.compose("""Here is an example of simple docstring to replace function's arguments
    Args:
        << >>
    """)
    def target_func(arg1):
        pass

    assert target_func.__doc__ == "Here is an example of simple docstring to replace function's arguments\n" \
                                  "Args:\n" \
                                  "    arg1: Docstring for arg1"


def test_DocHelper_compose_doc_decorator_works_with_fstring():
    doc = DocHelper(
        arg1='Docstring for arg1',
        arg2=('Docstring for arg2'),
        arg3=('type for arg3', 'Docstring for arg3')
    )

    @doc.compose("""Here is an example of simple docstring to replace function's arguments
    {something}
    Args:
        << >>
    """.format(something='special things'))
    def target_func(arg1):
        pass

    assert target_func.__doc__ == "Here is an example of simple docstring to replace function's arguments\n" \
                                  "special things\n" \
                                  "Args:\n" \
                                  "    arg1: Docstring for arg1"
