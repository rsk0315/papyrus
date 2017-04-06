template <class Weight>
struct Edge {
    const size_t src, dst;
    const Weight cost;
    Edge(size_t src, size_t dst, Weight cost):
        src(src), dst(dst), cost(cost)
    {}
};

template <class Weight>
bool operator <(const Edge<Weight> &e, const Edge<Weight> &f) {
    if (e.cost != f.cost) {
        return e.cost > f.cost;
    } else {
        return (e.src != f.src)? (e.src < f.src) : (e.dst < f.dst);
    }
}

template <class Weight>
using Edges=std::vector<Edge<Weight>>;
template <class Weight>
using Vertex=std::vector<Edge<Weight>>;

template <class Weight>
struct Graph: public std::vector<Vertex<Weight>> {
    static constexpr Weight INF=std::numeric_limits<Weight>::max()/4;
    Graph(): std::vector<Vertex<Weight>>() {}
    Graph(size_t v): std::vector<Vertex<Weight>>(v) {}
    void connect_u(size_t s, size_t d, Weight c=1) {
        (*this)[s].emplace_back(s, d, c);
        (*this)[d].emplace_back(d, s, c);
    }
    void connect_d(size_t s, size_t d, Weight c=1) {
        (*this)[s].emplace_back(s, d, c);
    }
};
