# Spacing Property (IChainPatternFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IChainPatternFeatureData~Spacing`

Gets or sets the distance between the pattern instances in the path in this chain pattern feature.
Gets or sets the distance between the pattern instances in the [path](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IChainPatternFeatureData~Path.md) in this chain pattern feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property Spacing As System.Double
```

```

Dim instance As IChainPatternFeatureData
Dim value As System.Double
 
instance.Spacing = value
 
value = instance.Spacing
```

```

System.double Spacing {get; set;}
```

```

property System.double Spacing {
   System.double get();
   void set (    System.double value);
}
```

#### Property Value

Distance between the pattern instances (see **Remarks**)

Remarks

This property is only available for distance and linkage distance chain patterns when [equal spacing](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IChainPatternFeatureData~SetEqualSpacing.md) is not set.

To:

- have SOLIDWORKS calculate the maximum number of pattern instances to fill the path using the specified distance, use [IChainPatternFeatureData::FillPath](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IChainPatternFeatureData~FillPath.md).   
  - or -
- set the number of pattern instances for the path using the specified distance, use [IChainPatternFeatureData::InstanceCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IChainPatternFeatureData~InstanceCount.md).

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
