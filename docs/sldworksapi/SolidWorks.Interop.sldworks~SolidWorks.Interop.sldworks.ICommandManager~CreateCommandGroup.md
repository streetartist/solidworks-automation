# CreateCommandGroup Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandManager~CreateCommandGroup`

Obsolete. Superseded by ICommandManager::CreateCommandGroup2.
Obsolete. Superseded by [ICommandManager::CreateCommandGroup2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandManager~CreateCommandGroup2.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function CreateCommandGroup( _
   ByVal UserID As System.Integer, _
   ByVal Title As System.String, _
   ByVal ToolTip As System.String, _
   ByVal Hint As System.String, _
   ByVal Position As System.Integer _
) As CommandGroup
```

```

Dim instance As ICommandManager
Dim UserID As System.Integer
Dim Title As System.String
Dim ToolTip As System.String
Dim Hint As System.String
Dim Position As System.Integer
Dim value As CommandGroup
 
value = instance.CreateCommandGroup(UserID, Title, ToolTip, Hint, Position)
```

```

CommandGroup CreateCommandGroup( 
   System.int UserID,
   System.string Title,
   System.string ToolTip,
   System.string Hint,
   System.int Position
)
```

```

CommandGroup^ CreateCommandGroup( 
   System.int UserID,
   System.String^ Title,
   System.String^ ToolTip,
   System.String^ Hint,
   System.int Position
) 
```

#### Parameters

*UserID*
:   Unique user-defined ID for this CommandGroup

*Title*
:   Name of the CommandGroup to create (see **Remarks**)

*ToolTip*
:   ToolTip for this CommandGroup

*Hint*
:   Text displayed in SOLIDWORKS status bar when a user's mouse pointer is over this CommandGroup

*Position*
:   Position of the CommandGroup in the CommandManager for all document templates (see **Remarks**)

    NOTE: Specify 0 to add the CommandGroup to the beginning of the CommandMananger, or specify -1 to add it to the end of the CommandManager.

#### Return Value

Pointer to [ICommandGroup](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandGroup.md) object

Remarks

You can also use [ICommandGroup::MenuPosition](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandGroup~HasMenu.md) to control the position of the CommandGroup in specific document templates.

If you change the definition of an existing CommandGroup (i.e., add or remove toolbar buttons), you must assign a new unique user-defined UserID to that CommandGroup. You must perform this action to avoid conflicts with any previously existing CommandGroupa and to allow for backward and forward compatibility of the CommandGroups in your application.

To add a CommandGroup to an existing SOLIDWORKS menu, specify the name of a parent menu in Title. For example, to add a CommandGroup to the Help menu, specify:  
  
Visual Basic:                    "&Help/MyApp Help"     
Visual C++ or C#:         "&Help\\MyApp Help"

**NOTE**: If you do not specify the name of a parent menu in Title, then the menu item appears on the Tools menu below the **Xpress Products** menu item.

You can turn off all menus or all toolbars for a CommandGroup . See [ICommandGroup::HasMenu](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandGroup~HasMenu.md) and [ICommandGroup::HasToolbar](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandGroup~HasToolbar.md) for details.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ICommandManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandManager.md)  
[ICommandManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandManager_members.md)  
[ICommandManager::RemoveCommandGroup Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandManager~RemoveCommandGroup.md)  
[ICommandManager::GetCommandGroup Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandManager~GetCommandGroup.md)  
[ICommandManager::GetGroups Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandManager~GetGroups.md)  
[ICommandManager::IGetGroups Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandManager~IGetGroups.md)  
[ICommandManager::NumberOfGroups Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandManager~NumberOfGroups.md)
