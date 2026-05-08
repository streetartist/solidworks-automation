# GetCurrentWorkingDirectory Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetCurrentWorkingDirectory`

Gets the current working directory being used by the SOLIDWORKS application.
Gets the current working directory being used by the SOLIDWORKS application.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetCurrentWorkingDirectory() As System.String
```

```

Dim instance As ISldWorks
Dim value As System.String
 
value = instance.GetCurrentWorkingDirectory()
```

```

System.string GetCurrentWorkingDirectory()
```

```

System.String^ GetCurrentWorkingDirectory(); 
```

#### Return Value

Current working directory with trailing backslash

Remarks

The current working directory is used when opening documents containing references. If explicit search folders are not set (see [ISldWorks::SetSearchFolders](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~SetSearchFolders.md)), then the SOLIDWORKS application initially tries to locate file references (for example, assembly component parts) in the current working directory. Interactively, the current working directory is used by the File Open dialog and is set when you choose the Open dialog button.

The most current [ISldWorks::OpenDoc6](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~OpenDoc6.md) method does not set the current working directory. Therefore, you might want to set the current working directory programmatically (see [ISldWorks::SetCurrentWorkingDirectory](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~SetCurrentWorkingDirectory.md)) before opening a file containing references. By doing this, your application behaves as if the file was opened interactively using the File Open dialog.

For more information on the search criteria used by the SOLIDWORKS application when loading file references, see SOLIDWORKS Help.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.md)  
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.md)  
[ISldWorks::GetCurrentMacroPathFolder Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetCurrentMacroPathFolder.md)  
[ISldWorks::GetCurrentMacroPathName Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetCurrentMacroPathName.md)  
[ISldWorks::SetCurrentWorkingDirectory Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~SetCurrentWorkingDirectory.md)  
[ISldWorks::GetExecutablePath Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetExecutablePath.md)
