template <class Weight>
std::vector<size_t> scc(const Graph<Weight> &g, Graph<Weight> *dag=nullptr) {
    // Returns the mapping: to which scc the vertex belongs
    const size_t v=g.size();
    std::vector<size_t> ord(v), low(v), index(v);
    std::stack<size_t> s;
    std::vector<bool> staying(v);
    size_t t=0, numcmp=0;

    std::function<void (size_t)> visit=[&](size_t v)->void {
        low[v] = ord[v] = ++t;
        s.emplace(v);
        staying[v] = true;

        for (const auto &e: g[v]) {
            size_t w=e.dst;
            if (ord[w] == 0) {
                // not visited yet
                visit(w);
                if (low[v] > low[w])
                    low[v] = low[w];
            } else if (staying[w]) {
                // second (or more) visit
                if (low[v] > ord[w])
                    low[v] = ord[w];
            }
        }

        if (low[v] == ord[v]) {
            size_t w;
            do {
                w = s.top();
                s.pop();
                staying[w] = false;
                index[w] = numcmp;
            } while (v != w);
            ++numcmp;
        }
    };

    for (size_t u=0; u<v; ++u)
        if (ord[u] == 0)
            visit(u);

    /* the size of each of components */
    // std::vector<int> cmp_size(numcmp);
    // for (int i: index)
    //    ++cmp_size[i];

    if (!dag)
        return index;

    dag->resize(numcmp);
    for (const auto &v: g)
        for (const auto &e: v)
            if (index[e.src] != index[e.dst])
                dag->connect_d(index[e.src], index[e.dst], e.cost);

    return index;
}
