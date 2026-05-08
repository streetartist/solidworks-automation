# Highlight Method (IEdge)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge~Highlight`

Add highlights or removes highlights from this edge.
Add highlights or removes highlights from this edge.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub Highlight( _
   ByVal State As System.Boolean _
) 
```

```

Dim instance As IEdge
Dim State As System.Boolean
 
instance.Highlight(State)
```

```

void Highlight( 
   System.bool State
)
```

```

void Highlight( 
   System.bool State
) 
```

#### Parameters

*State*
:   True adds highlights to this edge, false removes highlights from this edge

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IEdge Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge.md)  
[IEdge Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge_members.md)  
[IEdge::Display Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge~Display.md)  
[IFace2::Highlight Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~Highlight.md)  
[IFace2::IHighlight Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~IHighlight.md)  
[IVertex::Display Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVertex~Display.md)
