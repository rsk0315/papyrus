// returns n \equiv (a/b) (mod m)
i32 moddiv(i32 a, i32 b, i32 m) {
    i64 n=a*modpow(b, m-2, m)%m;
    return (i32)n;
}
