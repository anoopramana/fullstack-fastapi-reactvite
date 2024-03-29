This is a base template for a fullstack app using FastAPI in the background and React-Vite  

# Frontend

Step 1:
- Setup front and back end development environments with 
- For Backend: python pip
- For Frontend: NodeJS (has npm and npx)

Step 2:
- Build a frontend and create a react app using npx in new frontend directory using typescript as a template
- npx create-react-app frontend --template typescript 
- May ask to install create-react-app package say yes
- Takes a few mins as it adds ~1500 packages but should only take a few mins
- it also initialises a git repo
- it detects that you want to use typescript and creates a tsconfig.json for you
- Once installed check if it runs: %cd frontend AND THEN %npm start
- Should open local host to port 3000 and show the react icon rotating. 
- This is a development build and is not optimized. (Later for production use %npm run build)

*Modified step 2 as tailwind doesn't support create-react-app fully anymore since there are much better frameworks. 
Vite is one such frmework that is sugegsted. [https://vitejs.dev/guide/] 
-instead of create-react-app use npm to create a vite app in a frontend directory using react-typescript as a template
- %npm create vite@latest frontend -- --template react-ts
- %cd frontend 
- %npm install
- %npm run dev

Step 3:
Set up tailwind CSS for styling tailwindcss.com
- [https://tailwindcss.com/docs/guides/create-react-app]
- in a new terminal cd into frontend
- %npm install -D tailwindcss postcss autoprefixer 
- % npx tailwind init -p
- go through the guide and also delete unnecessary files

Step 4:
- Setup Backend in the main directory
- create a venv and install all dependencies
- make sure you're actually in the venv!
- useful to upgrade pip inside of venv %pip install --upgrade pip
- add packages for backend %pip install fastapi uvicorn pyyaml
- add a .gitignore file and include your venv, node_modules AND __pycache__
- add a requirements for venv %pip freeze > requirements.txt

Cloning my git repo for faster setup next time:
- Copy the url for a repo
- %git clone [URL]
- git checkout [name of branch]
- initiate the venv
- %pip install -r requirements.txt

# Backend
- In home directory create backend folder 
- In this folder create another folder called [appname]
- create an __init.py main.py, database.py, models.py files
- in main.py:
from fastapi import FastAPI
app = FastAPI()
@app.get("/")
async def hello():
    return "Hello from FastAPI"

- in database.py
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///./sqlite.db', connect_args={'check_same_thread': False})

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

- in models.py
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Table
from sqlalchemy.orm import relationship
from .database import Base

class tablename(Base):
    __tablename__= 'tablename'
    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False, unique=True)

Continue with project:
    https://www.youtube.com/watch?v=pG8DCjnhP74&list=PLRuA8IBw6y5WSh5Gc48xJ72YpK5kKA-oL&index=10