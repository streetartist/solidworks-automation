# CreateFlyoutGroup Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandManager~CreateFlyoutGroup`

Obsolete. Superseded by ICommandManager::CreateFlyoutGroup2.
Obsolete. Superseded by [ICommandManager::CreateFlyoutGroup2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandManager~CreateFlyoutGroup2.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function CreateFlyoutGroup( _
   ByVal UserID As System.Integer, _
   ByVal Title As System.String, _
   ByVal ToolTip As System.String, _
   ByVal Hint As System.String, _
   ByVal SmallIcon As System.String, _
   ByVal LargeIcon As System.String, _
   ByVal SmallImageList As System.String, _
   ByVal LargeImageList As System.String, _
   ByVal CallbackFunction As System.String, _
   ByVal UpdateCallbackFunction As System.String _
) As FlyoutGroup
```

```

Dim instance As ICommandManager
Dim UserID As System.Integer
Dim Title As System.String
Dim ToolTip As System.String
Dim Hint As System.String
Dim SmallIcon As System.String
Dim LargeIcon As System.String
Dim SmallImageList As System.String
Dim LargeImageList As System.String
Dim CallbackFunction As System.String
Dim UpdateCallbackFunction As System.String
Dim value As FlyoutGroup
 
value = instance.CreateFlyoutGroup(UserID, Title, ToolTip, Hint, SmallIcon, LargeIcon, SmallImageList, LargeImageList, CallbackFunction, UpdateCallbackFunction)
```

```

FlyoutGroup CreateFlyoutGroup( 
   System.int UserID,
   System.string Title,
   System.string ToolTip,
   System.string Hint,
   System.string SmallIcon,
   System.string LargeIcon,
   System.string SmallImageList,
   System.string LargeImageList,
   System.string CallbackFunction,
   System.string UpdateCallbackFunction
)
```

```

FlyoutGroup^ CreateFlyoutGroup( 
   System.int UserID,
   System.String^ Title,
   System.String^ ToolTip,
   System.String^ Hint,
   System.String^ SmallIcon,
   System.String^ LargeIcon,
   System.String^ SmallImageList,
   System.String^ LargeImageList,
   System.String^ CallbackFunction,
   System.String^ UpdateCallbackFunction
) 
```

#### Parameters

*UserID*
:   Unique, user-defined ID for the new flyout

*Title*
:   Name of the flyout to create

*ToolTip*
:   ToolTip for the new flyout

*Hint*
:   Text displayed in SOLIDWORKS status bar when a user's mouse pointer is over the flyout

*SmallIcon*
:   Path to the small bitmap or PNG used in the flyout

*LargeIcon*
:   Path to the large bitmap or PNG used in the flyout

*SmallImageList*
:   Path to the bitmap or PNG containing all of the small button and separator images for this flyout

*LargeImageList*
:   Path to the bitmap or PNG containing all of the large button and separator images for this flyout

*CallbackFunction*
:   Function to call when the flyout is selected

*UpdateCallbackFunction*
:   Optional update function that controls the state of the item; if specified, then SOLIDWORKS calls this function before displaying the item (see **Remarks**)

    |  |  |
    | --- | --- |
    | If this update function returns... | Then the SOLIDWORKS software... |
    | 0 | Disables the item |
    | 1 | Enables the item; this is the default state if no update function is specified |

#### Return Value

[IFlyoutGroup](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFlyoutGroup.md)

Remarks

After creating the flyout, display it on a CommandManager tab by calling [ICommandTabBox::AddCommands](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandTabBox~AddCommands.md). Call [IFlyoutGroup::AddContextMenuFlyout](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFlyoutGroup~AddContextMenuFlyout.md) to add it to context menus. Call [IFlyoutGroup::AddCommandItem](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFlyoutGroup~AddCommandItem.md) to add menu items to the flyout group.

If any flyout menu items are enabled, then the flyout button cannot be disabled by the flyout group's UpdateCallbackFunction. The sensitivity of the top-level flyout button is always determined by its enabled menu items. Disabled flyout menu items do not appear in the flyout menu. If there are no flyout menu items, then control of the top-level flyout button is returned to the flyout group's UpdateCallbackFunction.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ICommandManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandManager.md)  
[ICommandManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandManager_members.md)  
[ICommandManager::GetFlyoutGroup Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandManager~GetFlyoutGroup.md)  
[ICommandManager::GetFlyoutGroups Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandManager~GetFlyoutGroups.md)  
[ICommandManager::RemoveFlyoutGroup Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandManager~RemoveFlyoutGroup.md)  
[ICommandManager::NumberOfFlyoutGroups Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandManager~NumberOfFlyoutGroups.md)
