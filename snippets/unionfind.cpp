struct UnionFindTree {
    int n;
    vector<int> tree;
    UnionFindTree(int m) {
        tree = vector<int>(n=m, -1);
    }
    int find_root(int v) {
        if (tree[v] < 0) return v;
        return tree[v] = find_root(tree[v]);
    }
    bool unite(int x, int y) {
        x = find_root(x);
        y = find_root(y);
        if (x == y) return false;
        if (rank(x) < rank(y)) swap(x, y);
        tree[x] += tree[y];
        tree[y] = x;
        return true;
    }
    int rank(int v) {
        return -tree[find_root(v)];
    }
};
