from __future__ import annotations

from app.services.content_service import get_topic_by_id


def evaluate_quiz(topic_id: str, answers: list[int]) -> dict:
    topic = get_topic_by_id(topic_id)
    quiz_bank = topic["quiz_bank"]
    reviewed_questions: list[dict] = []
    correct_answers = 0

    for index, item in enumerate(quiz_bank):
        learner_answer = answers[index] if index < len(answers) else -1
        is_correct = learner_answer == item["correct_index"]
        if is_correct:
            correct_answers += 1

        reviewed_questions.append(
            {
                "question": item["question"],
                "selected_index": learner_answer,
                "correct_index": item["correct_index"],
                "is_correct": is_correct,
                "explanation": item["explanation"],
                "options": item["options"],
            }
        )

    total_questions = len(quiz_bank)
    score_percent = round((correct_answers / total_questions) * 100, 2) if total_questions else 0.0

    if score_percent >= 80:
        feedback = "Strong understanding. Move to Learn More or apply the topic in a mini-project."
    elif score_percent >= 50:
        feedback = "You understand the base idea, but a second pass with one hands-on example would help."
    else:
        feedback = "Revisit the generated explanation and focus on the core concepts before moving on."

    return {
        "topic_id": topic_id,
        "total_questions": total_questions,
        "correct_answers": correct_answers,
        "score_percent": score_percent,
        "feedback": feedback,
        "reviewed_questions": reviewed_questions,
    }
