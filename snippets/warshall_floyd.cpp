void warshall_floyd(const vvi &g, vvi &d, vvi &inter) {
    int n=g.size();
    d = g;
    inter.assign(n, vi(n, -1));
    int k, i, j;
    for (k=0; k<n; k++)
        for (i=0; i<n; i++)
            for (j=0; j<n; j++)
                if (d[i][k] + d[k][j] < d[i][j]) {
                    d[i][j] = d[i][k] + d[k][j];
                    inter[i][j] = k;
                }
}
