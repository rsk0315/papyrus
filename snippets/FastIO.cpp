#include <cstdio>
#include <cstdlib>
#include <cstdint>
#include <cstddef>
#include <cstring>
#include <cctype>
#include <numeric>

template <size_t E, bool T=1>
class FastScanner {
    char e[E|1],*t,*a;
    const double A=strtod("NaN",nullptr);
    FILE*o;
    bool i(){size_t n=fread(e,1,E,o);e[n]=0;a=e+n;t=e;return n;}
    bool i(ptrdiff_t n){size_t s=fread(e,1,E,o);e[n+=s]=0;a=e+n;t=e;return s;}
public:
    FastScanner(FILE*o=stdin):e{},t(e),a(e+E),o(o){i();}
    bool scan(double&n){if(!*t&&!i()){n=A;return 0;}char*s;n=strtod(t,&s);while(s==t){if(!i()){n=A;return 0;}n=strtod(t,&s);}if(s>=a){ptrdiff_t h=a-t;memcpy(e,t,h);if(i(h))n=strtod(e,&s);}t=s;return 1;}
    bool scan(char&n){n=*t++;if(n)return 1;if(!i())return 0;n=*t++;return 1;}
    bool scan(char*n){char*s=nullptr;for(;;++t){char h=*t;if(!h){if(s){ptrdiff_t r=t-s;memcpy(n,s,r);n+=r;}if(!i()){*n=0;return s;}h=*e;if(s)s=e;}if(!isspace(h)){if(!s){s=t;}}else if(s){ptrdiff_t r=t-s;memcpy(n,s,r);n[r]=0;++t;return 1;}}}
    template<class O,bool I=T>
    bool scan(O&n,typename std::enable_if<std::is_signed<O>::value>::type*_1=0,typename std::enable_if<I>::type*_2=0){bool s=0,h=0;n=0;for(;;++t){char r=*t;if(!r){if(!i())return s;r=*t;}if(isdigit(r)){s=1;n=n*10+r-'0';}else if(s){++t;break;}else if(r=='-'){h=1;}}if(h)n=-n;return 1;}
    template<class O,bool I=T>
    bool scan(O&n,typename std::enable_if<std::is_signed<O>::value>::type*_1=0,typename std::enable_if<!I>::type*_2=0){bool s=0,h=0;n=0;for(;;++t){char r=*t;if(!r){if(!i())return s;r=*t;}if(isdigit(r)){s=1;n=n*10+r-'0';}else if(s){break;}else if(r=='-'){h=1;}}if(h)n=-n;return 1;}
    template<class O,bool I=T>
    bool scan(O&n,typename std::enable_if<!std::is_signed<O>::value>::type*_1=0,typename std::enable_if<I>::type*_2=0){bool s=0;n=0;for(;;++t){char h=*t;if(!h){if(!i())return s;h=*t;}if(isdigit(h)){s=1;n=n*10+h-'0';}else if(s){++t;return 1;}}}
    template<class O,bool I=T>
    bool scan(O&n,typename std::enable_if<!std::is_signed<O>::value>::type*_1=0,typename std::enable_if<!I>::type*_2=0){bool s=0;n=0;for(;;++t){char h=*t;if(!h){if(!i())return s;h=*t;}if(isdigit(h)){s=1;n=n*10+h-'0';}else if(s){return 1;}}}
    template<class O,class...I>
    bool scan(O&&n,I&&...s){return scan(n)&&scan(s...);}
    bool scanln(char*n){char*s=t,*h=n;for(;;++t){char r=*t;if(!r){ptrdiff_t d=t-s;memcpy(h,s,d);h+=d;if(!i()){*h=0;return h-n;}s=e;r=*e;}if(r=='\n'){++t;ptrdiff_t d=t-s;memcpy(h,s,d);h[d]=0;return 1;}}}
    template<class O,class...I>
    bool scanln(O&&n,I&&...s){return scanln(n)&&scanln(s...);}
    char peek(){if(!*t)i();return*t;}
    bool ignore(char n){for(;;++t){if(!*t&&!i())return 0;if(*t-n)return 1;}}
    bool ignore(){for(;;++t){if(!*t&&!i())return 0;if(!isspace(*t))return 1;}}
    bool advance(){if(!*t&&!i())return 0;return*++t;}
    bool advance(ptrdiff_t n){if(!*t&&!i())return 0;for(ptrdiff_t s=a-t;s<=n;){n-=s;if(!i())return 0;s=a-t;}t+=n;return  *t;}
    template<class O>
    O next(){O n;scan(n);return n;}
    template<class O>
    FastScanner&operator>>(O&n){scan(n);return*this;}
};

template <size_t E>
class FastPrinter {
    char e[E|1],*t,*a;
    const char T[6]="%.16f";
    const size_t A=20,O=330;
    FILE*o;
    void i(){fwrite(e,1,t-e,o);t=e;}
public:
    FastPrinter(FILE*o=stdout):e{},t(e),a(t+E),o(o){}
    void print(double n){char s[O];size_t h=sprintf(s,T,n);char*r=t+h;if(r>=a){i();r=e+h;}memcpy(t,s,h);t=r;}
    void print(char n){if(t+1>=a)i();*t++=n;}
    void print(char*n){size_t s=strlen(n);char*h=t+s;if(h>=a){i();h=e+s;}if(s>=E){fwrite(n,1,s,o);return;}memcpy(t,n,s);t=h;}
    void print(const char*n){size_t s=strlen(n);char*h=t+s;if(h>=a){i();h=e+s;}if(s>=E){fwrite(n,1,s,o);return;}memcpy(t,n,s);t=h;}
    template<size_t I>
    void print(const char(&n)[I]){size_t s=I-1;char*h=t+s;if(h>=a){i();h=e+s;}if(s>=E){fwrite(n,1,s,o);return;}memcpy(t,n,s);t=h;}
    template<class I>
    void print(I n,typename std::enable_if<std::is_signed<I>::value>::type*_=0){if(t+A>=a)i();if(!n){*t++='0';return;}char s[A],*h=s+A,*r=h;if(n<0){*t++='-';n=-n;}while(n){*--h=n%10+'0';n/=10;}memcpy(t,h,r-h);t+=r-h;}
    template<class I>
    void print(I n,typename std::enable_if<!std::is_signed<I>::value>::type*_=0){if(t+A>=a)i();if(!n){*t++='0';return;}char s[A],*h=s+A,*r=h;while(n){*--h=n%10+'0';n/=10;}memcpy(t,h,r-h);t+=r-h;}
    template<class I,class...N>
    void print(I n,N&&...s){print(n),print(s...);}
    template<class I>
    void println(I n){print(n,'\n');}
    template<class I,class...N>
    void println(I n,N&&...s){print(n,' '),println(s...);}
    template<class I>
    void printlns(I n){print(n,'\n');}
    template<class I,class...N>
    void printlns(I n,N&&...s){print(n,'\n'),printlns(s...);}
    void flush(){fwrite(e,1,t-e,o);fflush(o);t=e;}
    template<class I>
    FastPrinter&operator<<(I n){print(n);return*this;}
    ~FastPrinter(){flush();}
};

constexpr size_t BUF_SIZE=(1<<17);
FastScanner<BUF_SIZE> cin;
FastPrinter<BUF_SIZE> cout;
