# RemoveCommandGroup Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandManager~RemoveCommandGroup`

Obsolete. Superseded by ICommandManager::RemoveCommandGroup2.
Obsolete. Superseded by [ICommandManager::RemoveCommandGroup2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandManager~RemoveCommandGroup2.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function RemoveCommandGroup( _
   ByVal UserID As System.Integer _
) As System.Boolean
```

```

Dim instance As ICommandManager
Dim UserID As System.Integer
Dim value As System.Boolean
 
value = instance.RemoveCommandGroup(UserID)
```

```

System.bool RemoveCommandGroup( 
   System.int UserID
)
```

```

System.bool RemoveCommandGroup( 
   System.int UserID
) 
```

#### Parameters

*UserID*
:   User-defined ID for this CommandGroup

#### Return Value

True if the CommandGroup is removed, false if not

Remarks

This method removes CommandGroups created using [ICommandManager::AddContextMenu](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandManager~AddContextMenu.md) and [ICommandManager::CreateCommandGroup](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandManager~CreateCommandGroup.md).

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ICommandManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandManager.md)  
[ICommandManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandManager_members.md)  
[ICommandManager::GetCommandGroup Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandManager~GetCommandGroup.md)  
[ICommandManager::GetGroups Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandManager~GetGroups.md)  
[ICommandManager::IGetGroups Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandManager~IGetGroups.md)  
[ICommandManager::NumberOfGroups Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandManager~NumberOfGroups.md)
