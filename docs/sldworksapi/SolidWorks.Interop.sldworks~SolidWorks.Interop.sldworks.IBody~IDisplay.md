# IDisplay Method (IBody)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody~IDisplay`

Obsolete. Superseded by IBody2::Display3.
Obsolete. Superseded by [IBody2::Display3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~Display3.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub IDisplay( _
   ByVal Part As PartDoc, _
   ByVal Color As System.Integer _
) 
```

```

Dim instance As IBody
Dim Part As PartDoc
Dim Color As System.Integer
 
instance.IDisplay(Part, Color)
```

```

void IDisplay( 
   PartDoc Part,
   System.int Color
)
```

```

void IDisplay( 
   PartDoc^ Part,
   System.int Color
) 
```

#### Parameters

*Part*

*Color*

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IBody Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody.md)  
[IBody Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody_members.md)
