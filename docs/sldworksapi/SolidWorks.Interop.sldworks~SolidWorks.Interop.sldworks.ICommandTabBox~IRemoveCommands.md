# IRemoveCommands Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandTabBox~IRemoveCommands`

Removes the specified buttons from this CommandManager tab box.
Removes the specified buttons from this CommandManager tab box.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IRemoveCommands( _
   ByVal CommandIDCount As System.Integer, _
   ByRef CommandIDs As System.Integer _
) As System.Boolean
```

```

Dim instance As ICommandTabBox
Dim CommandIDCount As System.Integer
Dim CommandIDs As System.Integer
Dim value As System.Boolean
 
value = instance.IRemoveCommands(CommandIDCount, CommandIDs)
```

```

System.bool IRemoveCommands( 
   System.int CommandIDCount,
   ref System.int CommandIDs
)
```

```

System.bool IRemoveCommands( 
   System.int CommandIDCount,
   System.int% CommandIDs
) 
```

#### Parameters

*CommandIDCount*
:   Number of buttons to remove from this CommandManager tab box

*CommandIDs*
:   - in-process, unmanaged C++: Pointer to an array of the command IDs for the buttons you want removed from this CommandManager tab box (see **Remarks**)

    - VBA, VB.NET, C#, and C++/CLI: Not supported

    See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

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
[ICommandTabBox::RemoveCommands Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandTabBox~RemoveCommands.md)
