using CompanyManagement.Models;
using Microsoft.AspNetCore.Authorization;
using Microsoft.AspNetCore.Mvc;
using System.Diagnostics;

namespace CompanyManagement.Controllers
{
    public class HomeController : Controller
    {
        private readonly ILogger<HomeController> _logger;


        public HomeController(ILogger<HomeController> logger, FlaskApiService flaskApiService)
        {
            _logger = logger;

        }

        [Authorize]
        public IActionResult Index()
        {
            return View();
        }


        public async Task<IActionResult> AuthenticateUser([FromForm] IFormFile image)
        {
            if (image == null)
            {
                return BadRequest(new { message = "Image file is required" });
            }

            var response = await _flaskApiService.AuthenticateUserAsync(image);
            return Ok(response);
        }

        [HttpPost("register")]
        public async Task<IActionResult> RegisterUser([FromForm] string name, [FromForm] IFormFile image)
        {
            if (string.IsNullOrEmpty(name) || image == null)
            {
                return BadRequest(new { message = "Name and image are required" });
            }

            var response = await _flaskApiService.RegisterUserAsync(name, image);
            return Ok(response);
        }
        [ResponseCache(Duration = 0, Location = ResponseCacheLocation.None, NoStore = true)]
        public IActionResult Error()
        {
            return View(new ErrorViewModel { RequestId = Activity.Current?.Id ?? HttpContext.TraceIdentifier });
        }
    }
}
