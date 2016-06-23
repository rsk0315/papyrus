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

#define key first
#define val second
#define debug(o) cerr << #o << ": " << (o) << endl;
#define debugl(o) cerr << #o << ": " << (o) << " (L" << __LINE__ << ")\n";
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
typedef map<int, string> mis;
typedef map<char, int> mci;
typedef map<char, char> mcc;
typedef map<char, string> mcs;
typedef map<string, int> msi;
typedef map<string, string> mss;

const i32 MOD=1e9+7;
const f64 EPS=1e-10;
const int di[4]={1,0,-1,0}, dj[4]={0,1,0,-1};
const int dI[8]={-1,0,1,-1,1,-1,0,1}, dJ[8]={-1,-1,-1,0,0,1,1,1};

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
        if (use_const_func) {
            return (*cfunc)(x, y);
        } else {
            return (*vfunc)(x, y);
        }
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

// returns n = (b**p) mod m
i32 modpow(i32 b, i32 p, i32 m) {
    i64 n=1, a=b%m;
    while (p) {
        if (p & 1) {
            n *= a;
            n %= m;
        }
        a *= a;
        a %= m;
        p >>= 1;
    }
    return (i32)n;
}

// returns n \equiv (a/b) (mod m)
i32 moddiv(i32 a, i32 b, i32 m) {
    i64 n=a*modpow(b, m-2, m)%m;
    return (i32)n;
}


int main(void) {
    
    return 0;
}
