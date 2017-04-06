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
    std::vector<typename RandomIt::difference_type> &output
) {
    typename RandomIt::difference_type n=last-first;
    std::vector<typename RandomIt::difference_type> index(n, -1);
    std::vector<typename RandomIt::value_type> lis(n, inf);
    typename RandomIt::difference_type len=-1;

    bool updated=true;
    for (RandomIt i=first; i<last; ++i) {
        auto cur=std::lower_bound(lis.begin(), lis.end(), *i);

        if ((cur-lis.begin()) > len) {
            len = (cur-lis.begin());
            updated = false;
        } else if (!updated) {
            output = index;
            updated = true;
        }

        index[cur-lis.begin()] = i-first;
        *cur = *i;
    }

    if (!updated)
        output = index;

    output.resize(++len);
    return len;
}
