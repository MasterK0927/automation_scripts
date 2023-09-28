import os
import subprocess
import time
import json

# Check if Visual Studio Code is installed
vscode_installed = subprocess.call(['code', '--version'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True) == 0

if not vscode_installed:
    print("Visual Studio Code is not installed. Please download and install it manually.")
else:
    print("Visual Studio Code is already installed.")

    # Open Visual Studio Code and wait for it to start
    subprocess.Popen(['code'], shell=True)
    time.sleep(5)  # Wait for 5 seconds to allow VSCode to start

    # Install VSCode extensions for competitive programming
    extensions = [
        'ms-vscode.cpptools',
        'aaron-bond.better-comments',
        'dartino.dartino',
        'coenraads.bracket-pair-colorizer',
        'mhutchie.git-graph',
        'eamodio.gitlens',
        'formulahendry.code-runner'
    ]

    for extension in extensions:
        subprocess.run(['code', '--install-extension', extension], stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)

    # Create a directory for competitive programming templates
    cp_templates_dir = os.path.expanduser('~/.cp_templates')
    os.makedirs(cp_templates_dir, exist_ok=True)

    # Create a C++ template file
    cpp_template_path = os.path.join(cp_templates_dir, 'cpp_template.cpp')
    with open(cpp_template_path, 'w') as cpp_template:
        cpp_template.write('#include <bits/stdc++.h>\n')
        cpp_template.write('using namespace std;\n\n')
        cpp_template.write('int main() {\n')
        cpp_template.write('    ios::sync_with_stdio(false);\n')
        cpp_template.write('    cin.tie(nullptr);\n\n')
        cpp_template.write('    // Your code here\n\n')
        cpp_template.write('    return 0;\n')
        cpp_template.write('}\n')

    # Configure VSCode settings for competitive programming
    vscode_settings_path = os.path.expanduser('~/.config/Code/User/settings.json')
    vscode_settings = {
        "editor.tabSize": 4,
        "editor.wordWrap": "off",
        "files.autoSave": "onFocusChange",
        "files.autoSaveDelay": 1000,
        "editor.defaultFormatter": "ms-vscode.cpptools",
        "editor.formatOnSave": True,
        "editor.formatOnPaste": True,
        "code-runner.executorMap": {
            "cpp": "cd $dir && g++ $fileName -o $fileNameWithoutExt && $dir$fileNameWithoutExt"
        },
        "code-runner.saveFileBeforeRun": True,
        "code-runner.runInTerminal": True,
        "cpp-template.defaultTemplate": cpp_template_path
    }

    with open(vscode_settings_path, 'w') as vscode_settings_file:
        json.dump(vscode_settings, vscode_settings_file, indent=4)

    print("Competitive programming environment for VSCode has been set up.")

    # Display instructions
    print("To use the C++ template, create a new .cpp file and open it in VSCode.")
    print("VSCode will automatically use the template for new .cpp files.")
