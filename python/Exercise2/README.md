## Person and Person Factory Unit
This project defines two main classes:
- **`Person`**: Represents a person with a name and date of birth
- **`PersonFactory`**: Manages a collection of `Person` objects, allowing creating of random people
    filtering by name and age, and generating "married names""
The code has been **refactored** to:
- use **pydantic** model for data vlidation and strict data model
- Add **logging** for debugging and tracking
- Fix indentified bugs(e.g. inverted age comparison logic)
- use better class and method names for more clarity
- Provide reproducible results via optional **random seed**
- include a main file for a entry point and a quick manual testing

## 🚀 Getting Started Follow these instructions to set up and run the project

### **1. Prerequisites** 
* **Python 3.8** or newer. You can download it from [python.org](https://www.python.org/downloads/).

### **2. Setup Instructions**
1. **Clone or Download the Code**
    clone the code https://github.com/niraj11k/CodingAssessment2025.07.git
    Create a new folder for the project and place the following two files inside it:
        * `codeToRefactor.py` 
        * `codeToRefactor-test.py`
2. **requirements.txt file**
    Check in the same folder, if you already have `requirements.txt` file.
    If not, create a new file named `requirements.txt` and add the following line to it. This file lists all the necessary Python packages for the project. 
    ``` pydantic ```
3. **Create and Activate a Virtual Environment (Recommended)**
    It's highly recommended to use a virtual environment to keep project dependencies isolated.
    Open your terminal or command prompt in the project folder and run:
    ```bash 
    # Create the virtual environment 
    python -m venv venv
    # Activate it
        # On Windows:
        .\venv\Scripts\activate
        # On macOS/Linux:
        source venv/bin/activate
        ```
4. **Install Dependencies**
    With your virtual environment active, install the required packages using the `requirements.txt` file:
    ```bash 
    ``pip install -r requirements.txt`
    
5. **Running the Tests**
    To verify everything is working correctly, you can run the automated test suite.
    In your terminal, with the virtual environment activated and form the Excercise2 directory, 
    run the following command in verbose mode to see the outout for each test:
    ```bash```
    `pytest -v` --> run test in verbose mode

6. **Running main.py**
    To see how the code will output, you can run the main.py.
    In your terminal, with the virtual environment activated and from the Excercise2 directory,
    run the following command to see the output with dummy data
    ```bash```
    `python main.py`





