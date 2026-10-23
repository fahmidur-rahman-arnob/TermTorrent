"""
TermTorrent - Part 2 Sandbox
----------------------------

এই ছোট sandbox-এর উদ্দেশ্য হলো শেখা:

1. Dictionary দিয়ে একটি Task represent করা
2. List-এর মধ্যে multiple Task রাখা
3. for loop দিয়ে নির্দিষ্ট Task খুঁজে বের করা
4. Dictionary-এর value update করা
5. সব Task print করা

এই code এখনো TermTorrent-এর main application-এর অংশ নয়।
এটা শুধু concept practice করার জন্য।
"""


# =========================================================
# STEP 1 — CREATE MULTIPLE TASKS
# =========================================================

# এখানে আমরা একটি empty list তৈরি করছি।
#
# এই list-এর ভিতরে আমরা একাধিক Task রাখব।
#
# বর্তমানে আমাদের কোনো Task নেই।
#
# তাই:
#
#     tasks = []
#
# পরে এখানে dictionary যোগ হবে।
tasks = []


# ---------------------------------------------------------
# প্রথম Task
# ---------------------------------------------------------

# একটি Task আসলে একটি dictionary।
#
# Dictionary ব্যবহার করার সুবিধা হলো আমরা প্রতিটি
# piece of information-এর জন্য একটি meaningful key
# ব্যবহার করতে পারি।
#
# যেমন:
#
#     "id"     -> Task-এর পরিচয়
#     "name"   -> Task-এর নাম
#     "status" -> Task-এর বর্তমান অবস্থা
task_1 = {
    "id": 1,
    "name": "Ubuntu.iso",
    "status": "PENDING"
}


# Task-1-কে আমাদের tasks list-এর মধ্যে যোগ করছি।
tasks.append(task_1)


# ---------------------------------------------------------
# দ্বিতীয় Task
# ---------------------------------------------------------

task_2 = {
    "id": 2,
    "name": "Python.zip",
    "status": "PENDING"
}

tasks.append(task_2)


# ---------------------------------------------------------
# তৃতীয় Task
# ---------------------------------------------------------

task_3 = {
    "id": 3,
    "name": "Movie.mkv",
    "status": "PENDING"
}

tasks.append(task_3)


# =========================================================
# STEP 2 — DISPLAY TASKS BEFORE UPDATE
# =========================================================

print("========== BEFORE UPDATE ==========")


# এখানে আমরা tasks list-এর প্রতিটি Task-এর উপর
# loop করছি।
#
# প্রথম iteration:
#
#     task = task_1
#
# দ্বিতীয় iteration:
#
#     task = task_2
#
# তৃতীয় iteration:
#
#     task = task_3
#
# অর্থাৎ "task" variable-টি প্রতিবার একটি dictionary
# represent করবে।
for task in tasks:

    # Dictionary থেকে ID বের করছি।
    #
    # task হলো dictionary:
    #
    # {
    #     "id": 1,
    #     "name": "Ubuntu.iso",
    #     "status": "PENDING"
    # }
    #
    # তাই:
    #
    # task["id"]
    #
    # আমাদের 1 return করবে।
    print(
        f"ID: {task['id']} | "
        f"Name: {task['name']} | "
        f"Status: {task['status']}"
    )


# =========================================================
# STEP 3 — FIND A SPECIFIC TASK
# =========================================================

# এখন আমরা Task ID 2 খুঁজব।
#
# ধরে নাও user বলেছে:
#
#     "Task ID 2-এর status DOWNLOADING করো।"
#
# তাই আমাদের প্রথমে ID 2-এর Task খুঁজে বের করতে হবে।
target_task_id = 2


# ---------------------------------------------------------
# Search through all tasks
# ---------------------------------------------------------

# আমরা tasks list-এর প্রতিটি Task check করব।
#
# Example:
#
# প্রথমবার:
#     task["id"] = 1
#
# দ্বিতীয়বার:
#     task["id"] = 2
#
# তৃতীয়বার:
#     task["id"] = 3
#
# যখন ID 2 পাওয়া যাবে তখন আমরা সেই Task-এর
# status পরিবর্তন করব।
for task in tasks:

    # বর্তমান Task-এর ID কি target ID-এর সমান?
    #
    # Example:
    #
    #     1 == 2 → False
    #     2 == 2 → True
    #
    # যখন True হবে, তখন আমরা বুঝব যে আমাদের
    # প্রয়োজনীয় Task পাওয়া গেছে।
    if task["id"] == target_task_id:

        # Task পাওয়া গেছে।
        #
        # এখন dictionary-এর "status" key-এর value
        # পরিবর্তন করছি।
        #
        # আগে:
        #
        #     "status": "PENDING"
        #
        # পরে:
        #
        #     "status": "DOWNLOADING"
        task["status"] = "DOWNLOADING"

        # Task পাওয়া গেছে এবং update হয়ে গেছে।
        #
        # তাই আর অন্য Task search করার দরকার নেই।
        #
        # break loop-টি immediately বন্ধ করে দেবে।
        break


# =========================================================
# STEP 4 — DISPLAY TASKS AFTER UPDATE
# =========================================================

print("\n========== AFTER UPDATE ==========")


# আবার সব Task-এর উপর loop করছি।
#
# এবার আমরা দেখতে পাব যে Task ID 2-এর
# status পরিবর্তন হয়েছে।
for task in tasks:

    print(
        f"ID: {task['id']} | "
        f"Name: {task['name']} | "
        f"Status: {task['status']}"
    )