# Azure specific topics

## Docker & co.

__Hardware requirements__ to enable _WSL 2_:
* 4 GB RAM
* BIOS-Enabled virtualization
* Windows 10 64-bit

## Data Science Virtual Machine (DSVM) for Linux and Windows

[DSVM](https://learn.microsoft.com/en-us/azure/machine-learning/data-science-virtual-machine/overview) is a customized image for Data sicence. Azure Machine Learning (AzureML) however, is an end-to-end platform. The DSVM offers more flexibility. For instance it supports more languages, RDP Access, windows etc.

Notes:
* PostgreSQL is installed by default on Ubuntu, hence on DSVM for Ubuntu.

## Storage

Copying data to or from _Azure Blob Storage_ is done via the following tools:
* Python
* Azure Storage Explorer
* SSIS
* AzCopy

## Data Formats

* __ARFF(Attribute related file format)__ is used by Weka environment
    * __Weka__ is a collection of ML algorithms for data mining tasks on Windows Server 2019


## Azure Machine Learning Studio (Designer)

### Data Preparation Modules
* __Add columns__: Used to add a feature to the dataset.
* __Clean missing data__: Two important substitution techniques are
    * Multivariate Imputation using Chained Equation (MICE): In contrast to univariate methods like _mean_, _median_ etc. that look at only one column to fill the missing values of that column, this method takes other columns into consideration. Read this [article](https://www.numpyninja.com/post/mice-algorithm-to-impute-missing-values-in-a-dataset).
    * PCA:
* __Convert to Indicator Values__: Performs One Hot Encoding
* __SMOTE__: Used for oversampling. It is better than simply duplicating the underrepresented rows.


### Regression Modules
* __Poisson Regression__: A regression analysis used typically to model __counts__. E.g: Estimating the number of emergency service calls during an event. Projecting the number of customer inquiries subsequent to a promotion:
    * It has a poisson distribution.
    * It must be a whole number.
    * It must be positive number.

# General Data Science topics

## Deep Learning

### Recurrent Neural Networks (RNNs)
These types of networks are designed to take sequences of text as inputs or return sequences of text as outputs, or both. They're called recurrent because the network's hidden layers have a loop in which the output and cell state from each time step become inputs at the next time step. This recurrence serves as a form of memory.
It allows contextual information to flow through the network so that relevant outputs from previous time steps can be applied to network operations at the current time step.