from tp5.btree import BinaryTree, bt_iter_dfs, Node

AST=BinaryTree

def eval_ast(ast: AST) -> float:
#{+/0, −/1, ×/2, ÷/3}.
    tab=[]
    for c in bt_iter_dfs(ast.root):
        tab.append(c.key)
    calcul= tab[0]
    for i in range(1,len(tab)):
        if tab[i]==0:
            calcul += tab[i+1]
        if tab[i]==1:
            calcul -= tab[i+1]
        if tab[i]==2:
            calcul *= tab[i+1]
        if tab[i]==3:
            calcul /= tab[i+1]
    return calcul

if __name__ == '__main__':
    a = AST(Node(2, Node(1, Node(10),Node(5)), Node(0, Node(30), Node(5))))
    print(eval_ast(a))