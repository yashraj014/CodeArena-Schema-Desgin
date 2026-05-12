# from models import User,engine
# from sqlalchemy.orm import sessionmaker
# import random
# from sqlalchemy import or_,not_,and_,func
# Session=sessionmaker(bind=engine)

# session=Session()

# user=User(name="John Doe",age=30)
# user1=User(name="Yash Raj",age=21)
# user2=User(name="Iron Man",age=33)
# user3=User(name="Thor",age=35)


# session.add(user1)
# session.add_all([user2,user3])
# session.commit()

# user= session.query(User).filter_by(id=1).first()
# # user.name="Ram Krishna"
# session.delete(user)
# session.commit()

# for user in users:
#     print(f"id: {user.id} name: {user.name} age: {user.age}")

# names=["Harsh","Aniket","Yash","Prem"]
# ages=[30,25,22,45]

# for x in range(20):
#     user=User(name=random.choice(names),age=random.choice(ages))
#     session.add(user)
    
# session.commit()

# users=session.query(User).order_by(User.age, User.id).all()
# users=session.query(User).filter(not_((User.name=="Yash") | (User.name=="Harsh"))).all()
# users=session.query(User.name,func.count(User.id)).group_by(User.name).all()
# users=(session.query(User.age,func.count(User.id))
#        .filter(User.age>22)
#        .order_by(User.age)
#        .filter(User.age<40)
#        .group_by(User.age)
#        .all()
# )




# # for user in users:
# #     print(f"id:{user.id} name: {user.name} age: {user.age}")
# print(users)

from models import Coder,session,Contest,contest_registration,CoderProfile,Problem


# user1=User(name="Yash",age=21)
# user2=User(name="Aman",age=19)


# address1=Address(city="Patna",state='Bihar',zip_code=801105)
# address2=Address(city="Pune",state="Maharashtra",zip_code=759223)
# address3=Address(city="Anantpur",state="Andhra Pradesh",zip_code=9636363)

# user1.addresses.extend([address1,address3])
# user2.addresses.append(address2)

# session.add(user1)
# session.add(user2)
# session.commit()

# print(user1)
# print(user2)

# print(f"{user1.addresses}")
# print(f"{user2.addresses}")
# print(f"{address1.user}")

# --- TEST SCRIPT ---
if __name__ == "__main__":
    # 1. Create a Coder and their Profile simultaneously (One-to-One test)
    new_coder = Coder(
        username="algo_master", 
        password="securepassword123",
        profile=CoderProfile(
            current_rating=1850, 
            global_rank=402, 
            favourite_language="C++"
        )
    )
    
    # 2. Create a Contest with Problems (One-to-Many test)
    dev_sprint = Contest(
        name="Weekly DevSprint 101",
        problems=[
            Problem(title="A - Two Sum Advanced"),
            Problem(title="B - Dynamic Grid Paths"),
            Problem(title="C - Tree Inversion")
        ]
    )
    
    # 3. Register the Coder for the Contest (Many-to-Many test)
    # Because of our relationships, appending the object handles the bridging automatically!
    new_coder.contests.append(dev_sprint)
    
    # Add to session and save to DB
    session.add(new_coder)
    session.commit()
    
    print(f"Successfully saved user '{new_coder.username}' registered for '{new_coder.contests[0].name}'!")