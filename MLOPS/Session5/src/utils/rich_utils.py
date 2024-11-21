from rich.tree import Tree
from rich.console import Console

console = Console()

def print_config_tree(config, tree=None, name="Config"):
    if tree is None:
        tree = Tree(f"[bold]{name}")

    if hasattr(config, "__dict__"):
        items = config.__dict__.items()
    elif isinstance(config, dict):
        items = config.items()
    else:
        tree.add(f"[red]Unable to process config of type: {type(config)}[/red]")
        return

    for key, value in items:
        if isinstance(value, (int, float, str, bool)):
            tree.add(f"[cyan]{key}[/cyan]: [yellow]{value}[/yellow]")
        elif isinstance(value, dict):
            branch = tree.add(f"[cyan]{key}")
            print_config_tree(value, branch, key)
        elif isinstance(value, list):
            branch = tree.add(f"[cyan]{key}")
            for i, item in enumerate(value):
                if isinstance(item, dict):
                    print_config_tree(item, branch, f"{key}[{i}]")
                else:
                    branch.add(f"[yellow]{item}[/yellow]")
        else:
            tree.add(f"[cyan]{key}[/cyan]: [magenta]{type(value).__name__}[/magenta]")

    if name == "Config":
        console.print(tree)

def print_config_tree_wrapper(config):
    print_config_tree(config)
