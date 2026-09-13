# MSU - CMSE 201 - Fall 2025
This is the CMSE 201 Fall 2025 course content repository for instructors.  Content on the `main` branch is rendered and distributed to a JupyterBook hosted here: [https://msu-cmse-courses.github.io/cmse201-f25-jb](https://msu-cmse-courses.github.io/cmse201-f25-jb).

## Getting started

Clone this git repository to your computer:\
`git clone https://github.com/msu-cmse-courses/cmse201-s25-jb.git`\
this will create a directory called `cmse201-s25-jb` with all of the source files.

If you want to be able to build and publish the html yourself then you may find it useful to create a conda environment:\
`conda create -n cmse201`\
`conda activate cmse201`

and then installing these packages:\
`pip install jupyter-book`\
`pip install ghp-import`

`jupyter-book` commands begin with `jb` and are used to build the static html (in the `_build` folder).  The `ghp-import` package commits the content of the `_build` folder to a special branch of the repo (`gh_pages`) that hosts the JupyterBook on the github.io site.


## To create STUDENT versions of notebooks

`python makeStudentVersion.py name_of_notebook-INSTRUCTOR.ipynb`

This will create a corresponding `name_of_notebook-STUDENT.ipynb` file where
every cell that has "ANSWER" in the first line will be removed. This includes
both code cells _and_ markdown cells.

## Adding a lesson to the main branch

To add a lesson, do the following on your terminal:

1) Make sure you are in the main branch:\
   `git checkout main`
2) Make sure the branch is updated:\
   `git pull origin main`
3) Copy the final versions of all of the files you need into that Day's folder (e.g. Day-02)
4) Create the STUDENT version of the notebook.
5) Update the `_toc.yml` file to uncomment out that day's notebooks and update the filenames if they have changed.
6) Add the notebooks and all of their dependent files and commit locally (don't forget `_toc.yml`!):\
   `git add Day-02/Day-02_Fidget_Spinners_STUDENT.ipynb Day-02/Day-02_Fidget_Spinners_INSTRUCTOR.ipynb Day-02/fidget_spinner.jpg _toc.yml`
7) Commit your work locally:\
   `git commit -m 'day 2 content'`
8) Push to the remote repository:\
   `git push origin main`
9) Publish to the github.io site:\
   `jb build .`\
   `ghp-import -n -p -f _build/html`\
   or alternatively:\
   `./build_and_deploy.sh`
