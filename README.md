# News Reporting Tool
News Reporting Tool app is a micro data analysis app for news feed with python flask and postgresql deploying on
ubuntu 16.04 LTS hosted on vagrant virtual machine (VM)

## Technical Features

include:

- Python 3.5
- Flask Framework
- Postgresql
- Virtualbox and Vagrant

## Functional Features

1. What are the most popular three articles of all time?
2. Who are the most popular article authors of all time?
3. On which days did more than 1% of requests lead to errors?

## Steps of Launching News Reporting Tool
### 1. Install Virtualbox
- Download virtual box from *https://www.virtualbox.org/wiki/Download_Old_Builds_5_1*
- Follow the instructions to setup virtualbox

### 2. Install Git
- Download git from *https://git-scm.com/downloads*
- Follow the instructions to set up git bash 

### 3. Install Vagrant
- Download the old version of vagrant from *https://www.vagrantup.com/downloads* 
if the current version is non-compatible with your OS
- Follow the instructions to setup vagrant.  

### 4. Download Datafile, Vagrantfile, and Source Codes
- Download vagrantfile from *https://github.com/udacity/fullstack-nanodegree-vm*
- Download newsdata.zip from 
*https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip*
- Git clone from *https://github.com/melc/news*

    ```
    cd fullstack-nanodegree-vm/vagrant
    mkdir news
    cd news
    git clone https://github.com/melc/news
    ```
- Unzip newsdata.zip and move *newsdata.sql* to *news* folder

### 5. Start the Virtual Machine
- Install ubuntu 16.04 LTS on VM

    ```
    cd vagrant/
    vagrant up
    ```
- Login to installed ubuntu VM

    `vagrant ssh`     *(note: $ will be changed to vagrant@vagrant:~$)*

### 6. Launch the Application
- Create database *news*

    ```
    cd vagrant/news
    psql -d news -f newsdata.sql
    ```
- Launch application.py

    `python3.5 application.py`

- Open browser and type in `localhost:8000` 
