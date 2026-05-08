# DMouseEvents_MouseNotifyEventHandler Delegate

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DMouseEvents_MouseNotifyEventHandler`

Fired whenever a mouse event occurs.
Fired whenever a mouse event occurs.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Public Delegate Function DMouseEvents_MouseNotifyEventHandler( _
   ByVal Message As System.Integer, _
   ByVal WParam As System.Integer, _
   ByVal LParam As System.Integer _
) As System.Integer
```

```

Dim instance As New DMouseEvents_MouseNotifyEventHandler(AddressOf HandlerMethod)
```

```

public delegate System.int DMouseEvents_MouseNotifyEventHandler( 
   System.int Message,
   System.int WParam,
   System.int LParam
)
```

```

public delegate System.int DMouseEvents_MouseNotifyEventHandler( 
   System.int Message,
   System.int WParam,
   System.int LParam
)
```

#### Parameters

*Message*
:   Message to be sent

*WParam*
:   Additional message\_dependent information

*LParam*
:   X, Y in a packed long requiring unpacking; see GET\_X\_LPARAM and GET\_Y\_LPARAM in MSDN for details on how to unpack LParam

Remarks

If developing a C++ application, use [swMouseNotify](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swMouseNotify_e.html) to register for this notification.

Example

The following sample code shows a possible approach to decoding WParam and LParam.

'--------------------------------------------------------------

void NotifyHandler( UINT message, WPARAM wParam, LPARAM lParam)

{

long x = GET\_X\_LPARAM(lParam);//Uses Windows macro

long y = GET\_Y\_LPARAM(lParam);//Uses Windows macro

switch(message)

{

case WM\_MOUSEWHEEL:

case WM\_MOUSEMOVE:

//Your code to process event

break;

case WM\_LBUTTONDOWN:

//Your code to process event

break;

case WM\_LBUTTONUP:

//Your code to process event

break;

case WM\_RBUTTONDOWN:

//Your code to process event

break;

case WM\_RBUTTONUP:

//Your code to process event

break;

case WM\_MBUTTONDOWN:

//Your code to process event

break;

case WM\_MBUTTONUP:

//Your code to process event

break;

case WM\_LBUTTONDBLCLK:

//Your code to process event

break;

case WM\_RBUTTONDBLCLK:

//Your code to process event

break;

case WM\_MBUTTONDBLCLK:

//Your code to process event

break;

}

}

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[DMouseEvents\_MouseNotifyEventHandler Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DMouseEvents_MouseNotifyEventHandler.md)  
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.md)
