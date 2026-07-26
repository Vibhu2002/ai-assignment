# Before Token Optimization

## Scenario

A multi-agent AI pipeline contains five agents:

1. Planner
2. Research
3. Retriever
4. Reviewer
5. Writer

Each agent receives the complete conversation history and retrieved documents.

### Token Usage

| Agent | Tokens |
|-------|--------|
| Planner | 20,000 |
| Research | 20,000 |
| Retriever | 20,000 |
| Reviewer | 20,000 |
| Writer | 20,000 |

**Total Input Tokens = 100,000**

### Problems

- High API cost
- Increased latency
- Duplicate context passed to every agent
- Poor scalability