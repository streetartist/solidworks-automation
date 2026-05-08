# ShowModelWindow Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFrame~ShowModelWindow`

Shows a client model window.
Shows a client model window.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub ShowModelWindow( _
   ByVal LpModelWindow As ModelWindow _
) 
```

```

Dim instance As IFrame
Dim LpModelWindow As ModelWindow
 
instance.ShowModelWindow(LpModelWindow)
```

```

void ShowModelWindow( 
   ModelWindow LpModelWindow
)
```

```

void ShowModelWindow( 
   ModelWindow^ LpModelWindow
) 
```

#### Parameters

*LpModelWindow*
:   [Model window](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelWindow.md)

Example

[Switch Documents (C#)](Switch_Documents_Example_CSharp.htm)  
[Switch Documents (VB.NET)](Switch_Documents_Example_VBNET.htm)  
[Switch Documents (VBA)](Switch_Documents_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IFrame Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFrame.md)  
[IFrame Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFrame_members.md)  
[IFrame::GetHWnd Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFrame~GetHWnd.md)  
[IFrame::GetHWndx64 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFrame~GetHWndx64.md)  
[IFrame::GetModelWindowCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFrame~GetModelWindowCount.md)  
[IFrame::IGetModelWindows Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFrame~IGetModelWindows.md)  
[IFrame::ModelWindows Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFrame~ModelWindows.md)
