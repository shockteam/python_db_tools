### mysql_fk_check

Lists all tables with corresponding foreign key names that reference a particular table or ID, example:

```

$ ./mysql_fk_check --table inDB.Entity --id 12949 --all

inDB.Entity.entity_id '12949' is referenced in the following tables: 

+----------------------+------------------------+
| TABLE NAME           | FK NAME                |
+----------------------+------------------------+
| inDB.Asset           | Asset_ibfk_1           |
| inDB.Device          | Device_ibfk_1          |
| inDB.EntityComponent | EntityComponent_ibfk_1 |
| inDB.EntityCost      | EntityCost_ibfk_1      |
| inDB.EntityLocation  | EntityLocation_ibfk_1  |
| inDB.Fault           | Fault_ibfk_1           |
| inDB.ProductionState | ProductionState_ibfk_1 |
+----------------------+------------------------+

Complete list of references for inDB.Entity.entity_id : 

```
