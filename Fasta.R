library(bio3d)
demo("pdb")
demo("pca")

pdb <- read.pdb("myfile.pdb")
pdb <- read.pdb("/path/to/my/data/myfile.pdb")



blast <‐ blast.pdb(aa)

hits <‐ plot(blast)

install.packages("seqinr")
library("seqinr") # This line importing the seqinr library 
dnaseq<- read.fasta(file = "/Users/andrewsingari/Downloads/sequence1.fasta")   


gravy_scores <- sapply(dnaseq, gravy)


gravy(dnaseq)



install.packages("ggplot")
library("ggplot")

# Create the bar graph
ggplot(df, aes(x=protein, y=gravy_score, fill=protein)) + 
  geom_bar(stat="identity", color="black") +
  theme_classic() +
  ggtitle("GRAVY Score for Protein Sequence AEN69297.1") +
  xlab("Protein Sequence") +
  ylab("GRAVY Score")



# Define the amino acid hydrophobicity values
hydrophobicity <- c("A"=-0.5, "C"=0.4, "D"=3.0, "E"=3.0, "F"=1.9, "G"=-0.4, "H"=-3.2, "I"=1.8, "K"=3.0, "L"=1.8, 
                    "M"=1.3, "N"=3.0, "P"=-1.6, "Q"=2.5, "R"=3.0, "S"=0.6, "T"=0.5, "V"=1.1, "W"=-0.9, "Y"=-0.7)

# Compute the GRAVY score
seq <- dnaseq[["AEN69297.1"]]
seq <- toupper(seq)  # convert to uppercase
seq <- gsub("[^ACDEFGHIKLMNPQRSTVWY]", "", seq)  # remove non-amino acid characters
gravy_score <- sum(hydrophobicity[as.character(strsplit(seq, "")[[1]])]) / nchar(seq)
gravy_score




























