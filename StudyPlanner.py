from datetime import datetime
import os
from zoneinfo import ZoneInfo
import requests
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("CANVAS_API_TOKEN")
BASE_URL = os.getenv("SCHOOL")

def get_data(path):
    url = BASE_URL + path

    headers = {
        "Authorization": f"Bearer {TOKEN}"
    }

    data = []

    while url:
        response = requests.get(url, headers=headers)

        if response.status_code != 200:
            print(f"ERROR: {response.status_code}")
            print(response.text)
            return[]

        data.extend(response.json())

        url = None

        if "Link" in response.headers:
            links = response.headers["Link"].split(",")

            for link in links:
                if 'rel="next"' in link:
                    url = link.split(";")[0].strip("<>")

    return data

def get_courses():
    return get_data("/courses?enrollment_state=active")

def get_assignments(course_id):
    path = f"/courses/{course_id}/assignments?per_page=100"
    return get_data(path)

def show_assignments(course_name, assignments):
    mountain_time = ZoneInfo("America/Boise")
    now = datetime.now(mountain_time)

    upcoming = []

    for assignment in assignments:
        due_date = assignment.get("due_at")

        if due_date is None:
            continue

        due_date = datetime.fromisoformat(
            due_date.replace("Z", "+00:00")
        )

        upcoming.append((due_date, assignment["name"]))

    upcoming.sort()

    print(f"Assignments for {course_name}")

    for due_date, name in upcoming:
        due_date = due_date.replace(tzinfo=mountain_time)


        days_left = (due_date - now).days

        if due_date < now:
            status = "Passed"
        elif days_left <= 3:
            status = "Due soon"
        else:
            status = "Coming up"

        print(f"{status}")
        print(f"  {name}")
        print(f"  Due: {due_date.strftime('%b %d, %Y')}")



def main():
    if not TOKEN:
        print("No token")

    print("             CANVAS TODO TRACKER")

    courses = get_courses()

    courses = [
        course for course in courses
        if "Fa26" in course["name"] or "F26" in course["name"]
    ]

    while True:
        print("\nYour Courses:")

        for i, course in enumerate(courses, start=1):
            print(f"{i}. {course['name']}")

        print("0. Exit")

        choice = input("\nChoose a course: ")

        if choice == "0":
            break

        selected_course = courses[int(choice) - 1]

        print(f"\nLoading assignments for {selected_course['name']}")

        assignments = get_assignments(selected_course["id"])

        show_assignments(
            selected_course["name"],
            assignments
        )


if __name__ == "__main__":
    main()