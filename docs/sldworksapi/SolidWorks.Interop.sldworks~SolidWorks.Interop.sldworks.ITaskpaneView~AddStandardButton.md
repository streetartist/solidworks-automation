# AddStandardButton Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITaskpaneView~AddStandardButton`

Adds a standard SOLIDWORKS button to the Task Pane.
Adds a standard SOLIDWORKS button to the Task Pane.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function AddStandardButton( _
   ByVal BitmapOption As System.Integer, _
   ByVal ToolTip As System.String _
) As System.Boolean
```

```

Dim instance As ITaskpaneView
Dim BitmapOption As System.Integer
Dim ToolTip As System.String
Dim value As System.Boolean
 
value = instance.AddStandardButton(BitmapOption, ToolTip)
```

```

System.bool AddStandardButton( 
   System.int BitmapOption,
   System.string ToolTip
)
```

```

System.bool AddStandardButton( 
   System.int BitmapOption,
   System.String^ ToolTip
) 
```

#### Parameters

*BitmapOption*
:   Type of standard SOLIDWORKS button as defined in [swTaskPaneBitmapsOptions\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swTaskPaneBitmapsOptions_e.html)

*ToolTip*
:   ToolTip for the standard SOLIDWORKS button

#### Return Value

True if a standard SOLIDWORKS button is added to the Task Pane, false if not

Example

[Add Buttons to Task Pane (VBA)](Add_Buttons_to_Task_Pane_Example_VB.htm)  
[Add Buttons to Task Pane (VB.NET)](Add_Buttons_to_Task_Pane_Example_VBNET.htm)  
[Add Buttons to Task Pane (C#)](Add_Buttons_to_Task_Pane_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ITaskpaneView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITaskpaneView.md)  
[ITaskpaneView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITaskpaneView_members.md)  
[ITaskpaneView::AddCustomButton Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITaskpaneView~AddCustomButton.md)  
[DTaskpaneViewEvents\_TaskPaneToolbarButtonClickedEventHandler Delegate](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DTaskpaneViewEvents_TaskPaneToolbarButtonClickedEventHandler.md)  
[ITaskpaneView::GetButtonState Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITaskpaneView~GetButtonState.md)  
[ITaskpaneView::SetButtonState Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITaskpaneView~SetButtonState.md)
