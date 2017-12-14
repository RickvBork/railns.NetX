
hierholzerscores_nationaal_B <- read.table("~/git/railnl_new/railns_NetX/data/hierholzerscores_nationaal_B.csv", quote="\"", comment.char="")

hierholzerscores_nationaal_BO <- read.table("~/git/railnl_new/railns_NetX/data/hierholzerscores_nationaal_BO.csv", quote="\"", comment.char="")

hierholzerscores_nationaal_C <- read.table("~/git/railnl_new/railns_NetX/data/hierholzerscores_nationaal_C.csv", quote="\"", comment.char="")

hierholzerscores_nationaal_CO <- read.table("~/git/railnl_new/railns_NetX/data/hierholzerscores_nationaal_CO.csv", quote="\"", comment.char="")


hist(c(hierholzerscores_nationaal_B[1:1000,1]),xlab = "Score", main="Histogram score, will. begin station met één verbinding")

hist(c(hierholzerscores_nationaal_BO[1:1000,1]),xlab = "Score", main="Histogram score, will station met één verbinding en optimalisatie")

hist(c(hierholzerscores_nationaal_C[1:1000,1]),xlab = "Score", main="Histogram score, will. begin station met één verbinding, neighbor is kritiek")

hist(c(hierholzerscores_nationaal_CO[1:1000,1]),xlab = "Score", main="Histogram score, will. begin station met één verbinding, neighbor is kritiek, met optimalisatie")



######################### noordholland #################


hierholzerscores_nationaal_B <- read.table("~/git/railnl_new/railns_NetX/data/hierholzerscores_nh_B.csv", quote="\"", comment.char="")

hierholzerscores_nationaal_BO <- read.table("~/git/railnl_new/railns_NetX/data/hierholzerscores_nh_BO.csv", quote="\"", comment.char="")

hierholzerscores_nationaal_C <- read.table("~/git/railnl_new/railns_NetX/data/hierholzerscores_nh_C.csv", quote="\"", comment.char="")

hierholzerscores_nationaal_CO <- read.table("~/git/railnl_new/railns_NetX/data/hierholzerscores_nh_CO.csv", quote="\"", comment.char="")


hist(c(hierholzerscores_nationaal_B[1:1000,1]),xlab = "Score", main="Histogram score, will. begin station met één verbinding, NH")

hist(c(hierholzerscores_nationaal_BO[1:1000,1]),xlab = "Score", main="Histogram score, will station met één verbinding en optimalisatie, NH")

hist(c(hierholzerscores_nationaal_C[1:1000,1]),xlab = "Score", main="Histogram score, will. begin station met één verbinding, neighbor is kritiek, NH")

hist(c(hierholzerscores_nationaal_CO[1:1000,1]),xlab = "Score", main="Histogram score, will. begin station met één verbinding, neighbor is kritiek, met optimalisatie, NH")
