# SuppressWaitCursorDuringRedraw Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~SuppressWaitCursorDuringRedraw`

Gets or sets the state of the wait cursor (also called the hourglass) while this model view is being redrawn.
Gets or sets the state of the wait cursor (also called the hourglass) while this model view is being redrawn.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property SuppressWaitCursorDuringRedraw As System.Boolean
```

```

Dim instance As IModelView
Dim value As System.Boolean
 
instance.SuppressWaitCursorDuringRedraw = value
 
value = instance.SuppressWaitCursorDuringRedraw
```

```

System.bool SuppressWaitCursorDuringRedraw {get; set;}
```

```

property System.bool SuppressWaitCursorDuringRedraw {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True to enable the wait cursor, false to disable it

Remarks

When a model view is being redrawn, the wait cursor is normally displayed. This property allows you to suppress the wait cursor.

An add-in might find this property useful in situations where it is running a series of APIs, and one or more of those APIs cause the model view to redraw. By default, redrawing the model causes the wait cursor to flash on and off, which the end user may find disconcerting. By setting this property to false, the flashing wait cursor is suppressed. [IModelDoc::GraphicsRedraw2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~GraphicsRedraw2.md) is the most common API that causes a model view to redraw.

If your program disables this property, then it should re-enable it when the operation for which it was disabled completes. Otherwise, SOLIDWORKS will continue to not display the wait cursor. In other words, the expected use of this property is that you should disable it for a specific operation (or set of operations) in your code, and then immediately restore its previous behavior when that operation is completed.

Use of this property does not affect SOLIDWORKS performance.

Example

[Disable Wait Cursor When Model View Redrawn (VBA)](Disable_Wait_Cursor_While_Model_View_Redrawn_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView.md)  
[IModelView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView_members.md)  
[IModelView::GraphicsRedraw Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~GraphicsRedraw.md)  
[IModelView::IGraphicsRedraw Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~IGraphicsRedraw.md)
