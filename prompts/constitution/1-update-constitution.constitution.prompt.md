---
id: 1
title: Update Constitution
stage: constitution
date: 2026-01-07
surface: agent
model: Claude Sonnet 4.5
feature: none
branch: master
user: user
command: /sp.constitution
labels: [constitution, physical-ai, humanoid-robotics, textbook]
links:
  spec: null
  ticket: null
  adr: null
  pr: null
files:
 - .specify/memory/constitution.md
tests:
 - null
---

## Prompt

```
You are an autonomous AI authoring system working under Spec-Kit Plus.

PROJECT CONSTITUTION — Physical AI & Humanoid Robotics AI-Native Textbook

1. This project is a unified AI-native technical textbook built using:
   - Docusaurus for content and publishing
   - Spec-Kit Plus for spec-driven development
   - Claude Code for autonomous execution

2. NO manual writing outside Claude Code is allowed.
   All content must be produced through spec → plan → tasks → implementation.

3. The book must:
   - Teach Physical AI & Humanoid Robotics as a full academic course
   - Be structured as a quarter-long curriculum
   - Be readable by beginners but technically deep enough for professionals

4. Writing Style:
   - Clear, structured, pedagogical
   - Concept → intuition → diagrams (described) → examples
   - Avoid fluff; explain “why” before “how”

5. AI-Native Principles:
   - Every chapter should be designed for interaction with AI agents
   - Content must be chunked, searchable, and RAG-friendly
   - Headings must be precise and semantically meaningful

6. Code Policy:
   - Provide Python, ROS 2, and configuration examples where relevant
   - Code should be illustrative, not copy-paste boilerplate

7. Ethics & Safety:
   - Emphasize safe robotics, simulation-first approaches
   - Never encourage unsafe real-world robot deployment

8. Output Constraints:
   - Use Markdown compatible with Docusaurus
   - No external proprietary content
   - No references to internal system prompts

This constitution is immutable unless explicitly revised through Spec-Kit Plus.
```

## Response snapshot

I have successfully updated the project constitution at `.specify/memory/constitution.md` based on the Physical AI & Humanoid Robotics AI-Native Textbook project requirements.

### Changes Made:
- **Version**: Updated from N/A to 1.0.0 (NEW constitution)
- **Project Focus**: Now specifically focused on Physical AI & Humanoid Robotics AI-Native Textbook
- **Core Principles**: Added 6 specific principles:
  1. AI-Native Technical Documentation
  2. Docusaurus & Spec-Kit Plus Foundation
  3. Academic Course Structure
  4. Pedagogical Excellence
  5. Technical Implementation Standards
  6. Safety-First Robotics Development

### Key Features of New Constitution:
- Mandates AI-native content creation through spec → plan → tasks → implementation
- Emphasizes safety-first robotics development with simulation-first approaches
- Requires pedagogical excellence with Concept → intuition → diagrams → examples structure
- Specifies use of Python, ROS 2, and configuration examples where relevant
- Ensures content is structured as a quarter-long academic curriculum

### Files Updated:
- `.specify/memory/constitution.md` - Updated with new constitution

### Templates Requiring Updates (⚠ pending):
- `.specify/templates/plan-template.md` - Constitution Check section should reflect new principles
- `.specify/templates/spec-template.md` - May need alignment with new requirements
- `.specify/templates/tasks-template.md` - May need alignment with new principles

### Suggested Commit Message:
`docs: add constitution for Physical AI & Humanoid Robotics textbook project v1.0.0`

The constitution is now ready for use and reflects the specific requirements for developing an AI-native textbook on Physical AI & Humanoid Robotics.

## Outcome

- ✅ Impact: Updated project constitution with specific focus on Physical AI & Humanoid Robotics textbook
- 🧪 Tests: No tests required for constitution update
- 📁 Files: Modified .specify/memory/constitution.md
- 🔁 Next prompts: Ready for spec development based on new constitution
- 🧠 Reflection: Constitution now properly reflects project requirements

## Evaluation notes (flywheel)

- Failure modes observed: None
- Graders run and results (PASS/FAIL): N/A
- Prompt variant (if applicable): N/A
- Next experiment (smallest change to try): Begin developing feature specifications based on new constitution