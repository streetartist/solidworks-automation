# FillPath Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IChainPatternFeatureData~FillPath`

Gets or sets whether the maximum number of pattern instances to fill the path is calculated by SOLIDWORKS for this chain pattern feature.
Gets or sets whether the maximum number of pattern instances to fill the path is calculated by SOLIDWORKS for this chain pattern feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property FillPath As System.Boolean
```

```

Dim instance As IChainPatternFeatureData
Dim value As System.Boolean
 
instance.FillPath = value
 
value = instance.FillPath
```

```

System.bool FillPath {get; set;}
```

```

property System.bool FillPath {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True if the maximum number of pattern instances to fill the path is calculated by SOLIDWORKS, false if not (see **Remarks**)

Remarks

This property is available for all types of chain patterns, but it is only available for distance and distance linkage chain patterns when [equal spacing](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IChainPatternFeatureData~SetEqualSpacing.md) is not set.

To set the distance between the pattern instances, use [IChainPatternFeatureData::Spacing](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IChainPatternFeatureData~Spacing.md).

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this property.

Example

[Create and Modify Distance Chain Pattern Feature (C#)](Create_and_Modify_Distance_Chain_Pattern_Feature_Example_CSharp.htm)  
[Create and Modify Distance Chain Pattern Feature (VB.NET)](Create_and_Modify_Distance_Chain_Pattern_Feature_Example_VBNET.htm)  
[Create and Modify Distance Chain Pattern Feature (VBA)](Create_and_Modify_Distance_Chain_Pattern_Feature_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IChainPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IChainPatternFeatureData.md)  
[IChainPatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IChainPatternFeatureData_members.md)
