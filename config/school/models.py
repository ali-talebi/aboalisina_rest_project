from django.db import models
from django.contrib.auth.models import User 
from django_jalali.db import models as jmodels
from django.db.models import Q
from django.core.exceptions import ValidationError


# Create your models here.

class StudentInformation(models.Model):
    client = models.OneToOneField(User, on_delete=models.PROTECT)

    personal_picture = models.FileField(upload_to="personal_document/personal_picture/")
    certificate_iranian_picture = models.FileField(upload_to="personal_document/certificate_iranian/")
    passport_picture = models.FileField(upload_to="personal_document/passport_picture/")

    personal_iranian_id = models.CharField(max_length=10, unique=True)
    personal_foreign_id = models.CharField(max_length=20, null=True, blank=True)

    name = models.CharField(max_length=50)
    family = models.CharField(max_length=50)
    hbd = jmodels.jDateTimeField()

    father_name = models.CharField(max_length=50)
    father_iranian_id = models.CharField(max_length=10)
    father_certificate_iranian = models.FileField(upload_to="personal_document/father_certificate_iranian/")
    father_card_melli_iranian = models.FileField(upload_to="personal_document/father_card_melli_iranian/")

    mother_name = models.CharField(max_length=50)
    mother_iranian_id = models.CharField(max_length=10)
    mother_certificate_iranian = models.FileField(upload_to="personal_document/mother_certificate_iranian/")
    mother_card_melli_iranian = models.FileField(upload_to="personal_document/mother_card_melli_iranian/")

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.client.username}"

    class Meta:
        db_table = "student_information_table"
        verbose_name_plural = "Student Information Management"

        constraints = [
            models.UniqueConstraint(
                fields=["personal_foreign_id"],
                name="unique_code_when_not_null",
                condition=Q(personal_foreign_id__isnull=False),
            )
        ]


    
    
    
    
def validate_file_size(file):
    limit = 5 * 1024 * 1024  
    if file.size > limit:
        raise ValidationError("File size must be under 5MB.")


def upload_class_path(instance, filename, class_number):
    return f"student_education_information/{instance.client.id}/class_{class_number}/{filename}"


def class1_path(instance, filename):
    return upload_class_path(instance, filename, 1)


def class2_path(instance, filename):
    return upload_class_path(instance, filename, 2)


def class3_path(instance, filename):
    return upload_class_path(instance, filename, 3)


def class4_path(instance, filename):
    return upload_class_path(instance, filename, 4)


def class5_path(instance, filename):
    return upload_class_path(instance, filename, 5)


def class6_path(instance, filename):
    return upload_class_path(instance, filename, 6)


def class7_path(instance, filename):
    return upload_class_path(instance, filename, 7)


def class8_path(instance, filename):
    return upload_class_path(instance, filename, 8)


def class9_path(instance, filename):
    return upload_class_path(instance, filename, 9)


def class10_path(instance, filename):
    return upload_class_path(instance, filename, 10)


def class11_path(instance, filename):
    return upload_class_path(instance, filename, 11)


def class12_path(instance, filename):
    return upload_class_path(instance, filename, 12)


class StudentEducationInformation(models.Model):

    client = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="education_information"
    )

    class_1 = models.FileField(upload_to=class1_path, validators=[validate_file_size], blank=True, null=True)
    class_2 = models.FileField(upload_to=class2_path, validators=[validate_file_size], blank=True, null=True)
    class_3 = models.FileField(upload_to=class3_path, validators=[validate_file_size], blank=True, null=True)
    class_4 = models.FileField(upload_to=class4_path, validators=[validate_file_size], blank=True, null=True)
    class_5 = models.FileField(upload_to=class5_path, validators=[validate_file_size], blank=True, null=True)
    class_6 = models.FileField(upload_to=class6_path, validators=[validate_file_size], blank=True, null=True)
    class_7 = models.FileField(upload_to=class7_path, validators=[validate_file_size], blank=True, null=True)
    class_8 = models.FileField(upload_to=class8_path, validators=[validate_file_size], blank=True, null=True)
    class_9 = models.FileField(upload_to=class9_path, validators=[validate_file_size], blank=True, null=True)
    class_10 = models.FileField(upload_to=class10_path, validators=[validate_file_size], blank=True, null=True)
    class_11 = models.FileField(upload_to=class11_path, validators=[validate_file_size], blank=True, null=True)
    class_12 = models.FileField(upload_to=class12_path, validators=[validate_file_size], blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.client.username} Education Documents"


    
    
    
# class Student_Education_Information(models.Model):
    
#     base_path = "student_education_information"
#     client  = models.OneToOneField(User,on_delete=models.CASCADE)
#     class_1 = models.FileField(upload_to=f"{base_path}/class_1/")
#     class_2 = models.FileField(upload_to=f"{base_path}/class_2/")
#     class_3 = models.FileField(upload_to=f"{base_path}/class_3/")
#     class_4 = models.FileField(upload_to=f"{base_path}/class_4/")
#     class_5 = models.FileField(upload_to=f"{base_path}/class_5/")
#     class_6 = models.FileField(upload_to=f"{base_path}/class_6/")
#     class_7 = models.FileField(upload_to=f"{base_path}/class_7/")
#     class_8 = models.FileField(upload_to=f"{base_path}/class_8/")
#     class_9 = models.FileField(upload_to=f"{base_path}/class_9/")
#     class_10 = models.FileField(upload_to=f"{base_path}/class_10/")
#     class_11 = models.FileField(upload_to=f"{base_path}/class_11/")
#     class_12 = models.FileField(upload_to=f"{base_path}/class_12/")
    
#     def __str__(self):
#         return f'{self.client}'
    