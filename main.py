from question import Question

if __name__ == "__main__":
    question = Question()

    while (True):
        answer = question.put_question()
        print(answer)

        user_input = input()

        if answer == user_input:
            print("Success!!\n")
        else:
            print("Failed...\n")
