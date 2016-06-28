template <typename T>
class SegmentTree {
    private:
        typedef const T cT;
        int n;          // the number of nodes + 1
        vector<T> tree; // 1-indexed tree
        T e;            // neutral element for given func
        T (*vfunc)(T, T);
        cT& (*cfunc)(cT&, cT&);
        bool use_const_func;

        void make_tree(int m, T fill) {
            n = 1;
            while (n < m) n <<= 1;
            tree = vector<T>(n<<1, e=fill);
        }
        T func(T x, T y) {
            if (use_const_func) return (*cfunc)(x, y);
            else return (*vfunc)(x, y);
        }

    public:
        SegmentTree(int m, cT& (*f)(cT&, cT&)=max<T>, T fill=0) {
            cfunc = f;
            use_const_func = true;
            make_tree(m, fill);
        }
        SegmentTree(int m, T (*f)(T, T), T fill=0) {
            vfunc = f;
            use_const_func = false;
            make_tree(m, fill);
        }
        //   let leaf[i] == tree[n+i-1],
        // returns f(leaf[a], leaf[a+1], ..., leaf[b-1])
        T seg_value(int a, int b, int i=1, int l=0, int r=-1) {
            if (r == -1) r = n;
            if (a<=l && b>=r) return tree[i];

            T v=e;
            int c=(l+r)>>1;

            if (c > a) v = func(v, seg_value(a, b, i<<1|0, l, c));
            if (c < b) v = func(v, seg_value(a, b, i<<1|1, c, r));
            return v;
        }
        void store(int i, T x) {
            i += n;
            while (i) {
                tree[i] = func(tree[i], x);
                i >>= 1;
            }
        }
};
