def load_questions(filename):
    questions = []
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            if "|" in line:
                q, a = line.strip().split('|', 1)
                questions.append({'question': q, 'answer': a})
    return questions
def show_questions(questions_):
    score = 0
    for q in  questions_:
        print(q['question'])
        user_answer = input("Your answer: ").strip()
        if user_answer.lower() == q['answer'].lower():
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong! The correct answer is '{q['answer']}'.\n")
    print(f"Quiz Completed! Your score: {score}/{len(questions_)}")

questions1 = load_questions('quiz_game.txt')
show_questions(questions1)

