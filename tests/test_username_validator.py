from username_validator import UsernameValidator
import pytest

def test_reserved_names():
  with pytest.raises(Exception):
    UsernameValidator().validate_reserved("www")

def test_validate_all():
  with pytest.raises(Exception):
    UsernameValidator().validate_all("www")

def test_additional_reserved_name():
  with pytest.raises(Exception):
    UsernameValidator(additional_names=["my_name"]).validate_reserved("my_name")

def test_custom_reserved_names():
  UsernameValidator(reserved_names=[]).validate_reserved("www")

def test_confusable_validate_all():
  with pytest.raises(Exception):
    UsernameValidator().validate_confusables(u'j\u0430ne_doe')
