# AutoSINTA (Automatic SINTA Kemdikbud Synchronization)

An unofficial application to automatically bulk-sync SINTA Kemdikbud author publication data without human labor.

## 1. About

**AutoSINTA** is an automatic [SINTA Kemdikbud](https://sinta.kemdikbud.go.id) synchronization program written in Python. This unofficial program accesses the SINTA API using the `requests` Python module. It helps SINTA administrators in any Indonesian university to carry out author publication data update without manual labor (i.e., sync per author instead of in bulk). **AutoSINTA** is open source and licensed under [GNU General Public License v3.0](https://choosealicense.com/licenses/gpl-3.0). Anyone can make edit to the application and distribute the program as long as the terms in such a GNU v3.0 license is fulfilled.

**AutoSINTA** is developed by S. Lykamanuella, an undergraduate physics student in Satya Wacana Christian University (SWCU). This project was in collaboration with Directorate of Research and Community Service of SWCU.

Also visit [the AutoSINTA web page](https://groaking.github.io/autosinta).

## 2. Download

You can download the latest version of **AutoSINTA** from the release menu in this GitHub repository.

## 3. How to use

### 1. Ensure that your computer is connected to the internet;

### 2. Download **AutoSINTA** using the provided link;

### 3. Upon successful download, double-click the AutoSINTA to launch the program;

### 4. Click "Run Anyway" when the Windows Defender SmartScreen popup appears;

> *Also read [this article](https://www.addictivetips.com/windows-tips/fix-no-run-anyway-option-on-smartscreen-windows-10) on running an unsigned Windows program.*

> *The AutoSINTA program is guaranteed to be virus-less. You can check and audit the source code yourself in this GitHub repository.*

### 5. The **AutoSINTA** window will appear as follows;

![1](https://github.com/groaking/groaking.github.io/assets/93555329/d151b083-5745-4c62-8165-c4b1376a1f71)

### 6. Enter your SINTA Author Verificator (AV) on the "Username" and "Password" input fields. Then click the "LOGIN" button;

![2](https://github.com/groaking/groaking.github.io/assets/93555329/b2764d89-36d9-4288-813d-f847449364c5)

### 7. Ensure the following dialog window pops up;

![3](https://github.com/groaking/groaking.github.io/assets/93555329/5c9aa858-6a5c-4d05-b2b1-30b6a14f8f19)

> *If login failed, check your internet connection and login credentials, then try again.*

### 8. Upon successful login, determine the types of publication you want to synchronize;

![4](https://github.com/groaking/groaking.github.io/assets/93555329/36cccf57-4e63-40b8-9916-a8f59b4f8db2)

### 9. Click the "Load Author List" button to load the list of university authors you have access to. The following dialog will pop up once the author list has been loaded;

![6](https://github.com/groaking/groaking.github.io/assets/93555329/9d88e503-c706-4e1e-9e3a-a5c44d94937c)

### 10. Click the "Sync" button. The following window will appear;

![7](https://github.com/groaking/groaking.github.io/assets/93555329/1dd29eff-56e6-4f3c-877e-769978e4bfe9)

### 12. To synchronize the publication data of all authors, select "Sync all SINTA authors" and then click "SYNC NOW";

### 13. To synchronize only a selected list of authors, perform the following:

![8](https://github.com/groaking/groaking.github.io/assets/93555329/c4b1dac5-962e-4ab2-98ea-9b4f6341e035)

- Select "Only sync selected authors";
- Send the list of authors that will be synchronized from the left table to the right table, as shown;
- Click "SYNC NOW";

### 14. The SINTA synchronization process will commence momentarily. Wait until finished;

![9](https://github.com/groaking/groaking.github.io/assets/93555329/1bb42ff9-38ab-4e33-b86e-c54011899afc)

### 15. Upon the popping up of the following dialog, the synchronization process is complete;

![10](https://github.com/groaking/groaking.github.io/assets/93555329/a82f9451-65a3-4eae-b5e7-23667bc0e453)

### 16. You can double check in the [Author Verification](https://sinta.kemdikbud.go.id/authorverification) admin dashboard that the selected authors' publication data has been queued for synchronization;

![11](https://github.com/groaking/groaking.github.io/assets/93555329/784e09b6-43b3-4ba8-a892-e3145368b951)

### 17. Click `File > Quit` to terminate the AutoSINTA program.

![11](https://github.com/groaking/groaking.github.io/assets/93555329/0180b3d9-445c-4397-add0-346df8561cdd)
