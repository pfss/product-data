# Plan Pricing — Where to Move Next

**From:** Pedro — prepared as a work sample for *Pricing Strategy Manager*, Commerce Product Org
**To:** Hiring team
**Re:** Which plan tier absorbs the next price move, and why

*Note: this memo uses an illustrative model I built for this application, not real Netflix data. It's meant to demonstrate the reasoning and format, not to claim insider numbers. The interactive version of the underlying model is linked at the bottom.*

---

### The decision in one line

Lead the next price action with **Premium**, hold **Standard** flat as the base under active erosion pressure, and treat **Standard with Ads** as a volume lever, not a price lever, until the subscriber base matures further.

### Why

The role description names the core inputs directly — consumer demand, price elasticity, competitive landscape — so I modeled each tier on the same three primitives: current price, an illustrative price-elasticity coefficient, and a willingness-to-pay range. That produces one comparable output per tier: what a price change does to blended revenue once you net subscriber loss against the higher take-rate.

Under the assumptions I used:

- **Premium** is the least price-elastic of the three (-0.30). Its base already selects for higher WTP — 4K, multiple screens — so a price increase loses relatively few subscribers and the take-rate gain dominates. It's the cleanest lever to pull first.
- **Standard** sits in the middle (-0.55) but carries the more important signal in the trend data: it's the only tier losing subscribers quarter over quarter, most likely to members trading down to Ads or up to Premium. That's not a pricing problem to solve with a price increase — raising price on a tier that's already leaking share just accelerates the leak. I'd hold it flat and treat the erosion as the thing to diagnose first.
- **Standard with Ads** is the most elastic (-0.95) and growing fastest in raw subscribers. That combination says the tier is still doing its job as a low-friction entry point; a price increase now would blunt the one lever that's working. The better play is protecting the growth curve and revisiting price once the base and its ad-monetization mix are more mature.

### What I'd want to be wrong about

The elasticity coefficients are the whole model — they're not measured (no conjoint study, no historical price-test data behind them), they're informed assumptions. I'd flag the Standard elasticity as the one most worth pressure-testing first: at -0.55 it's a genuine toss-up on some price moves, and if the real number is closer to Ads-tier elasticity, "hold flat" becomes "cut price to stop the bleed" instead. That's the kind of assumption I'd want a real willingness-to-pay study to replace before this went anywhere near a rate card.

### The ask

Move Premium price up first and watch the churn-risk flag stays clear at the tested level. Leave Standard untouched until we understand why it's the only tier losing share. Leave Ads-tier pricing alone this cycle and let the growth curve keep compounding.

---

**Interactive model:** `index.html` — every price move above is a slider; subscriber impact, revenue impact, and the churn-risk flag recalculate live as you change them.

*Prepared in the spirit of Netflix's "farming for dissent" — this is a starting position for debate, not a final call. Happy to walk through the model and take the other side of any assumption.*
