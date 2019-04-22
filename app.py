import read_csv
import workspaces
import sys
import constants


def main():
    print (constants.WELCOME_MESSAGE)
    students = read_csv.read_csv(sys.argv[1])
    print(students)
    [workspaces.get_workspaces_details(student, str(sys.argv[2])) for student in students]


if __name__ == '__main__':
    if (len(sys.argv)) != 3:
        print('format : `python app.py filename start/stop`')
        exit(0)
    else:
        main()
