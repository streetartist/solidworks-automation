# GetToolbarDock Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetToolbarDock`

Obsolete. Superseded by ISldWorks::GetToolbarDock2.
Obsolete. Superseded by [ISldWorks::GetToolbarDock2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetToolbarDock2.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetToolbarDock( _
   ByVal ModuleIn As System.String, _
   ByVal ToolbarIDIn As System.Integer _
) As System.Integer
```

```

Dim instance As ISldWorks
Dim ModuleIn As System.String
Dim ToolbarIDIn As System.Integer
Dim value As System.Integer
 
value = instance.GetToolbarDock(ModuleIn, ToolbarIDIn)
```

```

System.int GetToolbarDock( 
   System.string ModuleIn,
   System.int ToolbarIDIn
)
```

```

System.int GetToolbarDock( 
   System.String^ ModuleIn,
   System.int ToolbarIDIn
) 
```

#### Parameters

*ModuleIn*

*ToolbarIDIn*

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.md)  
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.md)
