# IGetCommandTabs Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandManager~IGetCommandTabs`

Gets the CommandManager tabs for the specified document type.
Gets the CommandManager tabs for the specified document type.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IGetCommandTabs( _
   ByVal DocumentType As System.Integer, _
   ByVal CommandTabCount As System.Integer _
) As CommandTab
```

```

Dim instance As ICommandManager
Dim DocumentType As System.Integer
Dim CommandTabCount As System.Integer
Dim value As CommandTab
 
value = instance.IGetCommandTabs(DocumentType, CommandTabCount)
```

```

CommandTab IGetCommandTabs( 
   System.int DocumentType,
   System.int CommandTabCount
)
```

```

CommandTab^ IGetCommandTabs( 
   System.int DocumentType,
   System.int CommandTabCount
) 
```

#### Parameters

*DocumentType*
:   Document type as defined in [swDocumentTypes\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swDocumentTypes_e.html)

*CommandTabCount*
:   Number of CommandManager tabs for DocumentType

#### Return Value

- in-process, unmanaged C++: Pointer to an array of [CommandManager tabs](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandTab.md)

- VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

Remarks

Before calling this method, call [ICommandManager::GetCommandTabCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandManager~GetCommandTabCount.md) to get the size of the array for this method.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ICommandManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandManager.md)  
[ICommandManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandManager_members.md)  
[ICommandManager::AddCommandTab Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandManager~AddCommandTab.md)  
[ICommandManager::CommandTabs Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandManager~CommandTabs.md)  
[ICommandManager::GetCommandTab Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandManager~GetCommandTab.md)  
[ICommandManager::RemoveCommandTab Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandManager~RemoveCommandTab.md)
