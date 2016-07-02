int edmonds_karp(const Graph &g, int s, int t) {
    int n=g.size();
    vvi flow(n, vi(n));
    vvi capacity(n, vi(n));
    int u;
    Edges::iterator e;

    for (u=0; u<n; u++)
        for (e=g[u].begin(); e!=g[u].end(); e++)
            capacity[e->src][e->dst] += e->weight;

    int total=0;
    while (1) {
        qi q; q.push(s);
        vi prev(n, -1); prev[s] = s;
        while (!q.empty() && prev[t]<0) {
            int u=q.front(); q.pop();
            for (e=g[u].begin(); e!=g[u].end(); e++)
                if (prev[e->dst]<0 && capacity[u][e->dst]>flow[u][e->dst]) {
                    prev[e->dst] = u;
                    q.push(e->dst);
                }
        }
        if (prev[t] < 0) return total;  // prev[x]==-1 <=> t-side
        int inc=INF;
        int j;
        for (j=t; prev[j]!=j; j=prev[j])
            inc = min(inc, capacity[prev[j]][j]-flow[prev[j]][j]);

        for (j=t; prev[j]!=j; j=prev[j]) {
            flow[prev[j]][j] += inc;
            flow[j][prev[j]] -= inc;
        }
        total += inc;
    }
}
