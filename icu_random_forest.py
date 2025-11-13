import numpy as np
from collections import Counter

class DecisionTree:
  def __init__(self, max_depth = 10, n_features = None, min_samples_split = 2):
    self.max_depth = max_depth
    self.n_features = n_features
    self.min_smaples_split = min_samples_split
    self.tree = None

  def fit(self, X, y, depth = 0):
    n_feats = X.shape[1] if not self.n_features else min(self.n_features, X.shape[1])
    if depth >= self.max_depth or len(np.unique(y)) == 1 or len(y) < self.min_samples_split:
      self.tree = Counter(y).most_common(1)[0][0]
      return
    feat_idxs = np.random.choice(X.shape[1], n_feats, replace=False)
    best_gain, best_feat, best_thresh = -1, None, None
    for feat in feat_idxs:
      for thresh in np.unique(X[:, feat]):
        left, right = X[:, feat] <= thresh, X[:, feat] > thresh
        if left.sum() == 0 or right.sum() == 0: continue
        gain = self._entropy(y) - (left.sum() * self._entropy(y[left]) + right.sum() * self._entropy(y[right])) / len(y)
        if gain > best_gain:
          best_gain, best_feat, best_thresh = gain, feat, thresh
    self.tree = {'feat': best_feat, 'thresh': best_thresh, 'left': DecisionTree(self.max_depth, self.n_features, self.min_samples_split), 'right': DecisionTree(self.max_depth, self.n_features, self.min_samples_split)}
    left_mask = X[:, best_feat] <= best_thresh
    self.tree['left'].fit(X[left_mask], y[left_mask], depth + 1)
    self.tree['right'].fit(X[~left_mask], y[~left_mask], depth + 1)

    def _entropy(self, y):
        ps = np.bincount(y) / len(y)
        return -np.sum([p * np.log2(p) for p in ps if p > 0])

    def predict(self, X):
        if isinstance(self.tree, dict):
            mask = X[:, self.tree['feat']] <= self.tree['thresh']
            preds = np.zeros(len(X), dtype=int)
            if mask.sum() > 0: preds[mask] = self.tree['left'].predict(X[mask])
            if (~mask).sum() > 0: preds[~mask] = self.tree['right'].predict(X[~mask])
            return preds
        return np.full(len(X), self.tree, dtype=int)
class RandomForest:
    def __init__(self, n_trees=10, max_depth=10, n_features=None, min_samples_split=2):
        self.n_trees, self.max_depth, self.n_features, self.min_samples_split, self.trees = n_trees, max_depth, n_features, min_samples_split, []

    def fit(self, X, y):
        for _ in range(self.n_trees):
            idxs = np.random.choice(len(X), len(X), replace=True)
            tree = DecisionTree(self.max_depth, self.n_features, self.min_samples_split)
            tree.fit(X[idxs], y[idxs])
            self.trees.append(tree)

    def predict(self, X):
        preds = np.array([tree.predict(X) for tree in self.trees])
        return np.array([Counter(preds[:, i]).most_common(1)[0][0] for i in range(len(X))])

    def score(self, X, y):
        return (self.predict(X) == y).mean()
