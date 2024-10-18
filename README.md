# This is flask application


We can create a virtual environment using two common approaches: `virtualenv` and `python -m venv`. Both methods are widely used, but `python -m venv` is built into Python 3. Let's look at how to create virtual environments using both approaches:

### 1. Using `virtualenv`

**Step 1: Install `virtualenv` (if not already installed)**
```bash
pip install virtualenv
```

**Step 2: Create a virtual environment**
```bash
virtualenv myenv
```
This will create a directory named `myenv` containing the virtual environment files.

**Step 3: Activate the virtual environment**

- **On Windows:**
  ```bash
  myenv\Scripts\activate
  ```

- **On macOS/Linux:**
  ```bash
  source myenv/bin/activate
  ```

**Step 4: Deactivate the virtual environment**
```bash
deactivate
```

---

### 2. Using `python -m venv`

**Step 1: Create a virtual environment**
```bash
python -m venv .venv
```
This creates a virtual environment named `.venv` in the current directory.

**Step 2: Activate the virtual environment**

- **On Windows:**
  ```bash
  .venv\Scripts\activate
  ```

- **On macOS/Linux:**
  ```bash
  source .venv/bin/activate
  ```

**Step 3: Deactivate the virtual environment**
```bash
deactivate
```

---

### Key Differences
- `virtualenv` works across different Python versions and needs to be installed separately via `pip`.
- `venv` is part of Python 3.3+ and doesn't require additional installation.

Both methods provide a similar experience for managing virtual environments.

---
Creating a `requirements.txt` file is simple and is typically done after we've installed the necessary packages in our environment. We can generate it using `pip` to list the installed packages and their versions.

**Generate the `requirements.txt` file**:

   Run the following command to export the installed packages and their versions into the `requirements.txt` file:
   ```bash
   pip freeze > requirements.txt
   ```

This command will create a `requirements.txt` file in your current directory containing a list of all the installed packages along with their versions.

### Example Content of a `requirements.txt`:
```bash
Flask==2.0.3
requests==2.26.0
SQLAlchemy==1.4.27
```

### Customizing the `requirements.txt`:
- You can manually edit the `requirements.txt` file to remove unnecessary packages or specify version constraints (e.g., `requests>=2.20.0`).


---

To install packages listed in a `requirements.txt` file, We can use `pip`, the Python package installer. Here’s how you can do it:

### Steps to Install Packages from `requirements.txt`

1. **Activate the Virtual Environment** (if you're using one)
- **On Windows:**
  ```bash
     .venv\Scripts\activate
  ```
- **On macOS/Linux:**
  ```bash
     source .venv/bin/activate
  ```

2. **Run the pip install command**
   Navigate to the directory where the `requirements.txt` file is located and run the following command:
   ```bash
   pip install -r requirements.txt
   ```

This command will read the `requirements.txt` file and install all the listed dependencies.

<!-- ### Example of a `requirements.txt` File

Here’s an example of how `requirements.txt` might look:
```
Flask==2.0.3
requests==2.26.0
SQLAlchemy==1.4.27
``` -->

### Verifying Installed Packages
After installation, you can verify that the packages are installed by running:
```bash
pip freeze
```
This will display the currently installed packages and their versions in your virtual environment.

---
