"""Results Table for Tada and perf."""


def add_resultstable(resultstable, current_size, mean, median, ratio):
    """Add elements into the resultstable."""
    resultstable.add_row([current_size, mean, median, ratio])


def display_resultstable(resultstable, to_md=False):
    """Print out the resultstable."""
    if to_md:
        print(to_markdown_table(resultstable))
    else:
        print(resultstable)


def to_markdown_table(pt):
    """Convert prettytable to markdown format"""
    _junc = pt.junction_char
    if _junc != "|":
        pt.junction_char = "|"
    markdown = [row[1:-1] for row in pt.get_string().split("\n")[1:-1]]
    pt.junction_char = _junc
    return "\n".join(markdown)
