---
name: delta-harden
description: >
  Phase 4 Hardening & Code Review Skill.
  Runs rm-slop plain-English documentation audit, routes multi-model code review to Vertex AI Model Garden Opus 5 ZDR, deepens codebase architecture (improve-codebase-architecture HTML reports), and validates final ROI savings.
  Triggers on: "delta harden", "phase 4 hardening", "opus 5 review", "anti slop audit", "rm-slop", "improve codebase architecture", "architecture review".
---

# Phase 4: Hardening & Launch (`delta-harden`)

Governs Phase 4 (Weeks 11-12) of the engagement lifecycle. Hardens documentation against AI slop, conducts zero data retention (ZDR) code review, deepens module architecture, and validates metric savings for handoff.

---

## 🔒 Hardening Protocols

1. **Plain-English Anti-Slop Audit (`rm-slop`)**: Strips corporate buzzwords, filler, and unmeasurable hand-wavy claims from PRDs and guides.
2. **Vertex AI Model Garden Opus 5 ZDR Peer Review**: Routes two-pass code review to ZDR-compliant Claude Opus 5 (`claude-opus-5`).
3. **Codebase Architecture Deepening (`improve-codebase-architecture`)**: Scans git commit hot spots for shallow modules, presents a visual HTML report with Mermaid before/after diagrams, and deepens seams for testability.
4. **ROI Benchmark Savings**: Calculates metric savings against `baseline_kpis.json` for customer executive report.

---

## 💻 CLI Execution

```bash
# Run Anti-Slop Audit:
python3 skills/delta-build/scripts/delta_cli.py harden --doc README.md
```

---

## ✋ Human Checkpoint (Phase Gate 4 Exit)
Customer sign-off on `HANDOFF_PACKET.md` and baseline ROI savings report prior to production launch.
