/**
 *  This source is dummy, to check whether colorizing is done properly.
 *  Not for executing (cannot be compiled).
 *  Underlined identifiers would be highlighted as "DEFINITION" (maybe purple)
 *  and others are not "DEFINITION"s.
 */

#ifndef TEST_BEHAVIOR

/* macro constants */
#define TEST_BEHAVIOR /* test */
        ^~~~~~~~~~~~~
#define ARRAY_SIZE 5
        ^~~~~~~~~~

#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <algorithm>
#include <vector>
#include <string>
#include <queue>
#include <functional>

/* type alias */
template <class T>
using lp_queue=std::priority_queue<T, deque<T>, std::greater<T>>;
      ^~~~~~~~

/* multi-line function declarations */
int function_with_long_name(
    ^~~~~~~~~~~~~~~~~~~~~~~
    std::pair<std::vector<std::string>, int> parameter_with_long_name,
    int short_name_parameter
) {
    // parameters would not be colorized
    return 0;
}

/* structures */
struct StructOne {
       ^~~~~~~~~
    int member;
        ^~~~~~
    StructOne() {}
    ^~~~~~~~~
    StructOne(int member): member(member) {}
    ^~~~~~~~~

    StructOne &operator +=(const StructOne &rhs) {
                        ^~
        this.member += rhs.member;
        return *this;
    }
    int memb_func();
} struct_one;
  ^~~~~~~~~~

int StructOne::memb_func() {
               ^~~~~~~~~
    return 0;
}

struct StructTwo: public StructOne {
       ^~~~~~~~~
    int operator +=() {
                 ^~
        return this->member;
    }
};

struct StructTwo struct_two;
                 ^~~~~~~~~~

/* functions */
int main() {
    ^~~~
    using namespace std;

    /* regular declarations and definitions */
    int foo, bar=1, *baz=NULL, &qux=foo, quux[ARRAY_SIZE]={bar}, corge;
        ^~~  ^~~     ^~~        ^~~      ^~~~                    ^~~~~

    /* declarations with template arguments */
    std::vector<int> vector1(bar, 42), vector2;
                     ^~~~~~~           ^~~~~~~
    vector<pair<double, double>> pair1(1.0, -2.0), pair2;
                                 ^~~~~             ^~~~~

    /* lambda expressions */
    auto lambda=[foo, &bar, =baz](int s, int t)->int {
         ^~~~~~
        return foo*bar*s + baz*t;
    };

    /* function pointer (and following regular decls) */
    /* Work in progress; maybe difficult */
    double (*funcptr)(double)=std::sin, var;
             ^~~~~~~                    ^~~

    return 0;
}

#endif // TEST_BEHAVIOR
