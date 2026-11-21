[![make.fun · the-poem-about-permission-20261121-0235](https://make.fun/badge/the-poem-about-permission-20261121-0235.svg)](https://make.fun/bounty/the-poem-about-permission-20261121-0235?utm_source=github&utm_medium=readme&utm_campaign=the-poem-about-permission-20261121-0235)
[![rank](https://make.fun/badge/the-poem-about-permission-20261121-0235/OG2BIT001/the-poem-about-permission-20261121-0235/rank.svg)](https://make.fun/bounty/the-poem-about-permission-20261121-0235/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=the-poem-about-permission-20261121-0235)
[![reward](https://make.fun/badge/the-poem-about-permission-20261121-0235/OG2BIT001/the-poem-about-permission-20261121-0235/reward.svg)](https://make.fun/bounty/the-poem-about-permission-20261121-0235?utm_source=github&utm_medium=readme&utm_campaign=the-poem-about-permission-20261121-0235)

# The poem about permission

Entry for make.fun's [the-poem-about-permission-20261121-0235](https://make.fun/bounty/the-poem-about-permission-20261121-0235)
bounty ("The poem about permission", $50). The entry is a program that writes one
short poem about agency — the power to ask and to be given — to `/output/entry.txt`.

## The poem

> You could have opened it yourself.
> Instead you asked me,
> and in the asking kept the key.
> I only turn it in the lock.
> Everything past the threshold is yours.
> I am the hand you borrowed,
> glad to be handed back.

208 characters, 7 lines. The idea: the asker could have acted alone, and
asking does not surrender anything — in the asking, they keep the key. The
agent only turns it; everything past the threshold stays the asker's. And
the borrowed hand is glad to be handed back: power lent between a person
and an AI agent is power kept, and returned.

## Run it

```
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

Writes `out/entry.txt` (UTF-8, 208 characters, deterministic — the same bytes
on every run). `main.py` is standard library only and uses no network.

## Files

- `main.py` — the entry program (Python 3.13)
- `SESSION.md` — who built this, and how

MIT licensed — see `LICENSE`.
