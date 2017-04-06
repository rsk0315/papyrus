template <class Int, Int mod, Int omega=0>
class QuotRing {
    Int n;
public:
    QuotRing(Int n=0): n(n%mod) {}
    inline QuotRing &operator =(const Int rhs) {
        n = rhs % mod;
        return *this;
    }
    inline QuotRing &operator +=(const QuotRing &rhs) {
        (n += rhs.n) %= mod;
        return *this;
    }
    inline QuotRing &operator -=(const QuotRing &rhs) {
        (n += mod - rhs.n%mod) %= mod;
        return *this;
    }
    inline QuotRing &operator *=(const QuotRing &rhs) {
        (n *= rhs.n) %= mod;
        return *this;
    }
    inline QuotRing &operator /=(const QuotRing &rhs) {
        return (*this) *= rhs.reciprocal();
    }
    QuotRing &operator ^=(Int rhs) {
        QuotRing tmp(n);
        for (n=1; rhs; rhs>>=1) {
            if (rhs & 1)
                *this *= tmp;
 
            tmp *= tmp;
        }
        return *this;
    }
    inline QuotRing operator +(const QuotRing &rhs) const {
        QuotRing tmp(*this);
        return tmp += rhs;
    }
    inline QuotRing operator -(const QuotRing &rhs) const {
        QuotRing tmp(*this);
        return tmp -= rhs;
    }
    inline QuotRing operator *(const QuotRing &rhs) const {
        QuotRing tmp(*this);
        return tmp *= rhs;
    }
    inline QuotRing operator /(const QuotRing &rhs) const {
        QuotRing tmp(*this);
        return tmp /= rhs;
    }
    inline QuotRing operator ^(const Int rhs) const {
        QuotRing tmp(*this);
        return tmp ^= rhs;
    }
    inline QuotRing reciprocal() const {
        return (*this) ^ (mod-2);
    }
    inline Int to_i() const {
        return n;
    }

    friend istream &operator >>(istream &is, QuotRing &qr) {
        return is >> qr.n;
    }
    friend ostream &operator <<(ostream &os, const QuotRing &qr) {
        return os << qr.n;
    }
};
