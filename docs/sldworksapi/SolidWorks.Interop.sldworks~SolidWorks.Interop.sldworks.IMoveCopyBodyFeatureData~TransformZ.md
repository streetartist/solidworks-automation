# TransformZ Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMoveCopyBodyFeatureData~TransformZ`

Gets the z coordinate for either moving or rotating the selected bodies.
Gets the z coordinate for either moving or rotating the selected bodies.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property TransformZ As System.Double
```

```

Dim instance As IMoveCopyBodyFeatureData
Dim value As System.Double
 
instance.TransformZ = value
 
value = instance.TransformZ
```

```

System.double TransformZ {get; set;}
```

```

property System.double TransformZ {
   System.double get();
   void set (    System.double value);
}
```

#### Property Value

Meters for moving or radians for rotating

Remarks

Use [IMoveCopyBodyFeatureData::TransformType](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMoveCopyBodyFeatureData~TransformType.md) to get or set the transform type before setting this property.

[IMoveCopyBodyFeatureData::TransformReferenceEntity](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMoveCopyBodyFeatureData~TransformReferenceEntity.md) must be:

- NULL if moving the selected bodies  
  - or -
- a vertex if rotating the selected bodies

Example

[Move and Copy Body By Setting Transforms (VBA)](Move_and_Copy_Body_by_Setting_Transforms_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IMoveCopyBodyFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMoveCopyBodyFeatureData.md)  
[IMoveCopyBodyFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMoveCopyBodyFeatureData_members.md)  
[IMoveCopyBodyFeatureData::TransformX Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMoveCopyBodyFeatureData~TransformX.md)  
[IMoveCopyBodyFeatureData::TransformY Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMoveCopyBodyFeatureData~TransformY.md)
