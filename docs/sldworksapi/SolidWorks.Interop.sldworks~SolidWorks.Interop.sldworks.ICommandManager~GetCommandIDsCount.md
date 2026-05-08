# GetCommandIDsCount Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandManager~GetCommandIDsCount`

Gets the number of command IDs for the given command group.
Gets the number of command IDs for the given command group.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetCommandIDsCount( _
   ByVal UserGroupId As System.Integer _
) As System.Integer
```

```

Dim instance As ICommandManager
Dim UserGroupId As System.Integer
Dim value As System.Integer
 
value = instance.GetCommandIDsCount(UserGroupId)
```

```

System.int GetCommandIDsCount( 
   System.int UserGroupId
)
```

```

System.int GetCommandIDsCount( 
   System.int UserGroupId
) 
```

#### Parameters

*UserGroupId*
:   User-defined ID of a command group

#### Return Value

Number of command IDs in the given command group

Remarks

Call this method before calling [ICommandManager::IGetGroupDataFromRegistry](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandManager~IGetGroupDataFromRegistry.md) to determine the size of the array for that method.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ICommandManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandManager.md)  
[ICommandManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandManager_members.md)
