int k_shortest_path(const Graph &g, int s, int t, int k) {
    const int n=g.size();

    Graph h(n);
    int u;
    Edges::iterator e, f;
    for (u=0; u<n; u++)
        for (e=g[u].begin(); e!=g[u].end(); e++)
            h[e->dst].push_back(Edge(e->dst, e->src, e->weight));

    vi d(n, INF); d[t] = 0;
    vi p(n, -1);
    prique<Edge> q; q.push(Edge(t, t, 0));
    while (!q.empty()) {
        Edge e=q.top(); q.pop();
        if (p[e.dst] >= 0) continue;

        p[e.dst] = e.src;
        for (f=h[e.dst].begin(); f!=h[e.dst].end(); f++)
            if (e.weight + f->weight < d[f->dst]) {
                d[f->dst] = e.weight + f->weight;
                q.push(Edge(f->src, f->dst, e.weight+f->weight));
            }
    }

    int l=0;
    prique<Edge> r; r.push(Edge(-1, s, 0));
    while (!r.empty()) {
        Edge e=r.top(); r.pop();
        if (e.dst==t && ++l==k) return e.weight+d[s];

        for (f=g[e.dst].begin(); f!=g[e.dst].end(); f++) {
            int w=e.weight+f->weight-d[f->src]+d[f->dst];
            r.push(Edge(f->src, f->dst, w));
        }
    }
    return -1;  // not found
}
