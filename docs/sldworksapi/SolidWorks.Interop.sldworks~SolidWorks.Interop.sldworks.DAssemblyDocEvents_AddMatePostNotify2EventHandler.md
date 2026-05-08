# DAssemblyDocEvents_AddMatePostNotify2EventHandler Delegate

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DAssemblyDocEvents_AddMatePostNotify2EventHandler`

Fired after one or more mates are created in an assembly.
Fired after one or more mates are created in an assembly.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Public Delegate Function DAssemblyDocEvents_AddMatePostNotify2EventHandler( _
   ByRef Mates As System.Object _
) As System.Integer
```

```

Dim instance As New DAssemblyDocEvents_AddMatePostNotify2EventHandler(AddressOf HandlerMethod)
```

```

public delegate System.int DAssemblyDocEvents_AddMatePostNotify2EventHandler( 
   ref System.object Mates
)
```

```

public delegate System.int DAssemblyDocEvents_AddMatePostNotify2EventHandler( 
   System.Object^% Mates
)
```

#### Parameters

*Mates*
:   Array of new [mates](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMate2.md)

Remarks

If developing a C++ application, use [swAssemblyAddMatePostNotify2](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swAssemblyNotify_e.html) to register for this notification.

Example

[Fire Notification After Adding a Mate (VBA)](Fire_Notification_After_Adding_a_Mate_Example_VB.htm)  
[Fire Notification After Adding a Mate (VB.NET)](Fire_Notification_After_Adding_a_Mate_Example_VBNET.htm)  
[Fire Notification After Adding a Mate (C#)](Fire_Notification_After_Adding_a_Mate_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[DAssemblyDocEvents\_AddMatePostNotify2EventHandler Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DAssemblyDocEvents_AddMatePostNotify2EventHandler.md)  
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.md)
