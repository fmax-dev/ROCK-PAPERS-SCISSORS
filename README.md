# Rock, Paper and Scissors

A simple Rock, Paper, Scissors CLI game for beginners.

## Table of Contents
- [Features Overview](#features-overview)
- [Installation](#installation)
- [Usage](#usage)
- [Next Steps](#next-steps)


## Features Overview

- **Configurable match length** — choose your target wins at the start (e.g. 2 for Best of 3, 3 for Best of 5)
- **Win-by-2 rule** — if scores are close, the match extends until someone leads by 2
- **Input validation** — rejects any input that isn't `r`, `p`, or `s` and re-prompts
- **Emoji display** — shows 🪨 📄 ✂️ for each round result
- **Match history log** — every round outcome is recorded and printed at the end
- **Tie counter** — post-match summary includes how many ties occurred
- **Play again** — option to restart without relaunching the script


## Installation

To install this program, use the commands below:

```bash
git clone https://github.com/fmax-dev/ROCK-PAPERS-SCISSORS.git
cd ROCK-PAPERS-SCISSORS
```


## Usage

To start using this program:
1. Clone this repo using the commands above
2. Run the game:
   - **Windows:** `python rock_paper_scissor.py`
   - **Mac/Linux:** `python3 rock_paper_scissor.py`
3. Enter your target wins when prompted, then type `r`, `p`, or `s` each round


## Next Steps

Looking to expand the project? Here are some ideas, roughly in order of difficulty:

- **Add Lizard & Spock** — extend `CHOICES`, `EMOJIS`, `NAMES`, and `determine_round_winner` to support the [5-choice variant](https://bigbangtheory.fandom.com/wiki/Rock_Paper_Scissors_Lizard_Spock)
- **Persist scores across sessions** — save win/loss totals to a `scores.json` file so the leaderboard survives between runs
- **Track computer patterns** — instead of pure `random.choice`, have the computer weight its picks based on your recent move history
- **Add a 2-player mode** — prompt a second player for their choice (hide it from the first player using `getpass`)
- **Build a GUI** — replace the CLI with a simple window using `tkinter` (ships with Python, no install needed)
- **Package it** — add a `pyproject.toml` and publish to PyPI so others can install it with `pip install rock-paper-scissors`
