# CreateCommandGroup2 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandManager~CreateCommandGroup2`

Creates a new CommandGroup in the CommandManager.
Creates a new CommandGroup in the CommandManager.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function CreateCommandGroup2( _
   ByVal UserID As System.Integer, _
   ByVal Title As System.String, _
   ByVal ToolTip As System.String, _
   ByVal Hint As System.String, _
   ByVal Position As System.Integer, _
   ByVal IgnorePreviousVersion As System.Boolean, _
   ByRef Errors As System.Integer _
) As CommandGroup
```

```

Dim instance As ICommandManager
Dim UserID As System.Integer
Dim Title As System.String
Dim ToolTip As System.String
Dim Hint As System.String
Dim Position As System.Integer
Dim IgnorePreviousVersion As System.Boolean
Dim Errors As System.Integer
Dim value As CommandGroup
 
value = instance.CreateCommandGroup2(UserID, Title, ToolTip, Hint, Position, IgnorePreviousVersion, Errors)
```

```

CommandGroup CreateCommandGroup2( 
   System.int UserID,
   System.string Title,
   System.string ToolTip,
   System.string Hint,
   System.int Position,
   System.bool IgnorePreviousVersion,
   out System.int Errors
)
```

```

CommandGroup^ CreateCommandGroup2( 
   System.int UserID,
   System.String^ Title,
   System.String^ ToolTip,
   System.String^ Hint,
   System.int Position,
   System.bool IgnorePreviousVersion,
   [Out] System.int Errors
) 
```

#### Parameters

*UserID*
:   Unique user-defined ID for the new CommandGroup

*Title*
:   Name of the CommandGroup to create (see **Remarks**)

*ToolTip*
:   Tool tip for the CommandGroup

*Hint*
:   Text displayed in SOLIDWORKS status bar when a user's mouse pointer is over the CommandGroup

*Position*
:   Position of the CommandGroup in the CommandManager for all document templates (see **Remarks**)

    NOTE: Specify 0 to add the CommandGroup to the beginning of the CommandMananger, or specify -1 to add it to the end of the CommandManager.

*IgnorePreviousVersion*
:   True to remove all previously saved customization and toolbar information before creating a new CommandGroup, false to not (see **Remarks**)

*Errors*
:   Error code as defined in [swCreateCommandGroupErrors](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swCreateCommandGroupErrors.html)

#### Return Value

[ICommandGroup](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandGroup.md)

Remarks

Call [ICommandManager::GetGroupDataFromRegistry](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandManager~GetGroupDataFromRegistry.md) or [ICommandManager::IGetGroupDataFromRegistry](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandManager~IGetGroupDataFromRegistry.md) before calling this method to determine how to set IgnorePreviousVersion. Set IgnorePreviousVersion to true to prevent SOLIDWORKS from saving the current toolbar setting to the registry, even if there is no previous version.

You can also use [ICommandGroup::MenuPosition](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandGroup~HasMenu.md) to control the position of the CommandGroup in specific document templates.

If you change the definition of an existing CommandGroup (i.e., add or remove toolbar buttons), you must assign a new unique user-defined UserID to that CommandGroup. You must perform this action to avoid conflicts with any previously existing CommandGroups and to allow for backward and forward compatibility of the CommandGroups in your application.

To add a menu item for a CommandGroup to an existing SOLIDWORKS menu, specify the name of a parent menu in Title. For example, to add a CommandGroup to the Help menu, specify:  
  
Visual Basic:                    "&Help/MyApp Help"      
Visual C++ or C#:           "&Help\\MyApp Help"

**NOTE**: If you do not specify the name of a parent menu in Title, then the menu item for the CommandGroup appears on the Tools menu below the **Xpress Products** menu item.

You can turn off all menus or all toolbars for a CommandGroup. See [ICommandGroup::HasMenu](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandGroup~HasMenu.md) and [ICommandGroup::HasToolbar](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandGroup~HasToolbar.md) for details.

Example

[Create Flyouts in the CommandManager (C#)](Create_Flyouts_in_the_CommandManager_Example_CSharp.htm)  
[Create Flyouts in the CommandManager (VB.NET)](Create_Flyouts_in_the_CommandManager_Example_VBNET.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ICommandManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandManager.md)  
[ICommandManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandManager_members.md)  
[ICommandManager::RemoveCommandGroup2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandManager~RemoveCommandGroup2.md)  
[ICommandManager::GetCommandGroup Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandManager~GetCommandGroup.md)  
[ICommandManager::GetGroups Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandManager~GetGroups.md)  
[ICommandManager::IGetGroups Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandManager~IGetGroups.md)  
[ICommandManager::NumberOfGroups Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandManager~NumberOfGroups.md)
