# D1TotalInstances Property (ILinearPatternFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearPatternFeatureData~D1TotalInstances`

Gets or sets the total number of pattern instances in Direction 1 for this linear pattern feature.
Gets or sets the total number of pattern instances in Direction 1 for this linear pattern feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property D1TotalInstances As System.Integer
```

```

Dim instance As ILinearPatternFeatureData
Dim value As System.Integer
 
instance.D1TotalInstances = value
 
value = instance.D1TotalInstances
```

```

System.int D1TotalInstances {get; set;}
```

```

property System.int D1TotalInstances {
   System.int get();
   void set (    System.int value);
}
```

#### Property Value

Total number of pattern instances in Direction 1

Remarks

You can set this property when [ILinearPatternFeatureData::D1EndCondition](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearPatternFeatureData~D1EndCondition.md) is set to:

- [swPatternEndCondition\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swPatternEndCondition_e.html).swPatternEndCondition\_SpacingAndInstances

    - or -

- swPatternEndCondition\_e.swPatternEndCondition\_UpToReference and [ILinearPatternFeatureData::D1EndUseSpacing](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearPatternFeatureData~D1EndUseSpacing.md) is set to false.

For more information, see the **Linear Patterns and the Linear Pattern PropertyManager** topic in the SOLIDWORKS user-interface help.

Example

See the [ILinearPatternFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearPatternFeatureData.md) example.

Example

[Get Linear Pattern Feature Data (C#)](Get_Linear_Pattern_Feature_Data_Example_CSharp.htm)  
[Get Linear Pattern Feature Data (VB.NET)](Get_Linear_Pattern_Feature_Data_Example_VBNET.htm)  
[Get Linear Pattern Feature Data (VBA)](Get_Linear_Pattern_Feature_Data_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ILinearPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearPatternFeatureData.md)  
[ILinearPatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearPatternFeatureData_members.md)  
[ILinearPatternFeatureData::GetD1AxisType Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearPatternFeatureData~GetD1AxisType.md)  
[ILinearPatternFeatureData::D1Axis Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearPatternFeatureData~D1Axis.md)  
[ILinearPatternFeatureData::D1ReverseDirection Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearPatternFeatureData~D1ReverseDirection.md)  
[ILinearPatternFeatureData::D1Spacing Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearPatternFeatureData~D1Spacing.md)
