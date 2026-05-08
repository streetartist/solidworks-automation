# Display Method (IEdge)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge~Display`

Highlights this edge with the specified color.
Highlights this edge with the specified color.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub Display( _
   ByVal Width As System.Integer, _
   ByVal Red As System.Double, _
   ByVal Green As System.Double, _
   ByVal Blue As System.Double, _
   ByVal HighlightState As System.Boolean _
) 
```

```

Dim instance As IEdge
Dim Width As System.Integer
Dim Red As System.Double
Dim Green As System.Double
Dim Blue As System.Double
Dim HighlightState As System.Boolean
 
instance.Display(Width, Red, Green, Blue, HighlightState)
```

```

void Display( 
   System.int Width,
   System.double Red,
   System.double Green,
   System.double Blue,
   System.bool HighlightState
)
```

```

void Display( 
   System.int Width,
   System.double Red,
   System.double Green,
   System.double Blue,
   System.bool HighlightState
) 
```

#### Parameters

*Width*
:   Highlight width

*Red*
:   Red value of RGB value for the color, between 0 and 1

*Green*
:   Green value of RGB value for the color, between 0 and 1

*Blue*
:   Blue value if RGB value for the color, between 0 and 1

*HighlightState*
:   True if the edge is highlighted, false if not

Remarks

To show the same edge with a different color, hide it and then set a different color. SOLIDWORKS shows the edge in the specified color until you hide it. Rotation, zoom, other repaint actions do not cause the edge to disappear.

Example

[Add Highlighting to or Remove Highlighting From Edges (VBA)](Add_Highlighting_to_or_Remove_Highlight_from_Edges_Example_VB.htm)  
[Get Faces Affected by Feature (VBA)](Get_Faces_Affected_by_Feature_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IEdge Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge.md)  
[IEdge Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge_members.md)  
[IFace2::IHighlight Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~IHighlight.md)  
[IFace2::Highlight Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~Highlight.md)  
[IVertex::Display Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVertex~Display.md)  
[IEdge::Highlight Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge~Highlight.md)
