using System.ComponentModel.DataAnnotations;

namespace CompanyManagement.Entities
{
    public class Department
    {
        [Key]
        public int DepartmentId { get; set; }

        [Required, MaxLength(100)]
        public string DepartmentName { get; set; } = string.Empty;

        public string? Description { get; set; }

        public ICollection<Employee> Employees { get; set; } = new List<Employee>();
        public ICollection<Project> Projects { get; set; } = new List<Project>();
    }

}
