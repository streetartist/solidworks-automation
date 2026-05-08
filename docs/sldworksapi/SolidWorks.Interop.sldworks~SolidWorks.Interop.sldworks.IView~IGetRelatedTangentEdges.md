# IGetRelatedTangentEdges Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetRelatedTangentEdges`

Gets the visible tangent edges for the specified bendline in a flat-pattern drawing view.
Gets the visible tangent edges for the specified bendline in a [flat-pattern drawing view](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IsFlatPatternView.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IGetRelatedTangentEdges( _
   ByVal BendLine As SketchSegment, _
   ByVal NumOfTangentEdges As System.Integer _
) As Edge
```

```

Dim instance As IView
Dim BendLine As SketchSegment
Dim NumOfTangentEdges As System.Integer
Dim value As Edge
 
value = instance.IGetRelatedTangentEdges(BendLine, NumOfTangentEdges)
```

```

Edge IGetRelatedTangentEdges( 
   SketchSegment BendLine,
   System.int NumOfTangentEdges
)
```

```

Edge^ IGetRelatedTangentEdges( 
   SketchSegment^ BendLine,
   System.int NumOfTangentEdges
) 
```

#### Parameters

*BendLine*
:   Bendline whose visible tangent edges you want (see **Remarks**)

*NumOfTangentEdges*
:   Number of visible tangent edges for the specified bendline

#### Return Value

- in-process, unmanaged C++: Pointer to an array of visible tangent [edges](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge.md) for the specified bendline
- VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

Remarks

Before calling this method, call [IView::GetRelatedTangentEdgeCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetRelatedTangentEdgeCount.md) to get NumOfTangentEdges.

Hidden tangent edges are not returned by this method. Call [IDrawingDoc::ViewTangentEdges](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~ViewTangentEdges.md) to change the visibility of tangent edges in a drawing.

Call [IView::GetBendLineCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetBendLineCount.md) to get the number of bendlines in a flat-pattern drawing view. Call [IView::GetBendLines](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetBendLines.md) or [IView::IGetBendLines](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetBendLines.md) to get an array of bendlines for a flat-pattern drawing view. Use the value returned by IView::GetBendLineCount to determine the index of the bendline in the array of bendlines you want.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.md)  
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.md)  
[IView::GetRelatedTangentEdges Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetRelatedTangentEdges.md)
