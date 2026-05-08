# D1Axis Property (ILinearPatternFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearPatternFeatureData~D1Axis`

Gets or sets Direction 1 for this linear pattern feature.
Gets or sets Direction 1 for this linear pattern feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property D1Axis As System.Object
```

```

Dim instance As ILinearPatternFeatureData
Dim value As System.Object
 
instance.D1Axis = value
 
value = instance.D1Axis
```

```

System.object D1Axis {get; set;}
```

```

property System.Object^ D1Axis {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

#### Property Value

Direction 1 entity: linear [edge](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge.md), [line](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchLine.md), [axis](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefAxis.md), [dimension](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension.md), planar [face](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.md), planar [surface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface.md), conical face, conical surface, circular edge, or reference [plane](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefPlane.md)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ILinearPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearPatternFeatureData.md)  
[ILinearPatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearPatternFeatureData_members.md)  
[ILinearPatternFeatureData::GetD1AxisType Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearPatternFeatureData~GetD1AxisType.md)  
[ILinearPatternFeatureData::D1ReverseDirection Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearPatternFeatureData~D1ReverseDirection.md)  
[ILinearPatternFeatureData::D1Spacing Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearPatternFeatureData~D1Spacing.md)  
[ILinearPatternFeatureData::D1TotalInstances Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearPatternFeatureData~D1TotalInstances.md)  
[ILinearPatternFeatureData::VarySketch Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearPatternFeatureData~VarySketch.md)
