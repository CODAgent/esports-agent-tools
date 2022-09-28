# <a id="home">Esports Agent Inc. Tools</a>

Here are some tools that we use to help us out.

**[New users click here.](#setup)**

**[Returning users click here.](#aftersetup)**

---

## <a id="alltools">Tools we have</a>
- [CODAgent tourney analyzer](https://github.com/CODAgent/esports-agent-tools/tree/master/codagent/)

---

## <a id="setup">How to get setup</a>

### <a id="github">GitHub Account</a>

Now would just be a good time to make sure you have a GitHub account.  If you do, log in.  If you do not, make one.  DM [LonelyDock3](https://twitter.com/lonelydock3) on Twitter to have him add you to the CODAgent organization.


### <a id="python">Install Python</a>

Make sure you have python installed.  Preferably Python 3.  If you do not have python installed, you can search for a tutorial on "How to download Python" or you can download it [here](https://www.python.org/downloads/).

### <a id="clonerepo">Clone this repository</a>

1. In your file explorer or whatever you use to access your files, make a folder wherever you want called "AgentTools".  Copy the file path of this folder.
    - To do this you can hold the SHIFT key and right click on the folder.  Then select the option "Copy as path".

2. Open a terminal of your choice.
    - If you're Windows, you can use: 
        - cmd
        - PowerShell
        - Windows Terminal 
        - Bash
    - I believe Mac and Linux have their own respective terminals.

3. cd to the folder you made in your file explorer.
    - To do this type the word "cd" into your terminal, then a space, and then paste the path that you copied in step 1.  It should look like this in the terminal:
        
        ```
        cd the-path-you-copied
        ```

    Keep this terminal open and go back to your internet browser.

4. On [this page](https://github.com/CODAgent/esports-agent-tools) you should be able to see a green button on the top right of your screen that says "Code".  Click this button.

5. On this drop down, make sure you're on the "HTTPS" tab.  Copy the URL that is shown here.

6. Go back to your terminal window and type the following into the terminal and hit enter:

    ```
    git clone paste-the-URL-you-just-copied-here
    ```

7. After this, cd into the codebase by typing the following into your terminal and hitting enter:

    ```
    cd esports-agent-tools
    ```

This should clone the repository in the folder you created in step 1.  Contact [LonelyDock3](https://twitter.com/lonelydock3) if you have issues.

### <a id="createbranch">Create your own branch</a>

1. To check what branch you are on, type the following into your terminal and hit enter:

    ```
    git branch
    ```
    
    This will show all of the branches you have and there will be an asterick, \*, next to the branch you are currently on.  If you have not created any branches, it should say "\* master", which means your are currently on the master branch.

2. You should create your own branch to use the tools.  To do so, type the following into your terminal and hit enter (you can name the branch whatever you want, just remember the name):

    ```
    git checkout -b your-branch-name
    ```

3. Do step 1 again to see what branch you are currently on.  If you are on your branch, then proceed to step 4.  If you are still on the master branch, type the following to switch to your branch:

    ```
    git checkout your-branch-name
    ```

4. From here, you should push the branch so it is connected to the remote repository.  Type this into your terminal and then hit enter: 

    ```
    git push -u origin your-branch-name
    ```

Now you should have your branch setup and you should have your branch selected.

### <a id="setupenv">(Optional, but recommended) Setup your own environment</a>

1. In your terminal, type the following and hit enter: 

    ```
    pip3 install virtualenv
    ```

    OR

    ```
    pip install virutalenv
    ```

2. Create your virtual environment by typing this (you can call the environment whatever you want, but make sure it ends with "\_env":

    ```
    python3 -m venv your-virtual-environment-name_env
    ```

    OR

    ```
    python -m venv your-virtual-environment-name_env
    ```

Now your virtual environment is setup.  Make sure to activate it when you are going to use the tools (see how on step 1 [here](#aftersetup)).

### <a id="updatebranch">Update your branch to any of the latest changes made</a>

1. Make sure you are on the **master** branch:
    
    ```
    git branch
    ```

    - If you are then proceed to step 2.  If not:

        ```
        git checkout master 
        ```
        
        Then proceed to step 2.

2. Do a git pull:

    ```
    git pull
    ```

3. Go to your branch: 

    ```
    git checkout your-branch-name
    ```

4. Do a git pull:

    ```
    git pull
    ```

5. Merge the master branch into yours:

    ```
    git merge master
    ```

This should update your branch with any updated code or data.  If you run into any issues, contact [LonelyDock3](https://twitter.com/lonelydock3).

---

## <a id="aftersetup">After setup steps</a>

If you have already setup your files for the first time, then follow these steps whenever you are looking to use one of these tools: 

1. Activate your environment (if not already active).
    - If on Windows, type this into your terminal:

        ```
        your-environment-folder-name/Scripts/activate.bat
        ```

        - Make sure your terminal is cd'ed to the folder right before your environment folder
        - If you are using PowerShell, type this instead:
            
            ```
            your-environment-folder-name/Scripts/Activate.ps1
            ```

    - If on Mac or Linux, type this into your terminal: 

        ```
        source your-environment-folder-name/bin/activate
        ```

        - Make sure your terminal is cd'ed to the folder right before your environment folder


2. Update your local repository and branch to the latest changes of this remote repository by following the steps [here](#updatebranch).

3. Use the [tools](#alltools)!

**NOTE:** If you have any issues reach out to the developer - [LonelyDock3](https://twitter.com/lonelydock3)


