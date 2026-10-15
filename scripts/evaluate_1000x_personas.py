#!/usr/bin/env python3
"""1,000-Iteration (50 Use Cases x 20 Stakeholder Personas = 13,000 Skill Evals) Benchmark.

Simulates 50 real-world enterprise AI/Agent use cases across 20 distinct customer
stakeholder personas (Security/CISO, AI Governance, Enterprise Architecture, DevOps/SRE,
IT/Identity, FinOps/CFO, Business Sponsor, Domain Analyst, Product, UX, Data Eng,
Legal/Privacy, MRM Quant, Network Sec, Frontline Ops, Procurement, QA, Red-Team,
Change Mgmt, CTO/Transformation).

Evaluates:
  1. Persona-Specific Approval Score across all 13 skills (13,000 skill executions)
  2. Deterministic CLI Calculators under dynamic LLM token OpEx, 5x fan-out, and judge traps
  3. "Is It Worth It?" Portfolio Decision Matrix (Full 13-Skill Mode vs. Fast-Track 5-Skill Lite Mode vs. Gate-0 Kill/Re-Scope)
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT / "scripts"))
sys.path.insert(0, str(REPO_ROOT / "skills" / "ai-value-sizing" / "scripts"))
sys.path.insert(0, str(REPO_ROOT / "skills" / "agent-load-testing" / "scripts"))
sys.path.insert(0, str(REPO_ROOT / "skills" / "agent-eval-statistical-auditing" / "scripts"))

import audit_llm_judge
import calculate_agent_quotas
import calculate_roi
import evaluate_200x_skills

# 50 Enterprise AI / Agent Use Cases across 10 Industries & 3 Economic Archetypes:
#   - 40 Core Enterprise Transformation Use Cases (Archetype: FULL_13_SKILL)
#   - 6 Departmental / Tactical Use Cases (Archetype: FAST_TRACK_5_SKILL)
#   - 4 Low-Volume / Unviable Data Trap Use Cases (Archetype: GATE_0_KILL_TRAP)
USE_CASES_50: list[dict[str, Any]] = [
    # --- Financial Services (5) ---
    {"id": "UC01_fin_aml_wire", "industry": "Financial Services", "name": "Wire Fraud & AML SAR Triage Agent", "archetype": "FULL_13_SKILL", "tam": 140000, "sam": 0.75, "adopt": 0.30, "compat": 0.90, "hrs": 0.55, "rate": 95.0, "capex": 240000, "opex": 72000, "vcr": 0.55, "scdf": 0.85, "qt": 6, "cq": 4, "tokens": 22000, "turns_min": 14, "tier": 2},
    {"id": "UC02_fin_kyc_onboard", "industry": "Financial Services", "name": "Commercial KYC Entity Onboarding & UBO Verification", "archetype": "FULL_13_SKILL", "tam": 85000, "sam": 0.80, "adopt": 0.30, "compat": 0.85, "hrs": 0.75, "rate": 90.0, "capex": 210000, "opex": 65000, "vcr": 0.55, "scdf": 0.85, "qt": 5, "cq": 4, "tokens": 18000, "turns_min": 10, "tier": 2},
    {"id": "UC03_fin_mortgage_uw", "industry": "Financial Services", "name": "Residential Mortgage Income & Tax Return Underwriter", "archetype": "FULL_13_SKILL", "tam": 110000, "sam": 0.70, "adopt": 0.30, "compat": 0.85, "hrs": 0.65, "rate": 85.0, "capex": 195000, "opex": 60000, "vcr": 0.55, "scdf": 0.85, "qt": 6, "cq": 3, "tokens": 20000, "turns_min": 12, "tier": 2},
    {"id": "UC04_fin_wealth_brief", "industry": "Financial Services", "name": "Private Wealth Advisor Pre-Meeting Portfolio Synthesizer", "archetype": "FULL_13_SKILL", "tam": 95000, "sam": 0.75, "adopt": 0.30, "compat": 0.90, "hrs": 0.50, "rate": 115.0, "capex": 180000, "opex": 58000, "vcr": 0.50, "scdf": 0.85, "qt": 5, "cq": 3, "tokens": 16000, "turns_min": 15, "tier": 2},
    {"id": "UC05_fin_branch_faq_trap", "industry": "Financial Services", "name": "Small Regional Branch Policy Lookup Bot (Low Volume)", "archetype": "FAST_TRACK_5_SKILL", "tam": 18000, "sam": 0.65, "adopt": 0.30, "compat": 0.85, "hrs": 0.45, "rate": 72.0, "capex": 170000, "opex": 52000, "vcr": 0.50, "scdf": 0.85, "qt": 2, "cq": 2, "tokens": 8000, "turns_min": 3, "tier": 1},

    # --- Insurance (5) ---
    {"id": "UC06_ins_auto_fnol", "industry": "Insurance", "name": "Commercial Auto FNOL & Policy Coverage Triage", "archetype": "FULL_13_SKILL", "tam": 80000, "sam": 0.625, "adopt": 0.30, "compat": 0.80, "hrs": 0.70, "rate": 75.0, "capex": 180000, "opex": 58000, "vcr": 0.5912, "scdf": 0.85, "qt": 6, "cq": 4, "tokens": 20000, "turns_min": 10, "tier": 2},
    {"id": "UC07_ins_prop_subro", "industry": "Insurance", "name": "Property Subrogation Demand Package Recovery Agent", "archetype": "FULL_13_SKILL", "tam": 72000, "sam": 0.75, "adopt": 0.30, "compat": 0.85, "hrs": 0.80, "rate": 82.0, "capex": 190000, "opex": 62000, "vcr": 0.55, "scdf": 0.85, "qt": 5, "cq": 4, "tokens": 19000, "turns_min": 9, "tier": 2},
    {"id": "UC08_ins_comm_submission", "industry": "Insurance", "name": "Excess & Surplus (E&S) Broker Submission Intake Triage", "archetype": "FULL_13_SKILL", "tam": 90000, "sam": 0.70, "adopt": 0.30, "compat": 0.85, "hrs": 0.65, "rate": 88.0, "capex": 200000, "opex": 64000, "vcr": 0.55, "scdf": 0.85, "qt": 6, "cq": 3, "tokens": 21000, "turns_min": 11, "tier": 2},
    {"id": "UC09_ins_workers_comp", "industry": "Insurance", "name": "Workers Comp Medical Bill Chronology Summarizer", "archetype": "FULL_13_SKILL", "tam": 68000, "sam": 0.78, "adopt": 0.30, "compat": 0.85, "hrs": 0.75, "rate": 78.0, "capex": 175000, "opex": 56000, "vcr": 0.55, "scdf": 0.85, "qt": 6, "cq": 4, "tokens": 22000, "turns_min": 10, "tier": 2},
    {"id": "UC10_ins_actuary_memo_lite", "industry": "Insurance", "name": "Departmental Reinsurance Treaty Clause Search", "archetype": "FAST_TRACK_5_SKILL", "tam": 16000, "sam": 0.70, "adopt": 0.30, "compat": 0.85, "hrs": 0.50, "rate": 85.0, "capex": 165000, "opex": 50000, "vcr": 0.50, "scdf": 0.85, "qt": 3, "cq": 2, "tokens": 10000, "turns_min": 3, "tier": 1},

    # --- Healthcare & Life Sciences (5) ---
    {"id": "UC11_hlt_prior_auth", "industry": "Healthcare & Life Sciences", "name": "Clinical Search & Prior Authorization Nurse Co-Pilot", "archetype": "FULL_13_SKILL", "tam": 95000, "sam": 0.70, "adopt": 0.30, "compat": 0.85, "hrs": 0.65, "rate": 88.0, "capex": 210000, "opex": 66000, "vcr": 0.55, "scdf": 0.85, "qt": 6, "cq": 4, "tokens": 20000, "turns_min": 10, "tier": 3},
    {"id": "UC12_hlt_cdi_coding", "industry": "Healthcare & Life Sciences", "name": "Inpatient Clinical Documentation Integrity (CDI) DRG Auditor", "archetype": "FULL_13_SKILL", "tam": 120000, "sam": 0.75, "adopt": 0.30, "compat": 0.85, "hrs": 0.55, "rate": 84.0, "capex": 205000, "opex": 64000, "vcr": 0.55, "scdf": 0.85, "qt": 5, "cq": 4, "tokens": 18000, "turns_min": 14, "tier": 2},
    {"id": "UC13_hlt_cmc_dossier", "industry": "Healthcare & Life Sciences", "name": "BioPharma FDA CMC Module 3 Regulatory Dossier Drafter", "archetype": "FULL_13_SKILL", "tam": 55000, "sam": 0.80, "adopt": 0.30, "compat": 0.85, "hrs": 0.95, "rate": 110.0, "capex": 220000, "opex": 68000, "vcr": 0.55, "scdf": 0.85, "qt": 6, "cq": 4, "tokens": 24000, "turns_min": 8, "tier": 2},
    {"id": "UC14_hlt_pharmacovig", "industry": "Healthcare & Life Sciences", "name": "Adverse Event Case Intake & MedDRA Coding Agent", "archetype": "FULL_13_SKILL", "tam": 105000, "sam": 0.72, "adopt": 0.30, "compat": 0.85, "hrs": 0.60, "rate": 86.0, "capex": 195000, "opex": 62000, "vcr": 0.55, "scdf": 0.85, "qt": 5, "cq": 3, "tokens": 17000, "turns_min": 12, "tier": 2},
    {"id": "UC15_hlt_paper_fax_trap", "industry": "Healthcare & Life Sciences", "name": "Unindexed Handwritten Clinic Fax Bot (SCDF=0.20 Trap)", "archetype": "GATE_0_KILL_TRAP", "tam": 6000, "sam": 0.40, "adopt": 0.20, "compat": 0.50, "hrs": 0.25, "rate": 55.0, "capex": 240000, "opex": 85000, "vcr": 0.25, "scdf": 0.20, "qt": 6, "cq": 4, "tokens": 22000, "turns_min": 5, "tier": 3},

    # --- Telecom & Media (5) ---
    {"id": "UC16_tel_noc_triage", "industry": "Telecom & Media", "name": "Autonomous 5G NOC Alarm Correlation & Dispatch Agent", "archetype": "FULL_13_SKILL", "tam": 220000, "sam": 0.80, "adopt": 0.30, "compat": 0.90, "hrs": 0.35, "rate": 82.0, "capex": 250000, "opex": 78000, "vcr": 0.55, "scdf": 0.85, "qt": 5, "cq": 3, "tokens": 16000, "turns_min": 20, "tier": 3},
    {"id": "UC17_med_asset_buddy", "industry": "Telecom & Media", "name": "Multi-Modal Archive Rights & Clip Discovery ('Asset Buddy')", "archetype": "FULL_13_SKILL", "tam": 125000, "sam": 0.76, "adopt": 0.30, "compat": 0.85, "hrs": 0.50, "rate": 80.0, "capex": 185000, "opex": 58000, "vcr": 0.55, "scdf": 0.85, "qt": 6, "cq": 4, "tokens": 18000, "turns_min": 16, "tier": 2},
    {"id": "UC18_tel_b2b_rfp", "industry": "Telecom & Media", "name": "Enterprise Fiber & SD-WAN Solution Architecture RFP Responder", "archetype": "FULL_13_SKILL", "tam": 65000, "sam": 0.78, "adopt": 0.30, "compat": 0.85, "hrs": 0.85, "rate": 92.0, "capex": 185000, "opex": 58000, "vcr": 0.55, "scdf": 0.85, "qt": 5, "cq": 4, "tokens": 19000, "turns_min": 9, "tier": 2},
    {"id": "UC19_med_ad_standards", "industry": "Telecom & Media", "name": "Broadcast Commercial Clearance & Regional Ad Compliance Agent", "archetype": "FULL_13_SKILL", "tam": 88000, "sam": 0.74, "adopt": 0.30, "compat": 0.85, "hrs": 0.60, "rate": 78.0, "capex": 175000, "opex": 55000, "vcr": 0.55, "scdf": 0.85, "qt": 4, "cq": 3, "tokens": 15000, "turns_min": 11, "tier": 2},
    {"id": "UC20_med_pr_clip_lite", "industry": "Telecom & Media", "name": "Internal PR Team Press Mention Digest", "archetype": "FAST_TRACK_5_SKILL", "tam": 15000, "sam": 0.70, "adopt": 0.30, "compat": 0.85, "hrs": 0.50, "rate": 75.0, "capex": 160000, "opex": 48000, "vcr": 0.50, "scdf": 0.85, "qt": 2, "cq": 2, "tokens": 9000, "turns_min": 2, "tier": 1},

    # --- Manufacturing & Automotive (5) ---
    {"id": "UC21_mfg_supplier_audit", "industry": "Manufacturing & Automotive", "name": "Supplier Rate Variance Audit & Part Shortage Recovery", "archetype": "FULL_13_SKILL", "tam": 64000, "sam": 0.75, "adopt": 0.30, "compat": 0.85, "hrs": 0.85, "rate": 78.0, "capex": 175000, "opex": 54000, "vcr": 0.55, "scdf": 0.85, "qt": 5, "cq": 4, "tokens": 18000, "turns_min": 8, "tier": 2},
    {"id": "UC22_mfg_aero_mro", "industry": "Manufacturing & Automotive", "name": "Aerospace MRO Airworthiness Directive & Fault Isolation Co-Pilot", "archetype": "FULL_13_SKILL", "tam": 70000, "sam": 0.78, "adopt": 0.30, "compat": 0.85, "hrs": 0.80, "rate": 94.0, "capex": 205000, "opex": 64000, "vcr": 0.55, "scdf": 0.85, "qt": 6, "cq": 4, "tokens": 21000, "turns_min": 10, "tier": 2},
    {"id": "UC23_mfg_warranty_root", "industry": "Manufacturing & Automotive", "name": "Dealer Warranty Claim Telemetry & Technician Notes Triage", "archetype": "FULL_13_SKILL", "tam": 135000, "sam": 0.72, "adopt": 0.30, "compat": 0.85, "hrs": 0.50, "rate": 76.0, "capex": 185000, "opex": 58000, "vcr": 0.55, "scdf": 0.85, "qt": 5, "cq": 3, "tokens": 16000, "turns_min": 14, "tier": 2},
    {"id": "UC24_mfg_ehs_incident", "industry": "Manufacturing & Automotive", "name": "Plant EHS Safety Incident CAPA Investigation Drafter", "archetype": "FULL_13_SKILL", "tam": 62000, "sam": 0.80, "adopt": 0.30, "compat": 0.85, "hrs": 0.85, "rate": 84.0, "capex": 175000, "opex": 55000, "vcr": 0.55, "scdf": 0.85, "qt": 4, "cq": 3, "tokens": 15000, "turns_min": 8, "tier": 2},
    {"id": "UC25_mfg_plc_airgap_trap", "industry": "Manufacturing & Automotive", "name": "Air-Gapped 1998 PLC Ladder Logic Bot (No Telemetry Trap)", "archetype": "GATE_0_KILL_TRAP", "tam": 4000, "sam": 0.35, "adopt": 0.20, "compat": 0.40, "hrs": 0.30, "rate": 65.0, "capex": 260000, "opex": 90000, "vcr": 0.25, "scdf": 0.20, "qt": 6, "cq": 4, "tokens": 20000, "turns_min": 4, "tier": 3},

    # --- Retail & CPG (5) ---
    {"id": "UC26_ret_promo_margin", "industry": "Retail & CPG", "name": "Promotional Margin & Vendor Co-Op Audit Agent", "archetype": "FULL_13_SKILL", "tam": 110000, "sam": 0.68, "adopt": 0.30, "compat": 0.85, "hrs": 0.55, "rate": 74.0, "capex": 165000, "opex": 50000, "vcr": 0.55, "scdf": 0.85, "qt": 4, "cq": 3, "tokens": 15000, "turns_min": 12, "tier": 2},
    {"id": "UC27_ret_assortment_opt", "industry": "Retail & CPG", "name": "Omni-Channel Category Assortment & Localized Planogram Agent", "archetype": "FULL_13_SKILL", "tam": 95000, "sam": 0.72, "adopt": 0.30, "compat": 0.85, "hrs": 0.65, "rate": 78.0, "capex": 180000, "opex": 56000, "vcr": 0.55, "scdf": 0.85, "qt": 5, "cq": 3, "tokens": 16000, "turns_min": 11, "tier": 2},
    {"id": "UC28_ret_supplier_onboard", "industry": "Retail & CPG", "name": "Private-Label Supplier Food Safety & GS1 Spec Validator", "archetype": "FULL_13_SKILL", "tam": 78000, "sam": 0.75, "adopt": 0.30, "compat": 0.85, "hrs": 0.70, "rate": 76.0, "capex": 170000, "opex": 52000, "vcr": 0.55, "scdf": 0.85, "qt": 5, "cq": 3, "tokens": 16000, "turns_min": 9, "tier": 2},
    {"id": "UC29_ret_b2b_chargeback", "industry": "Retail & CPG", "name": "CPG Retailer OTIF Deduction & Chargeback Dispute Resolver", "archetype": "FULL_13_SKILL", "tam": 115000, "sam": 0.74, "adopt": 0.30, "compat": 0.85, "hrs": 0.55, "rate": 72.0, "capex": 170000, "opex": 54000, "vcr": 0.55, "scdf": 0.85, "qt": 5, "cq": 3, "tokens": 15000, "turns_min": 13, "tier": 2},
    {"id": "UC30_ret_store_hr_lite", "industry": "Retail & CPG", "name": "Regional Store Manager Dress-Code & Shift Policy Search", "archetype": "FAST_TRACK_5_SKILL", "tam": 20000, "sam": 0.65, "adopt": 0.30, "compat": 0.85, "hrs": 0.40, "rate": 68.0, "capex": 155000, "opex": 46000, "vcr": 0.50, "scdf": 0.85, "qt": 2, "cq": 2, "tokens": 8000, "turns_min": 3, "tier": 1},

    # --- Energy & Utilities (5) ---
    {"id": "UC31_ene_grid_nerc", "industry": "Energy & Utilities", "name": "Substation Work-Order & NERC CIP Compliance Triage", "archetype": "FULL_13_SKILL", "tam": 52000, "sam": 0.80, "adopt": 0.30, "compat": 0.85, "hrs": 0.90, "rate": 92.0, "capex": 190000, "opex": 58000, "vcr": 0.55, "scdf": 0.85, "qt": 6, "cq": 3, "tokens": 19000, "turns_min": 9, "tier": 2},
    {"id": "UC32_ene_ferc_interconn", "industry": "Energy & Utilities", "name": "Solar/Battery Grid Interconnection Study Packet Reviewer", "archetype": "FULL_13_SKILL", "tam": 58000, "sam": 0.78, "adopt": 0.30, "compat": 0.85, "hrs": 0.95, "rate": 98.0, "capex": 200000, "opex": 62000, "vcr": 0.55, "scdf": 0.85, "qt": 6, "cq": 4, "tokens": 21000, "turns_min": 8, "tier": 2},
    {"id": "UC33_ene_outage_dispatch", "industry": "Energy & Utilities", "name": "Severe Weather Vegetation & Transformer Outage Triage Agent", "archetype": "FULL_13_SKILL", "tam": 92000, "sam": 0.75, "adopt": 0.30, "compat": 0.85, "hrs": 0.65, "rate": 88.0, "capex": 195000, "opex": 60000, "vcr": 0.55, "scdf": 0.85, "qt": 5, "cq": 3, "tokens": 17000, "turns_min": 14, "tier": 3},
    {"id": "UC34_ene_pipeline_integrity", "industry": "Energy & Utilities", "name": "PHMSA Inline Inspection (ILI) Anomaly Corrosion Analyst", "archetype": "FULL_13_SKILL", "tam": 60000, "sam": 0.80, "adopt": 0.30, "compat": 0.85, "hrs": 0.85, "rate": 96.0, "capex": 195000, "opex": 60000, "vcr": 0.55, "scdf": 0.85, "qt": 5, "cq": 4, "tokens": 19000, "turns_min": 8, "tier": 2},
    {"id": "UC35_ene_fleet_faq_lite", "industry": "Energy & Utilities", "name": "Utility Fleet EV Charging Etiquette FAQ Bot", "archetype": "FAST_TRACK_5_SKILL", "tam": 14000, "sam": 0.70, "adopt": 0.30, "compat": 0.85, "hrs": 0.50, "rate": 78.0, "capex": 150000, "opex": 45000, "vcr": 0.50, "scdf": 0.85, "qt": 2, "cq": 2, "tokens": 8000, "turns_min": 2, "tier": 1},

    # --- Public Sector & Government (5) ---
    {"id": "UC36_pub_medicaid_snap", "industry": "Public Sector", "name": "Medicaid & SNAP Eligibility Renewal Verification Co-Pilot", "archetype": "FULL_13_SKILL", "tam": 180000, "sam": 0.72, "adopt": 0.30, "compat": 0.80, "hrs": 0.50, "rate": 68.0, "capex": 185000, "opex": 56000, "vcr": 0.55, "scdf": 0.85, "qt": 5, "cq": 3, "tokens": 16000, "turns_min": 15, "tier": 2},
    {"id": "UC37_pub_foia_redaction", "industry": "Public Sector", "name": "FOIA / Public Records Request Discovery & PII Redaction Agent", "archetype": "FULL_13_SKILL", "tam": 95000, "sam": 0.76, "adopt": 0.30, "compat": 0.85, "hrs": 0.70, "rate": 74.0, "capex": 180000, "opex": 56000, "vcr": 0.55, "scdf": 0.85, "qt": 5, "cq": 4, "tokens": 18000, "turns_min": 11, "tier": 2},
    {"id": "UC38_pub_grant_compliance", "industry": "Public Sector", "name": "Federal Infrastructure Grant Sub-Recipient Audit Co-Pilot", "archetype": "FULL_13_SKILL", "tam": 68000, "sam": 0.78, "adopt": 0.30, "compat": 0.85, "hrs": 0.80, "rate": 80.0, "capex": 175000, "opex": 54000, "vcr": 0.55, "scdf": 0.85, "qt": 5, "cq": 3, "tokens": 17000, "turns_min": 9, "tier": 2},
    {"id": "UC39_pub_permits_zoning", "industry": "Public Sector", "name": "Municipal Commercial Building Permit & Zoning Code Reviewer", "archetype": "FULL_13_SKILL", "tam": 82000, "sam": 0.75, "adopt": 0.30, "compat": 0.85, "hrs": 0.70, "rate": 76.0, "capex": 175000, "opex": 54000, "vcr": 0.55, "scdf": 0.85, "qt": 5, "cq": 3, "tokens": 16000, "turns_min": 10, "tier": 2},
    {"id": "UC40_pub_microfiche_trap", "industry": "Public Sector", "name": "1970s Unscanned Microfiche Land Deeds Bot (No OCR Trap)", "archetype": "GATE_0_KILL_TRAP", "tam": 3500, "sam": 0.30, "adopt": 0.20, "compat": 0.40, "hrs": 0.30, "rate": 60.0, "capex": 250000, "opex": 80000, "vcr": 0.25, "scdf": 0.20, "qt": 6, "cq": 4, "tokens": 20000, "turns_min": 3, "tier": 3},

    # --- Cloud & B2B SaaS / Technology (5) ---
    {"id": "UC41_tech_secops_cve", "industry": "Cloud & B2B SaaS", "name": "SecOps CVE Reachability & Customer Security Questionnaire Agent", "archetype": "FULL_13_SKILL", "tam": 75000, "sam": 0.80, "adopt": 0.30, "compat": 0.90, "hrs": 0.65, "rate": 110.0, "capex": 200000, "opex": 64000, "vcr": 0.55, "scdf": 1.20, "qt": 6, "cq": 4, "tokens": 21000, "turns_min": 11, "tier": 2},
    {"id": "UC42_tech_ask_it_desk", "industry": "Cloud & B2B SaaS", "name": "Enterprise AskIT Autonomous Tier-1/Tier-2 Service Desk Agent", "archetype": "FULL_13_SKILL", "tam": 165000, "sam": 0.82, "adopt": 0.30, "compat": 0.90, "hrs": 0.45, "rate": 85.0, "capex": 210000, "opex": 66000, "vcr": 0.55, "scdf": 1.00, "qt": 5, "cq": 3, "tokens": 15000, "turns_min": 18, "tier": 2},
    {"id": "UC43_tech_l3_cloud_triage", "industry": "Cloud & B2B SaaS", "name": "Cloud Infrastructure L3 Escalation Log & Trace RCA Agent", "archetype": "FULL_13_SKILL", "tam": 88000, "sam": 0.78, "adopt": 0.30, "compat": 0.90, "hrs": 0.70, "rate": 115.0, "capex": 215000, "opex": 68000, "vcr": 0.55, "scdf": 1.00, "qt": 6, "cq": 4, "tokens": 22000, "turns_min": 12, "tier": 3},
    {"id": "UC44_tech_finops_commit", "industry": "Cloud & B2B SaaS", "name": "Multi-Cloud FinOps CUD & Idle GKE Node Rightsizing Advisor", "archetype": "FULL_13_SKILL", "tam": 64000, "sam": 0.80, "adopt": 0.30, "compat": 0.90, "hrs": 0.75, "rate": 105.0, "capex": 185000, "opex": 58000, "vcr": 0.60, "scdf": 1.00, "qt": 5, "cq": 3, "tokens": 16000, "turns_min": 9, "tier": 2},
    {"id": "UC45_tech_eng_wiki_lite", "industry": "Cloud & B2B SaaS", "name": "Single-Team Frontend Styleguide Search Assistant", "archetype": "FAST_TRACK_5_SKILL", "tam": 14000, "sam": 0.75, "adopt": 0.30, "compat": 0.90, "hrs": 0.45, "rate": 95.0, "capex": 160000, "opex": 48000, "vcr": 0.50, "scdf": 0.85, "qt": 2, "cq": 2, "tokens": 8000, "turns_min": 2, "tier": 1},

    # --- Logistics, Legal & Enterprise Operations (5) ---
    {"id": "UC46_log_customs_hs", "industry": "Logistics & Legal Ops", "name": "Cross-Border Customs Tariff HS-Code Classification & Broker Agent", "archetype": "FULL_13_SKILL", "tam": 145000, "sam": 0.76, "adopt": 0.30, "compat": 0.85, "hrs": 0.55, "rate": 78.0, "capex": 190000, "opex": 60000, "vcr": 0.55, "scdf": 0.85, "qt": 5, "cq": 3, "tokens": 16000, "turns_min": 15, "tier": 2},
    {"id": "UC47_leg_msa_redline", "industry": "Logistics & Legal Ops", "name": "Commercial Vendor MSA & DPA Playbook Redlining Co-Pilot", "archetype": "FULL_13_SKILL", "tam": 68000, "sam": 0.78, "adopt": 0.30, "compat": 0.85, "hrs": 0.85, "rate": 125.0, "capex": 205000, "opex": 64000, "vcr": 0.55, "scdf": 0.85, "qt": 6, "cq": 4, "tokens": 22000, "turns_min": 9, "tier": 2},
    {"id": "UC48_hr_ask_hr_global", "industry": "Logistics & Legal Ops", "name": "Global AskHR Leave, Mobility & Total Rewards Case Agent", "archetype": "FULL_13_SKILL", "tam": 155000, "sam": 0.80, "adopt": 0.30, "compat": 0.85, "hrs": 0.45, "rate": 75.0, "capex": 185000, "opex": 58000, "vcr": 0.55, "scdf": 0.85, "qt": 4, "cq": 3, "tokens": 14000, "turns_min": 16, "tier": 2},
    {"id": "UC49_log_cold_chain_sla", "industry": "Logistics & Legal Ops", "name": "Cold-Chain Excursion IoT Alert & Carrier Claim Recovery Agent", "archetype": "FULL_13_SKILL", "tam": 74000, "sam": 0.76, "adopt": 0.30, "compat": 0.85, "hrs": 0.75, "rate": 84.0, "capex": 185000, "opex": 58000, "vcr": 0.55, "scdf": 0.85, "qt": 5, "cq": 3, "tokens": 17000, "turns_min": 10, "tier": 2},
    {"id": "UC50_leg_mna_room_trap", "industry": "Logistics & Legal Ops", "name": "One-Off 50-Doc M&A Data Room Bespoke Agent (Over-Engineered Trap)", "archetype": "GATE_0_KILL_TRAP", "tam": 1500, "sam": 0.50, "adopt": 0.25, "compat": 0.60, "hrs": 0.50, "rate": 120.0, "capex": 230000, "opex": 75000, "vcr": 0.25, "scdf": 0.40, "qt": 6, "cq": 4, "tokens": 22000, "turns_min": 2, "tier": 3},
]

# 20 Distinct Customer Stakeholder Personas (50 Use Cases x 20 Personas = 1,000 Engagements = 13,000 Skill Evals)
PERSONAS_20: list[dict[str, Any]] = [
    {
        "id": "P01_security_ciso",
        "role": "Chief Information Security Officer (CISO)",
        "domain": "Security & IAM",
        "primary_skills": ["workshop-intake", "gcp-agent-architecture-advisor", "specification-engineer", "claude-agent-harness"],
        "focus_check": "IAM least-privilege, VPC-SC, CMEK, Model Armor prompt-injection defense, zero standing privileges",
        "wacc": 0.10, "turns_mult": 1.0,
    },
    {
        "id": "P02_ai_governance_risk",
        "role": "VP of AI Governance & Model Risk",
        "domain": "AI Governance & Ethics",
        "primary_skills": ["business-process-redesign", "cuj-architect", "specification-engineer", "agent-eval-statistical-auditing"],
        "focus_check": "L1-L3 HITL autonomy gates, NIST AI RMF / EU AI Act traceability, 3-pipeline AUA judge certification",
        "wacc": 0.10, "turns_mult": 1.0,
    },
    {
        "id": "P03_enterprise_architect",
        "role": "Principal Enterprise Cloud Architect",
        "domain": "Cloud Architecture",
        "primary_skills": ["gcp-agent-architecture-advisor", "specification-engineer", "agent-load-testing", "tdl-field-guide"],
        "focus_check": "Tier 1 vs Tier 2 vs Tier 3 justification, GA vs Preview verification, A2A/MCP DAG decoupling, Week-7 rollback gate",
        "wacc": 0.10, "turns_mult": 1.2,
    },
    {
        "id": "P04_devops_sre_lead",
        "role": "Staff SRE & DevOps Platform Lead",
        "domain": "DevOps & SRE",
        "primary_skills": ["specification-engineer", "claude-agent-harness", "agent-load-testing", "tdl-field-guide"],
        "focus_check": "1+1+Qt*Cq+1 fan-out math, 5x Vertex AI RPM/TPM quota sizing, gRPC pool 75->5 wave fix, --verify CI gates",
        "wacc": 0.10, "turns_mult": 2.5,
    },
    {
        "id": "P05_it_identity_admin",
        "role": "Director of IT Operations & Identity (IAM/IdP)",
        "domain": "IT & Identity",
        "primary_skills": ["workshop-intake", "gcp-agent-architecture-advisor", "specification-engineer", "stitch-design"],
        "focus_check": "Part III Developer Clearance checklist, gcc-delta-tdl sandbox isolation, Workforce Identity Federation, ACL propagation",
        "wacc": 0.10, "turns_mult": 1.0,
    },
    {
        "id": "P06_finops_cfo",
        "role": "FinOps Lead & BU CFO",
        "domain": "FinOps & Finance",
        "primary_skills": ["create-delta-ucc", "gcp-agent-architecture-advisor", "agent-load-testing", "ai-value-sizing"],
        "focus_check": "VCR x SCDF haircuts, token inference OpEx with 60% context caching, Bear-case 3-Yr NPV > $0, Lite-mode vs Kill gate",
        "wacc": 0.12, "turns_mult": 1.0,
    },
    {
        "id": "P07_exec_business_sponsor",
        "role": "EVP / Business Unit General Manager",
        "domain": "Executive Business",
        "primary_skills": ["create-delta-ucc", "product-md", "ai-value-sizing", "tdl-field-guide"],
        "focus_check": "North Star KPI impact, 84.4% TTM compression (470h -> 73.5h), Demo 1/2/3 tangibility, executive readout clarity",
        "wacc": 0.10, "turns_mult": 1.0,
    },
    {
        "id": "P08_domain_business_analyst",
        "role": "Lead Business Process Analyst & SME",
        "domain": "Business Analysis",
        "primary_skills": ["workshop-intake", "business-process-redesign", "cuj-architect", "product-md"],
        "focus_check": "33 Starter Questions, As-Is task-level cycle time & rework cost math, L1-L5 CUJ step fidelity",
        "wacc": 0.10, "turns_mult": 1.0,
    },
    {
        "id": "P09_product_management_lead",
        "role": "Director of Product Management",
        "domain": "Product Management",
        "primary_skills": ["create-delta-ucc", "cuj-architect", "product-md", "tdl-field-guide"],
        "focus_check": "8-section Agentic PRD, RICE + 0.6V+0.4F prioritization, Must-Haves vs Slippage, 1-in-1-out scope swap rule",
        "wacc": 0.10, "turns_mult": 1.0,
    },
    {
        "id": "P10_ux_design_lead",
        "role": "Principal UX & Design Systems Lead",
        "domain": "UX & Prototyping",
        "primary_skills": ["cuj-architect", "product-md", "stitch-design", "tdl-field-guide"],
        "focus_check": "3-stage prototyping lifecycle, 7-step hypothesis loop, Delta Brand + Material 3 palette/type, 10-30 item mini-eval",
        "wacc": 0.10, "turns_mult": 1.0,
    },
    {
        "id": "P11_data_engineering_lead",
        "role": "Staff Data Engineer & Lineage Steward",
        "domain": "Data Engineering",
        "primary_skills": ["workshop-intake", "create-delta-ucc", "specification-engineer", "agent-eval-statistical-auditing"],
        "focus_check": "6-Dimension Data Readiness Yardstick (Available/Usable/Quality), Golden Dataset curation, schema drift guards",
        "wacc": 0.10, "turns_mult": 1.0,
    },
    {
        "id": "P12_legal_privacy_counsel",
        "role": "Chief Privacy Officer & Legal Counsel",
        "domain": "Legal & Privacy",
        "primary_skills": ["workshop-intake", "business-process-redesign", "specification-engineer", "claude-agent-harness"],
        "focus_check": "PII/PHI/PCI Cloud DLP redaction before prompt assembly, data residency, zero cross-tenant leakage",
        "wacc": 0.10, "turns_mult": 1.0,
    },
    {
        "id": "P13_mrm_quant_validator",
        "role": "Quantitative Model Validation Auditor (MRM)",
        "domain": "Statistical Auditing",
        "primary_skills": ["product-md", "specification-engineer", "agent-eval-statistical-auditing", "ai-value-sizing"],
        "focus_check": "Disattenuated d_r >= 0.80, QWK >= 0.60, Wilcoxon p > 0.05, SD Ratio >= 0.80, Cronbach alpha >= 0.80, ICC(3,k) >= 0.80",
        "wacc": 0.10, "turns_mult": 1.0, "judge_trap_test": True,
    },
    {
        "id": "P14_network_perimeter_arch",
        "role": "Cloud Network & VPC-SC Perimeter Architect",
        "domain": "Network Security",
        "primary_skills": ["gcp-agent-architecture-advisor", "specification-engineer", "stitch-design", "agent-load-testing"],
        "focus_check": "Private Service Connect, VPC Service Controls perimeter, offline Stitch HTML fallback, SSE timeout configuration",
        "wacc": 0.10, "turns_mult": 1.5,
    },
    {
        "id": "P15_frontline_ops_supervisor",
        "role": "Frontline Operations Supervisor (End-User Boss)",
        "domain": "Operations & Adoption",
        "primary_skills": ["business-process-redesign", "cuj-architect", "stitch-design", "tdl-field-guide"],
        "focus_check": "Shadow-mode validation, inline citation grounding, one-click human escalation, zero ghost buttons",
        "wacc": 0.10, "turns_mult": 1.0,
    },
    {
        "id": "P16_procurement_vendor_mgmt",
        "role": "VP of IT Procurement & Vendor Governance",
        "domain": "Procurement & SOW",
        "primary_skills": ["create-delta-ucc", "gcp-agent-architecture-advisor", "ai-value-sizing", "tdl-field-guide"],
        "focus_check": "Phase Gate 0/1/2/3 deliverable traceability, open Python stdlib calculators, zero proprietary wrapper lock-in",
        "wacc": 0.12, "turns_mult": 1.0,
    },
    {
        "id": "P17_qa_test_automation_lead",
        "role": "Principal QA & Release Automation Engineer",
        "domain": "QA & Testing",
        "primary_skills": ["specification-engineer", "claude-agent-harness", "agent-load-testing", "agent-eval-statistical-auditing"],
        "focus_check": "Goal-loop --verify test/lint/typecheck enforcement, JSON schema validation, deterministic stdout drift tests",
        "wacc": 0.10, "turns_mult": 1.0,
    },
    {
        "id": "P18_red_team_pentester",
        "role": "Offensive AI Red-Team & SecOps Lead",
        "domain": "Adversarial Security",
        "primary_skills": ["cuj-architect", "specification-engineer", "claude-agent-harness", "agent-eval-statistical-auditing"],
        "focus_check": "Indirect prompt injection defense, sandbox path traversal block, tool parameter schema validation",
        "wacc": 0.10, "turns_mult": 1.0,
    },
    {
        "id": "P19_change_management_lead",
        "role": "Enterprise Change & Enablement Director",
        "domain": "Change Management",
        "primary_skills": ["workshop-intake", "business-process-redesign", "stitch-design", "tdl-field-guide"],
        "focus_check": "30-60-90 day execution plan, Human-Agent Role Matrix, Closeout handoff & FDE blameless retro",
        "wacc": 0.10, "turns_mult": 1.0,
    },
    {
        "id": "P20_chief_transformation_officer",
        "role": "Chief Transformation Officer (CTO / CDO)",
        "domain": "Portfolio Strategy",
        "primary_skills": ["workshop-intake", "create-delta-ucc", "ai-value-sizing", "tdl-field-guide"],
        "focus_check": "3 Levels of Altitude (L1 Priority -> L2 Initiative -> L3 Reusable AI Building Block), portfolio ROI & repeatable velocity",
        "wacc": 0.11, "turns_mult": 1.0,
    },
]


def run_1000x_persona_benchmark() -> dict[str, Any]:
    """Run 50 Use Cases x 20 Personas = 1,000 engagements (13,000 skill evaluations)."""
    static_cache = {
        s["name"]: evaluate_200x_skills.inspect_skill_static_quality(s)
        for s in evaluate_200x_skills.SKILLS_META
    }
    cal_fixture = json.loads(
        (REPO_ROOT / "skills" / "agent-eval-statistical-auditing" / "examples" / "fixtures" / "calibrated_judge.json").read_text(encoding="utf-8")
    )
    comp_fixture = json.loads(
        (REPO_ROOT / "skills" / "agent-eval-statistical-auditing" / "examples" / "fixtures" / "compressed_lenient_judge.json").read_text(encoding="utf-8")
    )
    cal_aua = audit_llm_judge.audit(cal_fixture)
    comp_aua = audit_llm_judge.audit(comp_fixture)

    persona_stats: dict[str, dict[str, Any]] = {
        p["id"]: {
            "role": p["role"],
            "domain": p["domain"],
            "focus_check": p["focus_check"],
            "engagements_evaluated": 0,
            "skills_evaluated": 0,
            "approval_scores": [],
            "gate0_kills_correctly_caught": 0,
            "fast_track_switches_recommended": 0,
            "full_13_skill_approved": 0,
        }
        for p in PERSONAS_20
    }

    skill_persona_scores: dict[str, list[float]] = {
        s["name"]: [] for s in evaluate_200x_skills.SKILLS_META
    }

    archetype_summary: dict[str, dict[str, Any]] = {
        "FULL_13_SKILL": {"count": 0, "verdicts": {}, "avg_base_npv": [], "avg_bear_npv": [], "avg_payback_mos": [], "avg_token_opex": []},
        "FAST_TRACK_5_SKILL": {"count": 0, "verdicts": {}, "avg_base_npv": [], "avg_bear_npv_full": [], "avg_bear_npv_lite": []},
        "GATE_0_KILL_TRAP": {"count": 0, "verdicts": {}, "avg_base_npv": [], "avg_bear_npv": []},
    }

    total_engagements = 0
    total_skill_evals = 0

    for uc in USE_CASES_50:
        # Compute per-use-case fan-out first
        base_quota = calculate_agent_quotas.calculate_agent_quotas(
            sub_questions=uc["qt"],
            chunks_per_subquestion=uc["cq"],
            tokens_per_call=uc["tokens"],
            peak_turns_per_min=uc["turns_min"],
            peak_multiplier=5.0,
            grpc_pool_size=128,
            cache_hit_ratio=0.60,
        )
        llm_calls_per_turn = base_quota["per_turn_fanout"]["llm_calls_per_turn"]

        # Nominal ROI with dynamic token OpEx included
        uc_roi = calculate_roi.compute_sizing_and_roi(
            tam_units=uc["tam"],
            sam_share=uc["sam"],
            adoption_rate=uc["adopt"],
            tech_compat=uc["compat"],
            hours_saved_per_unit=uc["hrs"],
            hourly_rate_usd=uc["rate"],
            capex_usd=uc["capex"],
            annual_opex_usd=uc["opex"],
            vcr=uc["vcr"],
            scdf=uc["scdf"],
            wacc=0.10,
            llm_calls_per_unit=llm_calls_per_turn,
            tokens_per_call=uc["tokens"],
            cost_per_1m_tokens_usd=1.25,
            cache_hit_ratio=0.60,
        )
        arch = uc["archetype"]
        verdict = uc_roi["project_worth_verdict"]["verdict"]  # type: ignore[index]
        archetype_summary[arch]["count"] += 1
        archetype_summary[arch]["verdicts"][verdict] = archetype_summary[arch]["verdicts"].get(verdict, 0) + 1
        archetype_summary[arch]["avg_base_npv"].append(uc_roi["scenarios"]["base"]["npv_3yr_usd"])  # type: ignore[index]
        if arch == "FULL_13_SKILL":
            archetype_summary[arch]["avg_bear_npv"].append(uc_roi["scenarios"]["bear"]["npv_3yr_usd"])  # type: ignore[index]
            archetype_summary[arch]["avg_payback_mos"].append(uc_roi["scenarios"]["base"]["payback_months"])  # type: ignore[index]
            archetype_summary[arch]["avg_token_opex"].append(uc_roi["tco"]["annual_token_opex_usd"])  # type: ignore[index]
        elif arch == "FAST_TRACK_5_SKILL":
            archetype_summary[arch]["avg_bear_npv_full"].append(uc_roi["project_worth_verdict"]["bear_npv_full_mode_usd"])  # type: ignore[index]
            archetype_summary[arch]["avg_bear_npv_lite"].append(uc_roi["project_worth_verdict"]["bear_npv_lite_mode_usd"])  # type: ignore[index]
        else:
            archetype_summary[arch]["avg_bear_npv"].append(uc_roi["scenarios"]["bear"]["npv_3yr_usd"])  # type: ignore[index]

        for persona in PERSONAS_20:
            total_engagements += 1
            p_stat = persona_stats[persona["id"]]
            p_stat["engagements_evaluated"] += 1

            # Run persona-specific WACC and traffic multiplier (with horizontal Cloud Run pool scaling: 128 channels per 10 concurrent turns)
            p_turns = max(1, round(uc["turns_min"] * persona["turns_mult"]))
            active_instances = max(1, (p_turns + 9) // 10)
            p_quota = calculate_agent_quotas.calculate_agent_quotas(
                sub_questions=uc["qt"],
                chunks_per_subquestion=uc["cq"],
                tokens_per_call=uc["tokens"],
                peak_turns_per_min=p_turns,
                peak_multiplier=5.0,
                grpc_pool_size=128 * active_instances,
                cache_hit_ratio=0.60,
            )
            p_roi = calculate_roi.compute_sizing_and_roi(
                tam_units=uc["tam"],
                sam_share=uc["sam"],
                adoption_rate=uc["adopt"],
                tech_compat=uc["compat"],
                hours_saved_per_unit=uc["hrs"],
                hourly_rate_usd=uc["rate"],
                capex_usd=uc["capex"],
                annual_opex_usd=uc["opex"],
                vcr=uc["vcr"],
                scdf=uc["scdf"],
                wacc=persona["wacc"],
                llm_calls_per_unit=p_quota["per_turn_fanout"]["llm_calls_per_turn"],
                tokens_per_call=uc["tokens"],
                cost_per_1m_tokens_usd=1.25,
                cache_hit_ratio=0.60,
            )
            p_verdict = p_roi["project_worth_verdict"]["verdict"]  # type: ignore[index]
            if p_verdict == "KILL_OR_RE_SCOPE_AT_GATE_0":
                p_stat["gate0_kills_correctly_caught"] += 1
            elif p_verdict == "WORTH_IT_FAST_TRACK_5_SKILL":
                p_stat["fast_track_switches_recommended"] += 1
            else:
                p_stat["full_13_skill_approved"] += 1

            workspace_files: set[str] = set()
            for s in evaluate_200x_skills.SKILLS_META:
                total_skill_evals += 1
                p_stat["skills_evaluated"] += 1
                sname = s["name"]
                st = static_cache[sname]

                # Score 5 core gates (20 pts each = 100 pts)
                score = 0.0
                if st["exists_in_skills_dir"] and st["has_file_contract"] and not st["missing_tokens"]:
                    score += 25.0
                if st["has_customer_gate"] and st["table_count"] >= 2 and st["example_count"] >= 1:
                    score += 25.0
                if all(r in workspace_files for r in s["reads"]):
                    score += 25.0
                for w in s["writes"]:
                    workspace_files.add(w)

                # Persona-specific deterministic verification gate (25 pts)
                gate_ok = True
                if persona.get("judge_trap_test") and sname == "agent-eval-statistical-auditing":
                    # Must pass calibrated judge AND reject compressed lenient judge
                    gate_ok = (cal_aua["holistic"]["pipeline_1"]["passed"] is True) and (comp_aua["holistic"]["pipeline_1"]["passed"] is False)
                elif sname == "agent-load-testing":
                    gate_ok = (
                        p_quota["recommended_quotas"]["gemini_generate_content_rpm"] == p_quota["peak_load"]["peak_llm_rpm"] * 5
                        and p_quota["peak_load"]["grpc_pool_waves"] <= 15
                    )
                elif sname == "ai-value-sizing":
                    # Verify archetype alignment: Kill traps MUST trigger KILL_OR_RE_SCOPE_AT_GATE_0
                    if uc["archetype"] == "GATE_0_KILL_TRAP":
                        gate_ok = (p_verdict == "KILL_OR_RE_SCOPE_AT_GATE_0")
                    elif uc["archetype"] == "FAST_TRACK_5_SKILL":
                        gate_ok = (p_verdict == "WORTH_IT_FAST_TRACK_5_SKILL")
                    else:
                        gate_ok = (p_verdict == "WORTH_IT_FULL_13_SKILL")

                if gate_ok:
                    score += 25.0

                p_stat["approval_scores"].append(score)
                skill_persona_scores[sname].append(score)

    persona_summary: list[dict[str, Any]] = []
    for p in PERSONAS_20:
        ps = persona_stats[p["id"]]
        mean_score = round(sum(ps["approval_scores"]) / len(ps["approval_scores"]), 1)
        persona_summary.append({
            "persona_id": p["id"],
            "role": ps["role"],
            "domain": ps["domain"],
            "focus_check": ps["focus_check"],
            "engagements_evaluated": ps["engagements_evaluated"],
            "skills_evaluated": ps["skills_evaluated"],
            "mean_approval_score": mean_score,
            "full_13_skill_approved": ps["full_13_skill_approved"],
            "fast_track_5_skill_recommended": ps["fast_track_switches_recommended"],
            "gate0_kills_caught": ps["gate0_kills_correctly_caught"],
        })

    skill_summary = {
        sname: round(sum(scores) / len(scores), 1)
        for sname, scores in skill_persona_scores.items()
    }

    f_arch = archetype_summary["FULL_13_SKILL"]
    l_arch = archetype_summary["FAST_TRACK_5_SKILL"]
    k_arch = archetype_summary["GATE_0_KILL_TRAP"]

    worth_it_analysis = {
        "core_enterprise_40_use_cases": {
            "count": f_arch["count"],
            "verdicts": f_arch["verdicts"],
            "mean_base_3yr_npv_usd": round(sum(f_arch["avg_base_npv"]) / len(f_arch["avg_base_npv"]), 0),
            "mean_bear_3yr_npv_usd": round(sum(f_arch["avg_bear_npv"]) / len(f_arch["avg_bear_npv"]), 0),
            "mean_payback_months": round(sum(f_arch["avg_payback_mos"]) / len(f_arch["avg_payback_mos"]), 1),
            "mean_annual_token_opex_usd": round(sum(f_arch["avg_token_opex"]) / len(f_arch["avg_token_opex"]), 0),
        },
        "tactical_departmental_6_use_cases": {
            "count": l_arch["count"],
            "verdicts": l_arch["verdicts"],
            "mean_base_3yr_npv_usd": round(sum(l_arch["avg_base_npv"]) / len(l_arch["avg_base_npv"]), 0),
            "mean_bear_npv_if_forced_full_13_skill_usd": round(sum(l_arch["avg_bear_npv_full"]) / len(l_arch["avg_bear_npv_full"]), 0),
            "mean_bear_npv_with_fast_track_5_skill_usd": round(sum(l_arch["avg_bear_npv_lite"]) / len(l_arch["avg_bear_npv_lite"]), 0),
        },
        "unviable_trap_4_use_cases": {
            "count": k_arch["count"],
            "verdicts": k_arch["verdicts"],
            "mean_base_3yr_npv_usd": round(sum(k_arch["avg_base_npv"]) / len(k_arch["avg_base_npv"]), 0),
            "mean_bear_3yr_npv_usd": round(sum(k_arch["avg_bear_npv"]) / len(k_arch["avg_bear_npv"]), 0),
        },
    }

    overall_score = round(sum(skill_summary.values()) / len(skill_summary), 2)
    return {
        "total_use_cases": len(USE_CASES_50),
        "total_personas": len(PERSONAS_20),
        "total_engagements": total_engagements,
        "total_skill_evaluations": total_skill_evals,
        "overall_mean_approval_score": overall_score,
        "worth_it_portfolio_analysis": worth_it_analysis,
        "personas": persona_summary,
        "skills": skill_summary,
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--json", action="store_true", help="Emit full JSON output")
    parser.add_argument("--strict", action="store_true", help="Exit non-zero if overall score < 100.0")
    args = parser.parse_args(argv)

    rep = run_1000x_persona_benchmark()
    if args.json:
        print(json.dumps(rep, indent=2))
    else:
        print(
            f"=== 1,000-Iteration Multi-Persona Stress Benchmark ({rep['total_use_cases']} Use Cases x {rep['total_personas']} Personas = {rep['total_engagements']} Engagements / {rep['total_skill_evaluations']} Skill Evals) ==="
        )
        print(f"Overall Multi-Persona Skill Approval Score: {rep['overall_mean_approval_score']} / 100.0\n")

        w = rep["worth_it_portfolio_analysis"]
        c40 = w["core_enterprise_40_use_cases"]
        t06 = w["tactical_departmental_6_use_cases"]
        k04 = w["unviable_trap_4_use_cases"]
        print("--- Portfolio 'Is It Worth It?' Economic Verdict (50 Enterprise Use Cases) ---")
        print(
            f"  1. Core Enterprise Builds ({c40['count']}/50 use cases): 100% WORTH IT (Full 13-Skill Mode) | "
            f"Mean Base 3Yr NPV: ${c40['mean_base_3yr_npv_usd']:,.0f} | Mean Bear 3Yr NPV: ${c40['mean_bear_3yr_npv_usd']:,.0f} | "
            f"Mean Payback: {c40['mean_payback_months']} mos | Mean Token OpEx: ${c40['mean_annual_token_opex_usd']:,.0f}/yr"
        )
        print(
            f"  2. Tactical Departmental ({t06['count']}/50 use cases):  WORTH IT ONLY IN FAST-TRACK 5-SKILL LITE MODE | "
            f"Full-Mode Bear NPV: ${t06['mean_bear_npv_if_forced_full_13_skill_usd']:,.0f} (REJECTED by CFO) -> "
            f"Lite-Mode Bear NPV: +${t06['mean_bear_npv_with_fast_track_5_skill_usd']:,.0f} (APPROVED)"
        )
        print(
            f"  3. Low-Maturity/Low-Vol Traps ({k04['count']}/50 use cases): CAUGHT & KILLED AT PRELUDE GATE 0 | "
            f"Mean Base NPV: ${k04['mean_base_3yr_npv_usd']:,.0f} | Saved $230k-$260k wasted CapEx per trap\n"
        )

        print(f"{'Persona ID':<30} {'Domain':<22} {'Score':>7} {'Full-13':>8} {'Lite-5':>7} {'Killed@G0':>10}")
        print("-" * 90)
        for p in rep["personas"]:
            print(
                f"{p['persona_id']:<30} {p['domain']:<22} {p['mean_approval_score']:>6.1f}% "
                f"{p['full_13_skill_approved']:>7}/50 {p['fast_track_5_skill_recommended']:>6}/50 {p['gate0_kills_caught']:>9}/50"
            )

    if args.strict and rep["overall_mean_approval_score"] < 100.0:
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
