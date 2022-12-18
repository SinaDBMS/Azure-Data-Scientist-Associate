# Azure-Data-Scientist-Associate
Preparation notes for DP-100 Exam


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

### Modules

* __Convert to Indicator Values__: Performs One Hot Encoding
* __SMOTE__: Used for oversampling. It is better than simply duplicating the underrepresented rows.