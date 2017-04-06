#ifdef NO_UNLOCK_IO
#define getchar_unlocked getchar
#define putchar_unlocked putchar
#endif

struct FastIO {
    static void scan(double &x) {
        scanf("%lf", &x);
    }
    template <class Integral>
    static void scan(Integral &x) {
        int k, m=0;
        x = 0;
        for (;;) {
            k = getchar_unlocked();
            if (k == '-') {
                m = 1;
                break;
            } else if ('0' <= k && k <= '9') {
                x = k-'0';
                break;
            }
        }
        for (;;) {
            k = getchar_unlocked();
            if (k < '0' || k > '9')
                break;

            x = x*10 + k-'0';
        }

        if (m)
            x = -x;
    }
    template <class Arithmetic, class... Rest>
    static void scan(Arithmetic &x, Rest&... y) {
        scan(x);
        scan(y...);
    }
    static void print(double x, char c) {
        printf("%.12f%c", x, c);
    }
    static void print(const char *x, char c) {
        printf("%s%c", x, c);
    }
    template <class Integral>
    static void print(Integral x, char c) {
        int s=0, m=0;
        char f[20];
        if (x < 0) {
            m = 1;
            x = -x;
        }
        while (x) {
            f[s++] = x%10;
            x /= 10;
        }

        if (!s)
            f[s++] = 0;

        if (m) putchar_unlocked('-');
        while (s--)
            putchar_unlocked(f[s]+'0');

        putchar_unlocked(c);
    }
    template <class Arithmetic>
    static void println(Arithmetic x) {
        print(x, '\n');
    }
};
