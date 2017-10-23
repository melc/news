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
- follow the instructions to set up git bash 

### 3. Install Vagrant
- Download vagrant from *https://www.vagrantup.com/downloads*
- Follow the instructions to setup vagrant.  *(Note: if the current version is non-compatiable with your OS,
downgrade the version)*

### 4. Downloard Vagrantfile and Source Codes
- Download from *https://github.com/udacity/fullstack-nanodegree-vm*
- Download source codes from *https://github.com/melc/news*

    ```
    cd fullstack-nanodegree-vm/vagrant
    mkdir news
    cd news
    git clone https://github.com/melc/news
    ```
- Move *newsdata.sql* to *news* folder

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


