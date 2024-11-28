def parse_tree(traversal):
    """전위 순회 문자열을 트리로 파싱하는 함수"""
    stack = []
    root = []
    current = root
    
    for token in traversal.split():
        print(root)
        if token == '#':
            if stack:
                current = stack.pop()
        else:
            new_node = []
            current.append(new_node)
            stack.append(current)
            current = new_node
    
    return root[0] if root else []

def is_isomorphic(tree1, tree2):
    """두 트리가 동형인지 확인하는 함수"""
    # 자식 노드의 개수가 다르면 동형이 아님
    if len(tree1) != len(tree2):
        return False
    
    # 각각의 자식 노드들도 동형인지 확인
    # 자식 노드의 순서는 고려하지 않기 때문에 정렬한 후 비교
    sorted_tree1 = sorted(tree1, key=lambda x: str(x))
    sorted_tree2 = sorted(tree2, key=lambda x: str(x))
    
    for i in range(len(sorted_tree1)):
        if not is_isomorphic(sorted_tree1[i], sorted_tree2[i]):
            return False
    
    return True

def main():
    t = int(input())  # 테스트 케이스의 수 입력
    
    for _ in range(t):
        # 각 트리의 전위 순회 입력 받기
        tree1 = input().strip()
        tree2 = input().strip()
        
        # 전위 순회를 바탕으로 트리 구조로 변환
        tree1_structure = parse_tree(tree1)
        tree2_structure = parse_tree(tree2)
        
        # 두 트리가 동형인지 확인
        if is_isomorphic(tree1_structure, tree2_structure):
            print("The two trees are isomorphic.")
        else:
            print("The two trees are not isomorphic.")

if __name__ == "__main__":
    main()
