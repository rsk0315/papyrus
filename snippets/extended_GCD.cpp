int64_t ext_gcd(int64_t m, int64_t n, int64_t &x, int64_t &y) {
    /* Blankinship */
    for (int64_t u=y=1, v=x=0; m;) {
        int64_t q=n/m;
        std::swap(x-=q*u, u);
        std::swap(y-=q*v, v);
        std::swap(n-=q*m, m);
    }
    return n;
}
