# 07 Domain playbooks (read only the section that matches)

Contents: ML/CV, NLP/LLM/RAG/agents, Data/analytics, Backend/API, Frontend/web, Automation (n8n/Make/Zapier), DevOps/cloud, Algorithms, Research/writing.

## ML / Computer vision
- Baseline first (pretrained, zero or few-shot), then fine-tune only if the baseline falls short on the brief's metric.
- Data: inspect real samples, fix label noise, split by source or page (no leakage), write the annotation format and class definitions in the docs. Augment realistically (scan noise, skew, scale).
- Metric must match the task: for detection use IoU-based precision/recall and mAP, and for "no cutting off content" add a containment/coverage metric.
- Post-processing is part of the model: confidence tuning, NMS, box merging, margin padding, and a geometric/classical refinement step can beat a bigger model.
- Error analysis by category (size, layout, orientation, background). Show failures.
- Deployment: export (ONNX or similar) if size/latency matters, batch or tile large images, keep full resolution for outputs.
- Check licences of weights and libraries (AGPL, research-only) and state them.

## NLP / LLM / RAG / agents
- Build a small eval set first (20-50 real cases with expected outcomes), then iterate against it.
- Separate retrieval quality from generation quality. Log prompts, retrieved chunks, outputs.
- Guardrails: grounding instructions, refusal on missing evidence, output schema validation, retries with caps.
- Report cost and latency per request. Pin model versions. Never hard-code secrets.

## Data / analytics
- Profile data first (nulls, types, duplicates, outliers). Document every cleaning rule.
- Every chart answers one question, with units and source. Prefer a reproducible notebook or script plus a short written conclusion.

## Backend / API
- Contract first (OpenAPI or schema), validation at the edge, consistent errors, idempotency where relevant.
- Tests for core logic and one end-to-end path. Config via environment. Health endpoint. Seed data and a one-command start.

## Frontend / web
- Real states: loading, empty, error, success. Responsive, keyboard accessible, no console errors.
- One clear primary action per screen. Realistic sample data. Build and run instructions verified from scratch.

## Automation (n8n / Make / Zapier / agents)
- Export the workflow JSON, document triggers, credentials needed (names only), field mappings, failure paths and retries.
- Include a test payload and the expected result. Idempotent actions, rate-limit awareness, logging.

## DevOps / cloud
- Reproducible build (Dockerfile, pinned base), minimal image, non-root, health checks, env-based config, CI that runs the tests, a rollback note.

## Algorithms / DSA
- State complexity, prove edge cases with tests, include a brute-force checker for random testing.

## Research / writing
- Question, method, evidence, limits. Every claim cited to an opened source. Structure beats length.
