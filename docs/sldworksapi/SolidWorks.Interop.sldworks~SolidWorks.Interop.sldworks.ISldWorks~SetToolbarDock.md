# SetToolbarDock Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~SetToolbarDock`

Obsolete. Superseded by ISldWorks::SetToolbarDock2.
Obsolete. Superseded by [ISldWorks::SetToolbarDock2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~SetToolbarDock2.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub SetToolbarDock( _
   ByVal ModuleIn As System.String, _
   ByVal ToolbarIDIn As System.Integer, _
   ByVal DocStatePosIn As System.Integer _
) 
```

```

Dim instance As ISldWorks
Dim ModuleIn As System.String
Dim ToolbarIDIn As System.Integer
Dim DocStatePosIn As System.Integer
 
instance.SetToolbarDock(ModuleIn, ToolbarIDIn, DocStatePosIn)
```

```

void SetToolbarDock( 
   System.string ModuleIn,
   System.int ToolbarIDIn,
   System.int DocStatePosIn
)
```

```

void SetToolbarDock( 
   System.String^ ModuleIn,
   System.int ToolbarIDIn,
   System.int DocStatePosIn
) 
```

#### Parameters

*ModuleIn*

*ToolbarIDIn*

*DocStatePosIn*

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.md)  
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.md)
