# DMouseEvents_MouseRBtnDownNotifyEventHandler Delegate

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DMouseEvents_MouseRBtnDownNotifyEventHandler`

Fired when the right-mouse button is pressed down.
Fired when the right-mouse button is pressed down.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Public Delegate Function DMouseEvents_MouseRBtnDownNotifyEventHandler( _
   ByVal X As System.Integer, _
   ByVal Y As System.Integer, _
   ByVal WParam As System.Integer _
) As System.Integer
```

```

Dim instance As New DMouseEvents_MouseRBtnDownNotifyEventHandler(AddressOf HandlerMethod)
```

```

public delegate System.int DMouseEvents_MouseRBtnDownNotifyEventHandler( 
   System.int X,
   System.int Y,
   System.int WParam
)
```

```

public delegate System.int DMouseEvents_MouseRBtnDownNotifyEventHandler( 
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

If developing a C++ application, use [swMouseRBtnDownNotify](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swMouseNotify_e.html) to register for this notification.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[DMouseEvents\_MouseRBtnDownNotifyEventHandler Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DMouseEvents_MouseRBtnDownNotifyEventHandler.md)  
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.md)
