def test_module_attributes(Script):
    def_, = Script('__name__').completions()
    assert def_.name == '__name__'
    assert def_.line == None
    assert def_.column == None
    str_, = def_._goto_definitions()
    assert str_.name == 'str'
