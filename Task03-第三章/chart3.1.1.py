import numpy as np

# 假设我们已经学习到了简化的二维词向量
embeddings = {
    "king": np.array([0.9, 0.8]),
    "queen": np.array([0.9, 0.2]),
    "man": np.array([0.7, 0.9]),
    "woman": np.array([0.7, 0.3]),
    "egg": np.array([0.2, 0.1]),
    "chicken": np.array([0.3, 0.2]),
    "duck": np.array([0.4, 0.5]),
}

def cosine_similarity(vec1, vec2):
    dot_product = np.dot(vec1, vec2)
    norm_product = np.linalg.norm(vec1) * np.linalg.norm(vec2)
    return dot_product / norm_product

# king - man + woman
result_vec = embeddings["king"] - embeddings["man"] + embeddings["woman"]
result_vec2=embeddings["egg"]-embeddings["chicken"]+embeddings["duck"] 
# 计算结果向量与 "queen" 的相似度
sim = cosine_similarity(result_vec, embeddings["queen"])
sim2=cosine_similarity(result_vec2, embeddings["egg"])

print(f"king - man + woman 的结果向量: {result_vec}")
print(f"该结果与 'queen' 的相似度: {sim:.4f}")
print(f"egg - chicken + duck 的结果向量: {result_vec2}")
print(f"该结果与 'egg' 的相似度: {sim2:.4f}")

