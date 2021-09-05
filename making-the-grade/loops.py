def round_scores(student_scores):
    '''
    :param student_scores: list of student exam scores as float or int.
    :return: list of student scores *rounded* to nearest integer value.
    '''
    return [round(score) for score in student_scores]
    
def count_failed_students(student_scores):
    '''
    :param student_scores: list of integer student scores.
    :return: integer count of student scores at or below 40.
    '''
    return len([score for score in student_scores if score <= 40])
    
def above_threshold(student_scores, threshold):
    '''
    :param student_scores: list of integer scores
    :param threshold :  integer
    :return: list of integer scores that are at or above the "best" threshold.
    '''
    return [score for score in student_scores if score >= threshold]
    
def letter_grades(highest):
    '''
    :param highest: integer of highest exam score.
    :return: list of integer score thresholds for each F-A letter grades.
    '''
    return [41 + ((highest - 40) // 4 * i) for i in range(0, 4, 1)]
    
def student_ranking(student_scores, student_names):
    '''
     :param student_scores: list of scores in descending order.
     :param student_names: list of names in descending order by exam score.
     :return: list of strings in format ["<rank>. <student name>: <score>"].
     '''
    myList = []

    for index, thing in enumerate(zip(student_scores, student_names)):
        myList.append(f'{index + 1}. {thing[1]}: {thing[0]}')
    
    return myList

def perfect_score(student_info):
    '''
    :param student_info: list of [<student name>, <score>] lists
    :return: First [<student name>, 100] found OR "No perfect score."
    '''
    for thing in student_info:
        if 100 in thing:
            return thing
    return 'No perfect score.'