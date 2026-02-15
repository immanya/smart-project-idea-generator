# Smart Project Idea Generator
# Rule-Based Expert System using Forward Chaining

def get_user_input():
    print("===== SMART PROJECT IDEA GENERATOR =====")

    branch = input("Enter your branch (CSE/IT/etc): ").lower()
    interest = input("Enter your interest (ai/web/cybersecurity/data): ").lower()
    level = input("Enter your level (beginner/intermediate/advanced): ").lower()

    languages = input("Enter languages you know (comma separated e.g. python,java,html): ").lower().split(",")
    concepts = input("Enter concepts you know (comma separated e.g. dsa,dbms,ml): ").lower().split(",")

    facts = {
        "branch": branch,
        "interest": interest,
        "level": level,
        "languages": [lang.strip() for lang in languages],
        "concepts": [con.strip() for con in concepts]
    }

    return facts


def apply_rules(facts):
    suggestions = []
    fired_rules = []

    # Rule 1 - AI Beginner
    if facts["interest"] == "ai" and "python" in facts["languages"] and facts["level"] == "beginner":
        suggestions.append("Spam Email Classifier using Machine Learning")
        fired_rules.append("Rule 1: AI + Python + Beginner")

    # Rule 2 - AI Intermediate
    if facts["interest"] == "ai" and "python" in facts["languages"] and facts["level"] == "intermediate":
        suggestions.append("House Price Prediction using Linear Regression")
        fired_rules.append("Rule 2: AI + Python + Intermediate")

    # Rule 3 - AI Advanced
    if facts["interest"] == "ai" and facts["level"] == "advanced" and "python" in facts["languages"] and "ml" in facts["concepts"]:
        suggestions.append("Face Recognition System using OpenCV")
        fired_rules.append("Rule 3: AI + Advanced + Python + ML")

    # Rule 4 - AI without Python
    if facts["interest"] == "ai" and "python" not in facts["languages"]:
        suggestions.append("Learn Python before starting AI projects")
        fired_rules.append("Rule 4: AI but no Python")

    # Rule 5 - Web Basic
    if facts["interest"] == "web" and "html" in facts["languages"] and "css" in facts["languages"]:
        suggestions.append("Personal Portfolio Website")
        fired_rules.append("Rule 5: Web + HTML + CSS")

    # Rule 6 - Web Intermediate
    if facts["interest"] == "web" and "html" in facts["languages"] and "css" in facts["languages"] and "javascript" in facts["languages"] and facts["level"] == "intermediate":
        suggestions.append("Full Stack Blog Website")
        fired_rules.append("Rule 6: Web + HTML + CSS + JS + Intermediate")

    # Rule 7 - Strong DSA
    if "dsa" in facts["concepts"] and facts["level"] in ["intermediate", "advanced"]:
        suggestions.append("Mini Coding Practice Platform")
        fired_rules.append("Rule 7: Strong DSA")

    # Rule 8 - Data + DBMS
    if facts["interest"] == "data" and "python" in facts["languages"] and "dbms" in facts["concepts"]:
        suggestions.append("Sales Data Dashboard using CSV")
        fired_rules.append("Rule 8: Data + Python + DBMS")

    # Rule 9 - Cybersecurity Beginner
    if facts["interest"] == "cybersecurity" and facts["level"] == "beginner":
        suggestions.append("Password Strength Checker")
        fired_rules.append("Rule 9: Cybersecurity Beginner")

    # Default Rule
        # Rule 10 - AI + DSA Strong
    if facts["interest"] == "ai" and "dsa" in facts["concepts"]:
        suggestions.append("Build AI-based Problem Solver")
        fired_rules.append("Rule 10: AI + Strong DSA")
        # Rule 11 - Advanced Web
    if facts["interest"] == "web" and facts["level"] == "advanced":
        suggestions.append("E-commerce Website with Payment Integration")
        fired_rules.append("Rule 11: Advanced Web Development")


    if not suggestions:
        suggestions.append("Start with Basic Python Mini Projects")
        fired_rules.append("Default Rule Fired")

    return suggestions, fired_rules


def calculate_score(facts):
    score = 0

    if "python" in facts["languages"]:
        score += 2
    if "dsa" in facts["concepts"]:
        score += 2
    if "dbms" in facts["concepts"]:
        score += 1
    if facts["level"] == "intermediate":
        score += 2
    if facts["level"] == "advanced":
        score += 3

    return score


def main():
    facts = get_user_input()
    suggestions, fired_rules = apply_rules(facts)
    score = calculate_score(facts)

    total_rules = 11

    confidence = (len(fired_rules) / total_rules) * 100

    print("\n===== STUDENT PROFILE ANALYSIS =====")
    print("Interest:", facts["interest"])
    print("Level:", facts["level"])
    print("Score:", score)

    print("\n===== RECOMMENDED PROJECTS =====")
    for i, project in enumerate(suggestions, 1):
        print(f"{i}. {project}")

    print("\n===== CONFIDENCE LEVEL =====")
    print(f"{confidence:.2f}%")

    print("\n===== RULES FIRED =====")
    for rule in fired_rules:
        print(rule)


if __name__ == "__main__":
    main()
