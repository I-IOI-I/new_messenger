from django.db import models
from polymorphic.models import PolymorphicModel

from chats import consts


class Base(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class BaseChat(Base, PolymorphicModel):
    # PolymorphicModel это из отдельной библиотеки
    users = models.ManyToManyField('core.User', through='ChatMember')

    class Meta:
        verbose_name = 'чат'
        verbose_name_plural = 'чаты'


class OrderedChat(BaseChat):
    class Meta:
        ordering = ["-date_updated"]
        proxy = True


class DirectChat(BaseChat):
    # related_name чтобы django не ругался
    user1 = models.ForeignKey(
        'core.User',
        on_delete=models.SET_NULL,
        related_name='user1_direct_chats',
        null=True
    )
    user2 = models.ForeignKey(
        'core.User',
        on_delete=models.SET_NULL,
        related_name='user2_direct_chats',
        null=True
    )

    class Meta:
        verbose_name = 'личный чат'
        verbose_name_plural = 'личные чаты'

    def __str__(self):
        return f'Личный чат между "{self.user1}" и "{self.user2}"'


class GroupChat(BaseChat):
    admins = models.ManyToManyField('core.User', related_name='chats_admin')
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name = 'групповой чат'
        verbose_name_plural = 'групповые чаты'

    def __str__(self):
        return self.name


class Channel(BaseChat):
    admins = models.ManyToManyField('core.User', related_name='channels_admin')
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name = 'канал'
        verbose_name_plural = 'каналы'

    def __str__(self):
        return self.name


class ChatMember(Base):
    user = models.ForeignKey(
        'core.User',
        on_delete=models.CASCADE,
        related_name='chats_member',
    )

    chat = models.ForeignKey(
        BaseChat,
        on_delete=models.CASCADE,
    )

    role = models.CharField(
        max_length=255,
        choices=consts.ROLES_CHOICES,
        default=consts.CHAT_MEMBER,
    )

    class Meta:
        verbose_name = 'участник чата'
        verbose_name_plural = 'участники чата'

    def __str__(self):
        return f'{self.user.username} {self.chat.name}'


class Message(Base):
    chat = models.ForeignKey(
        BaseChat,
        on_delete=models.CASCADE,
        related_name='messages'
    )
    text = models.TextField()

    status = models.CharField(
        max_length=255,
        choices=consts.MESSAGE_STATUS_CHOICES,
        default=consts.MESSAGE_STATUS_SEND,
    )

    sender = models.ForeignKey(
        'core.User',
        on_delete=models.SET_NULL,
        null=True,
        related_name='messages'
    )

    manage = models.BooleanField(default=False)

    manage_type = models.CharField(
        max_length=255,
        choices=consts.MANAGE_MESSAGE_TYPE,
        null=True
    )

    class Meta:
        verbose_name = 'сообщение'
        verbose_name_plural = 'сообщения'

    def __str__(self):
        return f'{self.chat} {self.date_created}'
