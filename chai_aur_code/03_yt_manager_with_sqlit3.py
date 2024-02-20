import sqlite3
con = sqlite3.connect("youtube_video.db")

cursor = con.cursor()

cursor.execute("""
create table if not exists videos (
               id integer primary key,
               name text not null,
               time text not null
)
               """)

def list_videos():
    cursor.execute("SELECT * FROM videos")
    print('*'*70)
    for row in cursor.fetchall():
        print(row)
    print('*'*70)

def add_video(name,time):
    cursor.execute("insert into videos (name ,time) values (? , ?)",(name,time))
    con.commit()

def update_video(video_id,new_name,new_time):
    cursor.execute("update videos set name = ? , time = ? where id=?", (new_name,new_time,video_id))
    con.commit()

def delete_video(video_id):
    cursor.execute("delete from videos where id = ? ",(video_id,))
    con.commit()


def main():
    while True:

        print("\n YOutube manger app with DB")
        print("1. List videos")
        print("2. Add videos")
        print("3. Update videos")
        print("4. Delete videos")
        print("5. Exit app")
        choice = input("Enter your choice :")

        if (choice =='1'):
            list_videos()
        
        elif (choice =='2'):
            name = input("Enter the video name :")
            time = input("Enter the video time :")
            add_video(name,time)

        elif (choice =='3'):
            video_id = input("Enter video Id to update : ")
            name = input("Enter the video name :")
            time = input("Enter the video time :")
            update_video(video_id,name,time)

        elif (choice=='4'):
            video_id = input("Enter video Id to delete : ")
            delete_video(video_id)

        elif (choice=='5'):
            break

        else:
            print('Invalid choice....')

    con.close() 
if __name__ == "__main__":
    main()