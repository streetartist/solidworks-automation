# D1Direction Property (ILocalCurvePatternFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalCurvePatternFeatureData~D1Direction`

Gets or sets Direction 1 using the selected curve, edge, sketch, or sketch entity for this curve-driven component pattern feature.
Gets or sets Direction 1 using the selected curve, edge, sketch, or sketch entity for this curve-driven component pattern feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property D1Direction As System.Object
```

```

Dim instance As ILocalCurvePatternFeatureData
Dim value As System.Object
 
instance.D1Direction = value
 
value = instance.D1Direction
```

```

System.object D1Direction {get; set;}
```

```

property System.Object^ D1Direction {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

#### Property Value

[Curve](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve.md), [edge](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge.md), [sketch](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch.md), or sketch entity for Direction 1

Remarks

You must pre-select the direction entity using selection Mark = 1 before creating the feature definition. If you are using a 3D curve for Direction 1, then you must also pre-select the face normal entity using selection Mark = 64.

Use this property only when editing the pattern feature.

If you specify this property using a 3D curve, you should also specify [ILocalCurvePatternFeatureData::D1FaceNormal](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalCurvePatternFeatureData~D1FaceNormal.md).

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this property.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ILocalCurvePatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalCurvePatternFeatureData.md)  
[ILocalCurvePatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalCurvePatternFeatureData_members.md)  
[ILocalCurvePatternFeatureData::D1AlignmentMethod Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalCurvePatternFeatureData~D1AlignmentMethod.md)  
[ILocalCurvePatternFeatureData::D1CurveMethod Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalCurvePatternFeatureData~D1CurveMethod.md)  
[ILocalCurvePatternFeatureData::D1InstanceCount Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalCurvePatternFeatureData~D1InstanceCount.md)  
[ILocalCurvePatternFeatureData::D1IsEqualSpaced Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalCurvePatternFeatureData~D1IsEqualSpaced.md)  
[ILocalCurvePatternFeatureData::D1ReferencePoint Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalCurvePatternFeatureData~D1ReferencePoint.md)  
[ILocalCurvePatternFeatureData::D1ReverseDirection Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalCurvePatternFeatureData~D1ReverseDirection.md)  
[ILocalCurvePatternFeatureData::D1Spacing Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalCurvePatternFeatureData~D1Spacing.md)  
[ILocalCurvePatternFeatureData::D2Direction Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalCurvePatternFeatureData~D2Direction.md)
