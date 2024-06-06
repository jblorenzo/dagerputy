try:
    import pkg_resources
    version = pkg_resources.require("dagerputy")[0].version
except Exception, ImportError:
    version = 'unknown'
