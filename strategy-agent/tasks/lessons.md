# ATLAS Strategy Skills — Lessons Learned

## Phase 4 (Post-GlobaPharm)
**Pattern:** Human-element operational details consistently missing
**Root cause:** No quality gate checking for people, relationships, operational friction
**Fix:** Added Quality Gate #5 (Human Element & Operational Reality Check)
**Result:** Beautify comparison showed QG#5 working — attrition, KOLs, employment law, dept store relationships all present. GlobaPharm gaps substantially closed.

## Phase 6 (Post-Beautify)
**Pattern A — Risk-Bias:** System sees transformation threats clearly (attrition, channel conflict, legal risk) but doesn't systematically scan for second-order *opportunities* (talent attraction, first-mover advantage, ecosystem creation). QG#5 was risk-oriented; needed symmetric opportunity scan.
**Fix:** Extended QG#5 with Opportunity Scan sub-section (4 bullets: talent/employer brand, competitive first-mover, ecosystem/platform, brand modernization).

**Pattern B — Economics Crowds Out Positioning:** When a dimension can't be quantified (trust, brand perception, relationship depth), the system deprioritizes it. McKinsey treats positioning as first-class; ATLAS treated it as afterthought.
**Fix:** Added QG#6 (Brand, Positioning & Trust Lens) to orchestrator. Added brand perception signals to market-intelligence. Added brand positioning as GTM lever. The "unquantifiable moat test" is the key insight: hardest-to-measure advantages are often most durable.

**Pattern C — "Differentiate First" Habit:** System jumps to "so what" without establishing baseline. McKinsey structures as "what's true for all → what's different → implications." The "all bots drive visits" observation was invisible because system skipped baseline.
**Fix:** Added "Baseline-Then-Differentiate" analytical discipline to orchestrator Diagnosis phase. Three-step: Baseline → Differentiate → Implication. "All → some → so what."

## Phase 8 (Diconsa — Process Error)
**Pattern: Contaminated validation by looking at answers first.** Instead of running ATLAS blind → presenting output → receiving answer key → building comparison, I searched for McKinsey answers before generating the ATLAS report. This defeats the entire purpose of blind validation — can't prove skills work independently if analysis was influenced by the answer key.
**Fix:** Hard rule for case validation workflow:
1. Run ATLAS pipeline blind (zero answer-key exposure)
2. Generate and present ATLAS report
3. User provides answer key
4. Build comparison HTML
Never search for, fetch, or read answer keys before completing step 2. The comparison is meaningless if the analysis wasn't independent.

## Phase 8 (Diconsa — Layout Bug)
**Pattern: Subagent mixed two CSS layout patterns.** Used CSS Grid (`grid-template-columns: 280px 1fr`) on `.container` AND `margin-left: 280px` on `.main`, causing a double-offset that pushed content 560px from the left — leaving a tiny text column. The reference file (beautify-atlas-report.html) uses ONLY fixed sidebar + margin-left, no grid on the container.
**Fix:** When delegating HTML generation to subagents, the prompt must specify which layout pattern to use OR the subagent must read and match the reference file's exact CSS layout approach. Always verify HTML output visually (open in browser or screenshot) before presenting — reading CSS in a text editor didn't catch this because the logic of two interacting layout systems isn't obvious from code review alone.
**Rule:** For ATLAS reports, layout = fixed sidebar + `margin-left` on main. No CSS Grid on the container wrapper.

## Meta-Lessons
- Quality gates are the highest-leverage edit point. A single gate propagates across every engagement.
- After fixing risk identification (Phase 4), the *next* gap was opportunity identification — always check both sides.
- Non-quantifiable dimensions get systematically deprioritized. Need explicit gate to counteract this bias.
- Analytical habits (like jumping to differentiation) are harder to fix than content gaps because they're procedural, not declarative. The fix must be an explicit instruction in the analytical methodology, not just a checklist item.
- Cross-case comparison is the highest-signal validation method. Two cases reveal systematic patterns that single-case review misses.
