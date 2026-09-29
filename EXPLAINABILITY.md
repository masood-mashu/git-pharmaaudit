# Explainability, Auditability & Decision Logic: GitPharmaAudit

This document details the transparent decision architecture, algorithmic criteria, data provenance, and operational boundaries of **GitPharmaAudit**, ensuring complete compliance with OpenGAP standards and Checkpoint 02 requirements.

---

## 1. Input Data and Data Sources Used

**GitPharmaAudit** ingests structured, machine-verifiable data artifacts from well-defined sources to ensure total repeatability:
- **Manufacturing**: Manufacturing Execution System (MES) electronic batch manufacturing records (eBMR).
- **Public**: Public Key Infrastructure (PKI) X.509 digital signature certificates and OCSP responses.
- **Approved**: Approved pharmaceutical standard operating procedures (SOP) and master formula limits.
- **OpenGAP Specification Manifests**: Ingests `agent.yaml`, `RULES.md`, and local state from `memory/MEMORY.md`.

All data sources are parsed deterministically without dynamic external unverified calls, ensuring that evaluations reflect the exact state of the repository at the moment of inspection.

---

## 2. How It Decides and Reasoning Process

The decision pipeline operates through a multi-stage validation sequence designed to eliminate subjective ambiguity:

1. **Syntax & Schema Verification**: Ingested inputs are first validated against strict JSON and YAML schemas defined in `tools/`. Any malformed payloads are immediately rejected.
2. **Deterministic Metric Extraction**:
   - **verify_electronic_signature**: Uses `electronic-signature-verifier` to calculate validates fda 21 cfr part 11 compliance of digital signatures on batch records.
   - **check_audit_trail_immutability**: Uses `audit-trail-immutability-checker` to calculate verifies sequential chronological continuity and immutability of audit trail entries.
   - **verify_sop_version**: Uses `sop-version-controller` to calculate confirms that manufacturing batch execution used current effective sop revision.
3. **Policy Boundary Checks**: Extracted metrics are evaluated against the non-negotiable rules defined in `RULES.md`.
4. **Verdict Synthesis**:
   - **`APPROVED`**: Issued when all criteria strictly pass thresholds, zero compliance violations are detected, and data integrity is certified.
   - **`NEEDS_REVIEW`**: Issued when borderline metrics or ambiguous edge cases require human supervisor assessment.
   - **`BLOCKED`**: Issued immediately upon detecting any violation of zero-tolerance rules, severe risk factors, or non-compliant parameters.

When an electronic batch record is submitted for commercial release, the agent runs electronic_signature_verifier, audit_trail_immutability_checker, and sop_version_controller. If signatures are valid, audit trail intact, and active SOP used, it issues APPROVED. If minor deviation notes exist, it issues NEEDS_REVIEW. If signature forgery, missing timestamps, or audit trail deletions are found, it issues BLOCKED.

---

## 3. Constraints, Limitations, and Known Issues

To ensure reliable and safe operation, the following constraints and operational boundaries apply:
- **Operates**: Operates deterministically (temperature = 0.1) based on strict statutory cGMP regulations.
- **Does**: Does not bypass physical analytical chemistry QC testing certificates of analysis (CoA).
- **Maintains**: Maintains zero-tolerance for data tampering or backdated manufacturing timestamps.
- **Deterministic Execution Constraint**: All model prompts and evaluations must run with low temperature (`0.1`) to ensure predictable, reproducible scoring and eliminate hallucinated findings.
- **Human Authority**: The agent cannot self-execute irreversible external mutations; final approval is reserved strictly for human authorities as specified in `DUTIES.md`.
