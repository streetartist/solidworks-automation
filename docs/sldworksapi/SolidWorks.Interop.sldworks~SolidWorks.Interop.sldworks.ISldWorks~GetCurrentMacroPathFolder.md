# GetCurrentMacroPathFolder Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetCurrentMacroPathFolder`

Gets the name of the folder where the macro resides.
Gets the name of the folder where the macro resides.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetCurrentMacroPathFolder() As System.String
```

```

Dim instance As ISldWorks
Dim value As System.String
 
value = instance.GetCurrentMacroPathFolder()
```

```

System.string GetCurrentMacroPathFolder()
```

```

System.String^ GetCurrentMacroPathFolder(); 
```

#### Return Value

Name of the folder where the macro resides

Example

[Save Solid Body to File (C#)](Save_Solid_Body_to_File_Example_CSharp.htm)  
[Save Solid Body to File (VB.NET)](Save_Solid_Body_to_File_Example_VBNET.htm)  
[Save Solid Body to File (VBA)](Save_Solid_Body_to_File_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.md)  
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.md)  
[ISldWorks::GetCurrentMacroPathName Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetCurrentMacroPathName.md)  
[ISldWorks::GetCurrentWorkingDirectory Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetCurrentWorkingDirectory.md)  
[ISldWorks::GetMacroMethods Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetMacroMethods.md)  
[ISldWorks::RunMacro Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~RunMacro.md)
