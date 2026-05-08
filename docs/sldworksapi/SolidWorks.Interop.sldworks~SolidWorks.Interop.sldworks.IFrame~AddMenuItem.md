# AddMenuItem Method (IFrame)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFrame~AddMenuItem`

Obsolete. Superseded by IFrame::AddMenuItem2.
Obsolete. Superseded by [IFrame::AddMenuItem2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFrame~AddMenuItem2.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function AddMenuItem( _
   ByVal Menu As System.String, _
   ByVal Item As System.String, _
   ByVal Position As System.Integer, _
   ByVal CallbackFcnAndModule As System.String _
) As System.Boolean
```

```

Dim instance As IFrame
Dim Menu As System.String
Dim Item As System.String
Dim Position As System.Integer
Dim CallbackFcnAndModule As System.String
Dim value As System.Boolean
 
value = instance.AddMenuItem(Menu, Item, Position, CallbackFcnAndModule)
```

```

System.bool AddMenuItem( 
   System.string Menu,
   System.string Item,
   System.int Position,
   System.string CallbackFcnAndModule
)
```

```

System.bool AddMenuItem( 
   System.String^ Menu,
   System.String^ Item,
   System.int Position,
   System.String^ CallbackFcnAndModule
) 
```

#### Parameters

*Menu*

*Item*

*Position*

*CallbackFcnAndModule*

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IFrame Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFrame.md)  
[IFrame Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFrame_members.md)
