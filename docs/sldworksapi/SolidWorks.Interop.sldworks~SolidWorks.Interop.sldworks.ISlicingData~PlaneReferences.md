# PlaneReferences Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISlicingData~PlaneReferences`

Sets the reference entities of the first slicing plane.
Sets the reference entities of the first slicing plane.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

WriteOnly Property PlaneReferences As System.Object
```

```

Dim instance As ISlicingData
 
instance.PlaneReferences = value
```

```

System.object PlaneReferences {set;}
```

```

property System.Object^ PlaneReferences {
   void set (    System.Object^ value);
}
```

#### Property Value

Array of reference entities (see **Remarks**)

Remarks

Use this property to specify either:

- a planar entity (e.g., [IFace2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.md), [IRefPlane](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefPlane.md)) to produce a linear pattern of parallel slices

    - or -

- a linear entity (e.g., [IEdge](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge.md), [IRefAxis](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefAxis.md), [ISketchLine](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchLine.md)) and a vertex ([IRefPoint](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefPoint.md), [IVertex](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVertex.md)) to produce a radial pattern of slices whose axis is the linear entity.

Use [ISlicingData::NumberOfPlanes](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISlicingData~NumberOfPlanes.md) to specify the number of slices and [ISlicingData::Offset](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISlicingData~Offset.md) to specify the linear or radial spacing of the slices.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISlicingData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISlicingData.md)  
[ISlicingData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISlicingData_members.md)
