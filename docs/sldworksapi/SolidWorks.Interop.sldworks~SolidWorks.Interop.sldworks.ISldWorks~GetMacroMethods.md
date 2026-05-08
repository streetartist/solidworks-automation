# GetMacroMethods Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetMacroMethods`

Gets the names of the modules in the specified macro.
Gets the names of the modules in the specified macro.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetMacroMethods( _
   ByVal FilePathName As System.String, _
   ByVal Filter As System.Integer _
) As System.Object
```

```

Dim instance As ISldWorks
Dim FilePathName As System.String
Dim Filter As System.Integer
Dim value As System.Object
 
value = instance.GetMacroMethods(FilePathName, Filter)
```

```

System.object GetMacroMethods( 
   System.string FilePathName,
   System.int Filter
)
```

```

System.Object^ GetMacroMethods( 
   System.String^ FilePathName,
   System.int Filter
) 
```

#### Parameters

*FilePathName*
:   Path and macro filename whose module names you want

*Filter*
:   Filter as defined in [swMacroMethods\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swMacroMethods_e.html)

#### Return Value

Array of names of the modules in FilePathName

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.md)  
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.md)  
[ISldWorks::GetCurrentMacroPathFolder Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetCurrentMacroPathFolder.md)  
[ISldWorks::GetCurrentMacroPathName Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetCurrentMacroPathName.md)  
[ISldWorks::GetCurrentWorkingDirectory Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetCurrentWorkingDirectory.md)  
[ISldWorks::RunMacro Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~RunMacro.md)
