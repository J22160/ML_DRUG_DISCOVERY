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

Compunds are being labeled(Active\Inactive\Intermediate) based on their potency value (IC50 is half maximal Inhibitory concentration. Its is the most widely used and informative measure of a drugs efficacy. It indicates how much drug is needed to inhibit a biological process by half, thus providing a measure of potency of an antagonist drug in pharmacological research.) 
compounds having values < 1000 nM will be considered active , Those greater than 10000 nM will be considered to be inactive. 

