typedef pair<int, Edges> piE;

piE prim(const Graph &g, int r=0) {
    int n=g.size();
    Edges T;
    int total=0;

    vector<bool> visited(n);
    prique<Edge> q;
    q.push(Edge(-1, r, 0));
    while (!q.empty()) {
        Edge e=q.top(); q.pop();
        if (visited[e.dst]) continue;

        T.push_back(e);
        total += e.weight;
        visited[e.dst] = true;
        Edges::iterator f;
        for (f=g[e.dst].begin(); f!=g[e.dst].end(); f++)
            if (!visited[f->dst])
                q.push(*f);
    }
    return piE(total, T);
}
