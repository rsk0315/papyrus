class UnionFindTree {
    std::vector<int> tree;
public:
    UnionFindTree(size_t n): tree(n, -1) {}
    size_t find_root(size_t v) {
        if (tree[v] < 0) return v;
        return tree[v] = find_root(tree[v]);
    }
    bool unite(size_t x, size_t y) {
        x = find_root(x);
        y = find_root(y);
        if (x == y) return false;
        if (tree[x] > tree[y]) std::swap(x, y);
        tree[x] += tree[y];
        tree[y] = x;
        return true;
    }
    bool connected(size_t x, size_t y) {
        return find_root(x) == find_root(y);
    }
    size_t rank(size_t v) {
        return -tree[find_root(v)];
    }
};
