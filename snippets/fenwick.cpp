template <class T>
struct FenwickTree {
    vector<T> x;
    FenwickTree (int n) {
        x = vector<T>(n, 0);
    }
    T sum(int i, int j) {
        if (i == 0) {
            T S=0;
            for (j; j>=0; j=(j&(j+1))-1)
                S += x[j];

            return S;
        } else {
            return sum(0, j) - sum(0, i-1);
        }
    }
    void add(int k, T a) {
        for (; k<x.size(); k|=k+1)
            x[k] += a;
    }
};
