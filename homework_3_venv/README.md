# Virtual environment research

This research on virtual environments by Michael Ghoul. The article is available at doi:10.1111/1000-7 
You can easily reproduce this results by running scripts locally, because i added instructions to his script.

### General Information

OS: Windows 10, 21H2, x64
Python 3.11.0

The repository contains files:

+ `ultraviolence.py` - main script
+ `requirements.txt` - a list of packages required to install and run the script

### How to use

1. Copy this repository to your local PC. For example:

    ```
    git clone <url of repository>
    ```
    
2. Create a virtual environment named `venv ultraviolence`:

    ```
    python3.11 -m venv venv_ultraviolence
    ```

3. Activate the virtual environment with the command:

    ```
    source venv_ultraviolence/bin/activate
    ```

4. Run package installation from `requirements.txt`:

   `Attention! If the requirements.txt is not in the current directory, write the full path to the file.`

    ```
    pip install -r requirements.txt
    ```

5. Go to the folder `\venv_ultraviolence\lib\python3.11\site-packages\pandas\core`
and find `frame.py`. Open the file in any code editor and comment out (recommended) 
or delete 635-636 lines of code:

    ```
    # if index is not None and isinstance(index, set):
        # raise ValueError("index cannot be a set")
    ```
For quick code editing, I recommend using Notepad++. But you can use any code editor.

6. Finally! You can run the script:

   `Attention! If the ultraviolence.py is not in the current directory, write the full path to the file.`

    ```
    python ultraviolence.py
    ```
		
