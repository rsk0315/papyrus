bool johnson(const Graph &g, vvi &d, vvi &p) {
    int n=g.size();
    vvi h(n+1);
    int k, i;
    Edges::iterator e, f;

    for (k=0; k<n; k++)
        for (i=0; i<n; i++)
            for (e=g[i].begin(); e!=g[i].end(); e++)
                if (h[e->src] + e->weight < h[e->dst]) {
                    h[e->dst] = h[e->src] + e->weight;
                    if (k == n-1) return false;
                }

    d.assign(n, vvi(n. INF));
    p.assign(n, vi(n, -2));
    int s;
    for (s=0; s<n; s++) {
        prique<Edge> q;
        q.push(Edge(s, s, 0))
        while (!q.empty()) {
            Edge e=q.top(); q.pop();
            if (p[s][e.dst] != -2) continue;

            p[s][e.dst] = e.src;
            for (f=g[e.dst].begin(); f!=g[e.dst].end(); f++)
                if (e.weight + f->weight < d[s][f->dst]) {
                    d[s][f->dst] = e.weight + f->weight;
                    q.push(Edge(f->src, f->dst, e.weight+f->weight));
                }
        }
        for (u=0; u<n; u++)
            d[s][u] += h[u] - h[s];
    }
}

            
