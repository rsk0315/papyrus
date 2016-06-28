template <typename T>
struct BinaryIndexedTree {
    int n;
    vector<T> tree; // 1-indexed tree; stores v[1], ..., v[n]
    BinaryIndexedTree(int m, T fill=0) {
        n = m;
        tree = vector<T>(n+1, fill);
    }
    // v[i] += w;
    void add(int i, T w) {
        int j;
        for (j=i; j<=n; j+=j&-j) {
            tree[i] += w;
        }
    }
    // returns sum of v[i] for i in [1, m]
    T sum(int m) {
        T sum_=0;
        int i;
        for (i=m; i>0; i-=i&-i) {
            sum_ += tree[i];
        }
        return sum_;
    }
};
