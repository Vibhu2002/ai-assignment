# After Token Optimization

Two optimizations were applied.

## Optimization 1: Context Pruning

Instead of sending the full conversation to every agent, only the required context is forwarded.

Example:

Planner → Plan

Research → Plan + Relevant Documents

Writer → Research Summary

---

## Optimization 2: Context Compression

Large retrieved documents are summarized before passing them to the next agent.

---

## Token Usage

| Agent | Tokens |
|-------|--------|
| Planner | 6,000 |
| Research | 8,000 |
| Retriever | 7,000 |
| Reviewer | 4,000 |
| Writer | 3,000 |

**Total Input Tokens = 28,000**

Reduction:

100,000 → 28,000

**72% reduction**

### Quality Tradeoff

- Context Pruning: Negligible impact
- Context Compression: Minor loss of non-essential details