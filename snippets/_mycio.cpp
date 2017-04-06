#include <cstdio>
#include <cstdlib>
#include <cstdint>
#include <cstddef>
#include <cstring>
#include <cctype>
#include <numeric>

class FastScanner {
    static const size_t BUF_SIZE=(1<<17);
    static char *pos, buf[BUF_SIZE|1], *endbuf;
    const double FLT_FALLBACK=strtod("NaN", nullptr);
    bool buffer() {
        size_t len=fread(buf, 1, BUF_SIZE, stdin);
        buf[len] = '\0';
        endbuf = buf + len;
        pos = buf;
        return len;
    }
    bool buffer(ptrdiff_t oft) {
        size_t len=fread(buf, 1, BUF_SIZE, stdin);
        buf[oft+=len] = '\0';
        endbuf = buf + oft;
        pos = buf;
        return len;
    }
public:
    FastScanner() {
        buffer();
    }
    bool scan(double &d) {
        if (*pos == '\0' && !buffer()) {
            d = FLT_FALLBACK;
            return false;
        }

        char *endpos;
        d = strtod(pos, &endpos);

        while (endpos == pos)
            // no conversion is performed;
            // there are no floating-point expressions
            if (!buffer()) {
                d = FLT_FALLBACK;
                return false;
            }

        if (endpos >= endbuf) {
            // reaches EOB while parsing the string;
            // parsed string may be incomplete
            // (assume the expression is shorter than the buffer)
            ptrdiff_t left=endbuf-pos;
            memcpy(buf, pos, left);
            if (buffer(left))
                d = strtod(buf, &pos);
        }

        return true;
    }
    bool scan(char &c) {
        c = *pos++;
        if (c != '\0') return true;
        if (!buffer()) return false;

        c = *pos++;
        return true;
    }
    bool scan(char *s) {
        char *startpos=nullptr;
        for (;; ++pos) {
            char tmp=*pos;
            if (tmp == '\0') {
                // unbuffers to the argument when reaching EOB
                if (startpos) {
                    ptrdiff_t count=pos-startpos;
                    memcpy(s, startpos, count);
                    s += count;
                }

                if (!buffer()) {
                    *s = '\0';
                    return startpos;
                }

                tmp = *buf;
                if (startpos)
                    startpos = buf;
            }

            if (!isspace(tmp)) {
                if (!startpos) {
                    startpos = pos;
                }
            } else if (startpos) {
                ptrdiff_t count=pos-startpos;
                memcpy(s, startpos, count);
                s[count] = '\0';
                ++pos;
                return true;
            }

            // nop until a non-whitespace character appears
        }
    }
    template <class Integral>
    bool scan(
        Integral &i,
        typename std::enable_if<std::is_signed<Integral>::value>::type*_=0
    ) {
        bool started=false, neg=false;
        i = 0;
        for (;; ++pos) {
            char tmp=*pos;
            if (tmp == '\0') {
                if (!buffer()) return started;

                tmp = *pos;
            }

            if (isdigit(tmp)) {
                started = true;
                i = i*10 + tmp-'0';
            } else if (started) {
                break;
            } else if (tmp == '-') {
                neg = true;
            }
        }

        if (neg) i = -i;
        return true;
    }
    template <class Integral>
    bool scan(
        Integral &u,
        typename std::enable_if<!std::is_signed<Integral>::value>::type*_=0
    ) {
        // assumes that the unsigned expression has no signs for optimization
        bool started=false;
        u = 0;
        for (;; ++pos) {
            char tmp=*pos;
            if (tmp == '\0') {
                if (!buffer()) return started;

                tmp = *pos;
            }

            if (isdigit(tmp)) {
                started = true;
                u = u*10 + tmp-'0';
            } else if (started) {
                return true;
            }
        }
    }
    template <class CTypes, class... Rest>
    bool scan(CTypes &&first, Rest&&... rest) {
        return scan(first) && scan(rest...);
    }
    bool scanln(char *s) {
        char *src=pos, *dst=s;
        for (;; ++pos) {
            char tmp=*pos;
            if (tmp == '\0') {
                ptrdiff_t count=pos-src;

                // assume that s has enough capacity
                memcpy(dst, src, count);
                dst += count;

                if (!buffer()) {
                    *dst = '\0';
                    return dst != s;
                }

                src = buf;
                tmp = *buf;
            }

            if (tmp == '\n') {
                ++pos;
                ptrdiff_t count=pos-src;
                memcpy(dst, src, count);
                dst[count] = '\0';
                return true;
            }

            // nop until the current line ends
        }
    }
    template <class CharArray, class... Rest>
    bool scanln(CharArray &&first, Rest&&... rest) {
        return scanln(first) && scanln(rest...);
    }
    char peek() {
        if (*pos == '\0')
            buffer();

        return *pos;
    }
    bool ignore(char delim) {
        for (;; ++pos) {
            if (*pos == '\0' && !buffer())
                return false;

            if (*pos != delim)
                return true;
        }
    }
    bool ignore() {
        for (;; ++pos) {
            if (*pos == '\0' && !buffer())
                return false;

            if (!isspace(*pos))
                return true;
        }
    }
    bool advance() {
        // advances the pointer and returns the next character is safe
        if (!*pos && !buffer()) return false;

        return *++pos;
    }
    bool advance(ptrdiff_t i) {
        if (!*pos && !buffer()) return false;

        for (ptrdiff_t left=endbuf-pos; left<=i;) {
            i -= left;
            if (!buffer()) return false;

            left = endbuf-pos;
        }

        pos += i;
        return  *pos;
    }
    template <class T>
    T next() {
        T tmp;
        scan(tmp);
        return tmp;
    }
    template <class T>
    FastScanner &operator >>(T &tmp) {
        scan(tmp);
        return *this;
    }
} cin;

char FastScanner::buf[], *FastScanner::pos=buf;
char *FastScanner::endbuf=pos+BUF_SIZE;

class FastPrinter {
    static const size_t BUF_SIZE=(1<<17);
    static char *pos, buf[BUF_SIZE|1], *endbuf;
    const char FLT_FORMAT[6]="%.16f";
    const size_t INT_LEN=20, FLT_LEN=330;
    void weak_flush() {
        // flushes the internal buffer, but not flushing stdout
        fwrite(buf, 1, pos-buf, stdout);
        pos = buf;
    }
public:
    void print(double d) {
        char minibuf[FLT_LEN];
        size_t count=sprintf(minibuf, FLT_FORMAT, d);
        char *tmp=pos+count;
        if (tmp >= endbuf) {
            weak_flush();
            tmp = buf+count;
        }

        memcpy(pos, minibuf, count);
        pos = tmp;
    }
    void print(char c) {
        if (pos+1 >= endbuf)
            weak_flush();

        *pos++ = c;
    }
    void print(const char *s) {
        size_t count=strlen(s);
        char *tmp=pos+count;
        if (tmp >= endbuf) {
            weak_flush();
            tmp = buf + count;
        }

        if (count >= BUF_SIZE) {
            fwrite(s, 1, count, stdout);
            return;
        }

        memcpy(pos, s, count);
        pos = tmp;
    }
    template <size_t N>
    void print(const char (&s)[N]) {
        size_t count=N-1;
        char *tmp=pos+count;
        if (tmp >= endbuf) {
            weak_flush();
            tmp = buf + count;
        }

        if (count >= BUF_SIZE) {
            fwrite(s, 1, count, stdout);
            return;
        }

        memcpy(pos, s, count);
        pos = tmp;
    }
    template <class Integral>
    void print(
        Integral i,
        typename std::enable_if<std::is_signed<Integral>::value>::type*_=0
    ) {
        if (pos+INT_LEN >= endbuf)
            weak_flush();

        if (i == 0) {
            *pos++ = '0';
            return;
        }

        char minibuf[INT_LEN], *minipos=minibuf+INT_LEN, *endminibuf=minipos;
        if (i < 0) {
            *pos++ = '-';
            i = -i;
        }

        while (i) {
            *--minipos = i%10 + '0';
            i /= 10;
        }

        memcpy(pos, minipos, endminibuf-minipos);
        pos += endminibuf-minipos;
    }
    template <class Integral>
    void print(
        Integral u,
        typename std::enable_if<!std::is_signed<Integral>::value>::type*_=0
    ) {
        if (pos+INT_LEN >= endbuf)
            weak_flush();

        if (u == 0) {
            *pos++ = '0';
            return;
        }

        char minibuf[INT_LEN], *minipos=minibuf+INT_LEN, *endminibuf=minipos;
        while (u) {
            *--minipos = u%10 + '0';
            u /= 10;
        }

        memcpy(pos, minipos, endminibuf-minipos);
        pos += endminibuf-minipos;
    }
    template <class CTypes, class... Rest>
    void print(CTypes first, Rest&&... rest) {
        // prints arguments without separating characters
        print(first), print(rest...);
    }
    template <class CTypes>
    void println(CTypes first) {
        print(first, '\n');
    }
    template <class CTypes, class... Rest>
    void println(CTypes first, Rest&&... rest) {
        // prints arguments separated by a single space and terminates the line
        print(first, ' '), println(rest...);
    }
    template <class CTypes>
    void printlns(CTypes first) {
        print(first, '\n');
    }
    template <class CTypes, class... Rest>
    void printlns(CTypes first, Rest&&... rest) {
        // prints each of arguments per line
        print(first, '\n'), printlns(rest...);
    }
    void flush() {
        // flushes the buffer
        // should be called before main() returns
        fwrite(buf, 1, pos-buf, stdout);
        fflush(stdout);
        pos = buf;
    }
    template <class T>
    FastPrinter &operator <<(T tmp) {
        print(tmp);
        return *this;
    }
    ~FastPrinter() {
        flush();
    }
} cout;

char FastPrinter::buf[], *FastPrinter::pos=buf;
char *FastPrinter::endbuf=buf+BUF_SIZE;
