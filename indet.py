def get_answer(question):
    answers={"привет": "и тебе привет!", "как дела":"лучше всех", "пока":"увидимся"}
    return answers.get(question.lower(), "не понимаю")
print(get_answer("пРиВет"))