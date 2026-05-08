# AddCommandTabBox Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandTab~AddCommandTabBox`

Adds a tab box to this CommandManager tab.
Adds a tab box to this CommandManager tab.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function AddCommandTabBox() As CommandTabBox
```

```

Dim instance As ICommandTab
Dim value As CommandTabBox
 
value = instance.AddCommandTabBox()
```

```

CommandTabBox AddCommandTabBox()
```

```

CommandTabBox^ AddCommandTabBox(); 
```

#### Return Value

[CommandManager tab box](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandTabBox.md)

Remarks

The CommandManager tab box is always added to the end of the CommandManager tab, unless it is the first CommandManager tab box added to this CommandManager tab. If so, then this CommandManager tab box is placed at the beginning of the CommandManager tab.

The CommandManager tab box is not immediately visible. You must first [add buttons](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandTabBox~AddCommands.md) to the CommandManager tab box.

Example

[Create CommandManager Tab and Tab Boxes (VB.NET)](Create_CommandManager_Tab_and_Tab_Boxes_Example_VB.NET.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ICommandTab Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandTab.md)  
[ICommandTab Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandTab_members.md)
