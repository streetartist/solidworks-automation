# Activate Method (ICommandGroup)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandGroup~Activate`

Activates the CommandGroup.
Activates the CommandGroup.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function Activate() As System.Boolean
```

```

Dim instance As ICommandGroup
Dim value As System.Boolean
 
value = instance.Activate()
```

```

System.bool Activate()
```

```

System.bool Activate(); 
```

#### Return Value

True if the CommandGroup is activated, false if not

Remarks

After completely creating a CommandGroup, use this method to activate it. You only need to activate the top-level group; you do not need to activate child groups.

Example

[Create Flyouts in the CommandManager (C#)](Create_Flyouts_in_the_CommandManager_Example_CSharp.htm)  
[Create Flyouts in the CommandManager (VB.NET)](Create_Flyouts_in_the_CommandManager_Example_VBNET.htm)  
[Create Submenus in the CommandManager (C#)](Create_Submenus_in_the_CommandManager_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ICommandGroup Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandGroup.md)  
[ICommandGroup Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandGroup_members.md)  
[ICommandGroup::MenuPosition Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandGroup~MenuPosition.md)
