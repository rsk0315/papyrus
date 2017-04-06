class BasicTree {
    struct Edge {
        const size_t src, dst;
        Edge(size_t src, size_t dst): src(src), dst(dst) {}
    };
    std::vector<std::vector<Edge>> g;
    std::vector<int> depth;
    size_t root;
    std::vector<std::array<size_t, 18>> ancestors;
public:
    BasicTree(size_t v, size_t root=0):
        g(v), root(root), ancestors(g.size()+1)
    {}
    void connect(size_t src, size_t dst) {
        g[src].emplace_back(src, dst);
        g[dst].emplace_back(dst, src);
    }
    void trace_ancestor(size_t root=0) {
        for (size_t i=0; i<=g.size(); ++i)
            for (size_t j=0; j<18; ++j)
                ancestors[i][j] = g.size();
 
        depth.assign(g.size(), -1);
        depth[root] = 0;
 
        // get parent
        std::queue<size_t> q;
        q.emplace(root);
        while (!q.empty()) {
            size_t v=q.front();
            q.pop();
            for (const Edge &e: g[v]) {
                if (depth[e.dst] > -1) continue;
 
                ancestors[e.dst][0] = e.src;
                depth[e.dst] = depth[e.src]+1;
                q.emplace(e.dst);
            }
        }
 
        // get power-of-two-th ancestors by doubling
        for (size_t j=1; (1u<<j)<g.size(); ++j)
            for (size_t i=0; i<g.size(); ++i)
                ancestors[i][j] = ancestors[ancestors[i][j-1]][j-1];
    }
    size_t kth_ancestor(size_t v, size_t k) const {
        for (size_t i=0; k; (++i, k>>=1))
            if (k & 1)
                v = ancestors[v][i];
 
        return v;
    }
    size_t get_lca(size_t u, size_t v) const {
        if (depth[u] > depth[v]) std::swap(u, v);
        v = kth_ancestor(v, depth[v]-depth[u]);
 
        if (u == v) return u;
 
        for (size_t i=18; i--;)
            if (ancestors[u][i] != ancestors[v][i]) {
                u = ancestors[u][i];
                v = ancestors[v][i];
            }
 
        return ancestors[u][0];
    }
    int distance(size_t u, size_t v) const {
        size_t lca=get_lca(u, v);
        return depth[u]+depth[v] - 2*depth[lca];
    }
};
