from django.db import models

class Ship_params(models.Model):
  time = models.FloatField()
  zone = models.IntegerField(default=100)
  weight = models.FloatField()
  carrier = models.IntegerField(default=1)

  @property
  def cost(self):
      # Perform your computation based on previous inputs
      return self.time * self.zone * self.weight * self.carrier

