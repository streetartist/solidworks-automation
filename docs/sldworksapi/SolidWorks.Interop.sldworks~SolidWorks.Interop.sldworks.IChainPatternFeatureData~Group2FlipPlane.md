# Group2FlipPlane Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IChainPatternFeatureData~Group2FlipPlane`

Gets or sets whether to flip the position plane for Chain Group 2 in this chain pattern feature.
Gets or sets whether to flip the [position plane](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IChainPatternFeatureData~Group2PathPlane.md) for **Chain Group 2** in this chain pattern feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property Group2FlipPlane As System.Boolean
```

```

Dim instance As IChainPatternFeatureData
Dim value As System.Boolean
 
instance.Group2FlipPlane = value
 
value = instance.Group2FlipPlane
```

```

System.bool Group2FlipPlane {get; set;}
```

```

property System.bool Group2FlipPlane {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True to flip the position plane, false to not

Remarks

This property is only available for connected linkage chain patterns.

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this property.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IChainPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IChainPatternFeatureData.md)  
[IChainPatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IChainPatternFeatureData_members.md)  
[IChainPatternFeatureData::Group2PathLink1 Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IChainPatternFeatureData~Group2PathLink1.md)  
[IChainPatternFeatureData::Group2PathLink2 Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IChainPatternFeatureData~Group2PathLink2.md)  
[IChainPatternFeatureData::Group2PathPlane Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IChainPatternFeatureData~Group2PathPlane.md)  
[IChainPatternFeatureData::Group2PatternComponent Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IChainPatternFeatureData~Group2PatternComponent.md)  
[IChainPatternFeatureData::ClearGroup2Selections Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IChainPatternFeatureData~ClearGroup2Selections.md)
