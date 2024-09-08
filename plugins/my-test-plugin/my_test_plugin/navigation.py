try:
    from netbox.plugins import PluginMenuItem
except ImportError:
    from extras.plugins import PluginMenuItem
    

menu_items = (
    PluginMenuItem(
        link="plugins:my_test_plugin:view_one",
        link_text="My First View",
    ),
    PluginMenuItem(
        link="plugins:my_test_plugin:view_two",
        link_text="My Second View",
    ),
)