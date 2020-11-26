# Predicting the half maximal inhibitory concentration of various drugs on tyrosine protein kinase receptor FLT3 using machine learning model


![OIP](https://user-images.githubusercontent.com/71454551/100383427-96731a80-3043-11eb-8061-70d435030fab.png)

Machine Learning approaches provides a set of tool that can improve drug discovery and decision making for well defined questions with abundant, high quality data. 
Interpretation of model wil allow us to understand, How we can design a better drug. 
### Machine learning is a working horse of modern drug discovery and has been ever since the early days of QSAR.

## DATA COLLECTION 

The data is downloaded from chEMBL(ChEMBL is a manually curated database of bioactive molecules with drug-like properties. It brings together chemical, bioactivity and genomic data to aid the translation of genomic information into effective new drugs) using chembl_webresource_client library. The library is developed and supported by chEMBL group. The library help accessing chEMBL data.
The dataset is comprised of compounds that have been biologically tested for their activity towards target.

##### Here is a flowchart for dataset preparation :- 

![DATA PREP](https://user-images.githubusercontent.com/71454551/100384002-1a79d200-3045-11eb-9198-35bc75cbb41a.png)

###### Labeling the compounds as Active/Inactive/Intermediate
Compunds are being labeled(Active\Inactive\Intermediate) based on their potency value (IC50 is half maximal Inhibitory concentration. Its is the most widely used and informative measure of a drugs efficacy. It indicates how much drug is needed to inhibit a biological process by half, thus providing a measure of potency of an antagonist drug in pharmacological research.) 
compounds having values < 1000 nM will be considered active , Those greater than 10000 nM will be considered to be inactive. 
A function is created to label the molecules present in dataset.

##### Converting IC50 values to pIC50
The nature of potency values is logarithmic.If you look at dose-response curves, they are sigmoidal when you plot them in logarithmic space.

![DRC](https://user-images.githubusercontent.com/71454551/100385047-96751980-3047-11eb-84bf-5e44fd29dbb2.png)

Using pIC50 is the proper way to think about the data.
If your potency goes down because you've gone from micromolar to nanomolar, that’s an exponential change, not a linear change.
pIC50 is really the right way to think about potency of compounds. A function is created to convert IC50 values to logarithmic values.


## "Lipinski Rule of Five"
Lipinski rule of 5 helps in distinguishing between drug like and non drug like molecules. It predicts high probability of success or failure due to drug likeness for molecules complying with 2 or more of the following rules

1. No more than 5 hydrogen bond donors (the total number of nitrogen–hydrogen and oxygen–hydrogen bonds)
2. No more than 10 hydrogen bond acceptors (all nitrogen or oxygen atoms)
3. A molecular mass less than 500 daltons
4. An octanol-water partition coefficient[6] (log P) that does not exceed 5

A function is created to calculate molecular weight, logP, number of H donor and number of H acceptor.

![DATA processing](https://user-images.githubusercontent.com/71454551/100385591-12bc2c80-3049-11eb-9841-c527f83ba757.png)






