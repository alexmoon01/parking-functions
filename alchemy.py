from generate import gen_pfs


def transmogrify_step(pf: tuple):
    new_pf = list(pf)

    # Find indices of maximal and minimal elements of pf
    max_inds = tuple(i for i in range(len(pf)) if pf[i] == max(pf))
    min_inds = tuple(i for i in range(len(pf)) if pf[i] == min(pf))
    print(max_inds, min_inds)

    i, j = 0, 0
    if min(min_inds) > max(max_inds):
        print("HERE")
        i = max(min_inds)
        j = min(max_inds)
    else:
        i = max((k for k in min_inds if k < max(max_inds)))
        j = min((k for k in max_inds if k > min(min_inds)))
    tmp = new_pf[i]
    new_pf[i] = new_pf[j]
    new_pf[j] = tmp
    return tuple(new_pf)


print((1,2,2), transmogrify_step((1,2,2)))
print((2,1,2), transmogrify_step((2,1,2)))
print((2,2,1), transmogrify_step((2,2,1)))