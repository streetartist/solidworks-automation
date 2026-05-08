# RemoveCommands Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandTabBox~RemoveCommands`

Removes the specified buttons from this CommandManager tab box.
Removes the specified buttons from this CommandManager tab box.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function RemoveCommands( _
   ByVal CommandIDs As System.Object _
) As System.Boolean
```

```

Dim instance As ICommandTabBox
Dim CommandIDs As System.Object
Dim value As System.Boolean
 
value = instance.RemoveCommands(CommandIDs)
```

```

System.bool RemoveCommands( 
   System.object CommandIDs
)
```

```

System.bool RemoveCommands( 
   System.Object^ CommandIDs
) 
```

#### Parameters

*CommandIDs*
:   Array of command IDs for the buttons you want removed from this CommandManager tab box (see **Remarks**)

#### Return Value

True if the specified buttons are removed, false if not

Remarks

You can get the CommandID values using [ICommandGroup::CommandID](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandGroup~CommandID.md) or [ICommandGroup::ToolbarId](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandGroup~ToolbarId.md) after calling [ICommandGroup::Activate](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandGroup~Activate.md).

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ICommandTabBox Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandTabBox.md)  
[ICommandTabBox Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandTabBox_members.md)  
[ICommandTabBox::IRemoveCommands Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandTabBox~IRemoveCommands.md)
