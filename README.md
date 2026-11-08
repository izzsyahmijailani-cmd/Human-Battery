 print("\n" + "=" * 30)
        next_day = input("Do you want to log for the next day? (YES/NO): ").strip().upper()
        if next_day == "YES":
            day_count += 1
        else:
            running = False
