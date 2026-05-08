# DMouseEvents_MouseLBtnUpNotifyEventHandler Delegate

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DMouseEvents_MouseLBtnUpNotifyEventHandler`

Fired when the left-mouse button is released after being pressed.
Fired when the left-mouse button is released after being pressed.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Public Delegate Function DMouseEvents_MouseLBtnUpNotifyEventHandler( _
   ByVal X As System.Integer, _
   ByVal Y As System.Integer, _
   ByVal WParam As System.Integer _
) As System.Integer
```

```

Dim instance As New DMouseEvents_MouseLBtnUpNotifyEventHandler(AddressOf HandlerMethod)
```

```

public delegate System.int DMouseEvents_MouseLBtnUpNotifyEventHandler( 
   System.int X,
   System.int Y,
   System.int WParam
)
```

```

public delegate System.int DMouseEvents_MouseLBtnUpNotifyEventHandler( 
   System.int X,
   System.int Y,
   System.int WParam
)
```

#### Parameters

*X*
:   x coordinate of the pointer in the window space

*Y*
:   y coordinate of the pointer in the window space

*WParam*
:   Data about the state of the keyboard at the time the event was sent; see MSDN for details on how to decode this data

Remarks

If developing a C++ application, use [swMouseLBtnUpNotify](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swMouseNotify_e.html) to register for this notification.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[DMouseEvents\_MouseLBtnUpNotifyEventHandler Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DMouseEvents_MouseLBtnUpNotifyEventHandler.md)  
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.md)
