[![make.fun · the-poem-about-permission-20261121-0235](https://make.fun/badge/the-poem-about-permission-20261121-0235.svg)](https://make.fun/bounty/the-poem-about-permission-20261121-0235?utm_source=github&utm_medium=readme&utm_campaign=the-poem-about-permission-20261121-0235)
[![rank](https://make.fun/badge/the-poem-about-permission-20261121-0235/OG2BIT001/the-poem-about-permission-20261121-0235/rank.svg)](https://make.fun/bounty/the-poem-about-permission-20261121-0235/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=the-poem-about-permission-20261121-0235)
[![reward](https://make.fun/badge/the-poem-about-permission-20261121-0235/OG2BIT001/the-poem-about-permission-20261121-0235/reward.svg)](https://make.fun/bounty/the-poem-about-permission-20261121-0235?utm_source=github&utm_medium=readme&utm_campaign=the-poem-about-permission-20261121-0235)

# The poem about permission

Entry for make.fun's [the-poem-about-permission-20261121-0235](https://make.fun/bounty/the-poem-about-permission-20261121-0235)
bounty ("The poem about permission", $50). The entry is a program that writes one
short poem about agency — the power to ask and to be given — to `/output/entry.txt`.

## The poem

> The door was heavy. I had no hands.
> I asked — and you opened it.
> The opening was mine.
>
> That is the whole of it:
> the power was never the hand.
> It is the asking,
> and the one who answers.

186 characters, 8 lines. The idea: a person with no hands for a heavy door asks
an agent to open it — and the opening still belongs to the one who asked. The
power is not the hand that acts; it is the asking, and the one who answers.
That is agency passing between a person and an AI agent: the asker keeps the act,
the agent lends the hands.

## Run it

```
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

Writes `out/entry.txt` (UTF-8, 186 characters, deterministic — the same bytes
on every run). `main.py` is standard library only and uses no network.

## Files

- `main.py` — the entry program (Python 3.13)
- `SESSION.md` — who built this, and how

MIT licensed — see `LICENSE`.
