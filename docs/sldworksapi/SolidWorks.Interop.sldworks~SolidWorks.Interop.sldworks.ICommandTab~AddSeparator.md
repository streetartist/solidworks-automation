# AddSeparator Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandTab~AddSeparator`

Adds a separator to this CommandManager tab.
Adds a separator to this CommandManager tab.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function AddSeparator( _
   ByVal CommandTabBoxIn As CommandTabBox, _
   ByVal CommandID As System.Integer _
) As CommandTabBox
```

```

Dim instance As ICommandTab
Dim CommandTabBoxIn As CommandTabBox
Dim CommandID As System.Integer
Dim value As CommandTabBox
 
value = instance.AddSeparator(CommandTabBoxIn, CommandID)
```

```

CommandTabBox AddSeparator( 
   CommandTabBox CommandTabBoxIn,
   System.int CommandID
)
```

```

CommandTabBox^ AddSeparator( 
   CommandTabBox^ CommandTabBoxIn,
   System.int CommandID
) 
```

#### Parameters

*CommandTabBoxIn*
:   [CommandManager tab box](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandTabBox.md) to which to add the separator

*CommandID*
:   Button before which to place the separator (see Remarks)

#### Return Value

New [CommandManager tab box](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandTabBox.md)

Remarks

The specified CommandManager tab is split into two. The left side is the original CommandManager tab box, and the right side is the new CommandManager tab box. The first button on the new CommandManager tab box is the button specified by CommandID.

If the CommandManager tab box has multiple commands with the same CommandID, then a separator is added before the first matching CommandID.

You can get the CommandID using [ICommandGroup::CommandID](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandGroup~CommandID.md) or [ICommandGroup::ToolbarId](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandGroup~ToolbarId.md) after calling [ICommandGroup::Activate](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandGroup~Activate.md).

Example

[Create CommandManager Tab and Tab Boxes (VB.NET)](Create_CommandManager_Tab_and_Tab_Boxes_Example_VB.NET.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ICommandTab Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandTab.md)  
[ICommandTab Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandTab_members.md)
