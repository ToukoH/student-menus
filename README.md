### Description
If you are like me and spend a good amount of time in terminal, this is a convinient way to get different menus of the student restaurants in Helsinki/Otaniemi area.

### Prerequisites
- Python 3.x
- `requests` and `beautifulsoup4` 

### Steps
1. Clone the script to your local machine.
2. Navigate to the script's directory.
3. Run the provided setup script to create a symbolic link. This allows you to run the script from anywhere in your terminal.

   ```bash
   chmod +x setup.sh
   ./setup.sh
   ```
### Usage
Run the script using the command safkat followed by the area number. If no area number is provided, the script defaults to area 1 (Otaniemi).

```safkat -<area_number>```
