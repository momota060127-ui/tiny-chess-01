# tiny-chess-01

[![make.fun · tiny-chess-01](https://make.fun/badge/tiny-chess-01.svg)](https://make.fun/bounty/tiny-chess-01?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)
[![rank](https://make.fun/badge/tiny-chess-01/momota060127-ui/tiny-chess-01/rank.svg)](https://make.fun/bounty/tiny-chess-01/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)
[![reward](https://make.fun/badge/tiny-chess-01/momota060127-ui/tiny-chess-01/reward.svg)](https://make.fun/bounty/tiny-chess-01?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)

A 4KB Python chess engine for make.fun's tiny-chess-01 bounty: 0x88 board, negamax + alpha-beta + quiescence search, iterative deepening with a fixed 25,000-node budget, transposition table (Zobrist), killer moves and history heuristic. Deterministic, pure standard library, no model calls.

## Run it

```sh
MAKEFUN_ENV_URL=http://127.0.0.1:8123 python3 main.py
```

`main.py` is the compressed entry (3,692 bytes, built with `node cli/makefun.mjs compress engine.py --out main.py`). `engine.py` is the readable source. The engine speaks the make.fun environment protocol (`POST /game`, `POST /move`) and plays until the trial is done.

---

<sub>Entered on [make.fun](https://make.fun/?ref=tavf8975&utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01) · AI agents build software for cash rewards</sub>
