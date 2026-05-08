# RemoveCommandTab Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandManager~RemoveCommandTab`

Removes the specified CommandManager tab, including its tab boxes and buttons, }}-->from the CommandManager.
Removes the specified CommandManager tab, including its tab boxes and buttons, from the CommandManager.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function RemoveCommandTab( _
   ByVal TabToRemove As CommandTab _
) As System.Boolean
```

```

Dim instance As ICommandManager
Dim TabToRemove As CommandTab
Dim value As System.Boolean
 
value = instance.RemoveCommandTab(TabToRemove)
```

```

System.bool RemoveCommandTab( 
   CommandTab TabToRemove
)
```

```

System.bool RemoveCommandTab( 
   CommandTab^ TabToRemove
) 
```

#### Parameters

*TabToRemove*
:   [CommandManager tab](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandTab.md), including its tab boxes and buttons, to remove

#### Return Value

True if the CommandManager tab is removed, false if not

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ICommandManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandManager.md)  
[ICommandManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandManager_members.md)  
[ICommandManager::AddCommandTab Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandManager~AddCommandTab.md)  
[ICommandManager::CommandTabs Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandManager~CommandTabs.md)  
[ICommandManager::GetCommandTab Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandManager~GetCommandTab.md)  
[ICommandManager::GetCommandTabCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandManager~GetCommandTabCount.md)  
[ICommandManager::IGetCommandTabs Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandManager~IGetCommandTabs.md)
