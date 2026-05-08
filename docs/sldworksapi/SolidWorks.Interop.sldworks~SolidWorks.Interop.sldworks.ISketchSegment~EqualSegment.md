# EqualSegment Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSegment~EqualSegment`

Divides this sketch segment into equally spaced sketch segments or points.
Divides this sketch segment into equally spaced sketch segments or points.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function EqualSegment( _
   ByVal SketchType As System.Integer, _
   ByVal SegmentPoints As System.Integer _
) As System.Boolean
```

```

Dim instance As ISketchSegment
Dim SketchType As System.Integer
Dim SegmentPoints As System.Integer
Dim value As System.Boolean
 
value = instance.EqualSegment(SketchType, SegmentPoints)
```

```

System.bool EqualSegment( 
   System.int SketchType,
   System.int SegmentPoints
)
```

```

System.bool EqualSegment( 
   System.int SketchType,
   System.int SegmentPoints
) 
```

#### Parameters

*SketchType*
:   Type of entity with which to divide this sketch segment as defined in [swSketchSegmentType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swSketchSegmentType_e.html)

*SegmentPoints*
:   2 <= Number of sketchType entities into which to divide this sketch segment <= 100

#### Return Value

True if successful, false if not

Example

[Divide Sketch Segment (VBA)](Divide_Sketch_Segment_Example_VB.htm)  
[Divide Sketch Segment (VB.NET)](Divide_Sketch_Segment_Example_VBNET.htm)  
[Divide Sketch Segment (C#)](Divide_Sketch_Segment_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISketchSegment Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSegment.md)  
[ISketchSegment Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSegment_members.md)
