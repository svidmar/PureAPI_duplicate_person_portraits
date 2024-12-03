
# Profile Photo Checker for Pure's API

This Python script identifies persons in the Pure API who have more than one profile photo with the URI `/dk/atira/pure/person/personfiles/portrait`. The script handles pagination, displays progress, logs results, and gracefully manages errors.

## Features

- **Pagination Handling**: Fetches data in chunks using `offset` and `size` parameters.
- **Progress Meter**: Displays real-time progress with the `tqdm` library.
- **Error Handling**: Logs errors and skips problematic pages to ensure continuous execution.
- **Logging**: Logs the UUIDs of persons with multiple profile photos to a file.

## Requirements

- Python 3.6 or higher
- Install required packages:
  ```bash
  pip install requests tqdm
  ```

## Usage

1. Clone the repository or download the script.
2. Replace `your_api_key` in the script with your actual API key for the VBN API.
3. Run the script:
   ```bash
   python dup_portrait.py
   ```
4. The script will:
   - Fetch data from the Pure API.
   - Identify persons with more than one profile photo with the specified URI.
   - Log results to `persons_with_multiple_photos.log`.

5. Check the progress in the terminal and view the results in the log file.

## Output

- The script generates a log file: `persons_with_multiple_photos.log`.
- Example log entry:
  ```
  2024-12-03 12:00:00 - Person 4b4ef840-2a6c-4333-bbfa-010b57b92f66 has 2 profile photos with the specified URI.
  ```

## Limitations

- Ensure the API key has the necessary permissions to access the endpoint.
- The script assumes the API adheres to standard RESTful conventions.

## Contributing

Contributions are welcome! Feel free to submit a pull request or open an issue.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.
