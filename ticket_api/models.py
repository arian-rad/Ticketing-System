from django.db import models
from accounts.models import User


class Ticket(models.Model):
    subject = models.CharField(max_length=50, verbose_name='موضوع')
    create_at = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='تاریخ ویرایش')
    creator = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='کاربر ایجاد کننده')

    class Meta:
        verbose_name = 'تیکت'
        verbose_name_plural = 'تیکت ها'

    def __str__(self):
        return self.subject


class Message(models.Model):
    text = models.TextField(max_length=350, verbose_name='متن پیام')
    user = models.ForeignKey(User, verbose_name='کاربر', on_delete=models.CASCADE)
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE, verbose_name='تیکت مربوطه')
    image = models.ImageField(max_length=250, null=True, blank=True, upload_to='ticket_images/%Y/%m/%d')
    create_at = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='تاریخ ویرایش')

    class Meta:
        verbose_name = 'پیام تیکت'
        verbose_name_plural = 'پیام تیکت ها'

    def __str__(self):
        return self.text
