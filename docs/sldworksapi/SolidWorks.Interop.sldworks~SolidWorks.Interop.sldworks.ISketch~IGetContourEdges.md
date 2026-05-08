# IGetContourEdges Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~IGetContourEdges`

Gets the edges for a sketch that has one contour.
Gets the edges for a sketch that has one contour.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IGetContourEdges( _
   ByRef Xform As System.Double, _
   ByVal EdgeCount As System.Integer _
) As Edge
```

```

Dim instance As ISketch
Dim Xform As System.Double
Dim EdgeCount As System.Integer
Dim value As Edge
 
value = instance.IGetContourEdges(Xform, EdgeCount)
```

```

Edge IGetContourEdges( 
   ref System.double Xform,
   System.int EdgeCount
)
```

```

Edge^ IGetContourEdges( 
   System.double% Xform,
   System.int EdgeCount
) 
```

#### Parameters

*Xform*
:   Sketch entities, edges

*EdgeCount*
:   Number of edges

#### Return Value

- in-process, unmanaged C++: Pointer to an array of [edges](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge.md)

- VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

Remarks

This method supports sketches with one contour only. For sketches with multiple contours, use [ISketch::GetSketchContours](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~GetSketchContours.md) or [ISketch::IGetSketchContours](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~IGetSketchContours.md) and then [ISketchContour::GetEdges](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchContour~GetEdges.md) or [ISketchContour::IGetEdges](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchContour~IGetEdges.md).

To get the number of edges, call [ISketch::GetContourEdgesCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~GetContourEdgeCount.md) before calling this method.

Specifying the unit transform returns the edges in the space of the sketch.

If your application is expecting the returned edges to be in the context of the model's coordinate system, then xform should be the inverse of the transform returned by [ISketch::ModelToSketchTransform](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~ModelToSketchTransform.md).

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISketch Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch.md)  
[ISketch Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch_members.md)  
[ISketch::GetContourEdges Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~GetContourEdges.md)  
[ISketchContour Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchContour.md)
