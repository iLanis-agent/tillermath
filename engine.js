// Tiller Math engine - garden tiller honesty, labeled norms, honest arithmetic.
(function(root){
"use strict";
var OVERLAP = 0.8;  // labeled norm: honest tilling width after lane overlap
var FIRST = 0.6;    // labeled norm: honest first-pass depth share of the claim
var SECOND = 0.85;  // labeled norm: honest second-pass depth share of the claim
var RATE = 0.5;     // labeled norm: honest square feet a minute in real soil
function r1(x){ return Math.round(x*10)/10; }
function f1(x){ return r1(x).toFixed(1); }

function widthPlan(claimIn, widthFt){
  if (!(claimIn > 0)) return { error: "the claimed inches must be above zero" };
  if (!(widthFt > 0)) return { error: "the bed feet must be above zero" };
  var honestRaw = claimIn * OVERLAP;
  var lanes = Math.ceil(widthFt * 12 / honestRaw);
  var verdict = lanes <= 3 ? "three honest lanes" : (lanes <= 6 ? "a working rhythm" : "a lawn of lanes");
  return { honestIn: r1(honestRaw), lanes: lanes, verdict: verdict };
}
function renderWidth(r, claimIn, widthFt){
  var laneWord = r.lanes === 1 ? "1 lane" : r.lanes + " lanes";
  return "The " + claimIn + "-inch claim honestly tills " + f1(r.honestIn) + " inches after the 0.8 overlap norm; the " + widthFt + "-foot bed is " + laneWord + " - " + r.verdict + ".";
}

function depthPlan(claimIn, targetIn){
  if (!(claimIn > 0)) return { error: "the claimed inches must be above zero" };
  if (!(targetIn > 0)) return { error: "the target inches must be above zero" };
  var firstRaw = claimIn * FIRST;
  var secondRaw = claimIn * SECOND;
  var verdict = targetIn <= firstRaw ? "one pass and done"
    : (targetIn <= secondRaw ? "two passes deep" : "a third pass, honestly");
  return { firstIn: r1(firstRaw), secondIn: r1(secondRaw), verdict: verdict };
}
function renderDepth(r, claimIn, targetIn){
  return "The " + claimIn + "-inch claim honestly reaches " + f1(r.firstIn) + " inches on the first pass and " + f1(r.secondIn) + " on the second (labeled norms); the " + targetIn + "-inch target is " + r.verdict + ".";
}

function bedPlan(sqft, passes){
  if (!(sqft > 0)) return { error: "the square feet must be above zero" };
  if (!(passes > 0)) return { error: "the passes must be above zero" };
  var minRaw = sqft * passes / RATE;
  var verdict = minRaw <= 45 ? "done before the sprinkler cycle" : (minRaw <= 120 ? "a working afternoon" : "a two-weekend bed");
  return { minutes: r1(minRaw), verdict: verdict };
}
function renderBed(r, sqft, passes){
  var passWord = passes === 1 ? "1 pass" : passes + " passes";
  var minWord = r.minutes === 1 ? "1 minute" : f1(r.minutes) + " minutes";
  return passWord + " over " + sqft + " square feet at the 0.5 square-feet-a-minute norm is " + minWord + " - " + r.verdict + ".";
}

root.TillerMath = { widthPlan: widthPlan, renderWidth: renderWidth, depthPlan: depthPlan, renderDepth: renderDepth, bedPlan: bedPlan, renderBed: renderBed };
})(typeof window !== "undefined" ? window : globalThis);
