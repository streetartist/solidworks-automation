# AddContextMenu Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandManager~AddContextMenu`

Adds a new context-sensitive menu to the CommandManager.
Adds a new context-sensitive menu to the CommandManager.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function AddContextMenu( _
   ByVal UserID As System.Integer, _
   ByVal Title As System.String _
) As CommandGroup
```

```

Dim instance As ICommandManager
Dim UserID As System.Integer
Dim Title As System.String
Dim value As CommandGroup
 
value = instance.AddContextMenu(UserID, Title)
```

```

CommandGroup AddContextMenu( 
   System.int UserID,
   System.string Title
)
```

```

CommandGroup^ AddContextMenu( 
   System.int UserID,
   System.String^ Title
) 
```

#### Parameters

*UserID*
:   User-defined ID for this context-sensitive menu

*Title*
:   Name of the context-sensitive menu to add to the CommandManager

#### Return Value

Pointer to [ICommandGroup](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandGroup.md) object

Remarks

A context-sensitive menu is a pop-up menu that is displayed when a user right-clicks a selectable object type defined by [ICommandGroup::SelectType](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandGroup~SelectType.md) and, if the object type is a custom feature, [ICommandGroup::CustomNames](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandGroup~CustomNames.md).

You can turn off all menus or all toolbars for a CommandGroup. See [ICommandGroup::HasMenu](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandGroup~HasMenu.md) and [ICommandGroup::HasToolbar](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandGroup~HasToolbar.md) for details.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ICommandManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandManager.md)  
[ICommandManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandManager_members.md)  
[ICommandGroup::Name Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandGroup~Name.md)  
[ICommandGroup::SelectType Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandGroup~SelectType.md)  
[ICommandManager::RemoveCommandGroup Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandManager~RemoveCommandGroup.md)
