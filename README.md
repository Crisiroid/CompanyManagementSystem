# 🏢 Company Management System

## 📖 Project Overview
The **Company Management System** is designed to manage employees, departments, projects, salaries, and attendance records within an organization. This system provides structured data management, ensuring efficient tracking of employee activities and organizational operations.

## 👥 Authors
- **Amir Sajjad Hosein Pour**  
- **Alireza Rostami**  

## 🛠️ Technologies Used
- **ASP.NET 8** (Web API & MVC)
- **Entity Framework Core** (Code-First Approach)
- **SQL Server** (Database)
- **C#** (Backend Development)
- **Mermaid.js** (ER Diagram Visualization)

## 📌 Features
✅ **Employee Management** - Add, edit, delete, and view employee details.  
✅ **Department Management** - Manage departments and their employees.  
✅ **Project Assignment** - Assign employees to projects and define roles.  
✅ **Attendance Tracking** - Track employee attendance with check-in/check-out times.  
✅ **Salary Management** - Manage employee salaries, bonuses, and deductions.  
✅ **User Authentication** - Secure login system with roles and hashed passwords.  


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


## 🏗️ How to Run the Project
### 📌 **Prerequisites**
1. **Visual Studio 2022** (or later)  
2. **SQL Server 2019+**  
3. **.NET 8 SDK**  
4. **Entity Framework Core CLI**  

### 🚀 **Installation Steps**
1️⃣ Clone the repository:  
   ```sh
   git clone https://github.com/your-repo/company-management.git
   cd company-management
   ```

2️⃣ Restore dependencies:  
   ```sh
   dotnet restore
   ```

3️⃣ Apply database migrations:  
   ```sh
   dotnet ef database update
   ```

4️⃣ Run the project:  
   ```sh
   dotnet run
   ```

## 🔒 User Roles
| Role        | Description |
|-------------|------------|
| **Admin**   | Full access to the system |
| **Manager** | Can manage employees and projects |
| **Employee**| Can view personal data and attendance |

## 📜 License
This project is **open-source** under the **MIT License**.

---

### 🎯 **Contributions & Feedback**
We welcome contributions! Feel free to submit issues and pull requests.  
For any feedback, contact **Amir Sajjad Hosein Pour** or **Alireza Rostami**.  

