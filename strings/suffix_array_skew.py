def skew_rec(x : list[int], asize : int) -> list[int]:
    "Recursive skew SA construction algorithm."

    SA12 = [i for i in range(len(x)) if i % 3 != 0]
    
    SA12 = radix3(x, asize, SA12)
    new_alpha = collect_alphabet(x, SA12)
    if len(new_alpha) < len(SA12):
        # Recursively sort SA12.
        # Construct the u string and compute its suffix array
        u = build_u(x, new_alpha)
        # For the recursion, remember that the real alphabet has
        # two sentinels, so + 2
        sa_u = skew_rec(u, len(new_alpha) + 2)
        # Then map u's suffix array back to a sorted SA12
        m = len(sa_u) // 2
        SA12 = [u_idx(i, m) for i in sa_u if i != m]

    # Special case if the last index is class 0. Then the
    # following class 1 isn't there, but we should treat it
    # as the smallest string in the class.
    SA3 = ([len(x) - 1] if len(x) % 3 == 1 else []) + \
          [i - 1 for i in SA12 if i % 3 == 1]
    SA3 = bucket_sort(x, asize, SA3)
    return merge(x, SA12, SA3)