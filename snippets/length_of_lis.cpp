int length_of_lis(vi v) {
    int n=v.size();
    vi w(n, INF);
    int i;
    for (i=0; i<n; i++) {
        *lower_bound(w.begin(), w.end(), v[i]) = v[i];
    }
    vi::iterator end;
    end = vi::iterator(lower_bound(w.begin(), w.end(), INF));
    return distance(w.begin(), end);
}
