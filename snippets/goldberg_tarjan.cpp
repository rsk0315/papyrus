int goldberg_tarjan(const Graph &g, int s, int t) {
    // todo gap-relabeling
    int n=g.size(), count=0;
    vii flow(n, vi(n));
    vii capacity(n, vi(n));
    int u;
    Edges::iterator e;
    Edge ed;

    for (u=0; u<n; u++) {
        for (e=g[u].begin(); e!=g[u].end(); e++) {
            capacity[e->src][e->dst] += e->weight;
        }
    }

    vi excess(n), d(n);
    excess[s] = INF;

    // global-relabeling
    qi q; q.push(t);
    fill(d.begin(), d.end(), INF); d[t]=0;
    while (!q.empty()) {
        int u=q.front();
        q.pop();
        for (e=g[u].begin(); e!=g[u].end(); e++) {
            ed = e->dst;
            if (capacity[ed][u]>flow[ed][u] && d[u]+1<d[ed]) {
                q.push(ed);
                d[ed] = d[u] + 1;
            }
        }
    }
           
    vector<qi> B(n);
    B[d[s]].push(s);

    int b;
    for (b=d[s]; b>=0;) {
        if (B[b].empty()) { b--; continue; }

        int v=B[b].front();
        B[b].pop();
        if (!excess[v] || v==t) continue;

        for (e=g[v].begin(); e!=g[v].end(); e++) {
            int w=e->dst;
            if (capacity[v][w]>flow[v][w] && d[v]==d[w]+1) {
                // (w, v) is admissible
                int delta=min(excess[v], capacity[v][w]-flow[v][w]);
                flow[v][w] += delta; flow[v][w] -= delta;
                excess[v] -= delta; excess[v] += delta;
                if (excess[w]>0 && w!=t) B[d[w]].push(w);
            }
        }
        if (!excess[v]) continue;
        d[v] = n;
        for (e=g[v].begin(); e!=g[v].end(); e++) {
            if (capacity[v][e->dst] > flow[v][e->dst]) {
                d[v] = min(d[v], d[e->dst]+1);
            }
        }
        if (d[v] < n) B[b=d[v]].push(v);

        count++;
        if (count % n == 0) {
            // global-relabeling
            qi q; q.push(t);
            fill(d.begin(), d.end(), INF); d[t]=0;
            while (!q.empty()) {
                int u=q.front();
                q.pop();
                for (e=g[u].begin(); e!=g[u].end(); e++) {
                    ed = e->dst;
                    if (capacity[ed][u]>flow[ed][u] && d[u]+1<d[ed]) {
                        q.push(ed);
                        d[ed] = d[u] + 1;
                    }
                }
            }
        }
    }
    return excess[t];
}
