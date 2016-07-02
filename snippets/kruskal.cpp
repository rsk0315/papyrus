typedef pair<int, Edges> piE;

piE kruskal(const Graph &g) {
    int n=g.size();
    UnionFindTree tree(n);
    prique<Edge> q;
    int u;
    Edges::iterator e;

    for (u=0; u<n; u++)
        for (e=g[u].begin(); e!=g[u].end(); e++)
            if (u < e->dst)
                q.push(*e);

    int total=0;
    Edges F;
    while (F.size()<n-1 && !q.empty()) {
        Edge e=q.top(); q.pop();
        if (tree.unite(e.src, e.dst)) {
            F.push_back(e);
            total += e.weight;
        }
    }
    return piE(total, F);
}
