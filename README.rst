Django SAML Test
================

*RHEL 7 on AWS*

src/dj-saml-idp/project/keys
----------------------------

- http://stackoverflow.com/a/14464908/185820


RHEL 7
------

::

    sudo yum groupinstall "Development Tools"
    sudo yum install httpd
    sudo yum install mod_wsgi
    sudo yum install git
    sudo yum install python2-pip python-virtualenv

    # Requires epel & zope interface from vendor/
    sudo yum install python2-certbot-apache certbot

    sudo yum install libjpeg-devel
    sudo yum install screen
    sudo yum install swig
    sudo yum install libffi-devel
    sudo yum install openssl-devel


Apache
------

::

    WSGIScriptAlias / /path/to/mysite.com/mysite/wsgi.py
    WSGIPythonHome /path/to/venv
    WSGIPythonPath /path/to/mysite.com

    <Directory /path/to/mysite.com/mysite>
    <Files wsgi.py>
    Require all granted
    </Files>
    </Directory>
