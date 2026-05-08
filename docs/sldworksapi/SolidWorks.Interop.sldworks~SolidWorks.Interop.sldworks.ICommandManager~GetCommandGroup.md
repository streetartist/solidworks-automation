# GetCommandGroup Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandManager~GetCommandGroup`

Gets the CommandGroup using the specified ID.
Gets the CommandGroup using the specified ID.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetCommandGroup( _
   ByVal UserID As System.Integer _
) As CommandGroup
```

```

Dim instance As ICommandManager
Dim UserID As System.Integer
Dim value As CommandGroup
 
value = instance.GetCommandGroup(UserID)
```

```

CommandGroup GetCommandGroup( 
   System.int UserID
)
```

```

CommandGroup^ GetCommandGroup( 
   System.int UserID
) 
```

#### Parameters

*UserID*
:   User-defined ID for this CommandGroup

#### Return Value

Pointer to [ICommandGroup](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandGroup.md) object

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ICommandManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandManager.md)  
[ICommandManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandManager_members.md)  
[ICommandManager::GetGroups Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandManager~GetGroups.md)  
[ICommandManager::IGetGroups Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandManager~IGetGroups.md)  
[ICommandManager::RemoveCommandGroup Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandManager~RemoveCommandGroup.md)  
[ICommandManager::NumberOfGroups Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandManager~NumberOfGroups.md)
