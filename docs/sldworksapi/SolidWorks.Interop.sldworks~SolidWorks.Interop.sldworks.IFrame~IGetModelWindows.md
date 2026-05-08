# IGetModelWindows Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFrame~IGetModelWindows`

Gets the child model windows for this frame.
Gets the child model windows for this frame.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IGetModelWindows( _
   ByVal ModelWindowCount As System.Integer _
) As ModelWindow
```

```

Dim instance As IFrame
Dim ModelWindowCount As System.Integer
Dim value As ModelWindow
 
value = instance.IGetModelWindows(ModelWindowCount)
```

```

ModelWindow IGetModelWindows( 
   System.int ModelWindowCount
)
```

```

ModelWindow^ IGetModelWindows( 
   System.int ModelWindowCount
) 
```

#### Parameters

*ModelWindowCount*
:   Number of child windows for this frame

#### Return Value

- in-process, unmanaged C++: Pointer to an array of [model windows](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelWindow.md)

- VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

Remarks

Call [IFrame::GetModelWindowCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFrame~GetModelWindowCount.md) before calling this method to get the size of the array.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IFrame Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFrame.md)  
[IFrame Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFrame_members.md)  
[IFrame::GetHWnd Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFrame~GetHWnd.md)  
[IFrame::GetHWndx64 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFrame~GetHWndx64.md)  
[IFrame::ShowModelWindow Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFrame~ShowModelWindow.md)  
[IFrame::ModelWindows Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFrame~ModelWindows.md)
