# SetOverrideDefaultParameter Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheetMetalFeatureData~SetOverrideDefaultParameter`

Obsolete. Superseded by ISheetMetalFeatureData::SetOverrideDefaultParameter2.
Obsolete. Superseded by [ISheetMetalFeatureData::SetOverrideDefaultParameter2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheetMetalFeatureData~SetOverrideDefaultParameter2.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function SetOverrideDefaultParameter( _
   ByVal OverrideDefaultParameter As System.Boolean _
) As System.Integer
```

```

Dim instance As ISheetMetalFeatureData
Dim OverrideDefaultParameter As System.Boolean
Dim value As System.Integer
 
value = instance.SetOverrideDefaultParameter(OverrideDefaultParameter)
```

```

System.int SetOverrideDefaultParameter( 
   System.bool OverrideDefaultParameter
)
```

```

System.int SetOverrideDefaultParameter( 
   System.bool OverrideDefaultParameter
) 
```

#### Parameters

*OverrideDefaultParameter*
:   True to override the default parameters, false to not

#### Return Value

Result code as defined in [swSheetMetalModifierError\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swSheetMetalModifierError_e.html)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISheetMetalFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheetMetalFeatureData.md)  
[ISheetMetalFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheetMetalFeatureData_members.md)  
[ISheetMetalFeatureData::GetOverrideDefaultParameter Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheetMetalFeatureData~GetOverrideDefaultParameter.md)
