using System.ComponentModel.DataAnnotations;

namespace CompanyManagement.Entities
{
    public class User
    {
        [Key]
        public int UserId { get; set; }

        [Required]
        public int EmployeeId { get; set; }
        public Employee Employee { get; set; } = null!;

        [Required, MaxLength(50)]
        public string Username { get; set; } = string.Empty;

        [Required]
        public string PasswordHash { get; set; } = string.Empty;

        [Required, MaxLength(20)]
        public string Role { get; set; } = "Employee"; // Admin, Employee, HR
    }

}
