class Knapsack {
    std::vector<int> weight, value;
    int64_t sum_w, sum_v;
    int algotype;
    static constexpr int64_t INF=1LL<<61;
    enum AlgoType {
        FEW_ITEMS=1,
        SMALL_CAPACITY,
        LITTLE_VALUE,
    };
public:
    Knapsack(): weight{}, value{}, sum_w(0), sum_v(0), algotype(0) {}
    void add_item(int w, int v) {
        weight.emplace_back(w);
        value.emplace_back(v);
        sum_w += w;
        sum_v += v;
        if (v > 1000) algotype = SMALL_CAPACITY;
        if (w > 1000) algotype = LITTLE_VALUE;
    }
    void add_item(int64_t w, int64_t v, size_t k) {
        int64_t w_=w, v_=v;
        for (size_t i=1; i<=k; i<<=1) {
            add_item(w_, v_);
            w_ += w_;
            v_ += v_;
            k -= i;
        }
        add_item(w*k, v*k);
    }
    int64_t solve(int64_t capacity) {
        if (sum_w <= capacity)
            return sum_v;

        size_t n=weight.size();
        if (n <= 30) algotype = FEW_ITEMS;

        if (algotype == FEW_ITEMS) {
            std::vector<std::pair<int64_t, int64_t>> items(1<<(n>>1));
            const size_t former=n>>1, latter=n-former;
            for (size_t i=0; i<items.size(); ++i)
                for (size_t j=0; j<former; ++j)
                    if (i>>j & 1) {
                        items[i].first += weight[j];
                        items[i].second += value[j];
                    }

            sort(items.begin(), items.end());
            size_t m=1;
            for (size_t i=1; i<items.size(); ++i)
                if (items[m-1].second < items[i].second)
                    items[m++] = items[i];

            items.resize(m);

            int64_t res=0;
            for (size_t i=0; i<(1u<<latter); ++i) {
                int64_t sw=0, sv=0;
                for (size_t j=0; j<latter; ++j)
                    if (i>>j & 1) {
                        sw += weight[former+j];
                        sv += value[former+j];
                    }

                if (sw <= capacity) {
                    auto tmp=std::lower_bound(
                        items.begin(), items.end(),
                        std::make_pair(capacity-sw, INF)
                    );
                    res = std::max(res, sv+(--tmp)->second);
                }
            }

            return res;
        } else if (algotype == SMALL_CAPACITY) {
            std::vector<int64_t> dp(capacity+1);
            for (size_t i=0; i<n; ++i)
                for (int64_t j=capacity; j>=weight[i]; --j)
                    dp[j] = std::max(dp[j], dp[j-weight[i]]+value[i]);

            return dp[capacity];
        } else if (algotype == LITTLE_VALUE) {
            std::vector<int64_t> dp(sum_v+1, INF);
            dp[0] = 0;
            for (size_t i=0; i<n; ++i)
                for (int64_t j=sum_v; j>=value[i]; --j)
                    dp[j] = std::min(dp[j], dp[j-value[i]]+weight[i]);

            for (size_t i=dp.size(); i--;)
                if (dp[i] <= capacity)
                    return i;
        }

        return -1;
    }
};
