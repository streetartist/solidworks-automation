# DTaskpaneViewEvents_TaskPaneToolbarButtonClickedEventHandler Delegate

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DTaskpaneViewEvents_TaskPaneToolbarButtonClickedEventHandler`

Fired when a toolbar button on the Task Pane is clicked.
Fired when a toolbar button on the Task Pane is clicked.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Public Delegate Function DTaskpaneViewEvents_TaskPaneToolbarButtonClickedEventHandler( _
   ByVal ButtonIndex As System.Integer _
) As System.Integer
```

```

Dim instance As New DTaskpaneViewEvents_TaskPaneToolbarButtonClickedEventHandler(AddressOf HandlerMethod)
```

```

public delegate System.int DTaskpaneViewEvents_TaskPaneToolbarButtonClickedEventHandler( 
   System.int ButtonIndex
)
```

```

public delegate System.int DTaskpaneViewEvents_TaskPaneToolbarButtonClickedEventHandler( 
   System.int ButtonIndex
)
```

#### Parameters

*ButtonIndex*
:   Index of the toolbar button on the Task Pane that was clicked

Remarks

If developing a C++ application, use [swAppTaskPaneToolbarButtonClicked](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swTaskPaneNotify_e.html) to register for this notification.

Example

[Add Buttons to Task Pane (VBA)](Add_Buttons_to_Task_Pane_Example_VB.htm)  
[Add Buttons to Task Pane (VB.NET)](Add_Buttons_to_Task_Pane_Example_VBNET.htm)  
[Add Buttons to Task Pane (C#)](Add_Buttons_to_Task_Pane_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[DTaskpaneViewEvents\_TaskPaneToolbarButtonClickedEventHandler Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DTaskpaneViewEvents_TaskPaneToolbarButtonClickedEventHandler.md)  
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.md)  
[ITaskpaneView::AddCustomButton Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITaskpaneView~AddCustomButton.md)  
[ITaskpaneView::AddStandardButton Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITaskpaneView~AddStandardButton.md)
