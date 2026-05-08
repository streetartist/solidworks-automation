# GetCommandTabs Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetCommandTabs`

Gets all of the SOLIDWORKS CommandManager tab names in this document.
Gets all of the SOLIDWORKS CommandManager tab names in this document.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetCommandTabs() As System.Object
```

```

Dim instance As IModelDocExtension
Dim value As System.Object
 
value = instance.GetCommandTabs()
```

```

System.object GetCommandTabs()
```

```

System.Object^ GetCommandTabs(); 
```

#### Return Value

Array of CommandManager tab names

Remarks

To activate and query the add-in CommandManager tabs, call [ICommandManager::CommandTabs](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandManager~CommandTabs.md).

Example

[Activate SOLIDWORKS CommandManager Tab (VBA)](Activate_SOLIDWORKS_CommandManager_Tab_Example_VB.htm)  
[Activate SOLIDWORKS CommandManager Tab (VB.NET)](Activate_SOLIDWORKS_CommandManager_Tab_Example_VBNET.htm)  
[Activate SOLIDWORKS CommandManager Tab (C#)](Activate_SOLIDWORKS_CommandManager_Tab_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.md)  
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.md)  
[ICommandManager::GetCommandTab Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandManager~GetCommandTab.md)  
[ICommandManager::IGetCommandTabs Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandManager~IGetCommandTabs.md)  
[ICommandManager::GetCommandTabCount Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandManager~GetCommandTabCount.md)  
[IModelDocExtension::ActiveCommandTab Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~ActiveCommandTab.md)  
[IModelDocExtension::ActiveCommandTabIndex Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~ActiveCommandTabIndex.md)  
[IModelDocExtension::CommandTabVisible Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~CommandTabVisible.md)
