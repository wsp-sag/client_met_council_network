## Batch Approach to Met Council Travel Model
The Met Council travel model was historically configured to run through a Cube 
Cataolog file which controls several Applications files. This document contains 
instructions to run the model using a batch file. In the catalog approach, 
users declare a scenario and fill out declare several important variables. The 
batch file sets those same variables, but requires the user to set them directly 
and there is likely room for improvement and feedback from Met Council staff to 
ensure that the process is clear and simple.

### Running the Batch File
The batch file approach is entirely contained in the met_council_model folder of 
the improve_batch_file branch. 

#### Folder Structure
Only the relevant folders for running the model through the batch file are 
discussed here. Folder and file descriptions accompany the hierarchy.
    - *data*: Contains all data (excluding lookup files) necessary to run the model.
        - *abm_logs*: Scenario print files are sent to this folder (not yet implemented).
        - *external*: Primary repository for input files needed to run the model.
        Contact john.helsel@wsp.com to receive a OneDrive link with this data 
        (since it is too large to commit to github). The data in the OneDrive 
        link should be downloaded and placed into the *external* folder in the 
        same structure present on the OneDrive link. The folder names within 
        *external* show the user who was responsible for creating the data.
        - *interim*: Outputs of the model created during model execution. 
        - *processed*: Finalized outputs from the model (not yet implemented).
    - *models*: Cube and TourCast script files as well as lookup files necessary 
    to run the MetCouncil ABM model.
        - *batch_file_abm*: The batch files, Cube scripts, TourCast binary and 
        input files, and lookup files necessary to run the model.
        - *cube_catalog_abm*: The MetCouncil ABM structure set up to run in Cube 
        catalog as delivered to WSP in January 2019.
    - *references*: Reference documents.

#### Running the model using batch files.
Batch files provide users a straightforward, text-file-controlled method for 
running the travel model. This method improves on the Cube Application process 
by ensuring changes in scripts can be easily tracked within Github (as opposed 
to binary catalog files) and permitting debugging by disentangling loops from 
Cube's abstraction process. This subsection provides step by step instructions 
for running the model "out of the box".

1) Download the *improve_batch_file* branch of the *client_met_council_network*.
2) Obtain a link to the *external* data folder from john.helsel@wsp.com. 
Download the data and insert into the empty *external* folder. Do not compress 
or alter the folder structure of this data.
3) In Windows File Explorer, navigate to *met_council_git/models/batch_file_abm*
and open *set_parameters.bat* in a text editor. Ensure that all supplied 
variables are correct. In Cube, you managed these values through the Key values. 
All of these values must be set manually now.
3) Open a Windows Powershell window and navigate to the *batch_file_abm* folder.
  - E.g. *cd C:\Users\jhelsel\client_met_council_network\models\batch_file_abm*
4) Run the batch file
  - *.\met_council_model.bat*

#### General batch commands
Batch files are very flexible, but can also be maddeningly obscure and throw 
up odd errors. Below, I've listed issues that I have run into over the past 
few months that will likely come into play as users adapt the batch file for 
their own purposes. This is not intended to be an exhaustive list of issues or 
work arounds, but I hope it is helpful.

Wikis and stackoverflow are invaluable resources since many users have asked and 
answered the problems that are likely to crop up in this project. But, I highly 
recommend https://en.wikibooks.org/wiki/Windows_Batch_Scripting and 
https://docs.microsoft.com/en-us/windows-server/administration/windows-commands/windows-commands 
as authoritative lists for finding all relevant commands and for useful documentation.

- FRAGILE FILE PATHS: To execute the model, users must pass a mixture of 
absolute and relative file paths between powershell, Cube, and python. These 
file paths are very, very fragile. Most errors causing the model to crash can be 
traced to an incorrect file path or a missing file. During debugging, users will 
should always check cube print files for IO errors and determine whether the 
file path is incorrect or whether the file is missing from the ready to download 
package. This is particularly true for TourCast, since the json files which 
guide TourCast are updated as absolute file paths and the log files are 
overwritten during model execution.
- CAPITALIZATION: Cube supports generous interpretations of user inputs and is 
often insensitive to user capitalization. Batch file paths and variable names 
(but not command line commands) are sensitive to capitalization and it is 
important for the user to sanitize their inputs and ensure that capitalizations 
are respected.
- TRAILING WHITESPACE CHARACTERS: Batch variables are strings that run to the end 
of the line. If users are experiencing unexplained errors for files written by or 
read into the model, they may be attributable to trailing space or tab characters 
that are not easily visible to the analyst. Users should check file names for 
extra spaces and ensure that looped variables (e.g. AM, PM, etc.) are properly 
specified.
- REPLACING CUBE TOKENS: Cube uses "{}@" characters as tokens where variable 
names are swapped to a literal string or numeric. Batch file uses "%" or "!" for 
that purpose.
- FOR LOOPS: By default, batch file evaluates variable names at the beginning of 
execution. This can cause problems in for loops that iterate over a series of 
values. To avoid this problem, ensure that the command 
"SetLocal EnableDelayedExpansion" is active at the top of the script and then 
use "!" instead of "%" to ensure that variable replacements are updated within 
the loop.
- COMMENTS: Batch files recognize double colons as comments ("::"). These should 
be placed at the start of the line. To create block comments (either for large 
chunks of explanatory text or to disable scripts for partial runs), begin comments 
with the line "%beginComment%" and end comments with the line ":endComment".

