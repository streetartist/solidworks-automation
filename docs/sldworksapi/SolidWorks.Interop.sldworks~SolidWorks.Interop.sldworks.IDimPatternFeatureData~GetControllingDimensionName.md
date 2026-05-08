# GetControllingDimensionName Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimPatternFeatureData~GetControllingDimensionName`

Gets the name of the controlling dimension for the pattern instance at the specified index in this variable pattern feature.
Gets the name of the controlling dimension for the pattern instance at the specified index in this variable pattern feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetControllingDimensionName( _
   ByVal Index As System.Integer _
) As System.String
```

```

Dim instance As IDimPatternFeatureData
Dim Index As System.Integer
Dim value As System.String
 
value = instance.GetControllingDimensionName(Index)
```

```

System.string GetControllingDimensionName( 
   System.int Index
)
```

```

System.String^ GetControllingDimensionName( 
   System.int Index
) 
```

#### Parameters

*Index*
:   Index of the controlling dimension pattern (see **Remarks**)

#### Return Value

Name of the controlling dimension of the pattern instance

Remarks

Use [IDimPatternFeatureData::GetControllingDimensionCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimPatternFeatureData~GetControllingDimensionCount.md) to get the number of controlling dimensions.

Example

[Insert Variable Pattern Feature (C#)](Insert_Advanced_Variable_Pattern_Feature_Example_CSharp.htm)  
[Insert Variable Pattern Feature (VB.NET)](Insert_Advanced_Variable_Pattern_Feature_Example_VBNET.htm)  
[Insert Variable Pattern Feature (VBA)](Insert_Advanced_Variable_Pattern_Feature_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDimPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimPatternFeatureData.md)  
[IDimPatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimPatternFeatureData_members.md)
