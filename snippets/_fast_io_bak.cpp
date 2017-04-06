#include <cstdio>
#include <cstdlib>
#include <cstdint>
#include <cstddef>
#include <cstring>
#include <numeric>

class FastIO {
    // output buffer must be larger than each output
    static const size_t BUF_SIZE=(1<<17);
    static constexpr char FLT_FORMAT[]="%.16f";
    static const size_t INT_LEN=20, FLT_LEN=330;
    static char inbuf[BUF_SIZE|1], *inptr, *endinbuf;
    static char outbuf[BUF_SIZE|1], *outptr, *endoutbuf;
    static void weak_flush() {
        // flushes the internal buffer, but not flushing stdout
        fwrite(outbuf, 1, outptr-outbuf, stdout);
        outptr = outbuf;
    }
    static void buffer() {
        // reads characters from stdin and buffers
        size_t len=fread(inbuf, 1, BUF_SIZE, stdin);
        inbuf[len] = '\0';
        inptr = inbuf;
    }
    static void buffer(size_t oft) {
        size_t len=fread(inbuf+oft, 1, BUF_SIZE-oft, stdin);
        inbuf[oft+len] = '\0';
    }
public:
    static void scan(double &d) {
        if (*inptr == '\0')
            buffer();

        char *tmp;
        d = strtod(inptr, &tmp);
        if (tmp < endinbuf && tmp != inptr) {
            // successfully scanned
            inptr = tmp;
            return;
        }

        // reachs EOB before/while converting
        ptrdiff_t left=endinbuf-inptr;
        memcpy(inbuf, inptr, left);
        buffer(left);

        d = strtod(inbuf, &inptr);
    }
    static void scan(char &c) {
        c = *inptr++;
        if (c != '\0') return;

        // reaches EOB
        buffer();
        c = *inptr++;
    }
    static void scan(char *s) {
        char *pos=inptr, *src=pos;
        bool started=false;
        for (;; ++pos) {
            char tmp=*pos;
            if (tmp == '\0') {
                // unbuffers and rebuffers if reaches EOB
                ptrdiff_t count=pos-src;
                memcpy(s, src, count);
                s += count;

                buffer();
                pos = src = inbuf;
                tmp = *inbuf;
            }

            if (tmp != ' ' && tmp != '\n') {
                // not delimiters
                if (!started) {
                    started = true;
                    src = pos;
                }
            } else if (started) {
                memcpy(s, src, pos-src);
                s[pos-src] = '\0';
                inptr = ++pos;
                return;
            }

            // nops until non-delimiter char appears
        }
    }
    template <class Integral>
    static void scan(
        Integral &i,
        typename std::enable_if<std::is_signed<Integral>::value>::type*_=0
    ) {
        bool started=false, neg=false;
        i = 0;
        for (;;) {
            char tmp=*inptr++;
            if (tmp == '\0') {
                buffer();
                tmp = *inptr++;
            }

            if (tmp >= '0' && tmp <= '9') {
                started = true;
                i = i*10 + tmp-'0';
            } else if (started) {
                ++tmp;
                break;
            } else if (tmp == '-') {
                neg = true;
            }
        }

        if (neg) i = -i;
    }
    template <class Integral>
    static void scan(
        Integral &u,
        typename std::enable_if<!std::is_signed<Integral>::value>::type*_=0
    ) {
        bool started=false;
        u = 0;
        for (;;) {
            char tmp=*inptr++;
            if (tmp == '\0') {
                buffer();
                tmp = *inptr++;
            }

            if (tmp >= '0' && tmp <= '9') {
                started = true;
                u = u*10 + tmp-'0';
            } else if (started) {
                ++tmp;
                break;
            }
        }
    }
    template <class Arithmetic, class... Rest>
    static void scan(Arithmetic &&x, Rest&&... y) {
        scan(x);
        scan(y...);
    }
    static void scanln(char *s) {
        char *pos=inptr, *src=pos;
        bool started=false;
        for (;; ++pos) {
            char tmp=*pos;
            if (tmp == '\0') {
                // unbuffers and rebuffers if reaches EOB
                ptrdiff_t count=pos-src;
                memcpy(s, src, count);
                s += count;

                buffer();
                pos = src = inbuf;
                tmp = *inbuf;
            }

            if (tmp != '\n') {
                // not newline
                if (!started) {
                    started = true;
                    src = pos;
                }
            } else if (started) {
                memcpy(s, src, pos-src);
                s[pos-src] = '\0';
                inptr = ++pos;
                return;
            }

            // nops until non-delimiter char appears
        }
    }
    static void eat_space() {
        for (;; ++inptr) {
            if (*inptr == '\0')
                buffer();

            if (*inptr != ' ' && *inptr != '\n')
                return;
        }
    }
    static void print(double d) {
        char minibuf[FLT_LEN];
        size_t count=snprintf(minibuf, sizeof minibuf, FLT_FORMAT, d);
        char *tmp=outptr+count;
        if (tmp >= endoutbuf) {
            weak_flush();
            tmp = outbuf+count;
        }

        memcpy(outptr, minibuf, count);
        outptr = tmp;
    }
    static void print(char c) {
        if (outptr+1 >= endoutbuf)
            weak_flush();

        *outptr++ = c;
    }
    static void print(const char *s) {
        size_t count=strlen(s);
        char *tmp=outptr+count;
        if (tmp >= endoutbuf) {
            weak_flush();
            tmp = outbuf + count;
        }

        memcpy(outptr, s, count);
        outptr = tmp;
    }
    static void print(char *s) {
        size_t count=strlen(s);
        char *tmp=outptr+count;
        if (tmp >= endoutbuf) {
            weak_flush();
            tmp = outbuf + count;
        }

        memcpy(outptr, s, count);
        outptr = tmp;
    }
    template <size_t N>
    static void print(const char (&s)[N]) {
        size_t count=strlen(s);
        char *tmp=outptr+count;
        if (tmp >= endoutbuf) {
            weak_flush();
            tmp = outbuf + count;
        }

        memcpy(outptr, s, count);
        outptr = tmp;
    }
    template <class Integral>
    static void print(
        Integral i,
        typename std::enable_if<std::is_signed<Integral>::value>::type*_=0
    ) {
        if (outptr+INT_LEN >= endoutbuf)
            weak_flush();

        if (i == 0) {
            *outptr++ = '0';
            return;
        }

        char minibuf[INT_LEN], *pos=minibuf+INT_LEN, *endminibuf=pos;
        if (i < 0) {
            *outptr++ = '-';
            i = -i;
        }

        while (i) {
            *--pos = i%10 + '0';
            i /= 10;
        }

        memcpy(outptr, pos, endminibuf-pos);
        outptr += endminibuf-pos;
    }
    template <class Integral>
    static void print(
        Integral u,
        typename std::enable_if<!std::is_signed<Integral>::value>::type*_=0
    ) {
        if (outptr+INT_LEN >= endoutbuf)
            weak_flush();

        if (u == 0) {
            *outptr++ = '0';
            return;
        }

        char minibuf[INT_LEN], *pos=minibuf+INT_LEN, *endminibuf=pos;

        while (u) {
            *--pos = u%10 + '0';
            u /= 10;
        }

        memcpy(outptr, pos, endminibuf-pos);
        outptr += endminibuf-pos;
    }
    template <class T, class... Rest>
    static void print(T x, Rest&&... y) {
        // prints arguments without separating characters
        print(x);
        print(y...);
    }
    template <class T>
    static void println(T x) {
        print(x, '\n');
    }
    template <class T, class... Rest>
    static void println(T x, Rest&&... y) {
        // prints arguments separated by a single space and terminates the line
        print(x, ' ');
        println(y...);
    }
    template <class T>
    static void printlns(T x) {
        print(x, '\n');
    }
    template <class T, class... Rest>
    static void printlns(T x, Rest&&... y) {
        // prints each of arguments per line
        print(x, '\n');
        printlns(y...);
    }
    static void flush() {
        // flushes the buffer
        // should be called before main() returns
        fwrite(outbuf, 1, outptr-outbuf, stdout);
        fflush(stdout);
        outptr = outbuf;
    }
};

char FastIO::inbuf[], *FastIO::inptr=FastIO::inbuf;
char *FastIO::endinbuf=FastIO::inbuf+FastIO::BUF_SIZE;
char FastIO::outbuf[], *FastIO::outptr=FastIO::outbuf;
char *FastIO::endoutbuf=FastIO::outbuf+FastIO::BUF_SIZE;
constexpr char FastIO::FLT_FORMAT[];
