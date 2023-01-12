# AzureDevops-CICD-Pipeline
This is Azure CICD pipeline code wich perform the below actions-
1. Trigger the build if any changes get pushed in Git.
2. setup databricks enviorment.
3. Run test cases using "sbt assembly".
4. create the assembly jars for sbumodules using "sbt assembly".
5. increase build number using "sbt release with-defaults".
6. push new version number in git.
7. create sumodules directory in dbfs location and jar files.
8. delete older jar files from dbfs submodules directory.
