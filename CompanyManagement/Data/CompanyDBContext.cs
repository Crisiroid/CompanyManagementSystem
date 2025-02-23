using Microsoft.EntityFrameworkCore;

namespace CompanyManagement.Data
{
    public class CompanyDBContext : DbContext
    {
        public CompanyDBContext(DbContextOptions options) : base(options) { }
        //public DbSet<User> Users { get; set; }
        //public DbSet<Token> Tokens { get; set; }
    }
}
