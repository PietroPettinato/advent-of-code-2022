######################################
##############  PART 1  ##############
######################################

class Tree:
    def __init__(self, name, father, data):
        self.name = name
        self.father = father
        self.children = []
        self.data = data

    def print_tree(self, space):
        print(space, self.name, add_dir_vals(self))
        for c in self.children:
            c.print_tree(str(space + '  '))

    def get_root(self):
        if self.father is None:
            return self
        return self.father.get_root()

    def add_children(self, c):
        self.children.append(c)

    def get_children(self, name):
        for c in self.children:
            if c.name == name:
                return c
        return None


def add_dir_vals(node: Tree):
    tot = node.data
    for c in node.children:
        tot += add_dir_vals(c)
    return tot


def walk_tree(node):
    tot_size = add_dir_vals(node)
    folders = []
    if tot_size <= 100000:
        # return node.name, tot_size
        folders.append(node)
    for c in node.children:
        folders.extend(walk_tree(c))
    return folders


def target_folder(node, space_needed):
    min_folder = None
    size = add_dir_vals(node)
    if size >= space_needed:
        min_folder = node
        for c in node.children:
            n = target_folder(c, space_needed)
            if n is not None:
                if add_dir_vals(n) < size:
                    min_folder = n
                    size = add_dir_vals(n)
    return min_folder


with open('input.txt') as f:
    node = None
    for line in f.readlines():
        match line[0:4]:
            case '$ cd':
                if line.strip('$ cd ').strip('\n') == '..':
                    node = node.father
                else:
                    try:
                        node = node.get_children(line[5:].strip('\n'))
                    except Exception:
                        node = Tree(line[5:].strip('\n'), node, 0)  # first time
            case '$ ls':
                pass
            case 'dir ':
                c = Tree(line[4:].strip('\n'), node, 0)
                node.add_children(c)
            case _:
                node.data += int(line.split()[0])

    root = node.get_root()
    print('\n--- File tree ---\n')
    root.print_tree('')
    folders = walk_tree(root)
    # print(folders)
    tot = 0
    for fo in folders:
        tot += add_dir_vals(fo)
    print('\n\nThe total size of selected folders is', tot)

    ######################################
    ##############  PART 2  ##############
    ######################################

    print('\n\n\nSpace used: ', add_dir_vals(root))
    print('Space free: ', 70000000 - add_dir_vals(root))
    space_needed = 30000000 - (70000000 - add_dir_vals(root))
    print('Space needed for the update: ', space_needed)

    min_folder = target_folder(root, space_needed)
    print('The folder that must be deleted is', min_folder.name, 'with size', add_dir_vals(min_folder))

f.close()
