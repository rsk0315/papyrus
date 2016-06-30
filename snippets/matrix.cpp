template <typename T>
struct Matrix {
    typedef vector<T> vT;
    typedef vector<vT> vvT;
    pair<int, int> size;
    vvT A;
    Matrix(void) {};
    Matrix(int h, int w) {
        size.first = h;
        size.second = w;
        A = vvT(h, vT(w));
    }
    Matrix(pair<int, int> s) {
        size = s;
        A = vvT(size.first, vT(size.second));
    }
    vT operator[](int i) const {
        return A[i];
    }
    vT& operator[](int i) {
        return A[i];
    }
    Matrix operator+(Matrix B)  {
        if (size != B.size)
            throw "ShapeNotAlignedException";

        Matrix<T> C(size);
        int i, j;
        for (i=0; i<size.first; i++)
            for (j=0; j<size.second; j++)
                C[i][j] = A[i][j] + B[i][j];

        return C;
    }
    Matrix operator+(void) {
        return *this;
    }
    Matrix operator-(void) {
        Matrix<T> B(size);
        int i, j;
        for (i=0; i<size.first; i++)
            for (j=0; j<size.second; j++)
                B[i][j] = -A[i][j];

        return B;
    }
    Matrix operator-(Matrix B) {
        if (size != B.size)
            throw "ShapeNotAlignedExcpetion";

        return *this+(-B);
    }
    Matrix operator*(Matrix B) {
        if (size.second != B.size.first)
            throw "ShapeNotAlignedException";

        int h=size.first, w=B.size.second;
        Matrix<T> C(h, w);
        int i, j, k;
        for (i=0; i<h; i++)
            for (j=0; j<w; j++)
                for (k=0; k<size.second; k++)
                    C[i][j] += A[i][k] * B[k][j];

        return C;
    }
    template <typename scalar>
    Matrix operator*(scalar x) {
        Matrix<T> B(size);
        int i, j;
        for (i=0; i<size.first; i++)
            for (j=0; j<size.second; j++)
                B[i][j] = x * A[i][j];

        return B;
    }
    Matrix operator^(Matrix B) {
        if (size != B.size)
            throw "ShapeNotAlignedException";

        Matrix<T> C(size);
        int i, j;
        for (i=0; i<size.first; i++)
            for (j=0; j<size.second; j++)
                C[i][j] = A[i][j] ^ B[i][j];

        return C;
    }
    Matrix operator&(Matrix B) {
        if (size.second != B.size.first)
            throw "ShapeNotAlignedException";

        int h=size.first, w=B.size.second;
        Matrix<T> C(h, w);
        int i, j, k;
        for (i=0; i<h; i++)
            for (j=0; j<w; j++)
                for (k=0; k<size.second; k++)
                    C[i][j] ^= A[i][k] & B[k][j];

        return C;
    }
    Matrix operator=(Matrix B) {
        size = B.size;
        A = B.A;
        return *this;
    }
    Matrix operator+=(Matrix B) {
        *this = *this + B;
        return *this;
    }
    Matrix operator-=(Matrix B) {
        *this = *this - B;
        return *this;
    }
    Matrix operator*=(Matrix B) {
        *this = *this * B;
        return *this;
    }
    Matrix operator&=(Matrix B) {
        *this = *this & B;
        return *this;
    }
    Matrix operator^=(Matrix B) {
        *this = *this ^ B;
        return *this;
    }
    bool operator==(Matrix B) {
        if (size != B.size) return false;

        int i, j;
        for (i=0; i<size.first; i++)
            for (j=0; j<size.second; j++)
                if (A[i][j] != B[i][j])
                    return false;

        return true;
    }
    bool operator!=(Matrix B) {
        return !(*this==B);
    }
    template <typename uint>
    Matrix pow(uint p) {
        Matrix B=A, P;
        int i;
        for (i=0; i<A.size; i++) {
            P[i][i] = 1;
        }
        while (p) {
            if (p & 1) {
                P *= B;
            }
            B *= B;
            p >>= 1;
        }
        return P;
    }
    template <typename uint>
    Matrix bitpow(uint p) {
        Matrix B=A, P;
        int i;
        for (i=0; i<A.size; i++) {
            // 0xFFFFFFFFFFFFFFFFuLL; identity element for '&'
            P[i][i] = -1;
        }
        while (p) {
            if (p & 1) {
                P &= B;
            }
            B &= B;
            p >>= 1;
        }
        return P;
    }
};

template <typename T, typename scalar>
Matrix<T> operator*(scalar x, Matrix<T> A) {
    return A*x;
}
