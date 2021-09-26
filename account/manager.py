from django.contrib.auth.base_user import BaseUserManager


class UserManager(BaseUserManager):
    use_in_migrations = True


    # to overright User function

    def create_user(self, email, password=None, **extra_fields):

        # to raise error if email is none
        if not email:
            raise ValueError('Email is require')

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    # to overright Super user function
    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff',True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(('Super user must have is_staff true'))

        return self.create_user(email, password, **extra_fields)
