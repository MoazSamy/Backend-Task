from django.db import models

class Task(models.Model):
    # Setting up 2-tuple multiple choices var
    STATES= (
        ("DRFT" , "Draft"),
        ("ACTV" , "Active"),
        ("DN" , "Done"),
        ("ARCH" , "Archived" )
    )

    # Defining the required DB fields
    id = models.PositiveBigIntegerField(primary_key=True)
    state = models.CharField(max_length=4, choices=STATES , default="DRFT" , editable=False)
    title = models.CharField(max_length=250)

    def __res__(self):
        return self.title
    
    def nextState(self):
        if self.state == "DRFT":
            self.state = "ACTV"
        elif self.state == "ACTV":
            self.state = "DN"
        elif self.state == "DN":
            self.state = "ARCH"
        elif self.state == "ARCH":
            return False
        return True
