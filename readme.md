Username Validation
========


Username validation methods extracted from [django-registration](https://github.com/ubernostrum/django-registration) for use outside of django apps (no dependency on django).

[James Bennett](https://github.com/ubernostrum)'s post [Let’s talk about usernames](https://www.b-list.org/weblog/2018/feb/11/usernames/) is a great write-up of both why and how to perform username validation.

This library performs both reserved name checking as well as [confusable homohomoglyph](https://confusable-homoglyphs.readthedocs.io/en/latest/readme.html) checking.

# Usage

An `Exception` will be thrown if the name is confusable or reserved.

## All checks

```
from username_validator import UsernameValidator

# checks both reserved names and confusable
UsernameValidator().validate_all("myname")
```

## Confusable checks only

```
from username_validator import UsernameValidator

UsernameValidator().validate_confusables_email("myname@something.com")
UsernameValidator().validate_confusables('j\u0430ne_doe') # will throw exception

```


## Reserved name checks only


```
from username_validator import UsernameValidator

UsernameValidator().validate_reserved("myname")
```

## Custom reserved list

You can add to the reserved list with domain specific names or replace it completely.  The default list is broken into categories and exposed, so you can pick and choose if you like.

### Extend reserved list with our custom names

```
UsernameValidator(additional_names=["myspecialname", "myothername"]).validate_reserved("myname")
```

### Replace default list with subset

```
from username_validator import UsernameValidator, PROTOCOL_HOSTNAMES, SENSITIVE_FILENAMES

UsernameValidator(reserved_names=(PROTOCOL_HOSTNAMES + SENSITIVE_FILENAMES)).validate_all("my_name")
```


## Credit

This code is pretty much a straight copy-paste of [django-registration](https://github.com/ubernostrum/django-registration), removing django utility methods.  Thank to [James Bennett](https://github.com/ubernostrum) for the excellent work.
