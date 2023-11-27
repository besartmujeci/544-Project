using System;
using System.Collections.Generic;
using System.IO;
using System.Text;
using System.Text.RegularExpressions;
using iTextSharp.text.pdf;
using iTextSharp.text.pdf.parser;
using System.Linq;
using System.Threading.Tasks;

using OpenAI.GPT3.Managers;
using OpenAI.GPT3;
using OpenAI.GPT3.ObjectModels;
using OpenAI.GPT3.ObjectModels.RequestModels;

class Program
{
    static async Task Main(string[] arg)
    {
        GetTextFromPDF();
        //await GetTextFromOpenAIAPI();
    }

    static void GetTextFromPDF()
    {
        string folderPath = "/Users/ruturajchintawar/Downloads/Davis-Besse_LERs/";

        List<string> files = Directory.GetFiles(folderPath).ToList();

        int count = files.Count();
        int suc = 0;

        // Output CSV file path
        string csvFilePath = "/Users/ruturajchintawar/Downloads/output.csv";

        // Create or overwrite the CSV file
        using (StreamWriter csvWriter = new StreamWriter(csvFilePath))
        {
            // Write header to CSV
            csvWriter.WriteLine("Filename,ExtractedText");

            foreach (string filename in files)
            {
                if (System.IO.Path.GetExtension(filename) == ".pdf")
                {
                    StringBuilder text = new StringBuilder();
                    using (PdfReader reader = new PdfReader(filename))
                    {
                        for (int i = 1; i <= reader.NumberOfPages; i++)
                        {
                            text.Append(PdfTextExtractor.GetTextFromPage(reader, i));
                        }
                    }

                    // Define patterns
                    string pattern = @"CAUSE OF EVENT:(.*?)(ANALYSIS OF EVENT:)";
                    string pattern2 = @"APPARENT CAUSE OF OCCURRENCE:(.*?)(ANALYSIS OF OCCURRENCE:)";

                    Regex regex = new Regex(pattern, RegexOptions.Singleline);
                    Regex regex2 = new Regex(pattern2, RegexOptions.Singleline);

                    string extractedText = "";

                    // Check for matches using both patterns
                    Match match = regex.Match(text.ToString());
                    Match match2 = regex2.Match(text.ToString());

                    // Choose the match with content
                    if (match.Success)
                    {
                        extractedText = match.Groups[1].Value.Trim();
                        suc++;
                    }
                    else if (match2.Success)
                    {
                        extractedText = match2.Groups[1].Value.Trim();
                        suc++;
                    }
                    else
                    {
                        Console.WriteLine("Pattern not found in the text.");
                    }

                    // Escape double quotes in the extracted text
                    extractedText = extractedText.Replace("\"", "\"\"");

                    // Enclose the value in double quotes
                    extractedText = $"\"{extractedText}\"";

                    // Write to CSV
                    csvWriter.WriteLine($"{System.IO.Path.GetFileName(filename)},{extractedText}");

                    Console.WriteLine(System.IO.Path.GetFileName(filename));
                    Console.WriteLine(extractedText);
                }
            }
        }

        Console.WriteLine($"Total files: {count}");
        Console.WriteLine($"Files with extraction: {suc}");

    }

    static async Task GetTextFromOpenAIAPI()
    {
        var service = new OpenAIService(new OpenAiOptions
        {
            ApiKey = "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"
        });

        service.SetDefaultModelId(Models.ChatGpt3_5Turbo);

        var messages = new List<ChatMessage>
        {
            ChatMessage.FromSystem("What is the cause of event?"),
            ChatMessage.FromUser(Console.ReadLine())
        };
        var req = new ChatCompletionCreateRequest
        {
            Messages = messages,
            N = 1,
            //MaxTokens = 2000,
            //FrequencyPenalty = 2.0f,
            //Temperature = 0.1f
        };

        var res = await service.ChatCompletion.CreateCompletion(req);

        if (res.Successful)
        {
            var resultContent = res.Choices.First().Message.Content;
            Console.WriteLine(resultContent);
        }

    }
}
