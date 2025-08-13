import re
from ai_explainer import generate_ai_explanation

def analyze_log(log_path):
    with open(log_path, 'r') as file:
        logs = file.read()

    # Simple pattern to check for database error
    pattern = r"FATAL: could not connect to database.*host=(\S+).*port=(\d+)"
    matches = re.findall(pattern, logs)

    if matches:
        print("🚨 Critical log pattern detected!")
        print(generate_ai_explanation())
    else:
        print("✅ No critical issues found in the logs.")

if __name__ == "__main__":
    analyze_log("system.log")
