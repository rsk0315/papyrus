void dijkstra(const Graph &g, int s, vi &d, vi &p) {
    int n=g.size();
    d.assign(n, INF); d[s] = 0;
    p.assign(n, -1);
    Qi q;  // e < f <=> e.weight > f.weight
    for (q.push(Edge(-2, s, 0)); !q.empty();) {
        Edge e = q.front(); q.pop();
        if (p[e.dst] != -1) continue;

        p[e.dst] = e.src;
        Edges::iterator f;
        for (f=g[e.dst].begin(); f!=g[e.dst].end(); f++) {
            if (e.weight+f->weight < d[f->dst]) {
                d[f->dst] = e.weight+f->weight;
                q.push(Edge(f->src, f->dst, e.weight+f->weight));
            }
        }
    }
}
