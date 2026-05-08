# GetToolbarState Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetToolbarState`

Obsolete. Superseded by ISldWorks::GetToolbarState2.
Obsolete. Superseded by [ISldWorks::GetToolbarState2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetToolbarState2.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetToolbarState( _
   ByVal Module As System.String, _
   ByVal ToolbarId As System.Integer, _
   ByVal ToolbarState As System.Integer _
) As System.Boolean
```

```

Dim instance As ISldWorks
Dim Module As System.String
Dim ToolbarId As System.Integer
Dim ToolbarState As System.Integer
Dim value As System.Boolean
 
value = instance.GetToolbarState(Module, ToolbarId, ToolbarState)
```

```

System.bool GetToolbarState( 
   System.string Module,
   System.int ToolbarId,
   System.int ToolbarState
)
```

```

System.bool GetToolbarState( 
   System.String^ Module,
   System.int ToolbarId,
   System.int ToolbarState
) 
```

#### Parameters

*Module*

*ToolbarId*

*ToolbarState*

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.md)  
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.md)
