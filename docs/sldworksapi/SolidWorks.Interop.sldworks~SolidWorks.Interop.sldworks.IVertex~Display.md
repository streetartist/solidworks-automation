# Display Method (IVertex)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVertex~Display`

Highlights the vertex in the specified color.
Highlights the vertex in the specified color.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub Display( _
   ByVal TopDoc As ModelDoc2, _
   ByVal Color As System.Integer, _
   ByVal Scale As System.Double, _
   ByVal HighlightState As System.Boolean _
) 
```

```

Dim instance As IVertex
Dim TopDoc As ModelDoc2
Dim Color As System.Integer
Dim Scale As System.Double
Dim HighlightState As System.Boolean
 
instance.Display(TopDoc, Color, Scale, HighlightState)
```

```

void Display( 
   ModelDoc2 TopDoc,
   System.int Color,
   System.double Scale,
   System.bool HighlightState
)
```

```

void Display( 
   ModelDoc2^ TopDoc,
   System.int Color,
   System.double Scale,
   System.bool HighlightState
) 
```

#### Parameters

*TopDoc*
:   [Model](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.md) in which to display the vertex

*Color*
:   COLORREF value for highlighting

*Scale*
:   Radius of the circle used to display the vertex

    NOTE: Vertex is displayed as a circle. By default, the radius is 4 pixels. Therefore, a scale of 1 is equal to 4 pixels.

*HighlightState*
:   True to highlight the vertex, false to not

Remarks

|  |  |
| --- | --- |
| **If HighlightState set to...** | **Then the vertex is...** |
| True | Highlighted in the color specified for Color |
| False | Hidden and Color is ignored |

Example

[Display Vertices (VBA)](Display_Vertices_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IVertex Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVertex.md)  
[IVertex Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVertex_members.md)
