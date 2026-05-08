# IGetProcedureNames Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~IGetProcedureNames`

Gets the names of the procedures in the specified module in the macro for the macro feature.
Gets the names of the procedures in the specified module in the macro for the macro feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub IGetProcedureNames( _
   ByVal ModuleName As System.String, _
   ByVal ProcedureCount As System.Integer, _
   ByRef ProcedureNames As System.String _
) 
```

```

Dim instance As IMacroFeatureData
Dim ModuleName As System.String
Dim ProcedureCount As System.Integer
Dim ProcedureNames As System.String
 
instance.IGetProcedureNames(ModuleName, ProcedureCount, ProcedureNames)
```

```

void IGetProcedureNames( 
   System.string ModuleName,
   System.int ProcedureCount,
   out System.string ProcedureNames
)
```

```

void IGetProcedureNames( 
   System.String^ ModuleName,
   System.int ProcedureCount,
   [Out] System.String^ ProcedureNames
) 
```

#### Parameters

*ModuleName*
:   Name of module

*ProcedureCount*
:   Number of procedures in ModuleName

*ProcedureNames*
:   - in-process, unmanaged C++: Pointer to an array of procedure names of size ProcedureCount

    - VBA, VB.NET, C#, and C++/CLI: Not supported

    See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

Remarks

Before calling this method, call [IMacroFeatureData::GetProcedureCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~GetParameterCount.md) to determine the size of the array.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IMacroFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData.md)  
[IMacroFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData_members.md)  
[IMacroFeatureData::GetModuleCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~GetModuleCount.md)  
[IMacroFeatureData::GetModuleNames Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~GetModuleNames.md)  
[IMacroFeatureData::GetProcedureNames Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~GetProcedureNames.md)  
[IMacroFeatureData::GetPropertyManagerHandleModuleCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~GetPropertyManagerHandleModuleCount.md)  
[IMacroFeatureData::GetPropertyManagerHandleModuleNames Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~GetPropertyManagerHandleModuleNames.md)  
[IMacroFeatureData::GetPropertyManagerHandleProcedureCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~GetPropertyManagerHandleProcedureCount.md)  
[IMacroFeatureData::GetPropertyManagerHandleProcedureNames Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~GetPropertyManagerHandleProcedureNames.md)  
[IMacroFeatureData::IGetPropertyManagerHandleModuleNames Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~IGetPropertyManagerHandleModuleNames.md)  
[IMacroFeatureData::IGetPropertyManagerHandleProcedureNames Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~IGetPropertyManagerHandleProcedureNames.md)  
[IMacroFeatureData::ModuleName Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~ModuleName.md)  
[IMacroFeatureData::ProcedureName Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~ProcedureName.md)  
[IMacroFeatureData::PropertyManagerHandleMacroFileName Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~PropertyManagerHandleMacroFileName.md)  
[IMacroFeatureData::PropertyManagerHandleModuleName Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~PropertyManagerHandleModuleName.md)  
[IMacroFeatureData::PropertyManagerHandleProcedureName Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~PropertyManagerHandleProcedureName.md)  
[IMacroFeatureData::SecurityHandleMacroFileName Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~SecurityHandleMacroFileName.md)  
[IMacroFeatureData::SecurityHandleModuleName Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~SecurityHandleModuleName.md)  
[IMacroFeatureData::SecurityHandleProcedureName Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~SecurityHandleProcedureName.md)
