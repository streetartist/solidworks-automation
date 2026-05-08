# GetGroupDataFromRegistry Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandManager~GetGroupDataFromRegistry`

Gets the command IDs of the given command group from the registry.
Gets the command IDs of the given command group from the registry.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetGroupDataFromRegistry( _
   ByVal UserGroupId As System.Integer, _
   ByRef UserIDs As System.Object _
) As System.Boolean
```

```

Dim instance As ICommandManager
Dim UserGroupId As System.Integer
Dim UserIDs As System.Object
Dim value As System.Boolean
 
value = instance.GetGroupDataFromRegistry(UserGroupId, UserIDs)
```

```

System.bool GetGroupDataFromRegistry( 
   System.int UserGroupId,
   out System.object UserIDs
)
```

```

System.bool GetGroupDataFromRegistry( 
   System.int UserGroupId,
   [Out] System.Object^ UserIDs
) 
```

#### Parameters

*UserGroupId*
:   User-defined ID of a command group

*UserIDs*
:   Array of command IDs for the given command group

#### Return Value

True if successful, false if not

Remarks

Call this API before calling [ICommandManager::CreateCommandGroup2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandManager~CreateCommandGroup2.md). The array of command IDs returned by this method helps you decide how to set the IgnorePreviousVersion parameter of ICommandManager::CreateCommandGroup2.

Example

[Create Flyouts in the CommandManager (VB.NET)](Create_Flyouts_in_the_CommandManager_Example_VBNET.htm)  
[Create Flyouts in the CommandManager (C#)](Create_Flyouts_in_the_CommandManager_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ICommandManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandManager.md)  
[ICommandManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandManager_members.md)  
[ICommandManger::IGetGroupDataFromRegistry](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandManager~IGetGroupDataFromRegistry.md)
