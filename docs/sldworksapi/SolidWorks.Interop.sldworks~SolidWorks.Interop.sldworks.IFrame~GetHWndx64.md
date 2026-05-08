# GetHWndx64 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFrame~GetHWndx64`

Gets the window handle for the main frame in 64-bit applications.
Gets the window handle for the main frame in 64-bit applications.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetHWndx64() As System.Long
```

```

Dim instance As IFrame
Dim value As System.Long
 
value = instance.GetHWndx64()
```

```

System.long GetHWndx64()
```

```

System.int64 GetHWndx64(); 
```

#### Return Value

Window handle

Remarks

This method is only available through early binding and with 64-bit versions of the SOLIDWORKS software.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IFrame Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFrame.md)  
[IFrame Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFrame_members.md)  
[IFrame::GetHWnd Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFrame~GetHWnd.md)  
[IFrame::GetModelWindowCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFrame~GetModelWindowCount.md)  
[IFrame::IGetModelWindows Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFrame~IGetModelWindows.md)  
[IFrame::ShowModelWindow Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFrame~ShowModelWindow.md)  
[IFrame::ModelWindows Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFrame~ModelWindows.md)
