# AddCustomButton2 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITaskpaneView~AddCustomButton2`

Adds a custom button to the Task Pane.
Adds a custom button to the Task Pane.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function AddCustomButton2( _
   ByVal ImageList As System.Object, _
   ByVal ToolTip As System.String _
) As System.Boolean
```

```

Dim instance As ITaskpaneView
Dim ImageList As System.Object
Dim ToolTip As System.String
Dim value As System.Boolean
 
value = instance.AddCustomButton2(ImageList, ToolTip)
```

```

System.bool AddCustomButton2( 
   System.object ImageList,
   System.string ToolTip
)
```

```

System.bool AddCustomButton2( 
   System.Object^ ImageList,
   System.String^ ToolTip
) 
```

#### Parameters

*ImageList*
:   :   Array of strings for the paths for the image files for the custom button (see **Remarks**)

*ToolTip*
:   ToolTip for the custom button

#### Return Value

True if the custom button is added to the Task Pane, false if not

Remarks

This method supports scaling for high resolution screens with high resolution operating system scaling options.

ImageList images can be:

- 20 x 20 pixels
- 32 x 32 pixels
- 40 x 40 pixels
- 64 x 64 pixels
- 96 x 96 pixels
- 128 x128 pixels

The images should use 256-color palette.

The size of the custom button displayed is dictated by both the monitor's or laptop's screen resolution and SOLIDWORKS icon size. You must set the custom button size before executing a macro or application that calls this method.

For example, if running Windows 7:

1. To set your monitor's or laptop's screen resolution:
   1. Click **Start > Control Panel > Appearance and  Personalization > Display**.
   2. Select a different icon size.
   3. Click **Apply**.
   4. Click **Log off now**.
2. Log back in.
3. Start SOLIDWORKS and open a part, assembly, or drawing.
4. Click **Tools > Customize** and on the Toolbars tab, click the **Icon size** that matches the size that you set in step 1b and click **OK** two twice.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ITaskpaneView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITaskpaneView.md)  
[ITaskpaneView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITaskpaneView_members.md)  
[ITaskpaneView::AddStandardButton Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITaskpaneView~AddStandardButton.md)  
[ITaskpaneView::GetButtonState Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITaskpaneView~GetButtonState.md)  
[ITaskpaneView::SetButtonState Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITaskpaneView~SetButtonState.md)  
[DTaskpaneViewEvents\_TaskPaneToolbarButtonClickedEventHandler Delegate](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DTaskpaneViewEvents_TaskPaneToolbarButtonClickedEventHandler.md)  
[ISldWorks::GetImageSize Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetImageSize.md)
