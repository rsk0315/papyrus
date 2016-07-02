vi sieve_of_eratosthenes(int n) {
    vi primes(n);
    int i, j;
    for (i=2; i<n; i++)
        primes[i] = i;

    for (i=2; i*i<n; i++)
        if (primes[i])
            for (j=i*i; j<n; j+=i)
                primes[j] = 0;

    return primes;
}
