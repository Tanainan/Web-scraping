library(jsonlite)
library(stringr)
library(mongolite)

setwd("~/Downloads/tutorial")

data1 <- data.frame(fromJSON(txt = "job.json"))
data2 <- data.frame(fromJSON(txt = "jobtopgun.json")) # make sure to remove "," and add "]" at the end of the file
data3 <- data.frame(fromJSON(txt = "jobth.json"))
data4 <- data.frame(fromJSON(txt = "phuketall.json"))
data5 <- data.frame(fromJSON(txt = "job2.json"))
data6 <- data.frame(fromJSON(txt = "jobtopsale.json"))
data7 <- data.frame(fromJSON(txt = "minor.json"))
data8 <- data.frame(fromJSON(txt = "techstar.json"))
data9 <- data.frame(fromJSON(txt = "techstar2.json"))
data10 <- data.frame(fromJSON(txt = "techstar3.json"))
data11 <- data.frame(fromJSON(txt = "reeracoen.json"))
data12 <- data.frame(fromJSON(txt = "jobpub.json"))
data13 <- data.frame(fromJSON(txt = "jobbkk.json"))
data14 <- data.frame(fromJSON(txt = "phitlokjob2.json"))
data15 <- data.frame(fromJSON(txt = "i-jobthai.json"))
data16 <- data.frame(fromJSON(txt = "jobkia.json"))


# clean data
for (i in 1:nrow(data1)){
  for (j in 1:ncol(data1)){
    
    # remove html tags
    data1[i,j] <- data.frame(str_replace_all(data1[i,j], "<[^>]+>", ""))
    
    # remove spacing
    data1[i,j] <- data.frame(str_replace_all(data1[i,j], "\\s\\s+", " "))
    
  }
}

for (i in 1:nrow(data2)){
  for (j in 1:ncol(data2)){
    
    # remove html tags
    data2[i,j] <- data.frame(str_replace_all(data2[i,j], "<[^>]+>", ""))
    
    # remove spacing
    data2[i,j] <- data.frame(str_replace_all(data2[i,j], "\\s\\s+", " "))
    
  }
}

for (i in 1:nrow(data3)){
  for (j in 1:ncol(data3)){
    
    # remove html tags
    data3[i,j] <- data.frame(str_replace_all(data3[i,j], "<[^>]+>", ""))
    
    # remove spacing
    data3[i,j] <- data.frame(str_replace_all(data3[i,j], "\\s\\s+", " "))
    
  }
}

for (i in 1:nrow(data4)){
  for (j in 1:ncol(data4)){
    
    # remove html tags
    data4[i,j] <- data.frame(str_replace_all(data4[i,j], "<[^>]+>", ""))
    
    # remove spacing
    data4[i,j] <- data.frame(str_replace_all(data4[i,j], "\\s\\s+", " "))
    
  }
}

for (i in 1:nrow(data5)){
  for (j in 1:ncol(data5)){
    
    # remove html tags
    data5[i,j] <- data.frame(str_replace_all(data5[i,j], "<[^>]+>", ""))
    
    # remove spacing
    data5[i,j] <- data.frame(str_replace_all(data5[i,j], "\\s\\s+", " "))
    
  }
}

for (i in 1:nrow(data6)){
  for (j in 1:ncol(data6)){
    
    # remove html tags
    data6[i,j] <- data.frame(str_replace_all(data6[i,j], "<[^>]+>", ""))
    
    # remove spacing
    data6[i,j] <- data.frame(str_replace_all(data6[i,j], "\\s\\s+", " "))
    
  }
}

for (i in 1:nrow(data7)){
  for (j in 1:ncol(data7)){
    
    # remove html tags
    data7[i,j] <- data.frame(str_replace_all(data7[i,j], "<[^>]+>", ""))
    
    # remove spacing
    data7[i,j] <- data.frame(str_replace_all(data7[i,j], "\\s\\s+", " "))
    
  }
}


for (i in 1:nrow(data8)){
  for (j in 1:ncol(data8)){
    
    # remove html tags
    data8[i,j] <- data.frame(str_replace_all(data8[i,j], "<[^>]+>", ""))
    
    # remove spacing
    data8[i,j] <- data.frame(str_replace_all(data8[i,j], "\\s\\s+", " "))
    
  }
}

for (i in 1:nrow(data9)){
  for (j in 1:ncol(data9)){
    
    # remove html tags
    data9[i,j] <- data.frame(str_replace_all(data9[i,j], "<[^>]+>", ""))
    
    # remove spacing
    data9[i,j] <- data.frame(str_replace_all(data9[i,j], "\\s\\s+", " "))
    
  }
}

for (i in 1:nrow(data10)){
  for (j in 1:ncol(data10)){
    
    # remove html tags
    data10[i,j] <- data.frame(str_replace_all(data10[i,j], "<[^>]+>", ""))
    
    # remove spacing
    data10[i,j] <- data.frame(str_replace_all(data10[i,j], "\\s\\s+", " "))
    
  }
}

for (i in 1:nrow(data11)){
  for (j in 1:ncol(data11)){
    
    # remove html tags
    data11[i,j] <- data.frame(str_replace_all(data11[i,j], "<[^>]+>", ""))
    
    # remove spacing
    data11[i,j] <- data.frame(str_replace_all(data11[i,j], "\\s\\s+", " "))
    
  }
}


for (i in 1:nrow(data12)){
  for (j in 1:ncol(data12)){
    
    # remove html tags
    data12[i,j] <- data.frame(str_replace_all(data12[i,j], "<[^>]+>", ""))
    
    # remove spacing
    data12[i,j] <- data.frame(str_replace_all(data12[i,j], "\\s\\s+", " "))
    
  }
}

for (i in 1:nrow(data13)){
  for (j in 1:ncol(data13)){
    
    # remove html tags
    data13[i,j] <- data.frame(str_replace_all(data13[i,j], "<[^>]+>", ""))
    
    # remove spacing
    data13[i,j] <- data.frame(str_replace_all(data13[i,j], "\\s\\s+", " "))
    
  }
}

for (i in 1:nrow(data14)){
  for (j in 1:ncol(data14)){
    
    # remove html tags
    data14[i,j] <- data.frame(str_replace_all(data14[i,j], "<[^>]+>", ""))
    
    # remove spacing
    data14[i,j] <- data.frame(str_replace_all(data14[i,j], "\\s\\s+", " "))
    
  }
}

for (i in 1:nrow(data15)){
  for (j in 1:ncol(data15)){
    
    # remove html tags
    data15[i,j] <- data.frame(str_replace_all(data15[i,j], "<[^>]+>", ""))
    
    # remove spacing
    data15[i,j] <- data.frame(str_replace_all(data15[i,j], "\\s\\s+", " "))
    
  }
}

for (i in 1:nrow(data16)){
  for (j in 1:ncol(data16)){
    
    # remove html tags
    data16[i,j] <- data.frame(str_replace_all(data16[i,j], "<[^>]+>", ""))
    
    # remove spacing
    data16[i,j] <- data.frame(str_replace_all(data16[i,j], "\\s\\s+", " "))
    
  }
}

m1 <- mongo(collection = "thaijobtoday", db = "Job")
m1$insert(data1)

m2 <- mongo(collection = "jobtopgun", db = "Job")
m2$insert(data2)

m3 <- mongo(collection = "jobth", db = "Job")
m3$insert(data3)

m4 <- mongo(collection = "phuketall", db = "Job")
m4$insert(data4)

m5 <- mongo(collection = "thaijobtoday2", db = "Job")
m5$insert(data5)

m6 <- mongo(collection = "jobtopsale", db = "Job")
m6$insert(data6)

m7 <- mongo(collection = "minor", db = "Job")
m7$insert(data7)

m8 <- mongo(collection = "techstar", db = "Job")
m8$insert(data8)

m9 <- mongo(collection = "techstar2", db = "Job")
m9$insert(data9)

m10 <- mongo(collection = "techstar3", db = "Job")
m10$insert(data10)

m11 <- mongo(collection = "reeracoen", db = "Job")
m11$insert(data11)

m12 <- mongo(collection = "jobpub", db = "Job")
m12$insert(data12)

m13 <- mongo(collection = "jobbkk", db = "Job")
m13$insert(data13)

m14 <- mongo(collection = "phitlokjob", db = "Job")
m14$insert(data14)

m15 <- mongo(collection = "i-jobthai", db = "Job")
m15$insert(data15)


m16 <- mongo(collection = "jobkia", db = "Job")
m16$insert(data16)
