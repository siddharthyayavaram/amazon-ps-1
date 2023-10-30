from django.db import models
from django.core.exceptions import ObjectDoesNotExist

class Ship_params(models.Model):
    unit_dim_choices = [
        ("m","meters"),
        ("cm","centimeters"),
        ("in","inches"),
        ("ft","feet"),
    ]
    unit_wt_choices = [
        ("kg","kilograms"),
        ("g","grams"),
        ("lb","pounds"),
    ]
    length = models.FloatField(default=10)
    unit_len = models.CharField(max_length=2,choices=unit_dim_choices, default="in")
    breadth = models.FloatField(default=10)
    unit_bre = models.CharField(max_length=2,choices=unit_dim_choices, default="in")
    height = models.FloatField(default=10)
    unit_hei = models.CharField(max_length=2,choices=unit_dim_choices, default="in")
    mode = models.IntegerField(default=2)
    actual_weight = models.IntegerField(default=1)
    unit_wt = models.CharField(max_length=2,choices=unit_wt_choices, default="lb")
    src_zip = models.IntegerField(default = 10001)
    dest_zip = models.IntegerField(default = 100)

    def billable_weight(self):
            
            def convert_to_pounds(value):
                if self.unit_wt == "kg":
                    return value * 2.20462  # 1 kilogram = 2.20462 pounds
                elif self.unit_wt == "g":
                    return value * 0.00220462  # 1 gram = 0.00220462 pounds
                else:
                    return value

            def convert_to_inches(value,dim):
                if dim == "m":
                    return value * 39.37  # 1 meter = 39.37 inches
                elif dim == "cm":
                    return value * 0.3937  # 1 centimeter = 0.3937 inches
                elif dim == "ft":
                    return value * 12  # 1 foot = 12 inches
                else:
                    return value
                    
            weight = convert_to_pounds(self.actual_weight)
            length_inches = convert_to_inches(self.length,self.unit_len)
            breadth_inches = convert_to_inches(self.breadth,self.unit_bre)
            height_inches = convert_to_inches(self.height,self.unit_hei)

            dim_weight = length_inches * breadth_inches * height_inches
            bill_weight = int(dim_weight / 139)

            if bill_weight > weight:
                return bill_weight
            else:
                return weight
    
    def get_first_three_digits(number):
    # Convert the number to a string
        number_str = str(number)
        
        # Check if the number has at least three digits
        if len(number_str) >= 3:
            # Get the first three characters from the string and convert them back to an integer
            first_three_digits = int(number_str[:3])
            return first_three_digits
        else:
            # The number has less than three digits, return the number itself
            return number
     
    def zone_calc(self):
        try:
            t2_entry = T2.objects.get(dest_zip=self.dest_zip, mode=self.mode)
            return t2_entry.zone
        except ObjectDoesNotExist:
            return None
        

    @property
    def cost(self):
        if self.billable_weight() > 150:
            return -1
        else:
            try:
                t1_entry = T1.objects.get(zones=self.zone_calc(), weight=self.billable_weight(), time=2)
                return t1_entry.price
            except ObjectDoesNotExist:
                return None

class T1(models.Model):
    zones = models.IntegerField(db_column='Zones', blank=True, null=True)  # Field name made lowercase.
    weight = models.IntegerField(db_column='Weight', blank=True, null=True)  # Field name made lowercase.
    time = models.IntegerField(db_column='Time', blank=True, null=True)  # Field name made lowercase.
    price = models.FloatField(db_column='Price', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'air'


class T2(models.Model):
    dest_zip = models.IntegerField(db_column='Dest_ZIP', blank=True, null = True)
    mode = models.IntegerField(db_column='Mode', blank=True, null = True)
    zone = models.IntegerField(db_column='Zone', blank=True, null = True)

    class Meta:
        managed = False
        db_table = 'zonetable'