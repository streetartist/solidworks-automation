# Display2 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~Display2`

Obsolete. Superseded by IBody2::Display3.
Obsolete. Superseded by [IBody2::Display3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~Display3.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub Display2( _
   ByVal Part As PartDoc, _
   ByVal Color As System.Integer, _
   ByVal Option As System.Integer _
) 
```

```

Dim instance As IBody2
Dim Part As PartDoc
Dim Color As System.Integer
Dim Option As System.Integer
 
instance.Display2(Part, Color, Option)
```

```

void Display2( 
   PartDoc Part,
   System.int Color,
   System.int Option
)
```

```

void Display2( 
   PartDoc^ Part,
   System.int Color,
   System.int Option
) 
```

#### Parameters

*Part*

*Color*

*Option*

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IBody2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.md)  
[IBody2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2_members.md)
