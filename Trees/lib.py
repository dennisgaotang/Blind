from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class BinaryTree:
    def __init__(self, data):
        """
        Optional parameter `data` can be:
        - A list (level-order) -> Builds tree from list
        - A TreeNode -> Uses it as the root
        - None -> Creates an empty tree
        """
        if isinstance(data, str):  # If data is a list, build the tree
            data = data.split(",")
            self.root = self.build_tree(data)
        elif isinstance(data, TreeNode):  # If data is a TreeNode, set as root
            self.root = data
        else:
            self.root = None  # Default to an empty tree


    def build_tree(self, level_order):
        if not level_order or level_order[0] == "null":
            return None

        root = TreeNode(int(level_order[0]))
        queue = deque([root])
        i = 1

        while queue and i < len(level_order):
            current = queue.popleft()

            # Left child
            if i < len(level_order) and level_order[i] != "null":
                current.left = TreeNode(int(level_order[i]))
                queue.append(current.left)
            i += 1

            # Right child
            if i < len(level_order) and level_order[i] != "null":
                current.right = TreeNode(int(level_order[i]))
                queue.append(current.right)
            i += 1

        return root

    def get_root(self):
        return self.root

    def print_tree(self):
        """ Prints the tree in level-order format """
        print(self.level_order)

    def __str__(self):
        """ Override to print the tree as a visual representation """
        if not self.root:
            return "Empty Tree"

        lines = []
        queue = deque([(self.root, 0)])
        levels = {}

        # BFS traversal to store nodes by level
        while queue:
            node, level = queue.popleft()
            if level not in levels:
                levels[level] = []
            levels[level].append(str(node.val) if node else " ")

            if node:
                queue.append((node.left, level + 1))
                queue.append((node.right, level + 1))

        # Formatting tree output
        max_level = max(levels.keys())
        max_width = 2 ** max_level  # Approximate max width of tree

        for level in range(max_level + 1):
            space = " " * (max_width // (2 ** (level + 1)))
            line = space.join(levels[level]).center(max_width)
            lines.append(line)

        return "\n".join(lines)

# Example Usage
level_order = ["1", "2", "3", "null", "null", "4", "5"]
tree = BinaryTree(level_order)

# Print the structured tree format
print(tree)
