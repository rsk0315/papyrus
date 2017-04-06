#include <cstdio>
#include <cstdlib>
#include <cstdint>
#include <cstddef>
#include <cstring>
#include <cctype>
#include <numeric>

class FastScanner {
    static const size_t E=(1<<17);
    static char*e,t[E|1],*a;
    const double T=strtod("NaN",nullptr);
    bool o(){size_t i=fread(t,1,E,stdin);t[i]=0;a=t+i;e=t;return i;}
    bool o(ptrdiff_t i){size_t n=fread(t,1,E,stdin);t[i+=n]=0;a=t+i;e=t;return n;}
public:
    FastScanner(){o();}
    bool scan(double&i){if(!*e &&!o()){i=T;return 0;}char*n;i=strtod(e,&n);while(n==e)if(!o()){i=T;return 0;}if(n>=a){ptrdiff_t s=a-e;memcpy(t,e,s);if(o(s))i=strtod(t,&e);}return 1;}
    bool scan(char&i){i=*e++;if(i)return 1;if(!o())return 0;i=*e++;return 1;}
    bool scan(char*i){char*n=nullptr;for(;;++e){char s=*e;if(!s){if(n){ptrdiff_t h=e-n;memcpy(i,n,h);i+=h;}if(!o()){*i=0;return n;}s=*t;if(n)n=t;}if(!isspace(s)){if(!n){n=e;}}else if(n){ptrdiff_t h=e-n;memcpy(i,n,h);i[h]=0;++e;return 1;}}}
    template<class A>
    bool scan(A&i,typename std::enable_if<std::is_signed<A>::value>::type*_=0){bool n=0,s=0;i=0;for(;;++e){char h=*e;if(!h){if(!o())return n;h=*e;}if(isdigit(h)){n=1;i=i*10+h-'0';}else if(n){break;}else if(h=='-'){s=1;}}if(s)i=-i;return 1;}
    template<class A>
    bool scan(A&i,typename std::enable_if<!std::is_signed<A>::value>::type*_=0){bool n=0;i=0;for(;;++e){char s=*e;if(!s){if(!o())return n;s=*e;}if(isdigit(s)){n=1;i=i*10+s-'0';}else if(n){return 1;}}}
    template<class A,class...O>
    bool scan(A&&i,O&&...n){return scan(i)&&scan(n...);}
    bool scanln(char*i){char*n=e,*s=i;for(;;++e){char h=*e;if(!h){ptrdiff_t r=e-n;memcpy(s,n,r);s+=r;if(!o()){*s=0;return s-i;}n=t;h=*t;}if(h=='\n'){++e;ptrdiff_t r=e-n;memcpy(s,n,r);s[r]=0;return 1;}}}
    template<class A,class...O>
    bool scanln(A&&i,O&&...n){return scanln(i)&&scanln(n...);}
    char peek(){if(!*e)o();return*e;}
    bool ignore(char i){for(;;++e){if(!*e &&!o())return 0;if(*e-i)return 1;}}
    bool ignore(){for(;;++e){if(!*e &&!o())return 0;if(!isspace(*e))return 1;}}
    bool advance(){if(!*e&&!o())return 0;return*++e;}
    bool advance(ptrdiff_t i){if(!*e&&!o())return 0;for(ptrdiff_t n=a-e;n<=i;){i-=n;if(!o())return 0;n=a-e;}e+=i;return  *e;}
    template<class A>
    A next(){A i;scan(i);return i;}
    template<class A>
    FastScanner&operator>>(A&i){scan(i);return*this;}
} cin;

char FastScanner::t[],*FastScanner::e=t,*FastScanner::a=e+E;

class FastPrinter {
    static const size_t E=(1<<17);
    static char*e,t[E|1],*a;
    const char T[6]="%.16f";
    const size_t A=20,O=330;
    void o(){fwrite(t,1,e-t,stdout);e=t;}
public:
    void print(double i){char n[O];size_t s=sprintf(n,T,i);char*h=e+s;if(h>=a){o();h=t+s;}memcpy(e,n,s);e=h;}
    void print(char i){if(e+1>=a)o();*e++=i;}
    void print(const char*i){size_t n=strlen(i);char*s=e+n;if(s>=a){o();s=t+n;}if(n>=E){fwrite(i,1,n,stdout);return;}memcpy(e,i,n);e=s;}
    template<size_t I>
    void print(const char(&i)[I]){size_t n=I-1;char*s=e+n;if(s>=a){o();s=t+n;}if(n>=E){fwrite(i,1,n,stdout);return;}memcpy(e,i,n);e=s;}
    template<class I>
    void print(I i,typename std::enable_if<std::is_signed<I>::value>::type*_=0){if(e+A>=a)o();if(!i){*e++='0';return;}char n[A],*s=n+A,*h=s;if(i<0){*e++='-';i=-i;}while(i){*--s=i%10+'0';i/=10;}memcpy(e,s,h-s);e+=h-s;}
    template<class I>
    void print(I i,typename std::enable_if<!std::is_signed<I>::value>::type*_=0){if(e+A>=a)o();if(!i){*e++='0';return;}char n[A],*s=n+A,*h=s;while(i){*--s=i%10+'0';i/=10;}memcpy(e,s,h-s);e+=h-s;}
    template<class I,class...N>
    void print(I i,N&&...n){print(i),print(n...);}
    template<class I>
    void println(I i){print(i,'\n');}
    template<class I,class...N>
    void println(I i,N&&...n){print(i,' '),println(n...);}
    template<class I>
    void printlns(I i){print(i,'\n');}
    template<class I,class...N>
    void printlns(I i,N&&...n){print(i,'\n'),printlns(n...);}
    void flush(){fwrite(t,1,e-t,stdout);fflush(stdout);e=t;}
    template<class I>
    FastPrinter&operator<<(I i){print(i);return*this;}
    ~FastPrinter(){flush();}
} cout;

char FastPrinter::t[],*FastPrinter::e=t,*FastPrinter::a=t+E;
