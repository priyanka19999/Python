from pymongo import MongoClient
from bson import ObjectId
client = MongoClient("mongodb+srv://<db_id>:<db_password>@youtube.ygp3hfz.mongodb.net/", tlsAllowInvalidCertificates=True)

# Note a good idea to include id and password in code files
#tlsAllowInvalidCertificates=True - not a good way to handle ssl
print(client)
db = client["ytmanager"] # Create a database named ytmanager from the MongoDB client.

video_collection = db["videos"]

print(video_collection)


def list_videos():
    for video in video_collection.find():
        print(f"ID: {video['_id']}, Name: {video['name']} and Time = {video['time']}")
        
def add_videos(name, time):
    video_collection.insert_one({"name": name, "time": time})
    
def update_videos(new_name, new_time, video_id):
    video_collection.update_one(
        {'_id': ObjectId(video_id)},
        {"$set":{"name":new_name, "time": new_time }}
        )
def delete_videos(video_id):
    video_collection.delete_one({"_id": ObjectId(video_id)})

def main():
    while True:
      print("\n Youtube Manger App") 
      print("1. list all videos")
      print("2. Add a new videos") 
      print("3. Update videos") 
      print("4. Delete videos") 
      print("5. Exit the app")  
      choice = input("Enter Your Choice: ")
      
      if choice == "1":
          list_videos()
      elif choice == '2':
          name = input("Enter the video name: ")
          time = input("Enter the video time: ")
          add_videos(name, time)
      elif choice == '3':
        video_id = input("Enter the video id to update: ")
        name = input("Enter the update video name: ")
        time = input("Enter the update video time: ")
        update_videos(name, time,video_id)    
      elif choice == '4':
        video_id = input("Enter the video id to update: ")
        delete_videos(video_id)
      elif choice == '5':
          break
      else:
          print("Invalid Choice Entered")
        

if __name__ == "__main__":
    main()