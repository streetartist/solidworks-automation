# GetRelatedTangentEdgeCount Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetRelatedTangentEdgeCount`

Gets the number of visible tangent edges for the specified bendline in a flat-pattern drawing view.
Gets the number of visible tangent edges for the specified bendline in a [flat-pattern drawing view](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IsFlatPatternView.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetRelatedTangentEdgeCount( _
   ByVal BendLine As System.Object _
) As System.Integer
```

```

Dim instance As IView
Dim BendLine As System.Object
Dim value As System.Integer
 
value = instance.GetRelatedTangentEdgeCount(BendLine)
```

```

System.int GetRelatedTangentEdgeCount( 
   System.object BendLine
)
```

```

System.int GetRelatedTangentEdgeCount( 
   System.Object^ BendLine
) 
```

#### Parameters

*BendLine*
:   Bendline whose visible tangent edges you want (see **Remarks**)

#### Return Value

Array of visible tangent edges for the specified bendline

Remarks

Hidden tangent edges are not returned by this method. Call [IDrawingDoc::ViewTangentEdges](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~ViewTangentEdges.md) to change the visibility of tangent edges in a drawing.

Call [IView::GetBendLineCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetBendLineCount.md) to get the number of bendlines in a flat-pattern drawing view. Call [IView::GetBendLines](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetBendLines.md) or [IView::IGetBendLines](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetBendLines.md) to get an array of bendlines for a flat-pattern drawing view. Use the value returned by IView::GetBendLineCount to determine the index of the bendline in the array of bendlines you want.

Example

[Get Tangent Edges of Bendlines (VB.NET)](Get_Tangent_Edges_of_Bendlines_Example_VBNET.htm)  
[Get Tangent Edges of Bendline (VBA)](Get_Tangent_Edges_of_Bendlines_Example_VB.htm)  
[Get Tangent Edges of Bendlines (C#)](Get_Tangent_Edges_of_Bendlines_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.md)  
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.md)  
[IView::GetRelatedTangentEdges Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetRelatedTangentEdges.md)  
[IView::IGetRelatedTangentEdges Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetRelatedTangentEdges.md)
