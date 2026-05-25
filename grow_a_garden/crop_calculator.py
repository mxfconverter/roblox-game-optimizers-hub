#!/usr/bin/env python3
"""
Roblox Build A Ring Farm (Grow a Garden) - Crop Mutation & Profitability Calculator (CLI)
Deployed by AverGames: https://avergames.com
"""

import sys

def main():
    print("=" * 60)
    print("🌻 Roblox Build A Ring Farm (Grow a Garden) Profitability Calculator 🌻")
    print("Brought to you by AverGames: https://avergames.com")
    print("=" * 60)

    # Build A Ring Farm crop catalog
    crops = {
        "1": {"name": "Basic Wheat", "cost": 10, "sell": 25, "time": 60, "mut_rate": 0.05, "mut_mult": 2.0},
        "2": {"name": "Golden Corn", "cost": 50, "sell": 140, "time": 180, "mut_rate": 0.08, "mut_mult": 2.5},
        "3": {"name": "Starlight Lily", "cost": 200, "sell": 620, "time": 400, "mut_rate": 0.12, "mut_mult": 3.0},
        "4": {"name": "Frost Pumpkin", "cost": 800, "sell": 2800, "time": 900, "mut_rate": 0.15, "mut_mult": 4.0}
    }

    print("\nSelect a Crop to Analyze:")
    for key, data in crops.items():
        print(f"{key}. {data['name']} (Seed Cost: ${data['cost']}, Grow Time: {data['time']}s)")
        
    choice = input("Enter choice (1-4): ").strip()
    
    if choice not in crops:
        print("Invalid choice. Exiting.")
        return
        
    crop = crops[choice]
    
    try:
        weather_mult = float(input("\nEnter weather profit multiplier (e.g. 1.0 for Normal, 1.5 for Sunny/Rainy): "))
        mutation_stack = int(input("Enter your current Mutation Stack upgrade level (0 to 10): "))
    except ValueError:
        print("Error: Invalid numeric input.")
        return

    # Calculate probability and values
    base_sell = crop['sell'] * weather_mult
    mutated_sell = base_sell * crop['mut_mult']
    
    # Each mutation level increases mutation rate by 2% base
    current_mut_rate = min(0.95, crop['mut_rate'] + (mutation_stack * 0.02))
    
    # Expected value per harvest
    expected_sell = (base_sell * (1 - current_mut_rate)) + (mutated_sell * current_mut_rate)
    expected_profit = expected_sell - crop['cost']
    
    # Calculate efficiency (per minute)
    profit_per_min = (expected_profit / crop['time']) * 60.0

    print("\n" + "-" * 40)
    print(f"🌾 Harvest Yield Analysis: {crop['name']}")
    print("-" * 40)
    print(f"Base Crop Sale Value : ${base_sell:.2f}")
    print(f"Mutated Sale Value   : ${mutated_sell:.2f} ({crop['mut_mult']}x)")
    print(f"Modified Mutation Rate: {current_mut_rate*100:.1f}% (Stack Lvl: {mutation_stack})")
    print(f"Expected Profit/Seed : ${expected_profit:.2f}")
    print(f"Efficiency Index     : ${profit_per_min:.2f} net profit per minute")
    print("-" * 40)
    
    print("\n💡 Optimization Tip: Prioritize Starlight Lilies when Mutation Stack is level 5+ for massive ROI boost!")
    print("For live dynamic calculators and multi-plot tools, check: https://avergames.com/games/build-a-ring-farm/income-calculator")
    print("=" * 60)

if __name__ == "__main__":
    main()
