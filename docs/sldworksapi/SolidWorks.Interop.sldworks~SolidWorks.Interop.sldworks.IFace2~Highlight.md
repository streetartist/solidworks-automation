# Highlight Method (IFace2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~Highlight`

Adds highlighting to or removes highlighting from a face.
Adds highlighting to or removes highlighting from a face.

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

Dim instance As IFace2
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
:   True adds highlighting, false removes highlighting

Remarks

Highlighting remains in effect until the model is rebuilt or redrawn.

This method is not supported for faces obtained from reference surface bodies.

Example

[Roll Back Model (C#)](Roll_Back_Model_Example_CSharp.htm)  
[Roll Back Model (VB.NET)](Roll_Back_Model_Example_VBNET.htm)  
[Roll Back Model (VBA)](Roll_Back_Model_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IFace2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.md)  
[IFace2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2_members.md)  
[IFace2::IHighlight Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~IHighlight.md)  
[IEdge::Highlight Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge~Highlight.md)
