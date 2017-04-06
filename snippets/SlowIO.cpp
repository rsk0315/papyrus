#ifdef NO_UNLOCK_IO
#define getchar_unlocked getchar
#define putchar_unlocked putchar
#endif

struct FastIO {
    static char *ptr, buf[1<<8];
    template <class Integral>
    static void scan(Integral &x) {
        bool neg=false;
        x = 0;
        for (;;) {
            int tmp=*ptr++;
            if (tmp == '-') {
                neg = true;
                break;
            } else if ('0' <= tmp && tmp <= '9') {
                x = tmp-'0';
                break;
            } else if (tmp == '\n' || tmp == '\0') {
                fgets(buf, sizeof buf, stdin);
                ptr = buf;
            }
        }
        for (;;) {
            int tmp=(*ptr++)-'0';
            if (tmp < 0 || tmp > 9) break;

            (x *= 10) += tmp;
        }

        if (neg) x = -x;
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

char FastIO::buf[];
char *FastIO::ptr=FastIO::buf;
