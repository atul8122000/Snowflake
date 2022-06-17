## Install SnowSQL in Linux

#### Step 1: login to your snowflake Account and follow below steps:
- help >> download >> CLI client >> [Snowflake Repository](https://sfc-repo.snowflakecomputing.com/snowsql/bootstrap/1.2/linux_x86_64/index.html)
- Right click on the latest SnowSQL CLI client link for Linux and click 'Copy link address'
 
#### Step 2: Open a terminal window and run below command.
```bash
wget <paste copied link address here>
```
##### Example:
``` bash
Wget https://sfc-repo.snowflakecomputing.com/snowsql/bootstrap/1.2/linux_x86_64/snowflake-snowsql-1.2.21-1.x86_64.rpm
```

#### Step 3: Install alien to run .rpm package
``` bash
sudo apt-get install alien
```

#### Step 4: Run this command to install snosql
```bash
sudo alien -i snowflake-snowsql-1.2.21-1.x86_64.rpm
```
#### Once installed, verify the installation by checking the version of SnowSQL.
```bash
snowsql -v
```
#### You can display the help section of SnowSQL client by running the following command:
```bash
snowsql
```

## Connect Snowflake using SnowSQL in Linux
```bash
snowsql -a <account-name> -u <username>
```
#### Example:
##### Web URL of Account: https://uz64318.southeast-asia.azure.snowflakecomputing.com/console#/internal/worksheet
##### Account name: uz64318.southeast-asia.azure
##### User Name: OSTECHNIX
#### Example:
```bash
snowsql -a uz64318.southeast-asia.azure -u OSTECHNIX
```






