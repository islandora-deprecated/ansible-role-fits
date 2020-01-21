Ansible Role: FITS
==================

![GitHub](https://img.shields.io/github/license/nycrecords/ansible-role-fits)
[![Build Status](https://travis-ci.com/nycrecords/ansible-role-fits.svg?branch=master)](https://travis-ci.com/nycrecords/ansible-role-fits)
[![Galaxy](https://img.shields.io/badge/galaxy-nycrecords.fits-blue.svg)](https://galaxy.ansible.com/nycrecords/fits)
![Ansible](https://img.shields.io/ansible/role/d/90497)
![Ansible](https://img.shields.io/ansible/quality/90497)

An Ansible role that installs [FITS](https://projects.iq.harvard.edu/fits) on:

* Centos/RHEL 7.x
* Ubuntu Xenial

Role Variables
--------------

Available variables are listed below, along with default values:

Version of FITS to install:

    fits_version: 1.1.1

Where to install FITS:

    fits_install_root: /opt


What to call the symlink created from above directory:

    fits_install_symlink: /opt/fits

User/group to install as:

    fits_user: tomcat
    fits_group: tomcat

Dependencies
------------

* nycrecords.java
  
Example Playbook
----------------

    - hosts: webservers
      roles:
        - { role: nycrecords.fits }

License
--------------

MIT