# ai-program-alignment-agent

This Ai Agent showcases AI-powered Technical Program Management that aligns cross-functional organizations around a common North Star Metric and evaluates competing program resolutions using the RICE prioritization framework.

# High Level Architecture

```text
                  User Input
                      │
                      ▼
              ┌───────────────┐
              │ LLM Analysis  │
              └───────┬───────┘
                      │
          ┌───────────┴───────────┐
          │                       │
          ▼                       ▼
    Metric Analysis         Resolution Analysis
          │                       │
          ▼                       ▼
  Candidate Metrics          RICE Inputs
          │                       │
          ▼                       ▼
     AI Reasoning          Python Calculation
          │                       │
          └───────────┬───────────┘
                      ▼
              ┌───────────────┐
              │ Final Report  │
              └───────────────┘
```

Possible future Ai agent based usescases
1. ai-program-risk-agent	- AI + risk management
2. ai-raid-assistant -	LLM + program management
3. ai-executive-status-generator	- AI + executive communication
4. ai-release-readiness - AI + SDLC
5. program-dependency-analyzer	- Graph/data + technical PM
6. program-knowledge-rag	- RAG + architecture
7. ai-requirements-analyzer	- Requirements + GenAI
8. program-health-dashboard	- Data + KPIs + visualization
