struct Edge {
    int src, dst;
    int weight;
    Edge(void) {};
    Edge(int s, int d, int w) {
        src = s;
        dst = d;
        weight = w;
    }
};

typedef vector<Edge> Edges;
typedef vector<Edges> Graph;

bool operator<(const Edge &e, const Edge &f) {
    if (e.weight != f.weight) {
        return e.weight > f.weight;
    } else if (e.src != f.src) {
        return e.src < f.src;
    } else {
        return e.dst < f.dst;
    }
}
