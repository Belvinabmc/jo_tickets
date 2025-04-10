from django.db import models
from django.contrib.auth.models import User
import qrcode
from io import BytesIO
from django.core.files import File

class Team(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=10)
    nickname = models.CharField(max_length=100)

    def _str_(self):
        return f"{self.name} ({self.code})"

class Stadium(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)

    def _str_(self):
        return self.name

class Event(models.Model):
    start = models.DateTimeField()
    stadium = models.ForeignKey(Stadium, on_delete=models.CASCADE)
    team_home = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='home_matches')
    team_away = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='away_matches')

    def _str_(self):
        return f"{self.team_home} vs {self.team_away} - {self.start.strftime('%Y-%m-%d %H:%M')}"

class Ticket(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    event = models.ForeignKey('Event', on_delete=models.CASCADE)
    qr_code = models.ImageField(upload_to='qr_codes/', blank=True, null=True)
    is_used = models.BooleanField(default=False)

    def _str_(self):
        return f"Ticket de {self.user.username} pour {self.event}"

    def save(self, *args, **kwargs):
        # Crée un contenu pour le QR Code
        qr_content = f"Ticket ID: {self.id}\nUser: {self.user.username}\nEvent: {self.event}"

        # Génère le QR code
        qr = qrcode.make(qr_content)

        # Enregistre l’image dans un fichier mémoire
        buffer = BytesIO()
        qr.save(buffer, format='PNG')
        buffer.seek(0)

        # Donne un nom au fichier QR
        file_name = f"ticket_{self.user.username}_{self.event.id}.png"
        self.qr_code.save(file_name, File(buffer), save=False)

        super().save(*args, **kwargs)