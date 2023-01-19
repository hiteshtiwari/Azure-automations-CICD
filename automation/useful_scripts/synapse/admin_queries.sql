-- Fetch schema and tables name
select schema_name(schema_id) as schemas_name, name as table_name from sys.tables order by schemas_name;
-- Fetch schema and views name
select schema_name(schema_id) as schemas_name, name as view_name from sys.views order by schemas_name;


-- Fetch users who are having access of schema
SELECT state_desc, permission_name, class_desc,
       SCHEMA_NAME(major_id) as schema_name ,
       USER_NAME(grantee_principal_id) as user_name
       FROM sys.database_permissions AS Perm
       JOIN sys.database_principals AS Prin
       ON Perm.major_ID = Prin.principal_id AND class_desc = 'SCHEMA' order by schema_name;
       
       
-- #Azure #Microsoft_Azure #Synapse
