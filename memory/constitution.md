<!--
Sync Impact Report:
- Version change: N/A → 1.0.0
- Modified principles: N/A (new constitution)
- Added sections: All principles and sections based on Physical AI & Humanoid Robotics project
- Removed sections: N/A (new constitution)
- Templates requiring updates:
  - .specify/templates/plan-template.md ⚠ pending
  - .specify/templates/spec-template.md ⚠ pending
  - .specify/templates/tasks-template.md ⚠ pending
  - .specify/templates/commands/*.md ⚠ pending
- Follow-up TODOs: None
-->

# Physical AI & Humanoid Robotics AI-Native Textbook Constitution

## Core Principles

### I. AI-Native Technical Documentation
All content must be produced through spec → plan → tasks → implementation. No manual writing outside Claude Code is allowed. Every chapter should be designed for interaction with AI agents, with content chunked, searchable, and RAG-friendly. Headings must be precise and semantically meaningful.

### II. Docusaurus & Spec-Kit Plus Foundation
The project utilizes Docusaurus for content and publishing, and Spec-Kit Plus for spec-driven development. All development follows the spec-driven approach with structured artifacts for specifications, plans, and tasks.

### III. Academic Course Structure
The book must teach Physical AI & Humanoid Robotics as a full academic course, structured as a quarter-long curriculum. Content must be readable by beginners but technically deep enough for professionals.

### IV. Pedagogical Excellence
Writing style must be clear, structured, and pedagogical following the pattern: Concept → intuition → diagrams (described) → examples. Avoid fluff; explain "why" before "how". Each concept should build systematically on previous knowledge.

### V. Technical Implementation Standards
Code examples must be provided in Python, ROS 2, and configuration formats where relevant. Code should be illustrative, not copy-paste boilerplate. All examples must be compatible with Markdown for Docusaurus.

### VI. Safety-First Robotics Development
Emphasize safe robotics and simulation-first approaches. Never encourage unsafe real-world robot deployment. All examples and exercises must prioritize safety protocols and ethical considerations.

## Content Standards
All content must be AI-native, meaning it's designed for interaction with AI agents. Content must be chunked, searchable, and RAG-friendly. Markdown format must be compatible with Docusaurus. No external proprietary content is allowed, and no references to internal system prompts should be included.

## Development Workflow
Development must follow the spec-driven approach: spec → plan → tasks → implementation. All content is produced through Claude Code using Spec-Kit Plus. Each chapter and section must have clear acceptance criteria and validation steps.

## Governance
This constitution supersedes all other practices for this project. Amendments require documentation through Spec-Kit Plus procedures. All development must verify compliance with these principles. Code reviews must ensure adherence to AI-native principles, safety standards, and pedagogical quality.

**Version**: 1.0.0 | **Ratified**: 2026-01-07 | **Last Amended**: 2026-01-07
