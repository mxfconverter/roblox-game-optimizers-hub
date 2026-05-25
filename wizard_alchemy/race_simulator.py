#!/usr/bin/env python3
"""
Roblox Wizard Alchemy - Race Reroll Gacha Probability Simulator (CLI)
Deployed by AverGames: https://avergames.com
"""

import sys
import random

def simulate_rerolls(target_rate, max_attempts=500):
    """Simulates rerolling until hitting the target race rate."""
    attempts = 0
    for i in range(1, max_attempts + 1):
        attempts += 1
        if random.random() < target_rate:
            return attempts, True
    return attempts, False

def main():
    print("=" * 60)
    print("🧙 Roblox Wizard Alchemy Race Reroll Gacha Simulator 🧙")
    print("Brought to you by AverGames: https://avergames.com")
    print("=" * 60)

    # Wizard Alchemy races with pull rates
    races = {
        "1": {"name": "Thestrals (S-Tier)", "rate": 0.01},
        "2": {"name": "Elf (S-Tier)", "rate": 0.03},
        "3": {"name": "Dwarf (A-Tier)", "rate": 0.10},
        "4": {"name": "Human (B-Tier)", "rate": 0.20}
    }

    print("\nSelect your Target Race to Simulate Rerolls:")
    for key, data in races.items():
        print(f"{key}. {data['name']} (Pull Rate: {data['rate']*100:.1f}%)")
        
    choice = input("Enter choice (1-4): ").strip()
    if choice not in races:
        print("Invalid choice. Exiting.")
        return
        
    target_race = races[choice]
    rate = target_race['rate']
    
    try:
        gold_per_reroll = int(input("\nEnter gold cost per single reroll (e.g. 500 gold): "))
        budget_rerolls = int(input("Enter your current reroll attempts budget (e.g. 50): "))
    except ValueError:
        print("Error: Invalid numeric input.")
        return

    # Cumulative math probability
    prob_success = 1.0 - ((1.0 - rate) ** budget_rerolls)
    expected_attempts_to_hit = round(1.0 / rate)
    expected_gold_cost = expected_attempts_to_hit * gold_per_reroll

    print("\n" + "-" * 40)
    print(f"📊 Probability Analysis for: {target_race['name']}")
    print("-" * 40)
    print(f"Single Attempt Success Rate : {rate*100:.1f}%")
    print(f"Budget Pulls Available      : {budget_rerolls} attempts")
    print(f"Cumulative Success Chance   : {prob_success*100:.2f}% (with your budget)")
    print(f"Statistically Expected Pulls: {expected_attempts_to_hit} attempts to guarantee 1 success")
    print(f"Average Gold Cost Required  : {expected_gold_cost:,} gold")
    print("-" * 40)

    # Run quick simulated trials
    print("\n🎲 Running 10 simulated trials with your budget...")
    successes = 0
    for trial in range(1, 11):
        attempts, won = simulate_rerolls(rate, budget_rerolls)
        status = f"SUCCESS (Attempt #{attempts})" if won else f"FAILED (Spent all {budget_rerolls} rolls)"
        print(f"  Trial {trial:02d}: {status}")
        if won:
            successes += 1
            
    print(f"\n👉 Simulation Result: Succeeded in {successes}/10 trials.")
    
    print("\n💡 Optimization Tip: Keep wands fully upgraded to farm gold faster before committing to heavy rerolls!")
    print("For full race stat tables & tier lists, check: https://avergames.com/games/wizard-alchemy/race-tier-list")
    print("For magic potion combination formulas, check: https://avergames.com/games/wizard-alchemy/magic-power-calculator")
    print("=" * 60)

if __name__ == "__main__":
    main()
