# AddCommands Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandTabBox~AddCommands`

Adds buttons to this CommandManager tab box.
Adds buttons to this CommandManager tab box.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function AddCommands( _
   ByVal CommandIDs As System.Object, _
   ByVal TextDisplayStyles As System.Object _
) As System.Boolean
```

```

Dim instance As ICommandTabBox
Dim CommandIDs As System.Object
Dim TextDisplayStyles As System.Object
Dim value As System.Boolean
 
value = instance.AddCommands(CommandIDs, TextDisplayStyles)
```

```

System.bool AddCommands( 
   System.object CommandIDs,
   System.object TextDisplayStyles
)
```

```

System.bool AddCommands( 
   System.Object^ CommandIDs,
   System.Object^ TextDisplayStyles
) 
```

#### Parameters

*CommandIDs*
:   Array of command IDs for the buttons (see **Remarks**)

*TextDisplayStyles*
:   Array of the text display styles for the buttons as defined in [swCommandTabButtonTextDisplay\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swCommandTabButtonTextDisplay_e.html)

#### Return Value

True if the buttons are added to the CommandManager tab box, false if not

Remarks

You can add both CommandGroup and FlyoutGroup items to CommandManager. Populate CommandIDs by calling [IFlyoutGroup::CmdID](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFlyoutGroup~CmdID.md) for FlyoutGroups and [ICommandGroup::CommandID](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandGroup~CommandID.md) or [ICommandGroup::ToolbarId](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandGroup~ToolbarId.md) after calling [ICommandGroup::Activate](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandGroup~Activate.md) for CommandGroups.

Example

[Create CommandManager Tab and Tab Boxes (VB.NET)](Create_CommandManager_Tab_and_Tab_Boxes_Example_VB.NET.htm)  
[Create CommandManager Tab and Tab Boxes (C#)](Create_CommandManager_Tab_and_Tab_Boxes_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ICommandTabBox Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandTabBox.md)  
[ICommandTabBox Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandTabBox_members.md)  
[ICommandTabBox::IAddCommands Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandTabBox~IAddCommands.md)
