try:
    from netbox.plugins import PluginConfig
except ImportError:
    from extras.plugins import PluginConfig


class MyTestPlugin(PluginConfig):
    name = "my_test_plugin"
    verbose_name = "My Test Plugin"
    description = "My Plugin Dev Testing"
    version = "0.1.0"
    author = "Manolis Kaliotis"
    author_email = "mkaliotis@gmail.com"
    base_url = "my-test-plugin"
    required_settings = []
    default_settings = {}


config = MyTestPlugin

