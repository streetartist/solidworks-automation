# CreateTaskpaneView2 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~CreateTaskpaneView2`

Obsolete. Superseded by ISldworks::CreateTaskpaneView3.
Obsolete. Superseded by [ISldworks::CreateTaskpaneView3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~CreateTaskpaneView3.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function CreateTaskpaneView2( _
   ByVal Bitmap As System.String, _
   ByVal ToolTip As System.String _
) As TaskpaneView
```

```

Dim instance As ISldWorks
Dim Bitmap As System.String
Dim ToolTip As System.String
Dim value As TaskpaneView
 
value = instance.CreateTaskpaneView2(Bitmap, ToolTip)
```

```

TaskpaneView CreateTaskpaneView2( 
   System.string Bitmap,
   System.string ToolTip
)
```

```

TaskpaneView^ CreateTaskpaneView2( 
   System.String^ Bitmap,
   System.String^ ToolTip
) 
```

#### Parameters

*Bitmap*
:   Path and file name of the bitmap for the tab of this Task Pane view (see Remarks)

*ToolTip*
:   ToolTip for this Task Pane view

#### Return Value

[Task Pane view](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITaskpaneView.md)

Remarks

The bitmap should be 16 colors and 16 x 18 (width x height) pixels. Any portions of the bitmap that are white (RGB 255,255,255) will be transparent.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.md)  
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.md)  
[ISldWorks::ActivateTaskPane Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~ActivateTaskPane.md)  
[ISldWorks::RefreshTaskpaneContent Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~RefreshTaskpaneContent.md)  
[ISldWorks::TaskPaneIsPinned Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~TaskPaneIsPinned.md)
