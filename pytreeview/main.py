import os
import argparse

def generate_tree(startpath, max_depth=None, ignore_dirs=None, ignore_files=None):
    if ignore_dirs is None:
        ignore_dirs = set(['.git', 'target', 'build'])
    if ignore_files is None:
        ignore_files = set(['.gitignore', '.DS_Store'])

    output = []
    for root, dirs, files in os.walk(startpath):
        dirs[:] = [d for d in dirs if d not in ignore_dirs]
        files = [f for f in files if f not in ignore_files]

        level = root.replace(startpath, '').count(os.sep)
        if max_depth is not None and level > max_depth:
            continue

        indent = '│   ' * (level - 1) + '├── ' if level > 0 else ''
        output.append(f'{indent}{os.path.basename(root)}/')

        if max_depth is not None and level == max_depth:
            continue

        for i, file in enumerate(files):
            if i == len(files) - 1 and len(dirs) == 0:
                file_indent = '│   ' * (level) + '└── '
            else:
                file_indent = '│   ' * (level) + '├── '
            output.append(f'{file_indent}{file}')

    return '\n'.join(output)

def main():
    parser = argparse.ArgumentParser(description='Generate a tree-like structure of files inside directory in Markdown format.')
    parser.add_argument('path', help='Path to the root directory')
    parser.add_argument('-d', '--depth', type=int, help='Maximum depth of the directory tree to display')
    args = parser.parse_args()

    tree = generate_tree(args.path, max_depth=args.depth)
    markdown_output = f"```\n{tree}\n```"
    print(markdown_output)

if __name__ == '__main__':
    main()