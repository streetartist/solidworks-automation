# GetLastToolbarID Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetLastToolbarID`

Gets the ID of the last toolbar added to the CommandManager.
Gets the ID of the last toolbar added to the [CommandManager](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandManager.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetLastToolbarID() As System.Integer
```

```

Dim instance As ISldWorks
Dim value As System.Integer
 
value = instance.GetLastToolbarID()
```

```

System.int GetLastToolbarID()
```

```

System.int GetLastToolbarID(); 
```

#### Return Value

ID of the last toolbar added to the CommandManager

Remarks

See [CommandManager and CommandGroups](sldworksAPIProgGuide.chm::/OVERVIEW/CommandManager_and_CommandGroups.htm) to learn how to create a CommandManager and add and remove CommandGroups.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.md)  
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.md)  
[ISldWorks::GetCommandID Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetCommandID.md)  
[ISldWorks::GetCommandManager Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetCommandManager.md)  
[ICommandGroup Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandGroup.md)
