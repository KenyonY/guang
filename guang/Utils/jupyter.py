from IPython.core.interactiveshell import InteractiveShell

def output(flag='all'):
    """
    'all', 'last', 'last_expr' or 'none'
    """
    InteractiveShell.ast_node_interactivity = flag

