using System.ComponentModel.DataAnnotations;

namespace CompanyManagement.Entities
{
    public class Attendance
    {
        [Key]
        public int AttendanceId { get; set; }

        [Required]
        public int EmployeeId { get; set; }
        public Employee Employee { get; set; } = null!;

        [Required]
        public DateTime AttendanceDate { get; set; }

        public TimeOnly? CheckInTime { get; set; }
        public TimeOnly? CheckOutTime { get; set; }

        [Required, MaxLength(20)]
        public string Status { get; set; } = "Present"; // Present, Absent, Late, Leave
    }

}
