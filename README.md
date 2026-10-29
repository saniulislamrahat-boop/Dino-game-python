# 🦖 Dino Game Python

A 2D dinosaur running game developed using **Python and Object-Oriented Programming (OOP)**. The project includes dinosaur animations, bird obstacles, trees, sound effects, and graphical assets to create an interactive gaming experience.

This project demonstrates my practical learning in Python programming, object-oriented design, game logic, and software development.

#Project Overview

The Dino Game is inspired by the classic dinosaur runner concept. Players control a dinosaur, avoid obstacles, and attempt to survive as the game progresses.

The project uses separate Python files for game components and asset folders to organize images and sound effects.

**Project name:** Dino Game Python  
**Programming language:** Python  
**Programming approach:** Object-Oriented Programming (OOP)  
**Version control:** Git and GitHub

##Features and Components

- **Dinosaur character:** Includes running and crouching sprite images.
- **Bird obstacles:** Uses bird image assets for flying obstacles.
- **Tree obstacles:** Includes multiple tree images.
- **Sound effects:** Separate audio files for jumping, death, and scoring events.
- **Game graphics:** Includes cloud and ground images.
- **Custom font:** Includes a font file for game text.
- **Modular code organization:** Separates dinosaur, bird, and main game code into different Python files.

#Technologies and Tools

- Python
- Object-Oriented Programming (OOP)
- Git
- GitHub
- Image and audio assets

The exact game framework and external dependencies can be confirmed from the Python source code.

## Object-Oriented Programming (OOP)

OOP helps organize code into classes and objects, making a game easier to maintain and extend.

This project has separate files for the dinosaur, bird, and main game logic. This structure supports organizing different game responsibilities separately.

Important OOP concepts to understand when studying this project:

- **Classes and objects:** Represent game entities and their behavior.
- **Attributes:** Store information about game objects.
- **Methods:** Define actions performed by game objects.
- **Encapsulation:** Keeps related data and behavior organized.
- **Modularity:** Separates components to make the code easier to understand and maintain.

The exact OOP principles implemented depend on the classes and methods defined in the source code.

## 📂 Project Structure

```text
dino game/
│
├── main.py
├── dino.py
├── bird.py
│
├── dino1.png
├── dino2.png
├── dino_crouch1.png
├── dino_crouch2.png
│
├── bird1.png
├── bird2.png
├── cloud.png
├── ground.png
├── font.ttf
│
├── sfx/
│   ├── dead.mp3
│   ├── jump.mp3
│   └── points.mp3
│
├── trees/
│   ├── tree1.png
│   ├── tree2.png
│   ├── tree3.png
│   ├── tree4.png
│   └── tree5.png
│
└── .gitignore
```

**File descriptions:**

| File or folder | Purpose |
|---|---|
| `main.py` | Main game entry point |
| `dino.py` | Dinosaur-related code |
| `bird.py` | Bird-related code |
| `sfx/` | Game sound effects |
| `trees/` | Tree obstacle images |
| `dino*.png` | Dinosaur sprite images |
| `bird*.png` | Bird sprite images |
| `cloud.png` | Cloud graphic |
| `ground.png` | Ground graphic |
| `font.ttf` | Custom font |
| `.gitignore` | Specifies files Git should ignore |

## Requirements

- Python installed on your computer.
- Required Python packages installed.
- All required image, sound, and font assets included in the project.

Check the Python imports in `main.py`, `dino.py`, and `bird.py` to identify the exact dependencies.

## How to Run the Game

### 1. Clone the repository

```bash
git clone https://github.com/saniulislamrahat-boop/Dino-game-python.git
```

### 2. Open the project directory

```bash
cd Dino-game-python
```

### 3. Check your Python installation

```bash
python --version
```

### 4. Install dependencies

Install the external packages required by the project. For example, if the source code uses Pygame:

```bash
pip install pygame
```

If the project requires other packages, install those as well.

### 5. Start the game

```bash
python main.py
```

Keep the image, sound, and font assets in their expected locations so the game can load them correctly.

## 🎮 Gameplay

The project is based on a dinosaur running game. The available assets suggest support for dinosaur animation, crouching, bird obstacles, tree obstacles, and sound effects.

The exact controls, scoring rules, collision behavior, and restart functionality depend on the implementation in `main.py` and the related Python files.

## Learning Outcomes

This project provides an opportunity to practice:

- Python programming.
- Object-Oriented Programming.
- Organizing code into separate modules.
- Working with graphical and audio assets.
- Developing game logic and handling player input.
- Debugging and testing a Python application.
- Using Git and GitHub for version control.



## 👨‍💻 Author

**Md. Sani-Ul Islam**

GitHub: [saniulislamrahat-boop](https://github.com/saniulislamrahat-boop)

## 📦 Repository

[View Dino Game Python on GitHub](https://github.com/saniulislamrahat-boop/Dino-game-python)

## 📜 License

No license has been specified yet. A license can be added later to clarify how others may use, modify, and distribute the project.

---

Thank you for visiting my project! This Dino Game represents my practical journey in learning Python, Object-Oriented Programming, and game development.
