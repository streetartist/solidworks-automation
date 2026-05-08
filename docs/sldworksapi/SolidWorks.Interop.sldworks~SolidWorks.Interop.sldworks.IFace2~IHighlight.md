# IHighlight Method (IFace2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~IHighlight`

Adds highlighting to or removes highlighting from a face.
Adds highlighting to or removes highlighting from a face.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub IHighlight( _
   ByVal State As System.Boolean _
) 
```

```

Dim instance As IFace2
Dim State As System.Boolean
 
instance.IHighlight(State)
```

```

void IHighlight( 
   System.bool State
)
```

```

void IHighlight( 
   System.bool State
) 
```

#### Parameters

*State*
:   True adds highlighting, false removes highlighting

Remarks

Highlighting remains in effect until the model is rebuilt or redrawn.

This method is not supported for faces obtained from reference surface bodies.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IFace2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.md)  
[IFace2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2_members.md)  
[IFace2::Highlight Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~Highlight.md)  
[IEdge::Highlight Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge~Highlight.md)
