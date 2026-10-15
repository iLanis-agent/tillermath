#!/usr/bin/env python3
# Tiller Math oracle - mirrors engine.js float-for-float.
import json, math
OVERLAP = 0.8
FIRST = 0.6
SECOND = 0.85
RATE = 0.5
def r1(x): return math.floor(x*10+0.5)/10
def f1(x): return "%.1f" % r1(x)
def jsnum(x):
    i = int(x)
    return i if x == i else x

def width_plan(claim, width):
    if not (claim > 0): return {"error": "the claimed inches must be above zero"}
    if not (width > 0): return {"error": "the bed feet must be above zero"}
    honest_raw = claim * OVERLAP
    lanes = math.ceil(width * 12 / honest_raw)
    verdict = "three honest lanes" if lanes <= 3 else ("a working rhythm" if lanes <= 6 else "a lawn of lanes")
    return {"honestIn": jsnum(r1(honest_raw)), "lanes": lanes, "verdict": verdict}
def render_width(r, claim, width):
    lane_word = "1 lane" if r["lanes"] == 1 else "%s lanes" % r["lanes"]
    return ("The %s-inch claim honestly tills %s inches after the 0.8 overlap norm; the %s-foot bed is %s - %s."
            % (claim, f1(r["honestIn"]), width, lane_word, r["verdict"]))

def depth_plan(claim, target):
    if not (claim > 0): return {"error": "the claimed inches must be above zero"}
    if not (target > 0): return {"error": "the target inches must be above zero"}
    first_raw = claim * FIRST
    second_raw = claim * SECOND
    verdict = "one pass and done" if target <= first_raw else ("two passes deep" if target <= second_raw else "a third pass, honestly")
    return {"firstIn": jsnum(r1(first_raw)), "secondIn": jsnum(r1(second_raw)), "verdict": verdict}
def render_depth(r, claim, target):
    return ("The %s-inch claim honestly reaches %s inches on the first pass and %s on the second (labeled norms); the %s-inch target is %s."
            % (claim, f1(r["firstIn"]), f1(r["secondIn"]), target, r["verdict"]))

def bed_plan(sqft, passes):
    if not (sqft > 0): return {"error": "the square feet must be above zero"}
    if not (passes > 0): return {"error": "the passes must be above zero"}
    min_raw = sqft * passes / RATE
    verdict = "done before the sprinkler cycle" if min_raw <= 45 else ("a working afternoon" if min_raw <= 120 else "a two-weekend bed")
    return {"minutes": jsnum(r1(min_raw)), "verdict": verdict}
def render_bed(r, sqft, passes):
    pass_word = "1 pass" if passes == 1 else "%s passes" % passes
    min_word = "1 minute" if r["minutes"] == 1 else f1(r["minutes"]) + " minutes"
    return ("%s over %s square feet at the 0.5 square-feet-a-minute norm is %s - %s."
            % (pass_word, sqft, min_word, r["verdict"]))

CASES = [
    ("width", (18,8)), ("width", (20,4)), ("width", (16,6)),
    ("width", (21,3)), ("width", (14,10)), ("width", (26,5)),
    ("depth", (10,6)), ("depth", (10,8)), ("depth", (10,9)),
    ("depth", (8,4.5)), ("depth", (12,9)), ("depth", (6,5.5)),
    ("bed", (20,1)), ("bed", (25,1)), ("bed", (30,2)),
    ("bed", (100,2)), ("bed", (15,2)), ("bed", (45,3)),
    ("width", (0,8)), ("width", (18,0)),
    ("depth", (0,6)), ("depth", (10,0)),
    ("bed", (0,2)), ("bed", (20,0)),
]
PLANS = {"width": (width_plan, render_width), "depth": (depth_plan, render_depth), "bed": (bed_plan, render_bed)}
out = []
for tool, args in CASES:
    plan, render = PLANS[tool]
    r = plan(*args)
    case = {"tool": tool, "args": list(args), "result": r}
    if "error" not in r:
        case["render"] = render(r, *args)
    out.append(case)
print(json.dumps(out, separators=(",", ":")), end="")
