# ai_explainer.py

def generate_ai_explanation():
    explanation = (
        "🧠 Root Cause Analysis Suggestion:\n"
        "- The log shows a database connection failure at host=127.0.0.1 port=5432.\n"
        "- Likely causes could include:\n"
        "  • Database server not running\n"
        "  • Network port blocked\n"
        "  • Incorrect database credentials\n\n"
        "✅ After retrying, the connection was re-established, indicating the issue was transient.\n"
        "📌 Recommendation: Monitor database uptime or add retry logic in production."
    )
    return explanation

if __name__ == "__main__":
    result = generate_ai_explanation()
    print(result)
