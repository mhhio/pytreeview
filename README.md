# PyTreeView

PyTreeView is a Python package that generates a tree-like structure of files inside specific directory in Markdown format. It's designed to help developers quickly visualize and share the structure of their Java projects.

## Installation

You can install PyTreeView using pip:

```
pip install pytreeview
```

## Usage

### Command Line

After installation, you can use PyTreeView from the command line:

```
pytreeview /path/to/your/java/project
```

To limit the depth of the tree:

```
pytreeview /path/to/your/java/project -d 3
```

This will display the directory tree up to 3 levels deep.

### Python Script

You can also use PyTreeView in your Python scripts:

```python
from pytreeview import generate_tree

project_path = "/path/to/your/java/project"
tree = generate_tree(project_path, max_depth=3)
print(tree)
```

## Features

- Generate a tree-like structure of Java projects
- Control the depth of the generated tree
- Ignore common directories and files (like .git, target, build)
- Output in Markdown format for easy sharing

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.