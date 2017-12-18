hillclimber_sim_an <- read.table("~/git/railnl_new/railns_NetX/data/hillclimber_sim_an.csv", quote="\"", comment.char="")

length_data = nrow(hillclimber_sim_an)

plot(seq(1,length_data),hillclimber_sim_an[1:length_data,1],xlab="Aantal iteraties",ylab="Score",main="Hillclimber nationaal")

lines(seq(1,length_data),hillclimber_sim_an[1:length_data,1])

