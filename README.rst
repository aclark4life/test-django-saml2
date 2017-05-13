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
