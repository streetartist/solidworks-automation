# GetContourEdges Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~GetContourEdges`

Gets the edges for a sketch that has one contour.
Gets the edges for a sketch that has one contour.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetContourEdges( _
   ByVal Xform As System.Object _
) As System.Object
```

```

Dim instance As ISketch
Dim Xform As System.Object
Dim value As System.Object
 
value = instance.GetContourEdges(Xform)
```

```

System.object GetContourEdges( 
   System.object Xform
)
```

```

System.Object^ GetContourEdges( 
   System.Object^ Xform
) 
```

#### Parameters

*Xform*
:   Array of size 16 doubles representing the transform

#### Return Value

Array of [edges](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge.md)

Remarks

This method supports sketches with one contour only. For sketches with multiple contours, use [ISketch::GetSketchContours](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~GetSketchContours.md) or [ISketch::IGetSketchContours](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~IGetSketchContours.md) and then [ISketchContour::GetEdges](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchContour~GetEdges.md) or [ISketchContour::IGetEdges](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchContour~IGetEdges.md).

Specifying the unit transform returns the edges in the space of the sketch.

If your application is expecting the returned edges to be in the context of the model's coordinate system, then xform should be the inverse of the transform returned by [ISketch::ModelToSketchTransform](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~ModelToSketchTransform.md).

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISketch Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch.md)  
[ISketch Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch_members.md)  
[ISketch::GetContourEdgeCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~GetContourEdgeCount.md)  
[ISketch::IGetContourEdges Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~IGetContourEdges.md)  
[ISketchContour Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchContour.md)
