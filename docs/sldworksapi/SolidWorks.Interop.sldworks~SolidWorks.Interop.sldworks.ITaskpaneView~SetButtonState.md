# SetButtonState Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITaskpaneView~SetButtonState`

Sets whether the Task Pane button is enabled.
Sets whether the Task Pane button is enabled.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub SetButtonState( _
   ByVal ButtonIndex As System.Integer, _
   ByVal Enable As System.Boolean _
) 
```

```

Dim instance As ITaskpaneView
Dim ButtonIndex As System.Integer
Dim Enable As System.Boolean
 
instance.SetButtonState(ButtonIndex, Enable)
```

```

void SetButtonState( 
   System.int ButtonIndex,
   System.bool Enable
)
```

```

void SetButtonState( 
   System.int ButtonIndex,
   System.bool Enable
) 
```

#### Parameters

*ButtonIndex*
:   Index of Task Pane button

*Enable*
:   True to enable Task Pane button, false to disable it

Example

[Add Buttons to Task Pane (C#)](Add_Buttons_to_Task_Pane_Example_CSharp.htm)  
[Add Buttons to Task Pane (VB.NET)](Add_Buttons_to_Task_Pane_Example_VBNET.htm)  
[Add Buttons to Task Pane (VBA)](Add_Buttons_to_Task_Pane_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ITaskpaneView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITaskpaneView.md)  
[ITaskpaneView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITaskpaneView_members.md)  
[ITaskpaneView::GetButtonState Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITaskpaneView~GetButtonState.md)  
[ITaskpaneView::AddCustomButton Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITaskpaneView~AddCustomButton.md)  
[ITaskpaneView::AddStandardButton Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITaskpaneView~AddStandardButton.md)  
[DTaskpaneViewEvents\_TaskPaneToolbarButtonClickedEventHandler Delegate](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DTaskpaneViewEvents_TaskPaneToolbarButtonClickedEventHandler.md)
