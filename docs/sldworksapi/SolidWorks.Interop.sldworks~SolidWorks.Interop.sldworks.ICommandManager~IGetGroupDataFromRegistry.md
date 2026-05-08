# IGetGroupDataFromRegistry Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandManager~IGetGroupDataFromRegistry`

Gets the command IDs of the given command group from the registry.
Gets the command IDs of the given command group from the registry.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IGetGroupDataFromRegistry( _
   ByVal UserGroupId As System.Integer, _
   ByVal Count As System.Integer, _
   ByRef UserIDs As System.Integer _
) As System.Boolean
```

```

Dim instance As ICommandManager
Dim UserGroupId As System.Integer
Dim Count As System.Integer
Dim UserIDs As System.Integer
Dim value As System.Boolean
 
value = instance.IGetGroupDataFromRegistry(UserGroupId, Count, UserIDs)
```

```

System.bool IGetGroupDataFromRegistry( 
   System.int UserGroupId,
   System.int Count,
   out System.int UserIDs
)
```

```

System.bool IGetGroupDataFromRegistry( 
   System.int UserGroupId,
   System.int Count,
   [Out] System.int UserIDs
) 
```

#### Parameters

*UserGroupId*
:   User-defined ID of a command group

*Count*
:   Number of command IDs in the given command group

*UserIDs*
:   - in-process, unmanaged C++: Pointer to an array of integer IDs

    - VBA, VB.NET, C#, and C++/CLI: Not supported

    See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

#### Return Value

True if successful, false if not

Remarks

Before calling this method call [ICommandManager::GetCommandIDsCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandManager~GetCommandIDsCount.md) to populate Count.

Use this method to compare command group IDs obtained through the user interface with those stored in the registry.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ICommandManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandManager.md)  
[ICommandManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandManager_members.md)  
[ICommandManager::GetGroupDataFromRegistry Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandManager~GetGroupDataFromRegistry.md)
