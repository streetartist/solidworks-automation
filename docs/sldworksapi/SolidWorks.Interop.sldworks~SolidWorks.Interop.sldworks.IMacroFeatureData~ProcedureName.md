# ProcedureName Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~ProcedureName`

Gets or sets a name of the procedure in the macro for this macro feature.
Gets or sets a name of the procedure in the macro for this macro feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property ProcedureName As System.String
```

```

Dim instance As IMacroFeatureData
Dim value As System.String
 
instance.ProcedureName = value
 
value = instance.ProcedureName
```

```

System.string ProcedureName {get; set;}
```

```

property System.String^ ProcedureName {
   System.String^ get();
   void set (    System.String^ value);
}
```

#### Property Value

Name of the procedure in the macro

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IMacroFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData.md)  
[IMacroFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData_members.md)  
[IMacroFeatureData::GetModuleCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~GetModuleCount.md)  
[IMacroFeatureData::GetModuleNames Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~GetModuleNames.md)  
[IMacroFeatureData::GetProcedureCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~GetProcedureCount.md)  
[IMacroFeatureData::GetProcedureNames Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~GetProcedureNames.md)  
[IMacroFeatureData::GetPropertyManagerHandleModuleCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~GetPropertyManagerHandleModuleCount.md)  
[IMacroFeatureData::GetPropertyManagerHandleModuleNames Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~GetPropertyManagerHandleModuleNames.md)  
[IMacroFeatureData::GetPropertyManagerHandleProcedureCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~GetPropertyManagerHandleProcedureCount.md)  
[IMacroFeatureData::GetPropertyManagerHandleProcedureNames Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~GetPropertyManagerHandleProcedureNames.md)  
[IMacroFeatureData::IGetModuleNames Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~IGetModuleNames.md)  
[IMacroFeatureData::IGetProcedureNames Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~IGetProcedureNames.md)  
[IMacroFeatureData::IGetPropertyManagerHandleModuleNames Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~IGetPropertyManagerHandleModuleNames.md)  
[IMacroFeatureData::IGetPropertyManagerHandleProcedureNames Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~IGetPropertyManagerHandleProcedureNames.md)  
[IMacroFeatureData::MacroFileName Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~MacroFileName.md)  
[IMacroFeatureData::ModuleName Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~ModuleName.md)  
[IMacroFeatureData::PropertyManagerHandleMacroFileName Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~PropertyManagerHandleMacroFileName.md)  
[IMacroFeatureData::PropertyManagerHandleModuleName Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~PropertyManagerHandleModuleName.md)  
[IMacroFeatureData::PropertyManagerHandleProcedureName Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~PropertyManagerHandleProcedureName.md)  
[IMacroFeatureData::SecurityHandleMacroFileName Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~SecurityHandleMacroFileName.md)  
[IMacroFeatureData::SecurityHandleModuleName Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~SecurityHandleModuleName.md)  
[IMacroFeatureData::SecurityHandleProcedureName Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~SecurityHandleProcedureName.md)
