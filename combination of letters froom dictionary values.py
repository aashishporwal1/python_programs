import itertools
dict={"1":["a","b"],"2":["c","d"]}
for combo in itertools.product(*[dict[i] for i in sorted(dict.keys())]):
    print("".join(combo))
