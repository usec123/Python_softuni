def add_lesson(lessons:list, lesson_title):
    if lesson_title not in lessons:
        lessons.append(lesson_title)
    return lessons

def insert_lesson(lessons:list, lesson_title, index):
    if lesson_title not in lessons:
        lessons.insert(index,lesson_title)
    return lessons

def remove_lesson(lessons:list, lesson_title):
    if lesson_title in lessons:
        index = lessons.index(lesson_title)
        if index+1 in range(len(lessons)):
            if 'Exercise' in lessons[index+1]:
                lessons.pop(index+1)
        lessons.remove(lesson_title)
    return lessons

def swap_lesson(lessons:list, first_title, second_title):
    if first_title in lessons and second_title in lessons:
        first_index = lessons.index(first_title)
        second_index = lessons.index(second_title)
        first_exercise = False
        second_exercise = False
        if first_index+1 in range(len(lessons)):
            first_exercise = 'Exercise' in lessons[first_index+1]
        if second_index+1 in range(len(lessons)):
            second_exercise = 'Exercise' in lessons[second_index+1]
        lessons[first_index], lessons[second_index] = lessons[second_index], lessons[first_index]
        if first_exercise and second_exercise:
            lessons[first_index + 1], lessons[second_index + 1] = lessons[second_index + 1], lessons[first_index + 1]
        elif not first_exercise and second_exercise:
            lessons.insert(first_index + 1, lessons.pop(second_index+1))
        elif first_exercise and not second_exercise:
            lessons.insert(second_index + 1, lessons.pop(first_index+1))
        return lessons
    
def exercise(lessons:list, title):
    if title in lessons and f'{title}-Exercise' not in lessons:
        index = lessons.index(title)
        lessons.insert(index+1,f'{title}-Exercise')
    elif title not in lessons:
        lessons.append(title)
        lessons.append(f'{title}-Exercise')
    return lessons

list_lessons = input().split(", ")
command = input()
while command != "course start":
    command = command.split(":")
    action, lesson_title = command[0], command[1]
    if len(command) > 2:
        index_or_lesson_title = command[2]
    if action == "Add":
        lessons = add_lesson(list_lessons, lesson_title)
    elif action == "Insert":
        lessons = insert_lesson(list_lessons, lesson_title, int(index_or_lesson_title))
    elif action == "Remove":
        lessons = remove_lesson(list_lessons, lesson_title)
    elif action == "Swap":
        lessons = swap_lesson(list_lessons, lesson_title, index_or_lesson_title)
    elif action == "Exercise":
        lessons = exercise(list_lessons, lesson_title)
    command = input()

for i,lesson in enumerate(list_lessons):
    print(f'{i+1}.{lesson}')