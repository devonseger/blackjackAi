### ✅ Blackjack AI Trainer - Phase 1 Checklist

#### 1️⃣ Card & Deck System

- [x] Create a `Card` class with:

  - [x] Suit (`♠, ♣, ♦, ♥`)
  - [x] Rank (`2-10, J, Q, K, A`)
  - [x] Value (Aces can be `1` or `11`)

- [x] Create a `Deck` class:
  - [x] Generate a full 52-card deck
  - [x] Shuffle the deck
  - [x] Implement a `deal_card()` method

---

#### 2️⃣ Player & Dealer System

- [x] Create a `Hand` class to:

  - [x] Store a list of `Card` objects
  - [x] Calculate the total hand value
  - [x] Handle **Aces** dynamically (`1` or `11`)

- [x] Implement **Player actions**:
  - [x] `hit()` → Draws a card from the deck
  - [x] `stand()` → Ends turn
  - [x] `check_bust()` → Determines if hand > 21

---

#### 3️⃣ Game Loop (Main Gameplay)

- [x] Deal **two cards** to player & dealer
- [x] Reveal **one** of the dealer's cards
- [x] Display **player's full hand**
- [x] Ask player for action (`hit` or `stand`)
  - [x] If `hit`: Draw card & check for bust
  - [x] If `stand`: Move to dealer’s turn

---

#### 4️⃣ Dealer's Turn

- [x] Dealer must **hit** until total is **17 or higher**
- [x] Compare hands and determine winner
- [x] Handle tie conditions
