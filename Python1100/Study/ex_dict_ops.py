
zDict = {"Code":None,
         "Tested":"All",
         7:"Seven",
         "Nine":9}

zDict["Code"] = "Ready!"
zDict.pop(7)
zDict.pop("Nine")
print(zDict)

zDict.clear()

zDict = dict("Code"="",
         "Tested"="All",
         7="Seven",
         "Nine"=9)
print(zDict)



