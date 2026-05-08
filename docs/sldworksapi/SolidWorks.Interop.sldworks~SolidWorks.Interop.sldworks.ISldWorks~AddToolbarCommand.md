# AddToolbarCommand Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~AddToolbarCommand`

Obsolete. Superseded by ISldWorks::AddToolbarCommand2.
Obsolete. Superseded by [ISldWorks::AddToolbarCommand2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~AddToolbarCommand2.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function AddToolbarCommand( _
   ByVal ModuleName As System.String, _
   ByVal ToolbarId As System.Integer, _
   ByVal ToolbarIndex As System.Integer, _
   ByVal CommandString As System.String _
) As System.Boolean
```

```

Dim instance As ISldWorks
Dim ModuleName As System.String
Dim ToolbarId As System.Integer
Dim ToolbarIndex As System.Integer
Dim CommandString As System.String
Dim value As System.Boolean
 
value = instance.AddToolbarCommand(ModuleName, ToolbarId, ToolbarIndex, CommandString)
```

```

System.bool AddToolbarCommand( 
   System.string ModuleName,
   System.int ToolbarId,
   System.int ToolbarIndex,
   System.string CommandString
)
```

```

System.bool AddToolbarCommand( 
   System.String^ ModuleName,
   System.int ToolbarId,
   System.int ToolbarIndex,
   System.String^ CommandString
) 
```

#### Parameters

*ModuleName*

*ToolbarId*

*ToolbarIndex*

*CommandString*

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.md)  
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.md)
