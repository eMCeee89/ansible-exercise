# Ansible exercise


## Start

Prerequisites: Ansible and Vagrant installed

Clone git repository and go to the base folder
```
ansible-exam $ ls
playbook.yml  README.md  Vagrantfile
```

Create virtual machine and provision it using Vagrant tool
```
ansible-exam $ vagrant up
Bringing machine 'direct-exam' up with 'virtualbox' provider...
==> direct-exam: Importing base box 'centos/7'...

...

==> direct-exam: Running provisioner: ansible...
    direct-exam: Running ansible-playbook...

...

direct-exam                : ok=4    changed=3    unreachable=0    failed=0
```

As a result you have the running virtual machine with linux CentOS 7 and nginx service
listening on http://10.11.12.13/


## Exam

**Goal**: Following services are running on the machine `direct-exam`:

1. PostgreSQL 10 database server
1. Some REST API micro-service
1. HAProxy
1. Ngingx

Also make some basic security considerations and configure firewall, store passwords using Ansible vault, ...

**Hint**: Organize your Ansible playbook and inventory file using Ansible roles and inventory groups in that way that we can use the same playbook to provision different HW setup (for example imagine that PostgreSQL server is running on one host, backend application instances each on dedicated host and frontend composed from Nginx and HAProxy also on different host.

### 1. PostgreSQL 10 database server

Installation of PostgresSQL in version 10 with some application database and user.

### 2. REST API micro-service

Code some simple RESTful application, for example using Python and Flask, which listens to 2 end-points:

* GET `/health` should return empty result with http status 204
* GET `/pg-settings` should return the result of `select * from pg_settings` query formatted in JSON

Run the application in 2 instances (listening to 2 different ports) as a linux services.

### 3. HAProxy

Balance /api/pg-settings requests evenly between 2 instances of REST API microservice

Also enable HAProxy `stats` page and use `/health` end-point for health check.

### 4. Nginx

Request to http://10.11.12.13/api/pg-settings is proxy passed to HAProxy which passes the request to one instance of the application which connects to the database and returns the JSON response.


## Solution instructions

Hello,

All it needs is to clone the repo, `cd direct-exam-marek-cvoren` into project directory, execute command `VAGRANT_CWD=$(pwd) vagrant up`, sit back and wait till the provisioning is over.

You can then enjoy following endpoints:

* [http://10.11.12.13/api/pg-settings](http://10.11.12.13/api/pg-settings)
* [http://10.11.12.13/stats](http://10.11.12.13/stats)
    * username: direct
    * password: direct-pass


Best regards,  
/Marek
