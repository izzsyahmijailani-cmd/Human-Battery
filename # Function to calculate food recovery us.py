# Function to calculate food recovery using nested if
def calculate_food_recovery(food_rating):
    if food_rating == 1:
        food_recovery = 15
    elif food_rating == 2:
        food_recovery = 8
    else:
        food_recovery = 2
    return food_recovery

# Function to generate visual battery icon using loop
def get_battery_icon(battery_level):
    if battery_level < 0:
        battery_level = 0
    elif battery_level > 100:
        battery_level = 100
        
    filled_blocks = int(battery_level // 10)
    empty_blocks = 10 - filled_blocks
    
bar = ""
    for i in range(filled_blocks):
        bar += "█"
    for i in range(empty_blocks):
        bar += "."
        
    return f"[{bar}] {battery_level}%"
# Function for AI Mode analysis
def ai_energy_assistant(battery_left, stress_level, total_consumption):
    print("\n[AI Assistant Active - Analyzing Your Energy Profile...]")
    
    diagnostic_steps = ["Checking Workload", "Analyzing fatigue factors", "Formulating recovery plan"]
    for step in diagnostic_steps:
        print(f" -> {step}...")
            
    if battery_left < 40:
        if stress_level >= 7:
            advice = "AI Recommendation: High burnout risk detected! Take a mandatory 30-minute nap and disconnect from work."
        else:
            advice = "AI Recommendation: Your energy is depleting fast. Try to reduce focus hours or increase resting time."
    else:
        advice = "AI Recommendation: Energy levels are stable. Maintain your current routine!"
        
    return advice

def run_human_battery_os():
    print("=" * 47)
    print("ADVANCE HUMAN BATTERY OS".center(47))
    print("=" * 47)

    initial_battery = 100
    
    # Tuple
    food_options = (
    ("1", "Clean & Nutritious Meal", 15),
    ("2", "Average/Mix of Healthy and junk", 8),
    ("3", "Heavy, processed or poor food", 2))
    
    # List requirement: store daily logs
    activity_logs = []
    day_count = 1
    running = True

    # Main Loop to allow multi-day simulation (Day 1, Day 2, Day 3...)
    while running:
        current_day = f"Day {day_count}"
        print(f"\n==================== {current_day} ====================")
        ai_choice = input("Do you want to use AI (Yes/No)?: ").strip().upper()

        if ai_choice == "YES":
            print("\n[AI Mode Enabled]")
            print("AI is gathering your lifestyle inputs...")
            
            sleep_hour = eval(input("Sleep Hour: "))
            working_hour = eval(input("Working Hour: "))
            resting_time = eval(input("Resting Time (in minutes): "))
            stress_level = int(input("Stress Level scale (from 1 to 10): "))
            phys_actv_hour = eval(input("Physical Activity Hour: "))

            print("How would you rate your food intake today?")
            for option in food_options:
                print(f"{option[0]} = {option[1]}")
                
            food_rating = int(input("Enter your food rating (1/2/3): "))
            food_recovery = calculate_food_recovery(food_rating)

            # Energy calculation
            if sleep_hour <= 8:
                sleep_deficite = 8 - sleep_hour
            else:
                sleep_deficite = 0

           galym

            ai_suggestion = ai_energy_assistant(battery_left, stress_level, total_consumption)
            battery_display = get_battery_icon(battery_left)

            print("-" * 25)
            print(f"Total Energy Consumed: {total_consumption}")
            print(f"Total Recovery Gained: {total_recovery}")
            print(f"Battery Status: {battery_display}")
            print(ai_suggestion)
            print("-" * 25)
            
            # Store into List
            activity_logs.append([current_day, battery_left, "AI Mode Used"])

        hannah

            if sleep_hour <= 8:
                sleep_deficite = 8 - sleep_hour
            else:
                sleep_deficite = 0

            sleep_cost = sleep_deficite * 4
            focus_cost = working_hour * 5
            stress_cost = stress_level * 2
            activity_cost = phys_actv_hour * 6
            total_consumption = sleep_cost + focus_cost + stress_cost + activity_cost

            rest_recovery_boost = (resting_time / 60) * 12
            total_recovery = rest_recovery_boost + food_recovery
            battery_left = initial_battery - total_consumption + total_recovery

          
            if battery_left < 50:
                if stress_level > 7:
                    status_message = "CRITICAL: Low battery & High stress! Rest immediately."
                else:
                    status_message = "WARNING: Low battery level. Take a break."
            else:
                status_message = "OPTIMAL: Energy level looks great!"

            battery_display = get_battery_icon(battery_left)
            activity_logs.append([current_day, battery_left, status_message])

            # Nested Loop Analysis & Percentage calculation
            print("\n[Nested Loop Analysis - Cost Breakdown]")
            cost_breakdown = [
                ("Sleep Cost", sleep_cost),
                ("Work Cost", focus_cost),
                ("Stress Cost", stress_cost),
                ("Activity Cost", activity_cost)]
        
            for category, cost in cost_breakdown:
                if total_consumption > 0:
                    percentage = (cost / total_consumption) * 100
                else:
                    percentage = 0.0
                    
                print(f"-> Category: {category}")
                for sub_step in range(1):
                    print(f"   Impact Value: {cost} units ({percentage:.1f}% of total consumption)")
           

        
            print("-" * 25)
            print(f"Total Energy Consumed: {total_consumption}")
            print(f"Total Recovery Gained: {total_recovery}")
            print(f"Battery Status: {battery_display}")
            print(f"Status: {status_message}")
            print("-" * 25)

        else:
            print("Invalid choice! Skipping this attempt.")

        print("\n" + "=" * 30)
                next_day = input("Do you want to log for the next day? (YES/NO): ").strip().upper()
                if next_day == "YES":
                    day_count += 1
                else:
                    running = False

    # Display full summary across all days stored in List
    print("\n[System Log Summary - All Days]")
    for log in activity_logs:
        battery_art = get_battery_icon(log[1])
        print(f"Record Saved -> Day: {log[0]} | Battery: {battery_art} | Note: {log[2]}")
    print("\nThank you for using ADVANCE HUMAN BATTERY OS!")

if __name__ == "__main__":
    run_human_battery_os()
