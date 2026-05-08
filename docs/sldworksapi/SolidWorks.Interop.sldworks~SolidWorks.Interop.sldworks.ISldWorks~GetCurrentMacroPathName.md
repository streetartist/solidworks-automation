# GetCurrentMacroPathName Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetCurrentMacroPathName`

Gets the path name for the macro currently running.
Gets the path name for the macro currently running.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetCurrentMacroPathName() As System.String
```

```

Dim instance As ISldWorks
Dim value As System.String
 
value = instance.GetCurrentMacroPathName()
```

```

System.string GetCurrentMacroPathName()
```

```

System.String^ GetCurrentMacroPathName(); 
```

#### Return Value

Path name for the macro currently running

Example

[Create Macro Feature Subfeature (VBA)](Create_Macro_Feature_Subfeature_Example_VB.htm)  
[Import Models As Solids (VBA)](Import_Models_as_Solids_Example_VB.htm)  
[Copy Document and Its Dependencies (VBA)](Copy_Document_and_Its_Dependencies_Example_VB.htm)  
[Copy Document and Its Dependencies (VB.NET)](Copy_Document_and_Its_Dependencies_Example_VBNET.htm)  
[Copy Document and Its Dependencies (C#)](Copy_Document_and_Its_Dependencies_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.md)  
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.md)  
[ISldWorks::GetCurrentMacroPathFolder Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetCurrentMacroPathFolder.md)  
[ISldWorks::GetCurrentWorkingDirectory Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetCurrentWorkingDirectory.md)  
[ISldWorks::RunMacro Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~RunMacro.md)  
[ISldWorks::GetMacroMethods Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetMacroMethods.md)
