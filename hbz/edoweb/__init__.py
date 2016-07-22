import pkg_resources  # part of setuptools
# See http://peak.telecommunity.com/DevCenter/setuptools#namespace-packages
try:
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    from pkgutil import extend_path
    __path__ = extend_path(__path__, __name__)

# version information
__version__ = pkg_resources.require("hbz.edoweb")[0].version
