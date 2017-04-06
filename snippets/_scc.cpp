template <class Weight>
std::vector<size_t> scc(const Graph<Weight> &g, Graph<Weight> *decmp=nullptr) {
    // Returns the mapping: which scc the vertex belongs to
    // Stores the decomposed graph into *decmp (unless NULL)
    const size_t v=g.size();
    std::vector<size_t> ord(v), index(v);
    std::stack<size_t> s;
    std::vector<bool> visited(v);
    size_t t=0;
    // std::vector<std::vector<size_t>> cmp;

    std::function<void (size_t)> visit=[&](size_t v)->void {
        index[v] = ord[v] = ++t;
        s.emplace(v);
        visited[v] = true;

        for (const auto &e: g[v]) {
            size_t w=e.dst;
            if (ord[w] == 0) {
                // not visited yet
                visit(w);
                if (index[v] > index[w])
                    index[v] = index[w];
            } else if (visited[w]) {
                // second (or more) visit
                if (index[v] > ord[w])
                    index[v] = ord[w];
            }
        }

        if (index[v] == ord[v]) {
            // cmp.emplace_back();
            while (true) {
                size_t w=s.top();
                s.pop();
                visited[w] = false;

                // cmp.back().emplace_back(w);
                if (v == w)
                    break;
            }
        }
    };

    for (size_t u=0; u<v; ++u)
        if (ord[u] == 0)
            visit(u);

    size_t numcmp=0;
    std::vector<size_t> num(v, v);
    for (size_t i=0; i<v; ++i) {
        if (num[index[i]] == v) {
            num[index[i]] = numcmp;
            index[i] = numcmp++;
        } else {
            index[i] = num[index[i]];
        }
    }

    /* the size of each of components */
    // std::vector<int> cmp_size(numcmp);
    // for (int i: index)
    //    ++cmp_size[i];

    if (!decmp)
        return index;

    decmp->resize(numcmp);
    for (const auto &v: g)
        for (const auto &e: v)
            if (index[e.src] != index[e.dst])
                decmp->connect_d(index[e.src], index[e.dst]);

    return index;
}
