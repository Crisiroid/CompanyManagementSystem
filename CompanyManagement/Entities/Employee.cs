using System.ComponentModel.DataAnnotations;

namespace CompanyManagement.Entities
{
    public class Employee
    {
        [Key]
        public int EmployeeId { get; set; }

        [Required, MaxLength(50)]
        public string FirstName { get; set; } = string.Empty;

        [Required, MaxLength(50)]
        public string LastName { get; set; } = string.Empty;

        [Required, EmailAddress, MaxLength(100)]
        public string Email { get; set; } = string.Empty;

        [MaxLength(20)]
        public string? Phone { get; set; }

        [Required]
        public DateTime HireDate { get; set; } = DateTime.UtcNow;

        [Required]
        public decimal Salary { get; set; }

        public int? ManagerId { get; set; }
        public Employee? Manager { get; set; } 

        public int? DepartmentId { get; set; }
        public Department? Department { get; set; }

        public ICollection<EmployeeProject> EmployeeProjects { get; set; } = new List<EmployeeProject>();
    }

}
