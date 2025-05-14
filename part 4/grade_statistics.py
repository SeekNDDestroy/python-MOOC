# Write your solution here
def user_input(examPoints, exerciseCompleted):
    while True:
        userInput = input("Exam points and exercises completed:")
        if not userInput:
            print(examPoints)
            print(exerciseCompleted)
            break
        userList= list(userInput.split(" "))
        examPoints.append(userList[0])
        exerciseCompleted.append(userList[1])
    
def exerciseCompletedToExercisePoints(exerciseCompleted : list, exercisePoints: list) -> int:
    for i in exerciseCompleted:
        for j in range(9, 0, -1):
            if (int(i) <= (j * 10)) and (int(i) > ((j - 1) * 10)):
                exercisePoints.append(j)
                

def gradeCalculator(examPoints : list, exercisePoints: list , grade : list) -> list:
    for i in range(len(examPoints)):
        grade.append(examPoints[i] + exercisePoints[i])
        




def main():
    exerciseCompleted = []

    examPoints = []
    exercisePoints = []

    grade = []

    user_input(examPoints, exerciseCompleted)
    exerciseCompletedToExercisePoints(exerciseCompleted, exercisePoints)
    print(exercisePoints)

    gradeCalculator(examPoints, exercisePoints, grade)
    print(grade)


if __name__ == "__main__":
    main()