void test_read_double(int n) {
    double d=0.0;
    for (int i=0; i<n; ++i) {
        double f;
        FastIO::scan(f);
        FastIO::println(f);
        d += f;
    }

    fprintf(stderr, "%.12f\n", d);
}

void test_read_string(int n) {
    int count=0;
    for (int i=0; i<n; ++i) {
        char str[1<<7];
        FastIO::scan(str);
        FastIO::println(str);

        ++count;
    }
}

void test_read_stringln(int n) {
    int count=0;
    FastIO::ignore();
    for (int i=0; i<n; ++i) {
        char str[1<<7];
        FastIO::scanln(str);
        FastIO::printlns(str);

        ++count;
    }
}

void test_read_char(int n) {
    for (int i=0; i<n; ++i) {
        char c;
        FastIO::scan(c);
        FastIO::print(c, " (", int(c), ")\n");
    }
}

void test_read_signed(int n) {
    for (int i=0; i<n; ++i) {
        signed m;
        FastIO::scan(m);
        FastIO::println(m);
    }
}

void test_read_unsigned(int n) {
    for (int i=0; i<n; ++i) {
        unsigned m;
        FastIO::scan(m);
        FastIO::println(m);
    }
}

int main() {
    signed n;
    FastIO::scan(n);
    test_read_double(n);

    FastIO::scan(n);
    test_read_string(n);

    FastIO::scan(n);
    test_read_stringln(n);

    FastIO::scan(n);
    test_read_char(n);

    FastIO::scan(n);
    test_read_signed(n);

    FastIO::scan(n);
    test_read_unsigned(n);

    FastIO::flush();
}

/*
Sample input:
3
0.1 2.3 4.5
1
ABC
2
ABC DE

2
ab
3
-1 -2 -3
4
-4 -5 -6 -7
-- end input

Expected output:
0.1000000000000000
2.2999999999999998
4.5000000000000000
ABC
ABC DE



a (97)
b (98)
-1
-2
-3
4
5
6
7
-- end output
*/
