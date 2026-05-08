# Reverse Property (IProjectionCurveFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IProjectionCurveFeatureData~Reverse`

Reverses the direction that the curve is projected.
Reverses the direction that the curve is projected.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property Reverse As System.Boolean
```

```

Dim instance As IProjectionCurveFeatureData
Dim value As System.Boolean
 
instance.Reverse = value
 
value = instance.Reverse
```

```

System.bool Reverse {get; set;}
```

```

property System.bool Reverse {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True to reverse the direction of this projected curve, false to not

Remarks

If all faces in [IProjectionCurveFeatureData::FaceArray](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IProjectionCurveFeatureData~FaceArray.md) are on the same side with respect to [IProjectionCurveFeatureData::Sketch](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IProjectionCurveFeatureData~Sketch.md), then this property is ignored. The projection direction is calculated from the selected sketches and faces.

You can reverse the direction in which the curve is projected when the selected face wraps around the plane of the curve. For example, if the sketch being projected is surrounded by a cylindrical face, then two possible projections exist. If this property is set to true, the direction based on the normal vector of the sketch is reversed. The default direction is along the sketch normal.

Example

See the [IProjectionCurveFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IProjectionCurveFeatureData.md) example.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IProjectionCurveFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IProjectionCurveFeatureData.md)  
[IProjectionCurveFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IProjectionCurveFeatureData_members.md)
