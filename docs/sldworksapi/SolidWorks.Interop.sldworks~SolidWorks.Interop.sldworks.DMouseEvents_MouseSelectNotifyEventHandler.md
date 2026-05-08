# DMouseEvents_MouseSelectNotifyEventHandler Delegate

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DMouseEvents_MouseSelectNotifyEventHandler`

Fired when the user makes a selection in the model view using the mouse.
Fired when the user makes a selection in the model view using the mouse.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Public Delegate Function DMouseEvents_MouseSelectNotifyEventHandler( _
   ByVal Ix As System.Integer, _
   ByVal Iy As System.Integer, _
   ByVal X As System.Double, _
   ByVal Y As System.Double, _
   ByVal Z As System.Double _
) As System.Integer
```

```

Dim instance As New DMouseEvents_MouseSelectNotifyEventHandler(AddressOf HandlerMethod)
```

```

public delegate System.int DMouseEvents_MouseSelectNotifyEventHandler( 
   System.int Ix,
   System.int Iy,
   System.double X,
   System.double Y,
   System.double Z
)
```

```

public delegate System.int DMouseEvents_MouseSelectNotifyEventHandler( 
   System.int Ix,
   System.int Iy,
   System.double X,
   System.double Y,
   System.double Z
)
```

#### Parameters

*Ix*
:   x coordinate of the pointer in the window space

*Iy*
:   y coordinate of the pointer in the window space

*X*
:   x coordinate of the pointer in world space

*Y*
:   y coordinate of the pointer in world space

*Z*
:   z coordinate of the pointer in world space

Remarks

If developing a C++ application, use [swMouseSelectNotify](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swMouseNotify_e.html) to register for this notification.

Example

[Run SOLIDWORKS Commands and Synthesize Mouse Events (C#)](Run_SolidWorks_Commands_and_Synthesize_Mouse_Events_Example_CSharp.htm)  
[Run SOLIDWORKS Commands and Synthesize Mouse Events (VB.NET)](Run_SolidWorks_Commands_and_Synthesize_Mouse_Events_Example_VBNET.htm)  
[Run SOLIDWORKS Commands and Synthesize Mouse Events (VBA)](Run_SOLIDWORKS_Commands_and_Synthesize_Mouse_Events_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[DMouseEvents\_MouseSelectNotifyEventHandler Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DMouseEvents_MouseSelectNotifyEventHandler.md)  
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.md)
