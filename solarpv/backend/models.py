from django.db import models


class Certificate(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True,blank=True)  # Field name made lowercase.
    userid = models.ForeignKey('User', db_column='userID', blank=True, on_delete=models.CASCADE)  # Field name made lowercase.
    report_number = models.IntegerField(db_column='report number', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    issue_date = models.IntegerField(db_column='issue date', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    standardid = models.ForeignKey('TestStandard',  db_column='standardID', blank=True, null=True, on_delete=models.CASCADE)  # Field name made lowercase.
    locationid = models.ForeignKey('Location',  db_column='locationID', blank=True, null=True, on_delete=models.CASCADE)  # Field name made lowercase.
    model_number = models.ForeignKey('Product',  db_column='model number', blank=True, null=True, on_delete=models.CASCADE)  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = True
        db_table = 'certificate'


class Client(models.Model):
    clientid = models.IntegerField(db_column='clientID', primary_key=True,blank=True)  # Field name made lowercase.
    client_name = models.CharField(db_column='client name', max_length=45, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    client_type = models.CharField(db_column='client type', max_length=45, blank=True, null=True)  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = True
        db_table = 'client'


class Location(models.Model):
    locationid = models.IntegerField(db_column='locationID', primary_key=True,blank=True)  # Field name made lowercase.
    address1 = models.CharField(max_length=45, blank=True, null=True)
    address2 = models.CharField(max_length=45, blank=True, null=True)
    city = models.CharField(max_length=45, blank=True, null=True)
    state = models.CharField(max_length=45, blank=True, null=True)
    postal_code = models.IntegerField(db_column='postal code', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    country = models.CharField(max_length=45, blank=True, null=True)
    phone_number = models.IntegerField(db_column='phone number', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    fax_number = models.IntegerField(db_column='fax number', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    clientid = models.ForeignKey(Client,  db_column='clientID', blank=True, null=True, on_delete=models.CASCADE)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'location'


class PerformanceData(models.Model):
    model_number = models.OneToOneField('Product',  db_column='model number', primary_key=True,blank=True, on_delete=models.CASCADE)  # Field renamed to remove unsuitable characters.
    sequenceid = models.ForeignKey('TestSequence',  db_column='sequenceID', on_delete=models.CASCADE)  # Field name made lowercase.
    max_system_voltage = models.IntegerField(db_column='max system voltage', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    voc = models.CharField(max_length=45, blank=True, null=True)
    isc = models.CharField(max_length=45, blank=True, null=True)
    vmp = models.CharField(max_length=45, blank=True, null=True)
    imp = models.CharField(max_length=45, blank=True, null=True)
    pmp = models.CharField(max_length=45, blank=True, null=True)
    ff = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'performance data'
        unique_together = (('model_number', 'sequenceid'),)


class Product(models.Model):
    model_number = models.IntegerField(db_column='model number', primary_key=True,blank=True)  # Field renamed to remove unsuitable characters.
    product_name = models.CharField(db_column='product name', max_length=45, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    cell_technology = models.CharField(db_column='cell technology', max_length=45, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    cell_manufacturer = models.CharField(db_column='cell manufacturer', max_length=45, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    number_of_cells = models.IntegerField(db_column='number of cells', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    number_of_cells_in_series = models.IntegerField(db_column='number of cells in series', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    number_of_series_strings = models.IntegerField(db_column='number of series strings', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    number_of_diodes = models.IntegerField(db_column='number of diodes', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    product_length = models.CharField(db_column='product length', max_length=45, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    product_width = models.CharField(db_column='product width', max_length=45, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    product_weight = models.CharField(db_column='product weight', max_length=45, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    superstate_type = models.CharField(db_column='superstate type', max_length=45, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    superstate_manufacturer = models.CharField(db_column='superstate manufacturer', max_length=45, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    substrate_type = models.CharField(db_column='substrate  type', max_length=45, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    substrate_manufacturer = models.CharField(db_column='substrate manufacturer', max_length=45, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    frame_type = models.CharField(db_column='frame type', max_length=45, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    frame_adhesive = models.CharField(db_column='frame adhesive', max_length=45, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    encapsulate_type = models.CharField(db_column='encapsulate type', max_length=45, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    encapsulate_manufacturer = models.CharField(db_column='encapsulate manufacturer', max_length=45, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    junction_box_type = models.CharField(db_column='junction box type', max_length=45, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    junction_box_manufacturer = models.CharField(db_column='junction box manufacturer', max_length=45, blank=True, null=True)  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = True
        db_table = 'product'


class Service(models.Model):
    serviceid = models.IntegerField(db_column='serviceID', primary_key=True,blank=True)  # Field name made lowercase.
    service_name = models.CharField(db_column='service name', max_length=45, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    description = models.CharField(max_length=200, blank=True, null=True)
    is_fi_required = models.CharField(db_column='is FI required', max_length=45, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    fi_frequency = models.CharField(db_column='FI frequency', max_length=45, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    standardid = models.ForeignKey('TestStandard',  db_column='standardID', blank=True, null=True, on_delete=models.CASCADE)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'service'


class TestSequence(models.Model):
    sequenceid = models.IntegerField(db_column='sequenceID', primary_key=True,blank=True)  # Field name made lowercase.
    sequence_name = models.CharField(db_column='sequence name', max_length=45, blank=True, null=True)  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = True
        db_table = 'test sequence'


class TestStandard(models.Model):
    standardid = models.IntegerField(db_column='standardID', primary_key=True,blank=True)  # Field name made lowercase.
    description = models.CharField(max_length=200, blank=True, null=True)
    published_date = models.CharField(db_column='published date', max_length=45, blank=True, null=True)  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = True
        db_table = 'test standard'


class User(models.Model):
    userid = models.IntegerField(db_column='userID', primary_key=True,blank=True)  # Field name made lowercase.
    first_name = models.CharField(db_column='first name', max_length=45, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    last_name = models.CharField(db_column='last name', max_length=45, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    middle_name = models.CharField(db_column='middle name', max_length=45, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    job_title = models.CharField(db_column='job title', max_length=45, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    email = models.CharField(max_length=45, blank=True, null=True)
    office_phone = models.IntegerField(db_column='office phone', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    cell_phone = models.IntegerField(db_column='cell phone', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    prefix = models.CharField(max_length=45, blank=True, null=True)
    clientid = models.ForeignKey(Client,  db_column='clientID', blank=True, null=True, on_delete=models.CASCADE)  # Field name made lowercase.
    usercol = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'user'
