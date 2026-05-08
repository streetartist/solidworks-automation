# SetOverrideDefaultParameter2 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheetMetalFeatureData~SetOverrideDefaultParameter2`

Sets whether to override the specified default parameter in this sheet metal feature in a multibody sheet metal part.
Sets whether to override the specified default parameter in this sheet metal feature in a multibody sheet metal part.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function SetOverrideDefaultParameter2( _
   ByVal Parameter As System.Integer, _
   ByVal OverrideDefaultParameter As System.Boolean _
) As System.Integer
```

```

Dim instance As ISheetMetalFeatureData
Dim Parameter As System.Integer
Dim OverrideDefaultParameter As System.Boolean
Dim value As System.Integer
 
value = instance.SetOverrideDefaultParameter2(Parameter, OverrideDefaultParameter)
```

```

System.int SetOverrideDefaultParameter2( 
   System.int Parameter,
   System.bool OverrideDefaultParameter
)
```

```

System.int SetOverrideDefaultParameter2( 
   System.int Parameter,
   System.bool OverrideDefaultParameter
) 
```

#### Parameters

*Parameter*
:   Default parameter as defined in [swSheetMetalOverrideDefaultParameters\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swSheetMetalOverrideDefaultParameters_e.html)

*OverrideDefaultParameter*
:   True to override Parameter, false to not

#### Return Value

Result code as defined in [swSheetMetalModifierError\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swSheetMetalModifierError_e.html)

Remarks

This property is only valid for multibody sheet metal parts created in SOLIDWORKS 2013 and later.

Example

See the [IBaseFlangeFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBaseFlangeFeatureData.md) examples.

Example

[Set Override Option for Auto Relief Default Parameters (C#)](Set_Override_Option_for_Auto_Relief_Default_Parameters_Example_CSharp.htm)  
[Set Override Option for Auto Relief Default Parameters (VB.NET)](Set_Override_Option_for_Auto_Relief_Default_Parameters_Example_VBNET.htm)  
[Set Override Option for Auto Relief Default Parameters (VBA)](Set_Override_Option_for_Auto_Relief_Default_Parameters_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISheetMetalFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheetMetalFeatureData.md)  
[ISheetMetalFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheetMetalFeatureData_members.md)  
[ISheetMetalFeatureData::GetOverrideDefaultParameter2 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheetMetalFeatureData~GetOverrideDefaultParameter2.md)  
[IBaseFlangeFeatureData::Initialize Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBaseFlangeFeatureData~Initialize.md)
