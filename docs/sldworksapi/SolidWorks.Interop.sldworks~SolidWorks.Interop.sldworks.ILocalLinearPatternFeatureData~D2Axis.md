# D2Axis Property (ILocalLinearPatternFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalLinearPatternFeatureData~D2Axis`

Gets or sets Direction 2 for this bidirectional linear component pattern feature.
Gets or sets Direction 2 for this bidirectional linear component pattern feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property D2Axis As System.Object
```

```

Dim instance As ILocalLinearPatternFeatureData
Dim value As System.Object
 
instance.D2Axis = value
 
value = instance.D2Axis
```

```

System.object D2Axis {get; set;}
```

```

property System.Object^ D2Axis {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

#### Property Value

Direction 2 entity: linear [edge](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge.md), [line](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchLine.md), [axis](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefAxis.md), [dimension](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension.md), planar [face](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.md), planar [surface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface.md), conical face, conical surface, circular edge, or reference [plane](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefPlane.md)

Remarks

Use [ILocalLinearPatternFeatureData::GetD2AxisType](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalLinearPatternFeatureData~GetD2AxisType.md) to determine the type of object to pass to this property.

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this property.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ILocalLinearPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalLinearPatternFeatureData.md)  
[ILocalLinearPatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalLinearPatternFeatureData_members.md)  
[ILocalLinearPatternFeatureData::D2ReverseDirection Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalLinearPatternFeatureData~D2ReverseDirection.md)  
[ILocalLinearPatternFeatureData::D2Spacing Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalLinearPatternFeatureData~D2Spacing.md)  
[ILocalLinearPatternFeatureData::D2TotalInstances Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalLinearPatternFeatureData~D2TotalInstances.md)  
[ILocalLinearPatternFeatureData::GetD2AxisType Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalLinearPatternFeatureData~GetD2AxisType.md)
