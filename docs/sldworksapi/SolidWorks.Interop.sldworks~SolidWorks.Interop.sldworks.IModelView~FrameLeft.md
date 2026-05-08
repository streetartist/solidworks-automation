# FrameLeft Property (IModelView)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~FrameLeft`

Gets or sets the left position of the frame of the document window that contains the model view in the SOLIDWORKS client area.
Gets or sets the left position of the frame of the document window that contains the model view in the SOLIDWORKS client area.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property FrameLeft As System.Integer
```

```

Dim instance As IModelView
Dim value As System.Integer
 
instance.FrameLeft = value
 
value = instance.FrameLeft
```

```

System.int FrameLeft {get; set;}
```

```

property System.int FrameLeft {
   System.int get();
   void set (    System.int value);
}
```

#### Property Value

Left position of document window in client area in pixels

Example

[Position Document Window (VBA)](Position_a_Document_Window_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView.md)  
[IModelView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView_members.md)  
[IModelView::FrameHeight Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~FrameHeight.md)  
[IModelView::FrameState Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~FrameState.md)  
[IModelView::FrameTop Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~FrameTop.md)  
[IModelView::FrameWidth Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~FrameWidth.md)
