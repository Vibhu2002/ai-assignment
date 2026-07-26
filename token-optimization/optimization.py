# Token Optimization Simulation

class AgentPipeline:
    def __init__(self):
        # Before Optimization (All agents receive full context)
        self.before_tokens = {
            "Planner": 20000,
            "Research": 20000,
            "Retriever": 20000,
            "Reviewer": 20000,
            "Writer": 20000
        }

        # After Optimization
        self.after_tokens = {
            "Planner": 6000,
            "Research": 8000,
            "Retriever": 7000,
            "Reviewer": 4000,
            "Writer": 3000
        }

    def total_tokens(self, token_dict):
        return sum(token_dict.values())

    def print_report(self):
        print("=" * 50)
        print("BEFORE OPTIMIZATION")
        print("=" * 50)

        for agent, tokens in self.before_tokens.items():
            print(f"{agent:<12}: {tokens}")

        before_total = self.total_tokens(self.before_tokens)
        print(f"\nTotal Tokens : {before_total}")

        print("\nOptimization Applied:")
        print("1. Context Pruning")
        print("2. Context Compression")

        print("\n" + "=" * 50)
        print("AFTER OPTIMIZATION")
        print("=" * 50)

        for agent, tokens in self.after_tokens.items():
            print(f"{agent:<12}: {tokens}")

        after_total = self.total_tokens(self.after_tokens)

        reduction = before_total - after_total
        percentage = (reduction / before_total) * 100

        print(f"\nTotal Tokens : {after_total}")
        print(f"Tokens Saved : {reduction}")
        print(f"Reduction    : {percentage:.2f}%")

        print("\nQuality Impact")
        print("- Context Pruning      : Negligible")
        print("- Context Compression : Minor loss of unnecessary details")


if __name__ == "__main__":
    pipeline = AgentPipeline()
    pipeline.print_report()