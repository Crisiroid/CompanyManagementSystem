using System;
using System.Net.Http;
using System.Net.Http.Headers;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Http;
using System.IO;

public class FlaskApiService
{
    private readonly HttpClient _httpClient;

    public FlaskApiService(HttpClient httpClient)
    {
        _httpClient = httpClient;
    }

    public async Task<string> AuthenticateUserAsync(IFormFile imageFile)
    {
        using var content = new MultipartFormDataContent();

        // Convert image to StreamContent
        using var stream = imageFile.OpenReadStream();
        var fileContent = new StreamContent(stream);
        fileContent.Headers.ContentType = new MediaTypeHeaderValue("image/jpeg"); // Change if needed

        content.Add(fileContent, "image", imageFile.FileName);

        var response = await _httpClient.PostAsync("http://127.0.0.1:5050/authenticate", content);

        return await response.Content.ReadAsStringAsync();
    }

    public async Task<string> RegisterUserAsync(string name, IFormFile imageFile)
    {
        using var content = new MultipartFormDataContent();

        content.Add(new StringContent(name), "name");

        using var stream = imageFile.OpenReadStream();
        var fileContent = new StreamContent(stream);
        fileContent.Headers.ContentType = new MediaTypeHeaderValue("image/jpeg");

        content.Add(fileContent, "image", imageFile.FileName);

        var response = await _httpClient.PostAsync("http://127.0.0.1:5050/register", content);

        return await response.Content.ReadAsStringAsync();
    }
}
