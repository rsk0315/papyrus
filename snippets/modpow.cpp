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
