d <- read.csv('new_data.csv')
summary(d)
mean(d$WordCount)
sd(d$WordCount)
mean(d$WordLength)
sd(d$WordLength)
mean(d$TTR)
sd(d$TTR)
mean(d$nounRatio)
mean(d$verbRatio)
mean(d$adverbRatio)
mean(d$adjectiveRatio)

with(d, tapply(WordCount,list(Discipline),mean, na.rm=TRUE))
with(d,wilcox.test(WordCount~Discipline))

with(d, tapply(TTR,list(Discipline),mean, na.rm=TRUE))
with(d,wilcox.test(TTR~Discipline))

with(d, tapply(nounRatio,list(Discipline),mean, na.rm=TRUE))
with(d,wilcox.test(nounRatio~Discipline))

with(d, tapply(verbRatio,list(Discipline),mean, na.rm=TRUE))
with(d,wilcox.test(verbRatio~Discipline))

with(d, tapply(WordLength,list(Discipline),mean,na.rm=TRUE))
with(d,wilcox.test(WordLength~Discipline))

with(d, tapply(adverbRatio,list(Discipline),mean, na.rm=TRUE))
with(d,wilcox.test(adverbRatio~Discipline))

with(d, tapply(adjectiveRatio,list(Discipline),mean, na.rm=TRUE))
with(d,wilcox.test(adjectiveRatio~Discipline))

with(d, xtabs(~Discipline+Clause))
with(d, chisq.test(xtabs(~Discipline+Clause)))

