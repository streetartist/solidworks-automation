# ICommandTab Interface

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandTab`

Allows add-in applications to create tabs and add them to the CommandManager. The add-in application must create and clean up its own tabs.
Allows add-in applications to create tabs and add them to the [CommandManager](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandManager.md). The add-in application must create and clean up its own tabs.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Public Interface ICommandTab 
```

```

Dim instance As ICommandTab
```

```

public interface ICommandTab 
```

```

public interface class ICommandTab 
```

Remarks

Your add-in must check to see if the tab already exists. If the tab already exists, then you should use that tab instead of creating a new tab. If your add-in does not check for an existing tab, then SOLIDWORKS will create a new tab each time it starts up.

Users can add buttons to and remove buttons from your CommandManager tab. However, if your add-in removes the CommandManager tab upon exiting SOLIDWORKS, then any customizations made by users will be lost.

Example

[Create CommandManager Tab and Tab Boxes (VB.NET)](Create_CommandManager_Tab_and_Tab_Boxes_Example_VB.NET.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ICommandTab Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandTab_members.md)  
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.md)  
[ICommandTabBox Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandTabBox.md)
