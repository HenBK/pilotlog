from django.db import models


class Aircraft(models.Model):
    AircraftID = models.CharField(
        max_length=255,
        null=True,
    )
    EquipmentType = models.CharField(
        max_length=255,
        null=True,
    )
    TypeCode = models.CharField(
        max_length=255,
        null=True,
    )
    Year = models.IntegerField(
        null=True,
    )
    Make = models.CharField(
        max_length=255,
        null=True,
    )
    Model = models.CharField(
        max_length=255,
        null=True,
    )
    Category = models.CharField(
        max_length=255,
        null=True,
    )
    Class = models.CharField(
        max_length=255,
        null=True,
    )
    GearType = models.CharField(
        max_length=255,
        null=True,
    )
    EngineType = models.CharField(
        max_length=255,
        null=True,
    )
    Complex = models.BooleanField(
        null=True,
    )
    HighPerformance = models.BooleanField(
        null=True,
    )
    Pressurized = models.BooleanField(
        null=True,
    )
    TAA = models.BooleanField(
        null=True,
    )


class Flight(models.Model):
    Date = models.DateField(
        null=True,
    )
    AircraftID = models.CharField(
        max_length=255,
        null=True,
    )
    From = models.CharField(
        max_length=255,
        null=True,
    )
    To = models.CharField(
        max_length=255,
        null=True,
    )
    Route = models.CharField(
        max_length=255,
        null=True,
    )
    TimeOut = models.TimeField(
        null=True,
    )
    TimeOff = models.TimeField(
        null=True,
    )
    TimeOn = models.TimeField(
        null=True,
    )
    TimeIn = models.TimeField(
        null=True,
    )
    OnDuty = models.TimeField(
        null=True,
    )
    OffDuty = models.TimeField(
        null=True,
    )
    TotalTime = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        null=True,
    )
    PIC = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        null=True,
    )
    SIC = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        null=True,
    )
    Night = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        null=True,
    )
    Solo = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        null=True,
    )
    CrossCountry = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        null=True,
    )
    NVG = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        null=True,
    )
    NVGOps = models.IntegerField(
        null=True,
    )
    Distance = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        null=True,
    )
    DayTakeoffs = models.IntegerField(
        null=True,
    )
    DayLandingsFullStop = models.IntegerField(
        null=True,
    )
    NightTakeoffs = models.IntegerField(
        null=True,
    )
    NightLandingsFullStop = models.IntegerField(
        null=True,
    )
    AllLandings = models.IntegerField(
        null=True,
    )
    ActualInstrument = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        null=True,
    )
    SimulatedInstrument = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        null=True,
    )
    HobbsStart = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        null=True,
    )
    HobbsEnd = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        null=True,
    )
    TachStart = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        null=True,
    )
    TachEnd = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        null=True,
    )
    Holds = models.IntegerField(
        null=True,
    )
    Approach1 = models.TextField(
        null=True,
    )
    Approach2 = models.TextField(
        null=True,
    )
    Approach3 = models.TextField(
        null=True,
    )
    Approach4 = models.TextField(
        null=True,
    )
    Approach5 = models.TextField(
        null=True,
    )
    Approach6 = models.TextField(
        null=True,
    )
    DualGiven = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        null=True,
    )
    DualReceived = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        null=True,
    )
    SimulatedFlight = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        null=True,
    )
    GroundTraining = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        null=True,
    )
    InstructorName = models.CharField(
        max_length=255,
        null=True,
    )
    InstructorComments = models.TextField(
        null=True,
    )
    Person1 = models.TextField(
        null=True,
    )
    Person2 = models.TextField(
        null=True,
    )
    Person3 = models.TextField(
        null=True,
    )
    Person4 = models.TextField(
        null=True,
    )
    Person5 = models.TextField(
        null=True,
    )
    Person6 = models.TextField(
        null=True,
    )
    FlightReview = models.BooleanField(
        null=True,
    )
    Checkride = models.BooleanField(
        null=True,
    )
    IPC = models.BooleanField(
        null=True,
    )
    NVGProficiency = models.BooleanField(
        null=True,
    )
    FAA6158 = models.BooleanField(
        null=True,
    )
    CustomFieldNameText = models.TextField(
        null=True,
    )
    CustomFieldNameNumeric = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        null=True,
    )
    CustomFieldNameHours = models.TimeField(
        null=True,
    )
    CustomFieldNameCounter = models.IntegerField(
        null=True,
    )
    CustomFieldNameDate = models.DateField(
        null=True,
    )
    CustomFieldNameDateTime = models.DateTimeField(
        null=True,
    )
    CustomFieldNameToggle = models.BooleanField(
        null=True,
    )
    PilotComments = models.TextField(
        null=True,
    )


class MapperConfig(models.Model):
    model_name = models.CharField(
        max_length=255,
    )
    config = models.JSONField()
