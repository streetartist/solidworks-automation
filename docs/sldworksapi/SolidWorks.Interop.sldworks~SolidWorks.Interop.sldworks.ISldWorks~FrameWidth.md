# FrameWidth Property (ISldWorks)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~FrameWidth`

Gets or sets the width of the frame of the SOLIDWORKS window.
Gets or sets the width of the frame of the SOLIDWORKS window.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property FrameWidth As System.Integer
```

```

Dim instance As ISldWorks
Dim value As System.Integer
 
instance.FrameWidth = value
 
value = instance.FrameWidth
```

```

System.int FrameWidth {get; set;}
```

```

property System.int FrameWidth {
   System.int get();
   void set (    System.int value);
}
```

#### Property Value

Width of the SOLIDWORKS window in pixels

Remarks

This property is valid only if [ISldWorks::FrameState](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~FrameState.md) is [swWindowState\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swWindowState_e.html).swWindowNormal.

Example

**Visual Basic for Applications (VBA)**

Option Explicit

Dim swApp As SldWorks.SldWorks

Sub main()

Set swApp = Application.SldWorks  
' Set the SOLIDWORKS window the specified height, width, state, and location  
swApp.**FrameHeight** = 500  
swApp.**FrameLeft** = 100  
swApp.**FrameState** = swWindowNormal  
swApp.**FrameTop** = 100  
swApp.**FrameWidth** = 500

End Sub

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.md)  
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.md)  
[ISldWorks::FrameHeight Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~FrameHeight.md)  
[ISldWorks::FrameLeft Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~FrameLeft.md)  
[ISldWorks::FrameTop Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~FrameTop.md)  
[IModelView::FrameHeight Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~FrameHeight.md)  
[IModelView::FrameLeft Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~FrameLeft.md)  
[IModelView::FrameState Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~FrameState.md)  
[IModelView::FrameTop Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~FrameTop.md)  
[IModelView::FrameWidth Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~FrameWidth.md)
