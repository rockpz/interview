'''
二叉树遍历：
深度优先遍历：DFS depth first search
1. 访问顶点v
2. 依次从v的未访问的邻节点出发，对图进行深度优先遍历；
   直到图中的v有路径相通的顶点都被访问；
3. 若此时图中有顶点未被访问，则从一个未被访问的顶点出发，
   重新进行深度优先遍历，直到图中所有顶点均被访问过为止
前序遍历 pre-order traversal    根 左 右
中序遍历 in-order traversal     左 根 右
后序遍历 post-order traversal   左 右 根

广度优先遍历：BFS breadth first search
1. 首先将根节点放入队列中
2. 从队列中取出第一个节点，并检验它是否为目标。
   如果找到目标，则结束搜寻并回传结果。
   否则将它所有尚未检验过的直接子节点加入队列中。
3. 若队列为空，表示整张图都检查过了，即图中没有欲搜寻的目标。
   结束搜寻并回传找不到目标。
4. 重复步骤2。
'''

class TreeNode():
	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None


class BinaryTree():
	def __init__(self):
		pass
