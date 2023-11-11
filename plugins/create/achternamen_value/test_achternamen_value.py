import plugins.clean

def test_check_type():
    my_plugin = plugins.clean.CleaningPlugins().plugins['missing999']
    assert type(my_plugin.process(2,3)) == int


def test_check_answer():
    my_plugin = plugins.clean.CleaningPlugins().plugins['missing999']
    assert my_plugin.process(2,3) == 5