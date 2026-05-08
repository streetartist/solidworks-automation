# HasMenu Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandGroup~HasMenu`

Gets or sets whether this CommandGroup has a menu.
Gets or sets whether this CommandGroup has a menu.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property HasMenu As System.Boolean
```

```

Dim instance As ICommandGroup
Dim value As System.Boolean
 
instance.HasMenu = value
 
value = instance.HasMenu
```

```

System.bool HasMenu {get; set;}
```

```

property System.bool HasMenu {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True if this CommandGroup has a menu, false if not (see **Remarks**)

Remarks

By default, this CommandGroup has a menu.

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
[ICommandGroup::HasMenu Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandGroup~HasMenu.md)  
[ICommandManager::AddContextMenu Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandManager~AddContextMenu.md)  
[ICommandGroup::MenuPosition Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandGroup~MenuPosition.md)
