
from models import Coder,session,Contest,CoderProfile,Problem


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
    
    new_coder.contests.append(dev_sprint)
    
    # Add to session and save to DB
    session.add(new_coder)
    session.commit()
    
    print(f"Successfully saved user '{new_coder.username}' registered for '{new_coder.contests[0].name}'!")