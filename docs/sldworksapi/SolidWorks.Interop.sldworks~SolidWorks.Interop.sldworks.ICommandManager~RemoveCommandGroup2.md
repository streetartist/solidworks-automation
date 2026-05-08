# RemoveCommandGroup2 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandManager~RemoveCommandGroup2`

Removes the specified CommandGroup from the CommandManager.
Removes the specified CommandGroup from the CommandManager.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function RemoveCommandGroup2( _
   ByVal UserID As System.Integer, _
   ByVal RuntimeOnly As System.Boolean _
) As System.Integer
```

```

Dim instance As ICommandManager
Dim UserID As System.Integer
Dim RuntimeOnly As System.Boolean
Dim value As System.Integer
 
value = instance.RemoveCommandGroup2(UserID, RuntimeOnly)
```

```

System.int RemoveCommandGroup2( 
   System.int UserID,
   System.bool RuntimeOnly
)
```

```

System.int RemoveCommandGroup2( 
   System.int UserID,
   System.bool RuntimeOnly
) 
```

#### Parameters

*UserID*
:   User-defined ID of the CommandGroup to remove

*RuntimeOnly*
:   True to remove the CommandGroup , saving its toolbar information in the registry; false to remove both the CommandGroup and its toolbar information in the registry

#### Return Value

Error code as defined in [swRemoveCommandGroupErrors](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swRemoveCommandGroupErrors.html)

Remarks

This method removes CommandGroups created using [ICommandManager::AddContextMenu](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandManager~AddContextMenu.md) and [ICommandManager::CreateCommandGroup2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandManager~CreateCommandGroup2.md).

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ICommandManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandManager.md)  
[ICommandManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandManager_members.md)
