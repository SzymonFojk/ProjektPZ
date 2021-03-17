from django.db import models
from django.contrib.auth.models import User
from PIL import Image

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    friends = models.ManyToManyField(User, related_name='friends', blank=True)


    def __str__(self):
        return f'{self.user.username} profile'

    def save(self, *args, **kwargs):


        img = Image.open(self.image.path)
        if img.height > 300 or img.width > 300:
            img.thumbnail((300, 300))
            img.save(self.image.path)

        try:
            this = Profile.objects.get(id=self.id).first()
            if this.image != self.image:
                this.image.delete(save=False)
        except:
            pass
        super(Profile, self).save(*args, **kwargs)

    def get_friends(self):
        return self.friends.all()

    def get_friends_number(self):
        return self.friends.all().count()

STATUS_CHOICES = (('send', 'send'), ('accepted', 'accepted'))

class Relationship(models.Model):
    sender = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="sender")
    receiver = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="receiver")
    status = models.CharField(max_length=8, choices=STATUS_CHOICES)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.sender}-{self.receiver}-{self.status}'



"""
class FriendList(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name = "user")
    friends = models.ManyToManyField(User, blank = True, related_name = "friends")

    def __str__(self):
        return self.user.username

    # jak wywolac metode z modelu bo .add != add_friend
    def add_friend(self, acc_id):
        if is_my_friend(acc_id):
            self.friends.add(acc_id)
            self.save()
        else:
            return "Already on friend list" #Gdy użytkownik jest na liście znajomych

    def remove_friend(self, friend_acc):
        self.friends.remove(friend_acc)
        self.save()
        friend_flist = FriendList.objects.get(user=friend_acc)
        friend_flist.friends.remove(self.user)
        friend_flist.friends.save()

    def is_my_friend(self, friend_acc):
        if friend_acc in self.friends.all():
            return True
        return False
"""
