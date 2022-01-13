# New Beginings API Server 
    This system provides api to create , edit , delete and retirve users information.
    new_beginings.yaml is the swagger API schema defined in the root folder of the project. 
## Requirement: 
* Python3.9
* Pip of python 3.9  ( python3.9 get-pip.py  - Linux command )

## Installation :
* change to root folder of project 
* pip3 install virtualenv ( command to install virutalenv)
* setup.sh  ( sets up the server environment)
* start.sh ( starts the server )

API server accessible with  http://localhost:8080/ 

## How to run functional test cases ? 
 * start.sh ( start the server in a terminal) 
 * source virtualenv/bin/activate
 * python3.9 -m test.api_test

## How to run unit test cases? 
 * source virtualenv/bin/activate
 * python3.9 -m  unittest
 


