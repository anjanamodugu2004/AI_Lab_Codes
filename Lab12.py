import math

def alpha_beta_pruning(node, depth, alpha, beta, is_max):
    if isinstance(game_tree[node], int):  
        return game_tree[node]
    
    if is_max:
        max_value = -math.inf
        for child in game_tree[node]:
            value = alpha_beta_pruning(child, depth + 1, alpha, beta, False)
            max_value = max(max_value, value)
            alpha = max(alpha, value)
            if beta <= alpha:
                break  
        return max_value
    else:
        min_value = math.inf
        for child in game_tree[node]:
            value = alpha_beta_pruning(child, depth + 1, alpha, beta, True)
            min_value = min(min_value, value)
            beta = min(beta, value)
            if beta <= alpha:
                break
        return min_value

def find_optimal_path(node, alpha, beta, is_max):
    path = [node]
    
    while node in game_tree and not isinstance(game_tree[node], int):
        if is_max:
            best_value = -math.inf
            best_child = None
            for child in game_tree[node]:
                value = alpha_beta_pruning(child, 0, alpha, beta, False)
                if value > best_value:
                    best_value = value
                    best_child = child
                alpha = max(alpha, best_value)
                if beta <= alpha:
                    break
        else:
            best_value = math.inf
            best_child = None
            for child in game_tree[node]:
                value = alpha_beta_pruning(child, 0, alpha, beta, True)
                if value < best_value:
                    best_value = value
                    best_child = child
                beta = min(beta, best_value)
                if beta <= alpha:
                    break
        path.append(best_child)
        node = best_child
        is_max = not is_max  
    
    return path

game_tree = {
    'A': ['B1', 'B2', 'B3'],
    'B1': ['C1', 'C2', 'C3'],
    'B2': ['C4', 'C5', 'C6'],
    'B3': ['C7', 'C8', 'C9'],
    'C1': 12, 'C2': 10, 'C3': 3,
    'C4': 5, 'C5': 8, 'C6': 10,
    'C7': 11, 'C8': 2, 'C9': 12
}

optimal_value = alpha_beta_pruning('A', 0, -math.inf, math.inf, True)
optimal_path = find_optimal_path('A', -math.inf, math.inf, True)

print("Optimal Value:", optimal_value)
print("Optimal Path:", " -> ".join(optimal_path))
