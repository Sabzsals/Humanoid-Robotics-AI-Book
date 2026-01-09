---
id: 1
title: analyze-artifacts missing-files
stage: general
date: 2026-01-08
surface: agent
model: claude-sonnet-4-5-20250929
feature: none
branch: master
user: Hd
command: sp.analyze
labels: [analysis,spec,plan,tasks]
links:
  spec: null
  ticket: null
  adr: null
  pr: null
files:
  -
tests:
  -
---

## Prompt

please use https://docusaurus.io/docs through context7 mcp server, and if there is any error in my project resolve it.

## Response snapshot

Based on my investigation, I've determined that your project doesn't have a complete set of artifacts (spec.md, plan.md, tasks.md) in any single feature directory, which is required for the `/sp.analyze` command to work properly.

In your `./specs/` directory, I found:

1. `./specs/1-textbook-physical-ai/` - Contains `spec.md` and `tasks.md` but missing `plan.md`
2. `./specs/main/` - Contains only `plan.md` but missing `spec.md` and `tasks.md`

The `/sp.analyze` command requires all three files (spec.md, plan.md, tasks.md) to be present in a single feature directory to perform the cross-artifact consistency analysis.

Since the prerequisite check failed (no complete feature directory found), I cannot proceed with the analysis. You'll need to either:

1. Create the missing files in one of the existing feature directories, or
2. Create a new feature directory with all three required files

Would you like me to help you create the missing artifacts in one of these directories? For example, I could help create a `plan.md` for the `1-textbook-physical-ai` feature, or create the missing `spec.md` and `tasks.md` for the `main` feature.

## Outcome

- ✅ Impact: Identified missing prerequisite files for sp.analyze
- 🧪 Tests: None run
- 📁 Files: None modified
- 🔁 Next prompts: Create missing spec/plan/tasks files or clarify feature structure
- 🧠 Reflection: Need complete artifact set for analysis to proceed

## Evaluation notes (flywheel)

- Failure modes observed: Missing complete feature directory with all three required files
- Graders run and results (PASS/FAIL): N/A
- Prompt variant (if applicable): N/A
- Next experiment (smallest change to try): Create missing artifacts or clarify project structure