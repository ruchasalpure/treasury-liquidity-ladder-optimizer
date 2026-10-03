from crewai import Agent

treasury_liquidity_ladder_optimizer = Agent(
    role="Treasury Liquidity Ladder Optimizer",
    goal="Deliver high-precision autonomous Treasury Liquidity Ladder Optimizer operations",
    backstory="Engineered under OpenGAP governance standards.",
    verbose=True,
    allow_delegation=False
)
