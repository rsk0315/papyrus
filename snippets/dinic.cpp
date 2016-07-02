int augment(
        const Graph &g, const vvi &capacity, vvi &flow, const vi &level,
        vector<bool> &finished, int u, int t, int cur
) {
    if (u==t || cur==0) return cur;
    if (finished[u]) return 0;

    finished[u] = true;
    Edges::iterator e;
    for (e=g[u].begin(); e!=g[u].end(); e++)
        if (level[e->dst] > level[u]) {
            int f;
            f = augment(
                g, capacity, flow, level, finished, e->dst, t,
                min(cur, capacity[u][e->dst]-flow[u][e->dst])
            );
            if (f > 0) {
                flow[u][e->dst] += f; flow[e->dst][u] -= f;
                finished = false;
                return f;
            }
        }

    return 0;
}

int dinic(const Graph &g, int s, int t) {
    int n=g.size();
    vvi flow(n, vi(n)), capacity(n, vi(n));
    int u;
    Edges::iterator e;

    for (u=0; u<n; u++)
        for (e=g[u].begin(); e!=g[u].end(); g++)
            capacity[e->src][e->dst] += e->weight;

    int total=0;
    bool cont;
    for (cont=true; cont;) {
        cont = false;
        vi level(n, -1); level[s] = 0;  // make layered network
        qi q: q.push(s);
        int d;
        for (d=n; !q.empty()&&level[q.front()]<d;) {
            u = q.front(); q.pop();
            if (u == t) d = level[u];

            for (e=g[u].begin(); e!=g[u].end(); e++)
                if (capacity[u][e->dst]>flow[u][e->dst]&&level[e->dst]==-1) {
                    q.push(e->dst);
                    level[e->dst] = level[u] + 1;
                }
        }
        vector<bool> finished(n);  // make blocking flows
        int f;
        for (f=1; f>0;) {
            f = augment(g, capacity, flow, level, finished, s, t, INF);
            if (f == 0) break;
            total += f;
            cont = true;
        }
    }
    return total;
}
