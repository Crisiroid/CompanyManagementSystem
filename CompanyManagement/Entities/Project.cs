using System.ComponentModel.DataAnnotations;

namespace CompanyManagement.Entities
{
    public class Project
    {
        [Key]
        public int ProjectId { get; set; }

        [Required, MaxLength(100)]
        public string ProjectName { get; set; } = string.Empty;

        public string? Description { get; set; }

        [Required]
        public DateTime StartDate { get; set; }

        public DateTime? EndDate { get; set; }

        public decimal? Budget { get; set; }

        public int? DepartmentId { get; set; }
        public Department? Department { get; set; }

        public ICollection<EmployeeProject> EmployeeProjects { get; set; } = new List<EmployeeProject>();
    }

}
