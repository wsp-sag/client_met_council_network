## Batch Approach to Met Council Travel Model
The Met Council travel model is currently configured to run through a Cube Cataolog file which controls several Applications files. This document contains instructions to run the model using a batch file. In the catalog approach, users declare a scenario and fill out declare several important variables. The batch file sets those same variables, but requires the user to set them directly and there is likely room for improvement and feedback from Met Council staff to ensure that the process is clear and simple.

### Running the Batch File
The batch file approach is entirely contained in the replacement_networks folder of the client_met_council_network branch. 

#### Folder Structure
Only the relevant folders for running the model through the batch file are discussed here. Description proceeds through the hierarchy.
  - *replacement_networks*: all work on the batch file is contained in replacement_networks.
    - *inputs*: contains zonal, household, and person data files taken directly from the CS model. (There are also reduced versions of the household and person files with the first 100 household IDs in order to decrease run times for testing.)
    - *lookup_files*: contains all necessary lookup files. Roughly corresponds to the *Inputs* folder in original model folder structure.
    - *network_06242019*: contains the new networks being tested by WSP. New networks will receive a similarly named folder.
    - *network_test_outputs*: contains abbreviated model outputs after running assignment on the latest highway network using trip tables converged on the old highway network (iteration 4).
    - *original_trip_tables*: converged trip tables from model runs with the original highway network. Used during assignment testing of new WSP networks.
    - *outputs*: all model outputs generated during the run are directed here (except for trip tables).
    - *replacement_scripts*: all cube scripts necessary to run the model. These are taken as directly as possible from the files provided by Cambridge Systematics. Most changes involved converting Cube Key characters ("{}@") to percent signs recognized by batch ("%"), simplifying file paths, and moving system commands out of cube scripts.
    - *TourCast*: all scripts and executables related to Cambridge Systematics'TourCast ABM. Certain scripts are updated during processing to ensure correctness of file paths.
    - *trip_files*: Trip files produced by the model run are directed here. (Perhaps these should be redirected?)
    - *replacement_networks.bat*: batch file containing instructions to run the complete travel model. Users must carefully check input file paths and variable values to ensure they are suitable for user's needs.
    - *test_new_networks.bat*: batch file containing instructions to run highway assignment (to convergence) on WSP's highway networks using trip tables taken from a converged travel model provided to WSP by Cambridge Systematics at the beginning of the project.
    - *TourCast.bat*: batch file containing instructions to run TourCast. Invoked by *replacement_networks.bat*.
    
#### Running the model using batch files.
Batch files provide users a straightforward, text-file-controlled method for running the travel model. This method improves on the Cube Application process by ensuring changes in scripts can be easily tracked within Github (as opposed to binary catalog files) and permitting debugging by disentangling loops from Cube's abstraction process. This subsection provides step by step instructions for running the model "out of the box".

1) Download the *walk_bike_skims* branch of the *client_met_council_network* repo and navigate to the replacement_networks folder.
2) Carefully examine *replacement_networks.bat* to ensure all supplied variable values are correct. In Cube, you managed these values through the Key values. But all of these values must be set manually now. (One future improvement would be to set the variables in an accompanying text file. But it's much easier to turn individual parameters off and on from within a single batch file for testing purposes.)
3) Open a Windows Powershell window and navigate to the replacement_networks folder.
  - E.g. *cd C:\Users\jhelsel\client_met_council_network\replacement_networks*
4) Run the batch file
  - *.\replacement_networks.bat*

#### General batch commands
Batch files are very flexible, but can also be maddeningly arcane and throw up odd errors. Below, I've listed issues that I have run into over the past few months that will likely come into play as users adapt the batch file for their own purposes. This is not intended to be an exhaustive list of issues or work arounds, but I hope it is helpful.

Wikis and stackoverflow are invaluable resources since many users have asked and answered the problems that are likely to crop up in this project. But, I highly recommend https://en.wikibooks.org/wiki/Windows_Batch_Scripting and https://docs.microsoft.com/en-us/windows-server/administration/windows-commands/windows-commands as authoritative lists for finding all relevant commands and for useful documentation.

- CAPITALIZATION: Cube supports generous interpretations of user inputs and is often insensitive to user capitalization. Batch file paths and variable names (but not command line commands) are sensitive to capitalization and it is important for the user to sanitize their inputs and ensure that capitalizations are respected.
- REPLACING CUBE TOKENS: Cube uses "{}@" characters as tokens where variable names are swapped to a literal string or numeric. Batch file uses "%" or "!" for that purpose.
- FOR LOOPS: By default, batch file evaluates variable names at the beginning of execution. This can cause problems in for loops that iterate over a series of values. To avoid this problem, ensure that the command "SetLocal EnableDelayedExpansion" is active at the top of the script and then use "!" instead of "%" to ensure that variable replacements are updated within the loop.
- COMMENTS: Batch files recognize double colons as comments ("::"). These should be placed at the start of the line. To create block comments (either for large chunks of explanatory text or to disable scripts for partial runs), begin comments with the line "%beginComment%" and end comments with the line ":endComment".

### Future improvements
The current approach has focused on *replacing* Cube Application functionality, but not on *improving* the model or removing bugs.
1) Move variables into a dedicated parameter file. This will hopefully improve readability and useability, as it will help users avoid having to hunt and search throughout the batch file to find all variables which may need to be updated.
2) Most of the files are highly generalized and do not contain manual interventions on a specific skim or zone. WSP (with guidance from Met Council staff) should identify scripts where Cube procedures were adjusted in ways tied to specific zones or links in order to ensure that those interventions are still needed, applied to the correct place, and otherwise suitable. Where they are now obsolete, they should be removed.
