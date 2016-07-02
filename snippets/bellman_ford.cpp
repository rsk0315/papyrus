bool bellman_ford(const Graph g, int s, vi &d, vi &p) {
    int n=g.size();
    d.assign(n, INF<<1); d[s]=0;
    p.assign(n, -2);

    bool has_negative_cycle=false;
    int k, i;
    Edges::iterator e;
    for (k=0; k<n; k++)
        for (i=0; i<n; i++)
            for (e=g[i].begin(); e!=g[i].end(); e++)
                if (d[e->src] + e->weight < d[e->dst]) {
                    d[e->dst] = d[e->src] + e->weight;
                    p[e->dst] = e->src;
                    if (k == n-1) {
                        d[e->dst] = -INF;
                        has_negative_cycle = true;
                    }
                }

    return !has_negative_cycle;
}
