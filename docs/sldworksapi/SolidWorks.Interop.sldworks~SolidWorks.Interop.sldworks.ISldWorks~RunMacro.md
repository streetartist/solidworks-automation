# RunMacro Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~RunMacro`

Obsolete. Superseded by ISldWorks::RunMacro2.
Obsolete. Superseded by [ISldWorks::RunMacro2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~RunMacro2.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function RunMacro( _
   ByVal FilePathName As System.String, _
   ByVal ModuleName As System.String, _
   ByVal ProcedureName As System.String _
) As System.Boolean
```

```

Dim instance As ISldWorks
Dim FilePathName As System.String
Dim ModuleName As System.String
Dim ProcedureName As System.String
Dim value As System.Boolean
 
value = instance.RunMacro(FilePathName, ModuleName, ProcedureName)
```

```

System.bool RunMacro( 
   System.string FilePathName,
   System.string ModuleName,
   System.string ProcedureName
)
```

```

System.bool RunMacro( 
   System.String^ FilePathName,
   System.String^ ModuleName,
   System.String^ ProcedureName
) 
```

#### Parameters

*FilePathName*
:   Path and file name of the project file containing the macro

*ModuleName*
:   Name of the module in the macro

*ProcedureName*
:   Name of the procedure in the module

#### Return Value

True if macro runs successfully, false if not

Remarks

See [SOLIDWORKS Macros](sldworksAPIProgGuide.chm::/GettingStarted/SOLIDWORKS_Macros.htm) for details.

Example

[Run Macro (VBA)](Run_Macro_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.md)  
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.md)  
[ISldWorks::GetCurrentMacroPathFolder Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetCurrentMacroPathFolder.md)  
[ISldWorks::GetCurrentMacroPathName Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetCurrentMacroPathName.md)  
[ISldWorks::RecordLine Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~RecordLine.md)  
[ISldWorks::GetMacroMethods Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetMacroMethods.md)
