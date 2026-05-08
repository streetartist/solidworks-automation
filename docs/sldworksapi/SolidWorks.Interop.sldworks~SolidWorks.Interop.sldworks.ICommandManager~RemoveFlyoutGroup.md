# RemoveFlyoutGroup Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandManager~RemoveFlyoutGroup`

Removes the specified flyout from the CommandManager.
Removes the specified flyout from the CommandManager.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function RemoveFlyoutGroup( _
   ByVal UserID As System.Integer _
) As System.Boolean
```

```

Dim instance As ICommandManager
Dim UserID As System.Integer
Dim value As System.Boolean
 
value = instance.RemoveFlyoutGroup(UserID)
```

```

System.bool RemoveFlyoutGroup( 
   System.int UserID
)
```

```

System.bool RemoveFlyoutGroup( 
   System.int UserID
) 
```

#### Parameters

*UserID*
:   User-defined ID of the flyout to remove

#### Return Value

True if removal successful, false if not

Example

[Create Flyouts in the CommandManager (C#)](Create_Flyouts_in_the_CommandManager_Example_CSharp.htm)  
[Create Flyouts in the CommandManager (VB.NET)](Create_Flyouts_in_the_CommandManager_Example_VBNET.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ICommandManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandManager.md)  
[ICommandManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandManager_members.md)  
[ICommandManager::CreateFlyoutGroup Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandManager~CreateFlyoutGroup.md)  
[ICommandManager::GetFlyoutGroup Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandManager~GetFlyoutGroup.md)  
[ICommandManager::GetFlyoutGroups Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandManager~GetFlyoutGroups.md)  
[ICommandManager::NumberOfFlyoutGroups Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandManager~NumberOfFlyoutGroups.md)
