# DSldWorksEvents_CommandOpenPreNotifyEventHandler Delegate

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DSldWorksEvents_CommandOpenPreNotifyEventHandler`

Fired before a command, including a PropertyManager page, executes or opens.
Fired before a command, including a PropertyManager page, executes or opens.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Public Delegate Function DSldWorksEvents_CommandOpenPreNotifyEventHandler( _
   ByVal Command As System.Integer, _
   ByVal UserCommand As System.Integer _
) As System.Integer
```

```

Dim instance As New DSldWorksEvents_CommandOpenPreNotifyEventHandler(AddressOf HandlerMethod)
```

```

public delegate System.int DSldWorksEvents_CommandOpenPreNotifyEventHandler( 
   System.int Command,
   System.int UserCommand
)
```

```

public delegate System.int DSldWorksEvents_CommandOpenPreNotifyEventHandler( 
   System.int Command,
   System.int UserCommand
)
```

#### Parameters

*Command*
:   SOLIDWORKS command ID as defined in [swCommands\_e](SolidWorks.Interop.swcommands~SolidWorks.Interop.swcommands.swCommands_e.md)

*UserCommand*
:   Third-party application's command item's ID (see **Remarks**)

#### Return Value

0 to execute the command or open a PropertyManager page, 1 to not

Remarks

If developing a C++ application, use [swAppCommandOpenPreNotify](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swAppNotify_e.html) to register for this notification.

The UserCommand argument is the ID assigned to your application's command item when it was added to a CommandGroup. For example:

```

cmdIndex0 = cmdGroup.AddCommandItem("CreateCube", -1, "Create a cube", "Create cube", 0, "CreateCube", "", 0);
```

```

cmdIds[0] = cmdGroup.get_CommandID(cmdIndex0);
```

Selecting the **Create cube** command in the user interface causes the CommandOpenPreNotify event to fire. The Command parameter is swCommands\_e.swCommands\_User\_Toolbar\_Min, and the userCommand parameter is cmdIDs[0].

Call [CommandCloseNotify](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DSldWorksEvents_CommandCloseNotifyEventHandler.md) to fire an event when the PropertyManager page is okay'd or canceled.

Example

[Fire Events When PropertyManager Page Opened and Canceled (VBA)](Fire_Events_When_PropertyManager_Page_Opened_and_Canceled_Example_VB.htm)  
[Fire Events When PropertyManager Page Opened and Canceled (VB.NET)](Fire_Events_When_PropertyManager_Page_Opened_and_Canceled_Example_VBNET.htm)  
[Fire Events When PropertyManager Page Opened and Canceled (C#)](Fire_Events_When_PropertyManager_Page_Opened_and_Canceled_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[DSldWorksEvents\_CommandOpenPreNotifyEventHandler Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DSldWorksEvents_CommandOpenPreNotifyEventHandler.md)  
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.md)  
[DSldWorksEvents\_CommandCloseNotifyEventHandler Delegate](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DSldWorksEvents_CommandCloseNotifyEventHandler.md)  
[ISldWorks::GetRunningCommandInfo Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetRunningCommandInfo.md)  
[ISldWorks::RunCommand Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~RunCommand.md)
