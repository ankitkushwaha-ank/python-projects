def get_user_input(prompt):
    response = input(prompt)
    return response.strip().lower()


def career_suggestion():
    print("Welcome to the Career Path Finder according to your stream and interest!")
    print("Answer the following questions to help us find out the best career for you.")

    # यूजर से इनपुट लेना
    education_level = get_user_input(
        "What is your highest education level? (high school/bachelor's degree/master's degree/PhD): ")
    interests = get_user_input("What are your interests? (technology/arts/science/business): ")
    strengths = get_user_input(
        "What are your strengths? (analytical thinking/creativity/problem-solving/communication): ")

    # सिंपल लॉजिक से करियर सजेशन देना
    if "technology" in interests and "analytical thinking" in strengths:
        if education_level in ["bachelor's degree", "master's degree", "phd"]:
            return "You might enjoy a career in software development or data science."
        else:
            return "Consider pursuing further education in computer science or information technology."
    elif "arts" in interests and "creativity" in strengths:
        return "A career in graphic design, fine arts, or digital media might be suitable for you."
    elif "science" in interests and "problem-solving" in strengths:
        if education_level in ["bachelor's degree", "master's degree", "phd"]:
            return "You might enjoy a career in scientific research, engineering, or healthcare."
        else:
            return "Consider pursuing further education in a scientific field that interests you."
    elif "business" in interests and "communication" in strengths:
        return "A career in marketing, sales, or business management might be suitable for you."
    else:
        return "Consider exploring different fields and gaining experience through internships or volunteering to find what best suits your interests and strengths."


def main():
    suggestion = career_suggestion()
    print("\nCareer Suggestion:")
    print(suggestion)


if __name__ == "__main__":
    main()


def get_user_input(prompt):
    response = input(prompt)
    return response.strip().lower()


def career_suggestion():
    print("Welcome to the Career Path Finder according to your stream and interest )
    print(answer
    the
    following
    questions
    to
    help
    us
    find
    out
    the
    best
    czrrer )
    # Simple logic to suggest a career based on the inputs
    if "technology" in interests and "analytical thinking" in strengths:
        if
    education_level in ["bachelor's degree", "master's degree", "PhD"]:
    return "You might enjoy a career in software development or data science."
    else:
    return "Consider pursuing further education in computer science or information technology."

elif "arts" in interests and "creativity" in strengths:
return "A career in graphic design, fine arts, or digital media might be suitable for you."
elif "science" in interests and "problem-solving" in strengths:
if education_level in ["bachelor's degree", "master's degree", "PhD"]:
    return "You might enjoy a career in scientific research, engineering, or healthcare."
else:
    return "Consider pursuing further education in a scientific field that interests you."
elif "business" in interests and "communication" in strengths:
return "A career in marketing, sales, or business management might be suitable for you."
else:
return "Consider exploring different fields and gaining experience through internships or volunteering to find what best suits your interests and strengths."


def main():
    suggestion = career_suggestion()
    print("\nCareer Suggestion:")
    print(suggestion)


if __name__ == "__main__":
    main()

