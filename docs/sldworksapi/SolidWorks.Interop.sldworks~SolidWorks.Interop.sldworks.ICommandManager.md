# ICommandManager Interface

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandManager`

Allows add-in applications to add and remove CommandGroups (menus and toolbars) to the CommandManager.
Allows add-in applications to add and remove [CommandGroups](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandGroup.md) (menus and toolbars) to the CommandManager.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Public Interface ICommandManager 
```

```

Dim instance As ICommandManager
```

```

public interface ICommandManager 
```

```

public interface class ICommandManager 
```

Remarks

Only one CommandManager can exist in an add-in application.

See [CommandManager and CommandGroups](sldworksAPIProgGuide.chm::/OVERVIEW/CommandManager_and_CommandGroups.htm) to learn how to create a CommandManager and add and remove CommandGroups.

Example

[Create Flyouts in the CommandManager (C#)](Create_Flyouts_in_the_CommandManager_Example_CSharp.htm)  
[Create Flyouts in the CommandManager (VB.NET)](Create_Flyouts_in_the_CommandManager_Example_VBNET.htm)  
[Create Submenus in the CommandManager (C#)](Create_Submenus_in_the_CommandManager_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ICommandManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandManager_members.md)  
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.md)
