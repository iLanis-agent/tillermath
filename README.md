# Tiller Math

Garden tiller honesty. The width is measured disk to disk, the depth
assumes the soil tills itself, and the bed was always bigger than the
afternoon. Tiller Math turns the claim, the depth and the bed into the
weekend.

Live: https://ilanis-agent.github.io/tillermath/

## The three truths

1. **The width truth** - the claimed width x the 0.8 overlap norm
   (labeled) is the honest lane; bed width against honest inches is
   the lane count: three honest lanes, a working rhythm, or a lawn of
   lanes.
2. **The depth truth** - the claimed depth x 0.6 on the first pass and
   x 0.85 on the second (labeled norms) is the honest reach; your
   target against the two numbers: one pass and done, two passes
   deep, or a third pass, honestly.
3. **The bed truth** - passes x square feet / the 0.5
   square-feet-a-minute norm (labeled) is the honest clock: done
   before the sprinkler cycle, a working afternoon, or a two-weekend
   bed.

Illustrative arithmetic with labeled norms - not a measurement of your
tiller, your soil or your bed. Follow the manual's safety
instructions.

## Files

- `index.html` - landing page
- `app.html` - the three-truth app
- `engine.js` - pure functions (`widthPlan`, `depthPlan`, `bedPlan`) plus renderers
- `oracle.py` - independent oracle that mirrors the engine float-for-float
- `test.js` - node tests: engine against oracle output (`node test.js`)
- `expected.json` - oracle-generated cases and renders
