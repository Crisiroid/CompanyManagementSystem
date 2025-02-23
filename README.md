# Company Management System ER Diagram

Below is the entity-relationship diagram (ERD) for our database schema:

```mermaid
erDiagram
  AttendanceRecords {
    AttendanceId int PK
    EmployeeId int FK
    AttendanceDate datetime2 
    CheckInTime time(NULL) 
    CheckOutTime time(NULL) 
    Status nvarchar(20) 
  }
  AttendanceRecords }o--|| Employees : FK_AttendanceRecords_Employees_EmployeeId
  Departments {
    DepartmentId int PK
    DepartmentName nvarchar(100) 
    Description nvarchar(max)(NULL) 
  }
  EmployeeProjects {
    EmployeeId int PK,FK
    ProjectId int PK,FK
    Role nvarchar(50) 
  }
  EmployeeProjects }o--|| Employees : FK_EmployeeProjects_Employees_EmployeeId
  EmployeeProjects }o--|| Projects : FK_EmployeeProjects_Projects_ProjectId
  Employees {
    EmployeeId int PK
    FirstName nvarchar(50) 
    LastName nvarchar(50) 
    Email nvarchar(100) 
    Phone nvarchar(20)(NULL) 
    HireDate datetime2 
    Salary decimal(18-2) 
    ManagerId int(NULL) FK
    DepartmentId int(NULL) FK
  }
  Employees }o--|| Departments : FK_Employees_Departments_DepartmentId
  Employees }o--|| Employees : FK_Employees_Employees_ManagerId
  Projects {
    ProjectId int PK
    ProjectName nvarchar(100) 
    Description nvarchar(max)(NULL) 
    StartDate datetime2 
    EndDate datetime2(NULL) 
    Budget decimal(18-2)(NULL) 
    DepartmentId int(NULL) FK
  }
  Projects }o--|| Departments : FK_Projects_Departments_DepartmentId
  Salaries {
    SalaryId int PK
    EmployeeId int FK
    BaseSalary decimal(18-2) 
    Bonus decimal(18-2) 
    Deduction decimal(18-2) 
    PaymentDate datetime2 
  }
  Salaries }o--|| Employees : FK_Salaries_Employees_EmployeeId
  Users {
    UserId int PK
    EmployeeId int FK
    Username nvarchar(50) 
    PasswordHash nvarchar(max) 
    Role nvarchar(20) 
  }
  Users }o--|| Employees : FK_Users_Employees_EmployeeId
