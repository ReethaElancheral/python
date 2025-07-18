def add_question(question_bank, topics, qid, question_text, options, answer, topic):
    if qid in question_bank:
        print(f"Question ID {qid} already exists.")
        return

    question_bank[qid] = {
        "question": question_text,
        "options": options,
        "answer": answer,
        "topic": topic
    }

    topics.add(topic)
    print(f"Question added under topic '{topic}'.")

def list_questions(question_bank):
    if not question_bank:
        print("No questions added yet.")
        return

    print("\n--- All Questions ---")
    for qid, data in question_bank.items():
        print(f"\nID: {qid}")
        print(f"Topic: {data['topic']}")
        print(f"Q: {data['question']}")
        for idx, opt in enumerate(data['options'], 1):
            print(f"   {idx}. {opt}")
        print(f"Answer: {data['answer']}")

def list_topics(topics):
    if not topics:
        print("No topics found.")
    else:
        print(f"Available Topics: {', '.join(topics)}")
