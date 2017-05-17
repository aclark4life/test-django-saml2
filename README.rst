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

OneLogin SAMLResponse
---------------------

::

    <samlp:Response xmlns:saml="urn:oasis:names:tc:SAML:2.0:assertion"
                    xmlns:samlp="urn:oasis:names:tc:SAML:2.0:protocol"
                    ID="R7160360b378fef81d99fa54c6e0a4aa5c9c1a015"
                    Version="2.0"
                    IssueInstant="2017-05-16T23:34:33Z"
                    Destination="{recipient}"
                    >
        <saml:Issuer>https://app.onelogin.com/saml/metadata/658891</saml:Issuer>
        <samlp:Status>
            <samlp:StatusCode Value="urn:oasis:names:tc:SAML:2.0:status:Success" />
        </samlp:Status>
        <saml:Assertion xmlns:saml="urn:oasis:names:tc:SAML:2.0:assertion"
                        xmlns:xs="http://www.w3.org/2001/XMLSchema"
                        xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
                        Version="2.0"
                        ID="pfx89aab9e8-af3e-ace9-97b6-c1086f076d7a"
                        IssueInstant="2017-05-16T23:34:33Z"
                        >
            <saml:Issuer>https://app.onelogin.com/saml/metadata/658891</saml:Issuer>
            <ds:Signature xmlns:ds="http://www.w3.org/2000/09/xmldsig#">
                <ds:SignedInfo>
                    <ds:CanonicalizationMethod Algorithm="http://www.w3.org/2001/10/xml-exc-c14n#" />
                    <ds:SignatureMethod Algorithm="http://www.w3.org/2000/09/xmldsig#rsa-sha1" />
                    <ds:Reference URI="#pfx89aab9e8-af3e-ace9-97b6-c1086f076d7a">
                        <ds:Transforms>
                            <ds:Transform Algorithm="http://www.w3.org/2000/09/xmldsig#enveloped-signature" />
                            <ds:Transform Algorithm="http://www.w3.org/2001/10/xml-exc-c14n#" />
                        </ds:Transforms>
                        <ds:DigestMethod Algorithm="http://www.w3.org/2000/09/xmldsig#sha1" />
                        <ds:DigestValue>SQDekGp/Ibp90eC3O5dwu37ZdJA=</ds:DigestValue>
                    </ds:Reference>
                </ds:SignedInfo>
                <ds:SignatureValue>BvY9Q7tHhiZSEuSuK4XrQ9Bqm8ItdG8I3mZbMvPYb8SmM9OrOVa5+jD05nn528jk+Zzbg6jSBKFplz1mlXnXJKeaJTBDVcV8nVnzojaj6P+WgUNOivl+oVh86mhy7+xQVpiPwHvz2PLwKP4vGW8YlWShoWMQCbqyDnGD4qAU94l1RRCQ8TvuD+qHyqQhuQK3T26dXTh/W04oB8WIQv6k//07dwF5zNRb/I5BZ/dtTZR8rr+cJG441+DFIc+4uQ3h9q3IHE0kSl7TQUky7akOdRnvB1ZZx8IhRdM7e7EvJYL+bbSrgizi18pPt4UMk+s2+NkNaK/ADvGQXEvVaaoYVw==</ds:SignatureValue>
                <ds:KeyInfo>
                    <ds:X509Data>
                        <ds:X509Certificate>MIIEHTCCAwWgAwIBAgIUGM9vFCkZxTmjpgMg4m3sqHXseiAwDQYJKoZIhvcNAQEFBQAwWjELMAkGA1UEBhMCVVMxEjAQBgNVBAoMCUFDTEFSS05FVDEVMBMGA1UECwwMT25lTG9naW4gSWRQMSAwHgYDVQQDDBdPbmVMb2dpbiBBY2NvdW50IDEwNjgwMzAeFw0xNzA1MTUyMjI0NTNaFw0yMjA1MTYyMjI0NTNaMFoxCzAJBgNVBAYTAlVTMRIwEAYDVQQKDAlBQ0xBUktORVQxFTATBgNVBAsMDE9uZUxvZ2luIElkUDEgMB4GA1UEAwwXT25lTG9naW4gQWNjb3VudCAxMDY4MDMwggEiMA0GCSqGSIb3DQEBAQUAA4IBDwAwggEKAoIBAQDIgZRhLBwDK4MjQ8+d7KrDQ9wJif1kcvbRhmWjoBiapjPrx+LLIWlzeZy2IjHHvEG9n+FbWgRHgs8V+uPcgjiwiQBFt7nDx3bcyvcAjv8h8FPWNoLRuHPX8uJdwJ4BLFLCe5ADalgNzU0+QTiREJYqqv43snTgovTxcGmEUSi5tAsV5s3JYV0m9UlfNnwRBkMSvTCMh2HhEyqK5ETdifXLp1WLWtEqUlMAf+4QYCWBSswjKlciF0/BWIziaZjLwfDe2fbfulcQDsFkw5f7clqka8P1kxxZSTWqCuIVx+yyV+AC5vRYVmY9s5YPKFtaMMi8Vn64NpMCw1z44cK8ct8tAgMBAAGjgdowgdcwDAYDVR0TAQH/BAIwADAdBgNVHQ4EFgQUpSE3UpRUUob9RTyGkfOZpd5lqqIwgZcGA1UdIwSBjzCBjIAUpSE3UpRUUob9RTyGkfOZpd5lqqKhXqRcMFoxCzAJBgNVBAYTAlVTMRIwEAYDVQQKDAlBQ0xBUktORVQxFTATBgNVBAsMDE9uZUxvZ2luIElkUDEgMB4GA1UEAwwXT25lTG9naW4gQWNjb3VudCAxMDY4MDOCFBjPbxQpGcU5o6YDIOJt7Kh17HogMA4GA1UdDwEB/wQEAwIHgDANBgkqhkiG9w0BAQUFAAOCAQEAgUxGgSjpCiacIyXSU41nI6K+b02zhEJVeQV4QR1IESADpQXSSgDMmMJtaOijNrZ5n8WTb8CE0N6egA9VX5ff3hSXTLHqzgdGNHOxK2+gV0jUACs55k9ROJxNEs+GmY9iIwy0weljssHdiHDuoczk27pnbgz+dQo0jDo9P1vfQQZjhe3F7EsPNfdJDyYOrl6ysDetC/rnrHQaH14hld6nkTVIjtohx8qyu2Q2vqvd1ScD9PKTs1HBh2mEsWb+CYohMXZmD19qWjbzeEc1nbQM5BKp/WhAKi8a2SxkAB8eYy21oqgChCK/5fUocsOICVfaHT+BdhV6xz94FspUuBYf4g==</ds:X509Certificate>
                    </ds:X509Data>
                </ds:KeyInfo>
            </ds:Signature>
            <saml:Subject>
                <saml:NameID Format="urn:oasis:names:tc:SAML:2.0:nameid-format:transient">aclark@aclark.net</saml:NameID>
                <saml:SubjectConfirmation Method="urn:oasis:names:tc:SAML:2.0:cm:bearer">
                    <saml:SubjectConfirmationData NotOnOrAfter="2017-05-16T23:37:33Z"
                                                  Recipient="{recipient}"
                                                  />
                </saml:SubjectConfirmation>
            </saml:Subject>
            <saml:Conditions NotBefore="2017-05-16T23:31:33Z"
                             NotOnOrAfter="2017-05-16T23:37:33Z"
                             >
                <saml:AudienceRestriction>
                    <saml:Audience/>
                </saml:AudienceRestriction>
            </saml:Conditions>
            <saml:AuthnStatement AuthnInstant="2017-05-16T23:34:32Z"
                                 SessionNotOnOrAfter="2017-05-17T23:34:33Z"
                                 SessionIndex="_b49f0e60-1cbb-0135-39ae-06cb00433bb7"
                                 >
                <saml:AuthnContext>
                    <saml:AuthnContextClassRef>urn:oasis:names:tc:SAML:2.0:ac:classes:PasswordProtectedTransport</saml:AuthnContextClassRef>
                </saml:AuthnContext>
            </saml:AuthnStatement>
        </saml:Assertion>
    </samlp:Response>

dj-saml-idp SAMLResponse
------------------------

::



    <samlp:Response xmlns:saml="urn:oasis:names:tc:SAML:2.0:assertion"
                    xmlns:samlp="urn:oasis:names:tc:SAML:2.0:protocol"
                    ID="_c78b84ed289d4c75b0efc3c6ee851ecd"
                    Version="2.0"
                    IssueInstant="2017-05-17T02:03:46Z"
                    Destination="https://aclark.myabsorb.com/account/saml"
                    >
        <saml:Issuer>https://dj-saml-idp.aclark.net</saml:Issuer>
        <samlp:Status>
            <samlp:StatusCode Value="urn:oasis:names:tc:SAML:2.0:status:Success" />
        </samlp:Status>
        <saml:Assertion xmlns:saml="urn:oasis:names:tc:SAML:2.0:assertion"
                        xmlns:xs="http://www.w3.org/2001/XMLSchema"
                        xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
                        Version="2.0"
                        ID="_ece9584fc7f84f37aa58bdc190e850b1"
                        IssueInstant="2017-05-17T02:03:46Z"
                        >
            <saml:Issuer>https://dj-saml-idp.aclark.net</saml:Issuer>
            <ds:Signature xmlns:ds="http://www.w3.org/2000/09/xmldsig#">
                <ds:SignedInfo>
                    <ds:CanonicalizationMethod Algorithm="http://www.w3.org/2001/10/xml-exc-c14n#" />
                    <ds:SignatureMethod Algorithm="http://www.w3.org/2000/09/xmldsig#rsa-sha1" />
                    <ds:Reference URI="#_ece9584fc7f84f37aa58bdc190e850b1">
                        <ds:Transforms>
                            <ds:Transform Algorithm="http://www.w3.org/2000/09/xmldsig#enveloped-signature" />
                            <ds:Transform Algorithm="http://www.w3.org/2001/10/xml-exc-c14n#">
                                <InclusiveNamespaces PrefixList="#default saml ds xs xsi"
                                                     xmlns="http://www.w3.org/2001/10/xml-exc-c14n#"
                                                     />
                            </ds:Transform>
                        </ds:Transforms>
                        <ds:DigestMethod Algorithm="http://www.w3.org/2000/09/xmldsig#sha1" />
                        <ds:DigestValue>hFNu4boa2CT1Y8O+AjrrSz18HtA=</ds:DigestValue>
                    </ds:Reference>
                </ds:SignedInfo>
                <ds:SignatureValue>sEljZ+JhzLpWZWUpfCYEFvZ+diPcstow7ynZYC0d9n27YjT3ieoTabTp8A9B+UojSaGAESD1RcWg1ALkcEkO94GSC3fqCKQSreHPlXmaP7TokF1ukhAdZu9UVL7okMc7E4SSeyt47ee0Eq4NASNDnh9uCrq/bCd9XTnNzb6/Av1GG59dRbHPMs4Saqy+UqCiDYeGy6Cja7WnP+eeQR6l/XONMcCEOdaPl4FHyU3QAQwgG3UhDXkmVgOVdyYlh4LMohHzBBa3WGBTm2hanPZBovveDAaF16S7ftMIUSvCNWSKdD0VS6qbCJw81HVn//e+OPUIBx0bmcgVk/wgvZDEZdk=</ds:SignatureValue>
                <ds:KeyInfo>
                    <ds:X509Data>
                        <ds:X509Certificate>MIIDZTCCAkygAwIBAgIBADANBgkqhkiG9w0BAQ0FADBMMQswCQYDVQQGEwJ1czELMAkGA1UECAwCTUQxDzANBgNVBAoMBkFDTEFSSzEfMB0GA1UEAwwWZGotc2FtbC1pZHAuYWNsYXJrLm5ldDAeFw0xNzA1MTcwMDM4MzJaFw0xODA1MTcwMDM4MzJaMEwxCzAJBgNVBAYTAnVzMQswCQYDVQQIDAJNRDEPMA0GA1UECgwGQUNMQVJLMR8wHQYDVQQDDBZkai1zYW1sLWlkcC5hY2xhcmsubmV0MIIBIzANBgkqhkiG9w0BAQEFAAOCARAAMIIBCwKCAQIAykosgghQluMK9lIsnCfALlzqSTQUD/vqi+G+jllWdJrIiVFSA6qYHJaFJ3smQCpHDO8d8TMJMtEZQR/Jg6ETf+mumigoOVYkKDfSNKxwWSmH9JJXBXeM7vTXhzM0O7pqUoyRUvp8xnn1Jv0CERiRoA5EPCaFrXO670CViu/NLPzJA2epPS++OqbDzn+XZqSxCKAWwgj3IX4ash6Jsrk/Xgf4bVBSgVnZRZ9XTgMVnxu7B10jeTPoOwoshgCzEEZF+2m6GFmV/ACe8nCpv47rv8053lNeTDiDGHMBpoA0aICbvge3OLCsXnQqPY6z7KeST1tCD0H+VJyBce0FBIo3rYECAwEAAaNQME4wHQYDVR0OBBYEFEhUGuuba4Sbln4dijEB9nGKqsBIMB8GA1UdIwQYMBaAFEhUGuuba4Sbln4dijEB9nGKqsBIMAwGA1UdEwQFMAMBAf8wDQYJKoZIhvcNAQENBQADggECAFOa3vVl8GGxIZU0G8Ld9VPl9R7CRANLceNhg1p+IFcOn7lB6Iqy1T8g7Z1ic0+X/SSN3uwOWxTM/Yp4oZQ1eCtGRvmPBx9G+AhOoftaQxDzX/Ug5AOWcbawDffabVhPaPf7vrkNHWirToZ5cArOXZgoYnOm0tfq8W/T+ay+yuN3kgnAAFNsyiK6IE/4VbNlQReCQCnIapOyDlxc6tDBL4t37xCDlup4+aO6LnG1tDMnOVxj+0vQMWbaQ3k78YFEmH3fOZFyDpra42aVWYx0fbFjz+LoOElMrXTwmR6VUcJZdGnXvMwsKsxa+s5ct7Uc1wKD+Wcf1bEC1ueu9RmOqHMS</ds:X509Certificate>
                    </ds:X509Data>
                </ds:KeyInfo>
            </ds:Signature>
            <saml:Subject>
                <saml:NameID Format="urn:oasis:names:tc:SAML:2.0:nameid-format:transient">aclark@aclark.net</saml:NameID>
                <saml:SubjectConfirmation Method="urn:oasis:names:tc:SAML:2.0:cm:bearer">
                    <saml:SubjectConfirmationData InResponseTo="_bbd0fa97-5384-4d77-849a-d1a117c0c2af"
                                                  NotOnOrAfter="2017-05-17T02:18:46Z"
                                                  Recipient="https://aclark.myabsorb.com/account/saml"
                                                  />
                </saml:SubjectConfirmation>
            </saml:Subject>
            <saml:Conditions NotBefore="2017-05-17T01:03:46Z"
                             NotOnOrAfter="2017-05-17T02:18:46Z"
                             />
            <saml:AuthnStatement AuthnInstant="2017-05-17T02:03:46Z">
                <saml:AuthnContext>
                    <saml:AuthnContextClassRef>urn:oasis:names:tc:SAML:2.0:ac:classes:PasswordProtectedTransport</saml:AuthnContextClassRef>
                </saml:AuthnContext>
            </saml:AuthnStatement>
        </saml:Assertion>
    </samlp:Response>


