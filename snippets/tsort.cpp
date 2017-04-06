template <class Weight>
std::vector<size_t> tsort(const Graph<Weight> &g) {
    std::vector<size_t> indeg(g.size());
    for (const auto &v: g)
        for (const auto &e: v)
            ++indeg[e.dst];

    std::queue<size_t> q;
    for (size_t i=0; i<g.size(); ++i)
        if (!indeg[i])
            q.emplace(i);

    std::vector<size_t> res;
    while (!q.empty()) {
        size_t v=q.front();
        q.pop();
        res.emplace_back(v);
        for (const auto &e: g[v])
            if (!--indeg[e.dst])
                q.emplace(e.dst);
    }

    if (res.size() < g.size()) return {};

    return res;
}
