# CreateTaskpaneView3 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~CreateTaskpaneView3`

Creates an application-level Task Pane view.
Creates an application-level Task Pane view.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function CreateTaskpaneView3( _
   ByVal ImageList As System.Object, _
   ByVal ToolTip As System.String _
) As TaskpaneView
```

```

Dim instance As ISldWorks
Dim ImageList As System.Object
Dim ToolTip As System.String
Dim value As TaskpaneView
 
value = instance.CreateTaskpaneView3(ImageList, ToolTip)
```

```

TaskpaneView CreateTaskpaneView3( 
   System.object ImageList,
   System.string ToolTip
)
```

```

TaskpaneView^ CreateTaskpaneView3( 
   System.Object^ ImageList,
   System.String^ ToolTip
) 
```

#### Parameters

*ImageList*
:   Array of strings of paths to six image files for the tab of this Task Pane view (see **Remarks**)

*ToolTip*
:   Tool tip for this Task Pane view

#### Return Value

[Task Pane view](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITaskpaneView.md)

Remarks

This method supports high resolution screens with high resolution operating system scaling options.

ImageList contains paths to PNG or BMP images in six pixel sizes:

- 20 X 20
- 32 X 32
- 40 X 40
- 64 X 64
- 96 X 96
- 128 X 128

The SOLIDWORKS user interface displays icons in three sizes: small, medium and large. After using this method to specify an image in six sizes, SOLIDWORKS selects the appropriate images to display as required by the current screen resolution or operating system scale.

| If OS scale is... | Then SOLIDWORKS icon... | Uses image pixel size... |
| --- | --- | --- |
| 100% | Small | 20X20 |
|  | Medium | 32X32 |
|  | Large | 40X40 |
| 150% | Small | 32X32 |
|  | Medium | 40X40 |
|  | Large | 64X64 |
| 200% | Small | 40X40 |
|  | Medium | 64X64 |
|  | Large | 96X96 |
| 250% | Small | 64X64 |
|  | Medium | 96X96 |
|  | Large | 128X128 |

The images should use a 256-color palette and gray (192, 192, 192) for transparent areas.

Example

[Add Task Pane View (VBA)](Add_Task_Pane_View_Example_VB.htm)  
[Add Task Pane View (VB.NET)](Add_Task_Pane_View_Example_VBNET.htm)  
[Add Task Pane View (C#)](Add_Task_Pane_View_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.md)  
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.md)  
[ISldWorks::ActivateTaskPane Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~ActivateTaskPane.md)  
[ISldWorks::RefreshTaskpaneContent Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~RefreshTaskpaneContent.md)  
[ISldWorks::TaskPaneIsPinned Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~TaskPaneIsPinned.md)  
[ISldWorks::GetImageSize Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetImageSize.md)
