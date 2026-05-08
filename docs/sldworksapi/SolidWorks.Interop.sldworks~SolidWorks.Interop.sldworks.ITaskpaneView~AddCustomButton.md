# AddCustomButton Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITaskpaneView~AddCustomButton`

Obsolete. Superseded by ITaskpaneView::AddCustomButton2.
Obsolete. Superseded by [ITaskpaneView::AddCustomButton2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITaskpaneView~AddCustomButton2.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function AddCustomButton( _
   ByVal BitmapPath As System.String, _
   ByVal ToolTip As System.String _
) As System.Boolean
```

```

Dim instance As ITaskpaneView
Dim BitmapPath As System.String
Dim ToolTip As System.String
Dim value As System.Boolean
 
value = instance.AddCustomButton(BitmapPath, ToolTip)
```

```

System.bool AddCustomButton( 
   System.string BitmapPath,
   System.string ToolTip
)
```

```

System.bool AddCustomButton( 
   System.String^ BitmapPath,
   System.String^ ToolTip
) 
```

#### Parameters

*BitmapPath*
:   Path and filename of the bitmap for the custom button

*ToolTip*
:   ToolTip for the custom button

#### Return Value

True if the custom button is added to the Task Pane, false if not

Remarks

Button images can be either BMP (bitmap) or PNG and should be 16 pixels wide x 16 pixels high. The bitmap image can be 8-, 16-, 24-, or 32-bit depth.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ITaskpaneView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITaskpaneView.md)  
[ITaskpaneView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITaskpaneView_members.md)  
[ITaskPaneView::AddStandardButton Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITaskpaneView~AddStandardButton.md)  
[DTaskpaneViewEvents\_TaskPaneToolbarButtonClickedEventHandler Delegate](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DTaskpaneViewEvents_TaskPaneToolbarButtonClickedEventHandler.md)  
[ITaskpaneView::GetButtonState Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITaskpaneView~GetButtonState.md)  
[ITaskpaneView::SetButtonState Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITaskpaneView~SetButtonState.md)
