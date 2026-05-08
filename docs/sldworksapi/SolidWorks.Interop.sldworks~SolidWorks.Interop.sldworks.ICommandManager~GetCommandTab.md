# GetCommandTab Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandManager~GetCommandTab`

Gets the specified CommandManager tab for the specified document type.
Gets the specified CommandManager tab for the specified document type.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetCommandTab( _
   ByVal DocumentType As System.Integer, _
   ByVal TabName As System.String _
) As CommandTab
```

```

Dim instance As ICommandManager
Dim DocumentType As System.Integer
Dim TabName As System.String
Dim value As CommandTab
 
value = instance.GetCommandTab(DocumentType, TabName)
```

```

CommandTab GetCommandTab( 
   System.int DocumentType,
   System.string TabName
)
```

```

CommandTab^ GetCommandTab( 
   System.int DocumentType,
   System.String^ TabName
) 
```

#### Parameters

*DocumentType*
:   Document type as defined in [swDocumentTypes\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swDocumentTypes_e.html)

*TabName*
:   Name of CommandManager tab

#### Return Value

[CommandManager tab](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandTab.md)

Remarks

The names of CommandManager tabs are not unique. If multiple CommandManager tabs exists with the same name for the specified document type, then the first matching tab is returned. If no tabs match the specified name for the specified document type, then NULL is returned.

Example

[Create CommandManager Tab and Tab Boxes (VB.NET)](Create_CommandManager_Tab_and_Tab_Boxes_Example_VB.NET.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ICommandManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandManager.md)  
[ICommandManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandManager_members.md)  
[ICommandManager::AddCommandTab Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandManager~AddCommandTab.md)  
[ICommandManager::CommandTabs Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandManager~CommandTabs.md)  
[ICommandManager::GetCommandTabCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandManager~GetCommandTabCount.md)  
[ICommandManager::IGetCommandTabs Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandManager~IGetCommandTabs.md)  
[ICommandManager::RemoveCommandTab Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandManager~RemoveCommandTab.md)
