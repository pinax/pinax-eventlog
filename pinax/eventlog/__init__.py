try:
    from importlib.metadata import version
except ImportError:
    from importlib_metadata import version

try:
    __version__ = version("pinax-eventlog")
except Exception:
    __version__ = "5.1.1"
