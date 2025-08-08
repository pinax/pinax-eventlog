from importlib.metadata import version

try:
    __version__ = version("pinax-eventlog")
except Exception:
    __version__ = "6.0.0rc1"
