class ModChoose {
    std::vector<int64_t> modfact_table;
    int64_t mod;
    int64_t moddiv(int64_t a, int64_t b) {
        int64_t n=a, k=b%mod, p=mod-2;
        while (p) {
            if (p & 1)
                (n *= k) %= mod;

            (k *= k) %= mod;
            p >>= 1;
        }

        return n;
    }
    int64_t modfact(int64_t n, int64_t &e) {
        // a p**e == n!
        int64_t a=1;
        while (n) {
            int64_t m=n/mod;
            if (m & 1) {
                (a *= mod - modfact_table[n%mod]) %= mod;
            } else {
                (a *= modfact_table[n%mod]) %= mod;
            }

            e += (n = m);
        }

        return a;
    }
public:
    ModChoose(size_t n, int64_t mod): modfact_table(n, 1), mod(mod) {
        size_t m=std::min<size_t>(n, mod);
        for (size_t i=1; i<m; ++i)
            modfact_table[i] = (modfact_table[i-1]*i) % mod;
    }
    int64_t get(int64_t n, int64_t k) {
        if (n < 0 || k < 0 || n < k) return 0;

        int64_t e1, e2, e3;
        int64_t a1, a2, a3;
        a1 = modfact(n, e1);
        a2 = modfact(k, e2);
        a3 = modfact(n-k, e3);

        if (e1 > e2+e3) return 0;
        return moddiv(a1, a2*a3);
    }
};
