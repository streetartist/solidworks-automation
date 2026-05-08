# FrameState Property (IModelView)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~FrameState`

Gets or sets the window state (minimum, maximum, or normal) for the frame of the document window that contains the model view in the SOLIDWORKS client area.
Gets or sets the window state (minimum, maximum, or normal) for the frame of the document window that contains the model view in the SOLIDWORKS client area.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property FrameState As System.Integer
```

```

Dim instance As IModelView
Dim value As System.Integer
 
instance.FrameState = value
 
value = instance.FrameState
```

```

System.int FrameState {get; set;}
```

```

property System.int FrameState {
   System.int get();
   void set (    System.int value);
}
```

#### Property Value

Window state as defined in [swWindowState\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swWindowState_e.html)

Example

[Position Document Window (VBA)](Position_a_Document_Window_Example_VB.htm)  
[Create Hidden Undo Object (VBA)](Create_Multiple_Undo_Command_Example_VB.htm)  
[Create Hidden Undo Object (VB.NET)](Create_Multiple_Undo_Command_Example_VBNET.htm)  
[Create Hidden Undo Object (C#)](Create_Multiple_Undo_Command_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView.md)  
[IModelView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView_members.md)  
[IModelView::FrameHeight Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~FrameHeight.md)  
[IModelView::FrameLeft Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~FrameLeft.md)  
[IModelView::FrameTop Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~FrameTop.md)  
[IModelView::FrameWidth Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~FrameWidth.md)
