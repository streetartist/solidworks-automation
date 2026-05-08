# D1FaceNormal Property (ILocalCurvePatternFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalCurvePatternFeatureData~D1FaceNormal`

Gets or sets the face on which the 3D curve lies for this curve-driven component pattern feature.
Gets or sets the face on which the 3D curve lies for this curve-driven component pattern feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property D1FaceNormal As System.Object
```

```

Dim instance As ILocalCurvePatternFeatureData
Dim value As System.Object
 
instance.D1FaceNormal = value
 
value = instance.D1FaceNormal
```

```

System.object D1FaceNormal {get; set;}
```

```

property System.Object^ D1FaceNormal {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

#### Property Value

[IFace2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.md)

Remarks

If you pre-select a 3D curve for Direction 1, then before creating the feature definition, you must also pre-select the face normal entity using selection Mark = 64.

Use this property only when editing the pattern feature.

This property is valid only when specifying [ILocalCurvePatternFeatureData::D1Direction](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalCurvePatternFeatureData~D1Direction.md) using a 3D curve.

If you try to change this property to null or Nothing, [IFeature::ModifyDefinition](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~ModifyDefinition.md) returns true but the property does not change.

For more information, see the **Curve Driven Component Pattern** topic in the SOLIDWORKS user-interface help.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ILocalCurvePatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalCurvePatternFeatureData.md)  
[ILocalCurvePatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalCurvePatternFeatureData_members.md)
