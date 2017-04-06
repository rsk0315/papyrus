template <class RandomIt>
typename RandomIt::difference_type li_subseq(
    RandomIt first, RandomIt last, const typename RandomIt::value_type &inf
) {
    std::vector<typename RandomIt::value_type> dp(last-first, inf);
    for (RandomIt i=first; i<last; ++i)
        *std::lower_bound(dp.begin(), dp.end(), *i) = *i;

    return std::lower_bound(dp.begin(), dp.end(), inf)-dp.begin();
}

template <class RandomIt>
typename RandomIt::difference_type li_subseq(
    RandomIt first, RandomIt last, const typename RandomIt::value_type &inf,
    std::vector<typename RandomIt::value_type> &output
) {
    typename RandomIt::difference_type n=last-first;
    std::vector<typename RandomIt::value_type> dp(n, inf);
    std::vector<int> index(n);

    for (int i=0; i<n; ++i) {
        RandomIt hint=std::lower_bound(dp.begin(), dp.end(), first[i]);
        index[i] = hint-dp.begin();
        *hint = first[i];
    }

    int m=*std::max_element(index.begin(), index.end());
    output.resize(m+1);
    for (int i=n; i--;)
        if (index[i] == m)
            output[m--] = first[i];

    return output.size();
}
