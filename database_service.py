import harperdb

# url is our harperdb cloud's website which I've created.
url = 'https://cloud-1-dataman.harperdbcloud.com'

# our username
username = 'shubhamu'          
# password set 
password = "shubham123"

# creating a db variable where I'll get the database information
db = harperdb.HarperDB(
    url = url,
    password = password,
    username = username
)

#to check weather out database is working or not
# print(db.describe_all())  

# Database
SCHEMA = 'workout_repo'
# Tables
TABLE = 'workouts'
TABLE_TODAY = 'workout_today'

# creating a function to insert workout_data
def insert_workout(workout_data):
    return db.insert(SCHEMA, TABLE, [workout_data])

# creating a function to delete a workout_id
def delete_workout(workout_id):
    return db.delete(SCHEMA, TABLE, [workout_id])

# creating a SQL function to get all workout information
def get_all_workouts():
    try:
        return db.sql(f"select video_id,channel,title,duration from {SCHEMA}.{TABLE}")
    except harperdb.exceptions.HarperDBError:
        return []

# creating a SQL get all function to get today's workout information
def get_workout_today():
    return db.sql(f"select * from {SCHEMA}.{TABLE_TODAY} where id = 0")


# creating a function to update today's workout information
def update_workout_today(workout_data, insert = False):
    workout_data['id'] = 0
    if insert:
        return db.insert(SCHEMA, TABLE_TODAY, [workout_data])
    return db.update(SCHEMA, TABLE_TODAY, [workout_data])