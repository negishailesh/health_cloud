# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser, AbstractBaseUser, PermissionsMixin, UserManager
from django.utils.translation import ugettext_lazy as _
from django.conf import settings
from django.utils import timezone


class Users(AbstractBaseUser, PermissionsMixin):
    """
    Model for Users login from extension
    """
    username = models.CharField(_('username'), max_length = 255, unique = True)
    first_name = models.CharField(_('first name'), max_length = 255, blank = True)
    last_name = models.CharField(_('last name'), max_length = 255, blank = True)
    email = models.EmailField(_('email address'), blank = True)
    is_staff = models.BooleanField(_('staff status'), default = False,
                                   help_text =_('Designates whether the user can log into this admin site.'))
    is_active = models.BooleanField(_('active'), default = True,
                                    help_text = _('Designates whether this user should be treated as '
                                                'active. Unselect this instead of deleting accounts.'))
    date_joined = models.DateTimeField(_('date joined'), default = timezone.now)
    phone = models.TextField(max_length = 20, null = True, blank = True)
    objects = UserManager()

    roles = models.ManyToManyField('Role')
    
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    def __unicode__(self):
        return self.email


class Role(models.Model):
    name = models.CharField(max_length=255, blank = True)

    def __unicode__(self):
        return self.name
   


  
