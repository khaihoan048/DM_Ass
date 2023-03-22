import jnius_config
import pandas
jnius_config.add_classpath('jedai-core-3.2.1-jar-with-dependencies.jar')

from jnius import autoclass
path='/home/nvkhoan/DM/JedAIToolkit/restaurant1Profiles'
EntitySerializationReader = autoclass("org.scify.jedai.datareader.entityreader.EntitySerializationReader")
data=EntitySerializationReader(path)
entityProfiles=data.getEntityProfiles()
profilesIterator = entityProfiles.iterator()
profiles=[]
while profilesIterator.hasNext():
        profile = profilesIterator.next()
        pf = {"id": len(profiles)}
        attributesIterator = profile.getAttributes().iterator()
        while attributesIterator.hasNext():
            attribute = attributesIterator.next()
            pf[attribute.getName()] = attribute.getValue()
        profiles.append(pf)
print(pandas.DataFrame(profiles))
