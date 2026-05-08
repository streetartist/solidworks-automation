# TransformReferenceEntity Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMoveCopyBodyFeatureData~TransformReferenceEntity`

Gets or sets the entity to reference when moving or rotating the selected bodies.
Gets or sets the entity to reference when moving or rotating the selected bodies.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property TransformReferenceEntity As System.Object
```

```

Dim instance As IMoveCopyBodyFeatureData
Dim value As System.Object
 
instance.TransformReferenceEntity = value
 
value = instance.TransformReferenceEntity
```

```

System.object TransformReferenceEntity {get; set;}
```

```

property System.Object^ TransformReferenceEntity {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

#### Property Value

Pointer to one of these entities:

- [Coordinate system](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.md)
- [Edge](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge.md)
- [Sketch point](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPoint.md)
- [Vertex](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVertex.md)

Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this method.

Example

[Copy and Rotate Body Using Edge (VBA)](Copy_and_Rotate_Body_using_Edge_Example_VB.htm)  
[Modify Move/Copy Body Using Vertex (C#)](Move_and_Copy_Body_Using_Vertex_Example_CSharp.htm)  
[Modify Move/Copy Body Using Vertex (VB.NET)](Move_and_Copy_Body_Using_Vertex_Example_VBNET.htm)  
[Modify Move/Copy Body Using Vertex (VBA)](Move_and_Copy_Body_using_Vertex_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IMoveCopyBodyFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMoveCopyBodyFeatureData.md)  
[IMoveCopyBodyFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMoveCopyBodyFeatureData_members.md)
