# GetExecutablePath Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetExecutablePath`

Gets the path to the SOLIDWORKS executable, sldworks.exe.
Gets the path to the SOLIDWORKS executable, sldworks.exe.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetExecutablePath() As System.String
```

```

Dim instance As ISldWorks
Dim value As System.String
 
value = instance.GetExecutablePath()
```

```

System.string GetExecutablePath()
```

```

System.String^ GetExecutablePath(); 
```

#### Return Value

Path for **sldworks.exe**

Example

This subroutine illustrates how to use this method:

'---------------------------------------------

Option Explicit

Sub main()

    Dim swApp As SldWorks.SldWorks

    Set swApp = Application.SldWorks

    

    ' Gives directory name without trailing backslash

    Debug.Print "SldWorks executable = " & swApp.GetExecutablePath

End Sub

'---------------------------------------------

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.md)  
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.md)  
[ISldWorks::GetCurrentMacroPathFolder Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetCurrentMacroPathFolder.md)  
[ISldWorks::GetCurrentWorkingDirectory Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetCurrentWorkingDirectory.md)  
[ISldWorks::GetDataFolder Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetDataFolder.md)
