#include <cstdio>
#include <cstdlib>
#include <cstdint>
#include <cstddef>
#include <cstring>
#include <cctype>
#include <numeric>

class FastIO {
    // output buffer must be larger than each output
    static const size_t BUF_SIZE=(1<<17);
    static constexpr char FLT_FORMAT[]="%.16f", FLT_FALLBACK[]="NaN";
    static const size_t INT_LEN=20, FLT_LEN=330;
    static char *inptr, inbuf[BUF_SIZE|1], *endinbuf;
    static char *outptr, outbuf[BUF_SIZE|1], *endoutbuf;
    static void weak_flush() {
        // flushes the internal buffer, but not flushing stdout
        fwrite(outbuf, 1, outptr-outbuf, stdout);
        outptr = outbuf;
    }
    static bool buffer() {
        // reads characters from stdin and buffers
        size_t len=fread(inbuf, 1, BUF_SIZE, stdin);
        inbuf[len] = '\0';
        inptr = inbuf;
        return len;
    }
    static bool buffer(size_t oft) {
        size_t len=fread(inbuf+oft, 1, BUF_SIZE-oft, stdin);
        inbuf[oft+len] = '\0';
        return len;
    }
public:
    // scan(...) returns true if and only if all scanning succeed
    // eat_space() returns false if and only if the next character is NULL
    // CTypes below are: char, char[], float, double, and integer types
    // Default fallback values are:
    //     NaN for floating-numbers, '\0' for char, 
    //     0 for integers, and "" for char[]
    static bool scan(float &d) {
        if (*inptr == '\0')
            if (!buffer()) {
                d = strtof(FLT_FALLBACK, nullptr);
                return false;
            }

        char *tmp;
        d = strtof(inptr, &tmp);
        if (tmp < endinbuf && tmp != inptr) {
            // successfully scanned
            inptr = tmp;
            return true;
        }

        // reachs EOB before/while converting
        ptrdiff_t left=endinbuf-inptr;
        memcpy(inbuf, inptr, left);
        if (buffer(left))
            d = strtof(inbuf, &inptr);

        return true;
    }
    static bool scan(double &d) {
        if (*inptr == '\0')
            if (!buffer()) {
                d = strtod(FLT_FALLBACK, nullptr);
                return false;
            }

        char *tmp;
        d = strtod(inptr, &tmp);
        if (tmp < endinbuf && tmp != inptr) {
            // successfully scanned
            inptr = tmp;
            return true;
        }

        // reachs EOB before/while converting
        ptrdiff_t left=endinbuf-inptr;
        memcpy(inbuf, inptr, left);
        if (buffer(left))
            d = strtod(inbuf, &inptr);

        return true;
    }
    static bool scan(char &c) {
        c = *inptr++;
        if (c != '\0') return true;
        if (!buffer()) return false;

        c = *inptr++;
        return true;
    }
    static bool scan(char *s) {
        char *pos=inptr, *src=pos;
        bool started=false;
        for (;; ++pos) {
            char tmp=*pos;
            if (tmp == '\0') {
                // unbuffers and rebuffers if reaches EOB
                ptrdiff_t count=pos-src;
                memcpy(s, src, count);
                s += count;

                if (!buffer()) {
                    *s = '\0';
                    return started;
                }

                pos = src = inbuf;
                tmp = *inbuf;
            }

            if (!isspace(tmp)) {
                // not delimiters
                if (!started) {
                    started = true;
                    src = pos;
                }
            } else if (started) {
                memcpy(s, src, pos-src);
                s[pos-src] = '\0';
                inptr = ++pos;
                return true;
            }

            // nops until non-delimiter char appears
        }
    }
    template <class Integral>
    static bool scan(
        Integral &i,
        typename std::enable_if<std::is_signed<Integral>::value>::type*_=0
    ) {
        bool started=false, neg=false;
        i = 0;
        for (;;) {
            char tmp=*inptr++;
            if (tmp == '\0')
                if (!buffer())
                    return started;

            if (isdigit(tmp)) {
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
        return true;
    }
    template <class Integral>
    static bool scan(
        Integral &u,
        typename std::enable_if<!std::is_signed<Integral>::value>::type*_=0
    ) {
        bool started=false;
        u = 0;
        for (;;) {
            char tmp=*inptr++;
            if (tmp == '\0')
                if (!buffer())
                    return started;

            if (isdigit(tmp)) {
                started = true;
                u = u*10 + tmp-'0';
            } else if (started) {
                ++tmp;
                return true;
            }
        }
    }
    template <class CTypes, class... Rest>
    static bool scan(CTypes &&x, Rest&&... y) {
        return scan(x) && scan(y...);
    }
    static bool scanln(char *s) {
        char *pos=inptr, *src=pos, *dst=s;
        for (;; ++pos) {
            char tmp=*pos;
            if (tmp == '\0') {
                // unbuffers and rebuffers if reaches EOB
                ptrdiff_t count=pos-src;
                memcpy(dst, src, count);
                dst += count;

                if (!buffer()) {
                    *dst = '\0';
                    return dst != s;
                }

                pos = src = inbuf;
                tmp = *inbuf;
            }

            if (tmp == '\n') {
                inptr = ++pos;
                memcpy(dst, src, pos-src);
                dst[pos-src] = '\0';
                return true;
            }

            // nops until non-delimiter char appears
        }
    }
    template <class CharArray, class... Rest>
    static bool scanln(CharArray &&x, Rest&&... y) {
        return scanln(x) && scanln(y...);
    }
    static bool ignore(char delim) {
        for (;; ++inptr) {
            if (*inptr == '\0')
                if (!buffer())
                    return false;

            if (*inptr != delim)
                return true;
        }
    }
    static bool ignore() {
        for (;; ++inptr) {
            if (*inptr == '\0')
                if (!buffer())
                    return false;

            if (!isspace(*inptr))
                return true;
        }
    }
    static void print(double d) {
        char minibuf[FLT_LEN];
        size_t count=sprintf(minibuf, FLT_FORMAT, d);
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

        if (count >= BUF_SIZE) {
            fwrite(s, 1, count, stdout);
            return;
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

        if (count >= BUF_SIZE) {
            fwrite(s, 1, count, stdout);
            return;
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

        if (count >= BUF_SIZE) {
            fwrite(s, 1, count, stdout);
            return;
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
    template <class CTypes, class... Rest>
    static void print(CTypes x, Rest&&... y) {
        // prints arguments without separating characters
        print(x), print(y...);
    }
    template <class CTypes>
    static void println(CTypes x) {
        print(x, '\n');
    }
    template <class CTypes, class... Rest>
    static void println(CTypes x, Rest&&... y) {
        // prints arguments separated by a single space and terminates the line
        print(x, ' '), println(y...);
    }
    template <class CTypes>
    static void printlns(CTypes x) {
        print(x, '\n');
    }
    template <class CTypes, class... Rest>
    static void printlns(CTypes x, Rest&&... y) {
        // prints each of arguments per line
        print(x, '\n'), printlns(y...);
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
constexpr char FastIO::FLT_FORMAT[], FastIO::FLT_FALLBACK[];
