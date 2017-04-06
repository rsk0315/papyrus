template <class Int, Int mod, Int omega>
void modulo_transform(
    vector<QuotRing<Int, mod, omega>> &f,
    const vector<QuotRing<Int, mod, omega>> &psi
) {
    if (!omega) return;

    size_t n=f.size(), t=n;
    for (size_t m=1; m<n; m<<=1) {
        t >>= 1;
        for (size_t i=0; i<m; ++i) {
            size_t j1=2*i*t, j2=j1+t-1;
            QuotRing<Int, mod, omega> s=psi[m+i];
            for (size_t j=j1; j<=j2; ++j) {
                QuotRing<Int, mod, omega> u=f[j], v=f[j+t]*s;
                f[j] = u+v;
                f[j+t] = u-v;
            }
        }
    }
}

template <class Int, Int mod, Int omega>
void modulo_transform_inv(
    vector<QuotRing<Int, mod, omega>> &f,
    const vector<QuotRing<Int, mod, omega>> &psi_1
) {
    if (!omega) return;

    size_t n=f.size(), t=1;
    for (size_t m=n; m>1; m>>=1) {
        size_t j1=0, h=m>>1;
        for (size_t i=0; i<h; ++i) {
            size_t j2=j1+t-1;
            QuotRing<Int, mod, omega> s=psi_1[h+i];
            for (size_t j=j1; j<=j2; ++j) {
                QuotRing<Int, mod, omega> u=f[j], v=f[j+t];
                f[j] = u+v;
                f[j+t] = (u-v)*s;
            }
            j1 += t << 1;
        }
        t <<= 1;
    }
    QuotRing<Int, mod, omega> u=n; u^=(mod-2);
    for (size_t j=0; j<n; ++j)
        f[j] *= u;
}

template <class RandomIt>
void order_bitrev(RandomIt first, RandomIt last) {
    ptrdiff_t n=last-first, m=n-1;
    for (ptrdiff_t i=0, j=1; j<m; ++j) {
        for (ptrdiff_t k=n>>1; k>(i^=k); k>>=1);

        if (j < i) swap(first[i], first[j]);
    }
}

template <class Int, Int mod, Int omega>
vector<QuotRing<Int, mod, omega>> convolute(
    vector<QuotRing<Int, mod, omega>> &f, vector<QuotRing<Int, mod, omega>> &g
) {
    size_t n=1; {
        size_t tmp=f.size()+g.size();
        while (n < tmp) n <<= 1;
    }

    Int m=2*n;
    QuotRing<Int, mod, omega> z=omega; z^=(mod-1)/m;
    QuotRing<Int, mod, omega> w=z.reciprocal();
    vector<QuotRing<Int, mod, omega>> psi(n, 1), psi_1(n, 1);
    for (size_t i=1; i<n; ++i) {
        psi[i] = psi[i-1]*z;
        psi_1[i] = psi_1[i-1]*w;
    }

    order_bitrev(psi.begin(), psi.end());
    order_bitrev(psi_1.begin(), psi_1.end());

    f.resize(n);
    g.resize(n);

    modulo_transform(f, psi);
    modulo_transform(g, psi);

    vector<QuotRing<Int, mod, omega>> h(n);
    for (size_t i=0; i<n; ++i)
        h[i] = f[i] * g[i];

    modulo_transform_inv(h, psi_1);
    return h;
}
