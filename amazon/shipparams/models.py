from django.db import models
from math import radians, sin, cos, sqrt, asin

class Ship_params(models.Model):
    # zone = models.IntegerField(default=100)
    length = models.FloatField(default=10)
    breadth = models.FloatField(default=10)
    height = models.FloatField(default=10)
    mode = models.IntegerField(default=2)
    slot = models.FloatField(default=1)
    days = models.FloatField(default=1)
    lat1 = models.FloatField(default=10.00)
    lon1 = models.FloatField(default=10.00)
    lat2 = models.FloatField(default=10.00)
    lon2 = models.FloatField(default=10.00)

    def billable_weight(self):
        dim_weight=self.length*self.breadth*self.height
        bill_weight=int(dim_weight/139)

        return bill_weight
    
    def haversine_distance(self):
        """
        Calculate the distance between two points on the Earth's surface using the haversine formula.

        Arguments:
        lat1 -- latitude of the first point (in degrees)
        lon1 -- longitude of the first point (in degrees)
        lat2 -- latitude of the second point (in degrees)
        lon2 -- longitude of the second point (in degrees)

        Returns:
        The distance between the two points (in miles).
        """
        # Convert latitude and longitude from degrees to radians
        lat1, lon1, lat2, lon2 = map(radians, [self.lat1, self.lon1, self.lat2, self.lon2])

        # Haversine formula
        dlon = lon2 - lon1
        dlat = lat2 - lat1
        a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
        c = 2 * asin(sqrt(a))
        radius = 6371  # Radius of the Earth in kilometers
        distance = c * radius

        return distance*0.621371  # conversion into miles
    
    @staticmethod   
    def get_last_dig(miles):
        if miles >= 1 and miles <= 50:
            return "1"
        elif miles >= 51 and miles <= 150:
            return "2"
        elif miles >= 151 and miles <= 300:
            return "3"
        elif miles >= 301 and miles <= 600:
            return "4"
        elif miles >= 601 and miles <= 1000:
            return "5"
        elif miles >= 1001 and miles <= 1400:
            return "6"
        elif miles >= 1401 and miles <= 1800:
            return "7"
        elif miles >= 1801:
            return "8"

    def zone_calc(self):

        res = self.haversine_distance()

        mode=self.mode
        days=self.days
        slot=self.slot

        if mode==1:
            print(self.get_last_dig(res))

        else:
            if days==1 :
                if slot==1:
                    zone="10"+self.get_last_dig(res)
                elif slot==2:
                    zone="10"+self.get_last_dig(res)
                elif slot==3:
                    zone="13"+self.get_last_dig(res)
            elif days==2:
                if slot==1:
                    zone="24"+self.get_last_dig(res)
                elif slot==2:
                    zone="20"+self.get_last_dig(res)
            elif days==3:
                zone="30"+self.get_last_dig(res)

        return zone

    @property
    def cost(self):
        if self.billable_weight()>150:
            return -1

        t1_entry = T1.objects.get(zones=self.zone_calc(), weight=self.billable_weight(), time=self.slot)
        return t1_entry.price

class T1(models.Model):
    zones = models.IntegerField(db_column='Zones', blank=True, null=True)  # Field name made lowercase.
    weight = models.IntegerField(db_column='Weight', blank=True, null=True)  # Field name made lowercase.
    time = models.IntegerField(db_column='Time', blank=True, null=True)  # Field name made lowercase.
    price = models.FloatField(db_column='Price', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'air'