def instructions():
    inst = """
    import pandas as pd
    ... other imports

    sys.path.append('../..')
    ... more imports

    """
    return inst


# %load_ext rozner_lib_python.jupyter_ext.jupyter_basic_magic
def load_ipython_extension(ipython):
    compiled_file = "jupyter_shared_log.py"
    # code = compile(instructions(), compiled_file, 'exec')
    # ipython.run_code(code)
    # ipython.run_line_magic("matplotlib", "inline")
    ipython.run_line_magic("load_ext", "autotime")
    ipython.run_line_magic("load_ext", "autoreload")
    ipython.run_line_magic("autoreload", "2")
