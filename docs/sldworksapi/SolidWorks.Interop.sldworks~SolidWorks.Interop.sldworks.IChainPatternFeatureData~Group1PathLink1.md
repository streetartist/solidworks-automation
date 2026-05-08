# Group1PathLink1 Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IChainPatternFeatureData~Group1PathLink1`

Gets or sets Path Link 1 in Chain Group 1 in this chain pattern feature.
Gets or sets **Path Link 1** in **Chain Group 1** in this chain pattern feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property Group1PathLink1 As System.Object
```

```

Dim instance As IChainPatternFeatureData
Dim value As System.Object
 
instance.Group1PathLink1 = value
 
value = instance.Group1PathLink1
```

```

System.object Group1PathLink1 {get; set;}
```

```

property System.Object^ Group1PathLink1 {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

#### Property Value

**Path Link 1** in **Chain Group 1**:

- Cylindrical [face](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.md),
- Circular or linear [edge](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge.md),
- [Sketch point](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPoint.md),
- [Vertex](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVertex.md), or
- [Reference axis](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefAxis.md)

Remarks

This property is available for all types of chain patterns.

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this property.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IChainPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IChainPatternFeatureData.md)  
[IChainPatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IChainPatternFeatureData_members.md)  
[IChainPatternFeatureData::Group1FlipPlane Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IChainPatternFeatureData~Group1FlipPlane.md)  
[IChainPatternFeatureData::Group1PathLink2 Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IChainPatternFeatureData~Group1PathLink2.md)  
[IChainPatternFeatureData::Group1PathPlane Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IChainPatternFeatureData~Group1PathPlane.md)  
[IChainPatternFeatureData::Group1PatternComponent Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IChainPatternFeatureData~Group1PatternComponent.md)
