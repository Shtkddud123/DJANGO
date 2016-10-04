from django.db import models

# First Science topic will get the ID of 1
# Second Science topic will get the ID of 2
# etc etc etc

class Science(models.Model):#inherit from models.model 
    topic = models.CharField(max_length=200) # what type of data?  we also need to characterise maxlengths
    lab_involvment = models.CharField(max_length=200)
    popularity = models.CharField(max_length=100)
    picture = models.CharField(max_length=10000) # max_length has to be long as we are dealing with other websites

    def __str__(self): # "A string representation of the object" 
        """Define the definition of the object"""
        return self.topic + '-' + self.popularity # Now when you call the object, it will simply print out it's topic in question and it's general popularity. 
    
class subfield(models.Model): # How to associate the above class with this class?
    # topic needs to be related to computational chemistry
    subtopic = models.ForeignKey(Science, on_delete = models.CASCADE) # when you need to delete the album, models.CASCADE allows the computer to delete the songs too automatically
    maths_heavy = models.CharField(max_length = 10)
    time_to_be_competent = models.CharField(max_length = 250)
    


