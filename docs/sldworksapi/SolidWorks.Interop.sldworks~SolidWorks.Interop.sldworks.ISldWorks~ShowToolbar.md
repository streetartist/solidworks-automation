# ShowToolbar Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~ShowToolbar`

Obsolete. Superseded by ISldWorks::ShowToolbar2.
Obsolete. Superseded by [ISldWorks::ShowToolbar2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~ShowToolbar2.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function ShowToolbar( _
   ByVal ModuleName As System.String, _
   ByVal ToolbarId As System.Integer _
) As System.Boolean
```

```

Dim instance As ISldWorks
Dim ModuleName As System.String
Dim ToolbarId As System.Integer
Dim value As System.Boolean
 
value = instance.ShowToolbar(ModuleName, ToolbarId)
```

```

System.bool ShowToolbar( 
   System.string ModuleName,
   System.int ToolbarId
)
```

```

System.bool ShowToolbar( 
   System.String^ ModuleName,
   System.int ToolbarId
) 
```

#### Parameters

*ModuleName*

*ToolbarId*

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.md)  
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.md)
