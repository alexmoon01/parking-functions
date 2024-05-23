from itertools import combinations, permutations
from avoidant import *


def gen_ndpfs(n: int):
    """
    Generate nondecreasing parking functions.
    :param n: Length parameter
    :return: All nondecreasing parking functions of length n.
    """
    ndpfs = {tuple([1])}
    for i in range(n-1):
        new_ndpfs = set()
        for ndpf in ndpfs:
            for j in range(ndpf[i], i+3):
                new_ndpfs.add((*ndpf, j))
        ndpfs = new_ndpfs
    return ndpfs


def gen_pfs(n: int):
    """
    Generate parking functions
    :param n: Length parameter
    :return: All parking functions of length n.
    """
    ndpfs = gen_ndpfs(n)
    pfs = set()
    for ndpf in ndpfs:
        pfs = pfs.union(set(permutations(ndpf)))
    return pfs


def pretty_print(fn: dict):
    for key in fn.keys():
        print(f"{key}: {fn[key]}")
    print("--------------------")
    print()


def count_preimage(fn: dict):
    preimages = dict()
    for key in fn.keys():
        if fn[key] in preimages.keys():
            preimages[fn[key]] += 1
        else:
            preimages[fn[key]] = 1
    return preimages


for n in range(3, 9):

    pfs = gen_pfs(n)
    print(f"{len(DA_avoid(pfs))}")
