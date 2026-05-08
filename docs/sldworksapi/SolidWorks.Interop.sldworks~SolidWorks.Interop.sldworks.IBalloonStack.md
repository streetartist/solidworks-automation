# IBalloonStack Interface

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBalloonStack`

Allows access to the properties that apply to a balloon stack, such as the direction of the stack.
Allows access to the properties that apply to a balloon stack, such as the direction of the stack.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Public Interface IBalloonStack 
```

```

Dim instance As IBalloonStack
```

```

public interface IBalloonStack 
```

```

public interface class IBalloonStack 
```

Remarks

Each of the notes in a balloon stack are individual notes. You must use the [INote](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote.md) interface to get and set properties of individual notes, such as the text itself.

Example

[Add Balloon to Stacked Balloon (C#)](Add_Balloon_to_Stacked_Balloon_Example_CSharp.htm)  
[Add Balloon to Stacked Balloon (VB.NET)](Add_Balloon_to_Stacked_Balloon_Example_VBNET.htm)  
[Add Balloon to Stacked Balloon (VBA)](Add_Balloon_to_Stacked_Balloon_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IBalloonStack Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBalloonStack_members.md)  
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.md)  
[IModelDocExtension::InsertStackedBalloon Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~InsertStackedBalloon.md)
