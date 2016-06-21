#include <iostream>
#include <string>
#include <algorithm>
#include <map>
#include <vector>
#include <cstdio>
#include <cmath>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <utility>

#define EPS (1e-9)
#define key first
#define val second
#define debug(o) cout << #o << " " << o << endl;
#define putd(d) printf("%d\n", d)
#define putf(f) printf("%.16f\n", f)
#define whole(s) s.begin(), s.end()

using namespace std;


typedef char i8;
typedef short i16;
typedef long i32;
typedef long long i64;
typedef float f32;
typedef double f64;
typedef unsigned char u8;
typedef unsigned short u16;
typedef unsigned long u32;
typedef unsigned long long u64;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef pair<int, int> pii;
typedef map<int, int> mii;
typedef map<int, char> mic;
typedef map<char, int> mci;
typedef map<string, int> msi;

struct UnionFind {
    int n;
    vector<int> d;
    UnionFind(void) {}
    UnionFind(int m) {
        n = m;
        d = vector<int>(n, -1);
    }
    int find_root(int v) {
        if (d[v] < 0) return v;
        return d[v] = find_root(d[v]);
    }
    bool unite(int x, int y) {
        x = find_root(x);
        y = find_root(y);
        if (x == y) return false;
        if (size(x) < size(y)) swap(x, y);
        d[x] += d[y];
        d[y] = x;
        return true;
    }
    int size(int v) {
        return -d[find_root(v)];
    }
};

template <typename T>
struct SegmentTree {
    int num_leaf;
    vector<T> d;
    T fill;
    T (*func)(T, T);
    const T& (*cfunc)(const T&, const T&);
    bool use_constfunc;

    SegmentTree(int n, const T& (*func_)(const T&, const T&)=max<T>, T fill_=0) {
        cfunc = func_;
        use_constfunc = true;
        num_leaf = 1;
        while (num_leaf < n) num_leaf <<= 1;
        fill = fill_;
        d = vector<T>(num_leaf<<1, fill);
    }
    SegmentTree(int n, T (*func_)(T, T), T fill_=0) {
        func = func_;
        use_constfunc = false;
        num_leaf = 1;
        while (num_leaf < n) num_leaf <<= 1;
        fill = fill_;
        d = vector<T>(num_leaf<<1, fill);
    }
    // returns f(d[i], d[i+1], ..., d[j]) for i, j in [a, b)
    T get_value(int a, int b, int node=1, int l=0, int r=-1) {
        if (r == -1) r = num_leaf;
        if (a<=l && b>=r) return d[node];

        T value=fill;
        int c=(l+r)>>1;

        if (use_constfunc) {
            if (c > a) value = (*cfunc)(value, get_value(a, b, node<<1|0, l, c));
            if (c < b) value = (*cfunc)(value, get_value(a, b, node<<1|1, c, r));
        } else {
            if (c > a) value = (*func)(value, get_value(a, b, node<<1|0, l, c));
            if (c < b) value = (*func)(value, get_value(a, b, node<<1|1, c, r));
        }
        return value;
    }
    void store(int i, T x) {
        int node=num_leaf+i;
        while (node) {
            if (use_constfunc) {
                d[node] = (*func)(d[node], x);
            } else {
                d[node] = (*cfunc)(d[node], x);
            }
            node >>= 1;
        }
    }
};

int main(void) {
    
    return 0;
}
