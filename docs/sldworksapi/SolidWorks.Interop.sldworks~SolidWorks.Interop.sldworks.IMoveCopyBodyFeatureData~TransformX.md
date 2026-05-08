# TransformX Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMoveCopyBodyFeatureData~TransformX`

Gets or sets the x coordinate for either moving or rotating the selected bodies.
Gets or sets the x coordinate for either moving or rotating the selected bodies.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property TransformX As System.Double
```

```

Dim instance As IMoveCopyBodyFeatureData
Dim value As System.Double
 
instance.TransformX = value
 
value = instance.TransformX
```

```

System.double TransformX {get; set;}
```

```

property System.double TransformX {
   System.double get();
   void set (    System.double value);
}
```

#### Property Value

x coordinate in meters for moving or radians for rotating

Remarks

Use [IMoveCopyBodyFeatureData::TransformType](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMoveCopyBodyFeatureData~TransformType.md) to get or set the transform type before setting this property.

[IMoveCopyBodyFeatureData::TransformReferenceEntity](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMoveCopyBodyFeatureData~TransformReferenceEntity.md) must be:

- Nothing or null if moving the selected bodies.  
  - or -
- a vertex if rotating the selected bodies.

Example

[Copy and Rotate Body Using Edge (VBA)](Copy_and_Rotate_Body_using_Edge_Example_VB.htm)  
[Move and Copy Body By Setting Transforms (VBA)](Move_and_Copy_Body_by_Setting_Transforms_Example_VB.htm)  
[Modify Move/Copy Body Using Vertex (C#)](Move_and_Copy_Body_Using_Vertex_Example_CSharp.htm)  
[Modify Move/Copy Body Using Vertex (VB.NET)](Move_and_Copy_Body_Using_Vertex_Example_VBNET.htm)  
[Modify Move/Copy Body Using Vertex (VBA)](Move_and_Copy_Body_using_Vertex_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IMoveCopyBodyFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMoveCopyBodyFeatureData.md)  
[IMoveCopyBodyFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMoveCopyBodyFeatureData_members.md)  
[IMoveCopyBodyFeatureData::TransformY Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMoveCopyBodyFeatureData~TransformY.md)  
[IMoveCopyBodyFeatureData::TransformZ Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMoveCopyBodyFeatureData~TransformZ.md)
