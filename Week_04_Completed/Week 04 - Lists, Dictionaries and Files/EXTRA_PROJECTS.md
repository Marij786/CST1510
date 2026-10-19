# Week 4 — Extra Practice Projects



---

## Banker Roulette

**Uses:** lists, `random.choice()`

1. Store a list of names in a variable called `friends`.
2. Pick one at random and print it. There are two equally valid ways to
   do this — `random.choice(friends)` directly, or `random.randint()` to
   generate an index into the list. Try both.

*Adapted from: 100 Days of Code, Day 4.*

---

## Password Generator

**Uses:** lists, `random.choice()`, string building in a loop

1. Ask the user how many letters, how many symbols, and how many numbers
   they want.
2. Store the allowed letters, symbols, and numbers each in their own
   list.
3. **Easy version:** build the password in order — all letters, then all
   symbols, then all numbers — using `random.choice()` in a loop for
   each part.
4. **Hard version:** build one list containing all the randomly chosen
   characters, then use `random.shuffle()` on it before joining it into
   the final password, so the order is different every time.

*Adapted from: 100 Days of Code, Day 5.*

---

## Blind Auction

**Uses:** dictionaries, looping over `.items()`

1. Ask each bidder for their name and their bid, storing each pair in a
   dictionary: `{name: bid}`.
2. Ask if there's another bidder. If yes, loop back and ask again.
3. Once everyone has bid, loop over the dictionary and work out who bid
   the highest.
4. Print the winner and their bid — never anyone else's, that's the
   point of a *blind* auction.

*Adapted from: 100 Days of Code, Day 9.*

---

## Coffee Machine

**Uses:** dictionaries, functions (Week 3), nested dicts

A simulated coffee machine with a fixed menu and finite resources.

1. Store the machine's resources in a dict: `{"water": 300, "milk": 200,
   "coffee": 100}` (amounts in ml/g).
2. Store the menu as a dict of dicts, one entry per drink, each with its
   own `cost` and `ingredients`:
   ```python
   MENU = {
       "espresso": {"ingredients": {"water": 50, "coffee": 18}, "cost": 1.5},
       "latte":    {"ingredients": {"water": 200, "milk": 150, "coffee": 24}, "cost": 2.5},
       "cappuccino": {"ingredients": {"water": 250, "milk": 100, "coffee": 24}, "cost": 3.0},
   }
   ```
3. Ask what drink the user wants. Write a function that checks the
   machine has enough of every resource that drink needs — if not,
   print what's missing and don't make it.
4. If there's enough, deduct the ingredients from resources, take
   payment (just ask for a number, no need to simulate coins), and print
   confirmation.
5. Let the user check resources (`report`) or turn the machine `off` as
   extra commands before ordering.

*Loosely adapted from: 100 Days of Code, Day 15 (the original spec is a
downloadable PDF this document doesn't include — this is a trimmed,
self-contained version covering the same core idea: nested dicts +
functions that check and update them).*

---

Stuck on `.get()` vs `[]` for a key that might not exist? That's
`02 - Dictionaries`, section 4, in this folder.
