Django SAML Test
================

*RHEL 7 on AWS*

selinux
-------

::

    [ec2-user@ip-172-30-2-147 ~]$ cat /etc/selinux/config 

    # This file controls the state of SELinux on the system.
    # SELINUX= can take one of these three values:
    #     enforcing - SELinux security policy is enforced.
    #     permissive - SELinux prints warnings instead of enforcing.
    #     disabled - No SELinux policy is loaded.
    SELINUX=permissive
    # SELINUXTYPE= can take one of three two values:
    #     targeted - Targeted processes are protected,
    #     minimum - Modification of targeted policy. Only selected processes are protected. 
    #     mls - Multi Level Security protection.
    SELINUXTYPE=targeted

RHEL 7
------

::

    sudo yum groupinstall "Development Tools"
    sudo yum install httpd
    sudo yum install mod_wsgi
    sudo yum install git
    sudo yum install python2-pip python-virtualenv

    # Certbot requires epel repo & zope interface RPM from vendor/
    rpm -Uvh python-zope-interface-4.0.5-4.el7.x86_64.rpm 
    sudo yum install python2-certbot-apache certbot

    sudo yum install libjpeg-devel
    sudo yum install screen
    sudo yum install swig
    sudo yum install libffi-devel
    sudo yum install openssl-devel

    # xmlsec requires RPMs from vendor/
    sudo rpm -Uvh xmlsec1-1.2.20-5.el7.x86_64.rpm 
    sudo rpm -Uvh xmlsec1-devel-1.2.20-5.el7.x86_64.rpm 
    sudo rpm -Uvh xmlsec1-openssl-1.2.20-5.el7.x86_64.rpm 
    sudo rpm -Uvh xmlsec1-openssl-devel-1.2.20-5.el7.x86_64.rpm 

Apache
------

::

    …

    WSGIScriptAlias / /srv/django-saml-test/project/wsgi.py
    <Directory /srv/django-saml-test/project>
            <Files wsgi.py>
                    Require all granted
            </Files>
    </Directory>
    </VirtualHost>

    WSGIPythonHome /srv/django-saml-test
    WSGIPythonPath /srv/django-saml-test

python-saml
-----------

- https://github.com/onelogin/python-saml/issues/30
