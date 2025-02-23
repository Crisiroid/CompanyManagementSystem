using System.ComponentModel.DataAnnotations;

namespace CompanyManagement.Entities
{
    public class Salary
    {
        [Key]
        public int SalaryId { get; set; }

        [Required]
        public int EmployeeId { get; set; }
        public Employee Employee { get; set; } = null!;

        [Required]
        public decimal BaseSalary { get; set; }

        public decimal Bonus { get; set; } = 0;
        public decimal Deduction { get; set; } = 0;

        public decimal TotalSalary => BaseSalary + Bonus - Deduction;

        [Required]
        public DateTime PaymentDate { get; set; }
    }

}
