# GetOverrideDefaultParameter2 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheetMetalFeatureData~GetOverrideDefaultParameter2`

Gets whether the specified default parameter is overridden in this sheet metal feature in a multibody sheet metal part.
Gets whether the specified default parameter is overridden in this sheet metal feature in a multibody sheet metal part.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetOverrideDefaultParameter2( _
   ByVal Parameter As System.Integer, _
   ByRef OverrideDefaultParameter As System.Boolean _
) As System.Integer
```

```

Dim instance As ISheetMetalFeatureData
Dim Parameter As System.Integer
Dim OverrideDefaultParameter As System.Boolean
Dim value As System.Integer
 
value = instance.GetOverrideDefaultParameter2(Parameter, OverrideDefaultParameter)
```

```

System.int GetOverrideDefaultParameter2( 
   System.int Parameter,
   out System.bool OverrideDefaultParameter
)
```

```

System.int GetOverrideDefaultParameter2( 
   System.int Parameter,
   [Out] System.bool OverrideDefaultParameter
) 
```

#### Parameters

*Parameter*
:   Default parameter as defined in [swSheetMetalOverrideDefaultParameters\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swSheetMetalOverrideDefaultParameters_e.html)

*OverrideDefaultParameter*
:   True if Parameter is overridden, false if not

#### Return Value

Result code as defined in [swSheetMetalModifierError\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swSheetMetalModifierError_e.html)

Remarks

This property is only valid for multibody sheet metal parts created in SOLIDWORKS 2013 and later.

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
[ISheetMetalFeatureData::SetOverrideDefaultParameter2 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheetMetalFeatureData~SetOverrideDefaultParameter2.md)
