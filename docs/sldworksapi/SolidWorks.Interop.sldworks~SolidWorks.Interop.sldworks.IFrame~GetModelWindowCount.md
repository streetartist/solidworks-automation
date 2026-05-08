# GetModelWindowCount Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFrame~GetModelWindowCount`

Gets the number of child model windows for this frame.
Gets the number of child model windows for this frame.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetModelWindowCount() As System.Integer
```

```

Dim instance As IFrame
Dim value As System.Integer
 
value = instance.GetModelWindowCount()
```

```

System.int GetModelWindowCount()
```

```

System.int GetModelWindowCount(); 
```

#### Return Value

Number of child model windows for this frame

Remarks

Call this method before calling [IFrame::IGetModelWindows](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFrame~IGetModelWindows.md) to get the size of the array.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IFrame Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFrame.md)  
[IFrame Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFrame_members.md)  
[IFrame::GetHWnd Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFrame~GetHWnd.md)  
[IFrame::GetHWndx64 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFrame~GetHWndx64.md)  
[IFrame::RemoveMenu Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFrame~RemoveMenu.md)  
[IFrame::RenameMenu Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFrame~RenameMenu.md)  
[IFrame::ShowModelWindow Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFrame~ShowModelWindow.md)  
[IFrame::ModelWindows Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFrame~ModelWindows.md)
