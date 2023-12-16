---
title: Loading the React Component, using Storybook
reviewers: Danny Cowen
---

In this section, we will create a demo of the fully interactive React component on your local machine. We use Storybook as a shell
in which to load the React component.

# Setting up your first React app

When using React, it is best practice to also use a software called Node.js. Node.js enables React apps to communicate with the server, which means that complex operations that lie outside of frontend development are dealt with seamlessly. 

We will now walk you through installing Node.js. Best practice is again to install a program called Node Version Manager, or nvm for short. nvm allows the user to switch between different versions of Node.js, which is important because different React apps may require different versions of Node.js to run as intended. Therefore, nvm is an important tool to use whenever using React!

!!! tip "nvm installation"
    The Github page for nvm is where these instructions have been written from. It offers more in-depth troubleshooting, but for the sake of simplicity, we will list the essential instructions for nvm installation.
    Reference: https://github.com/nvm-sh/nvm

# Installing nvm

1. ###Run the following install script:
```console
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.5/install.sh | bash
```
You now should have a hidden repository, accessible at `~/.nvm`

1. ###Check the install worked:
```console
open ~/.zshrc
```
Execute the above command in your Terminal. This should place you in a file used by your Terminal to execute commands, known as the Shell file.
    
    !!! warning 
        If you use bash as your shell, you may need to substitute `~/.zshrc` for `~/.bashrc` or `~./bash_profile`. Again, the nvm Github page has more specific troubleshooting for this.

1. ###Troubleshooting the shell (`~/.zshrc`, `~/.bashrc` etc.) file:
You should see the following script somewhere in your shell file:
```console
export NVM_DIR="$([ -z "${XDG_CONFIG_HOME-}" ] && printf %s "${HOME}/.nvm" || printf %s "${XDG_CONFIG_HOME}/nvm")"
[ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh" # This loads nvm
```
If it isn't there, copy the above script and paste it in the shell file. Then, execute the following command to save your changes (replace `~/.zshrc` with whichever shell file you use):
```console
source ~/.zshrc
```

1. ###Checking the install worked:
Make sure that you close the Terminal, and reopen it. You should now be able to type the following command, and receive a version number back:
```console
nvm -v
```

1. ###Installing Node.js via nvm:
For macOS/Linux users:
```console
nvm install --lts
```
For Windows users:
```console
nvm install lts
```

    !!! tip "LTS"
        'lts' stands for long-term support. This means that the developers of the software will commit to maintaining a stable release of that version, so you know it will be supported throughout your usage of it.
    

# Installing the React component

In order to load the React component, you must open a new Terminal (MacOS)/Command Prompt (Windows) in your code projects directory:

```console
cd /User/YourCodeProjectsDirectory
```

Then, clone the remote repository from Github, in order to locally install the React component:
```console
git clone https://github.com/rcpch/digital-growth-charts-react-component-library.git
```

Move into the directory containing your new local repository:
```console
cd digital-growth-charts-react-component-library
```

Github uses branches in order for developers to deploy and maintain stable software. Enter the following command in your Terminal to
begin working with the code approved for Storybook use:

```console
git checkout storybook-live
```

You have now completed the part of this tutorial dedicated to using Git!

# Running the React component in Storybook

1. ###Install package dependencies:
```console
npm install
```
This ensures that the dependencies of the React component (as specified in package.json) are installed prior to running

1. ###Opening Storybook:
```console
npm run storybook
```
This should load a development server in your Terminal/Command Prompt. Copy the url, and paste it into your browser to interact with your new React component!

!!! warning "Storybook in Safari"
    Storybook may run into errors when using Safari. The RCPCH Incubator Team advise using a different browser, such as Google Chrome, to enable full functionality of the software. 
    