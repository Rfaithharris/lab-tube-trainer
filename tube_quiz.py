import random

# Dictionary of lab tests and their correct tubes
lab_tests = {
    "CBC": {"tube": "Lavender (EDTA)", "notes": "Invert 8-10 times."},
    "CMP": {"tube": "Gold (SST)", "notes": "Fasting preferred. Centrifuge within 2 hrs."},
    "PT/INR": {"tube": "Light Blue (Citrate)", "notes": "Fill tube completely. Invert 3-4 times."},
    "Lactic Acid": {"tube": "Gray (Fluoride)", "notes": "Send on ice. No tourniquet."},
    "TSH": {"tube": "Gold (SST)", "notes": "Centrifuge and refrigerate if delay >2 hrs."},
    "Blood Culture": {"tube": "Blood Culture Bottles", "notes": "Use aseptic technique. Collect before antibiotics."},
    "Troponin": {"tube": "Green (Heparin)", "notes": "STAT test. Deliver to lab immediately."},
    "HgbA1c": {"tube": "Lavender (EDTA)", "notes": "Room temp is fine. No fasting needed."},
    "Ammonia": {"tube": "Lavender (EDTA)", "notes": "Place on ice immediately. Avoid hemolysis."},
    "Vitamin D": {"tube": "Gold (SST)", "notes": "Protect from light. Centrifuge."},
    "Lithium Level": {"tube": "Red (No Additive)", "notes": "Do NOT use SST. Trough level preferred."},
    "ESR": {"tube": "Lavender (EDTA)", "notes": "Fill tube completely to correct ratio."},
    "Glucose": {"tube": "Gray (Fluoride)", "notes": "Fasting preferred. Invert 8-10 times."}
}
def run_quiz():
    questions = random.sample(list(lab_tests.items()), k=5)  # Pick 5 random tests
    score = 0

    print("🧪 Lab Tube Type Training Quiz\n")

    for i, (test, info) in enumerate(questions, 1):
        correct_tube = info['tube']

        # Get 3 other tube types as distractors
        all_tubes = list({v['tube'] for v in lab_tests.values()})
        all_tubes.remove(correct_tube)
        choices = random.sample(all_tubes, k=2)
        choices.append(correct_tube)
        random.shuffle(choices)

        print(f"{i}. What tube is required for: {test}?")
        for idx, option in enumerate(choices, 1):
            print(f"  {idx}. {option}")

        try:
            answer = int(input("Your choice (1-3): "))
            selected = choices[answer - 1]
        except:
            print("Invalid input. Moving to next question.\n")
            continue

        if selected == correct_tube:
            print("✅ Correct!")
            score += 1
        else:
            print(f"❌ Incorrect. Correct answer: {correct_tube}")

        print(f"📝 Notes: {info['notes']}\n")

    print(f"🏁 Quiz complete! Your score: {score}/5")

if __name__ == "__main__":
    run_quiz()
