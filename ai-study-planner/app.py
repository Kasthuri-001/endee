# AI Study Planner (with search concept)

# Sample data
data = [
    "Study Maths for 2 hours",
    "Practice Physics problems",
    "Learn AI concepts",
    "Revise DSA topics"
]

print("✅ Data ready (stored like vector DB)\n")

# User input
query = input("🔍 Enter what you want to study: ").lower()

print("\n📊 Recommended Study Plan:\n")

# Simple semantic-like search
for item in data:
    if query in item.lower():
        print("-", item)