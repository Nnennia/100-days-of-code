from typing import List


def round_scores(students_scores: List[int]):
    """Rounds numbers in a list"""
    return [round(scores) for scores in students_scores]


def count_failed_students(student_score: List[int]):
    """Count failed scores"""
    failed = len([score for score in student_score if score <= 40])
    return failed


def above_threshold(students_score: List[int], threshold: int):
    """returns a list of scores that are >= to threshold"""
    return [score for score in students_score if score >= threshold]


def letter_grades(highest_score: str):
    """Where the highest scored is 100, and failing is <= 40"""
    return list(range(41, highest_score, (highest_score-40)//4))


def student_ranking(student_scores: List[int], student_names: List[str]):
    """join items in a list"""
    return [f"{index}. {student_name}: {student_score}"
            for index, (student_score, student_name) in
            enumerate(zip(student_scores, student_names), 1)]


def perfect_score(student_info: List):
    """find perfect score"""
    for student in student_info:
        if student[1] == 100:
            return student
    return []
