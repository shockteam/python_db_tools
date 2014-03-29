(linkedin)dpugache@dpugache-mn1 [python_db_tools]$ ./mysql_fk_check --table inDB.Entity --id 12949 --all

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

+---------------------------+-----------------------------+
| TABLE NAME                | FK NAME                     |
+---------------------------+-----------------------------+
| inDB.Alias                | Alias_ibfk_1                |
| inDB.Asset                | Asset_ibfk_1                |
| inDB.Cabinet              | Cabinet_ibfk_1              |
| inDB.CabinetTemplate      | CabinetTemplate_ibfk_1      |
| inDB.Cage                 | Cage_ibfk_1                 |
| inDB.ClassGroup           | ClassGroup_ibfk_1           |
| inDB.Company              | company_ibfk_1              |
| inDB.ComponentStock       | ComponentStock_ibfk_1       |
| inDB.Core                 | Core_ibfk_1                 |
| inDB.CustomData           | CustomData_ibfk_1           |
| inDB.CustomDataDefinition | CustomDataDefinition_ibfk_1 |
| inDB.Device               | Device_ibfk_1               |
| inDB.EntityApplications   | EntityApplications_ibfk_1   |
| inDB.EntityComponent      | EntityComponent_ibfk_1      |
| inDB.EntityCoordinates    | entitycoordinates_ibfk_1    |
| inDB.EntityCost           | EntityCost_ibfk_1           |
| inDB.EntityLocation       | EntityLocation_ibfk_1       |
| inDB.EntityLocation       | EntityLocation_ibfk_2       |
| inDB.EntityPiqMap         | EntityPiqMap_ibfk_1         |
| inDB.EntityRelationship   | EntityRelationship_ibfk_1   |
| inDB.EntityRelationship   | EntityRelationship_ibfk_2   |
| inDB.EntityTemplateMap    | EntityTemplateMap_ibfk_1    |
| inDB.EntityTypeEntity     | EntityTypeEntity_ibfk_1     |
| inDB.Fault                | Fault_ibfk_1                |
| inDB.FaultType            | FaultType_ibfk_1            |
| inDB.HardwareAddress      | HardwareAddress_ibfk_1      |
| inDB.Move                 | Move_ibfk_1                 |
| inDB.Move                 | Move_ibfk_3                 |
| inDB.Move                 | Move_ibfk_4                 |
| inDB.ProductionState      | ProductionState_ibfk_1      |
| inDB.Reservation          | Reservation_ibfk_1          |
| inDB.Site                 | Site_ibfk_1                 |
| inDB.Team                 | team_ibfk_1                 |
| inDB.Template             | Template_ibfk_1             |
| inDB.User                 | user_ibfk_1                 |
| inDB.UserGroup            | usergroup_ibfk_1            |
| inDB.UserGroupEntityMap   | UserGroupEntityMap_ibfk_2   |
+---------------------------+-----------------------------+
