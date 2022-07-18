'''
subdomain
branch
company
course

User
    FK - branch
    "name": "Botir",
    "gender": "m",   # "f"
    "date_of_birth": "2022\/06\/29",
    "phone": "901020320",
    "datas": [],
    "comment": null,
    "company_id": 2440,
    "relation_degree": 0,
    "photo": "",
    "created_by": 179119,
    "updated_by": 179119,
    "updated_at": "2022-07-15T15:35:57.000000Z",
    "created_at": "2022-07-15T15:35:57.000000Z",
    "id": 181263,
    ROLE arrayfield choice{
    CEO
    Branch Director
    Administrator
    Limited Administrator
    Teacher
    Marketer
    Cashier
    Student
    }


UserHistory
    "id": 3962238,
    "user": FK User
    "status": 20,
    "description": "{\"date_of_birth\":{\"from\":\"2022-06-29\",\"to\":\"2022\\\/06\\\/29\"}}",
    "created_at": "15.07.2022 20:45:47",
    "creator": FK User



'''


'''

"subdomain": [
    "name": "Paramount Education",
    "logo": "62f9QpbkHvoKWzhg.png",
    "about": null,
    "lead_about": null,
    "page_background": null,
    "form_background": null,
    "activated_till": "2022-07-20",
    "start_of_working_day": "07:00:00",
    "end_of_working_day": "20:00:00"
]
"branches": [
        "id": 1370,
        "name": "Paramount Education",
        "is_recalculation_on": 1
],
"courses": [
        "id": 6588,
        "name": "First Course",
        "image": null,
        "description": null,
        "lesson_duration": "90",
        "course_duration": 3,
        "lessons_per_module": 12,
        "parent": null,
        "price": 500000,
        "type": 2,
        "is_enabled": 1
]


Group
    "id": 27260,
    "branch_id": FK BRANCH,
    "company_group_number": 1,
    "code": "birinchi guruh",
    "name": "birinchi guruh",
    "days": 1,
    "exact_days": null,
    "lesson_start_time": "10:00",
    "lesson_end_time": "2022-07-15T06:30:00.000000Z",
    "status": 2,
    "type": 1,
    "course": FK COURSE
    "rooms": M2M ROOMS
    "teachers": M2M User
    "group_start_date": "2022-07-13",
    "group_end_date": "2022-10-13",
    "last_write_off_date": null,
    "next_write_off_date": null,
    "created_at": "13.07.2022 20:00:46",
    "updated_at": "15.07.2022 20:52:48",
    "tags": [],
    "student_count": 2
},
'''