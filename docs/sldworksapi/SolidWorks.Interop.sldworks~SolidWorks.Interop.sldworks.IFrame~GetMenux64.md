# GetMenux64 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFrame~GetMenux64`

Gets the menu handle for the main frame in 64-bit applications.
Gets the menu handle for the main frame in 64-bit applications.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetMenux64() As System.Long
```

```

Dim instance As IFrame
Dim value As System.Long
 
value = instance.GetMenux64()
```

```

System.long GetMenux64()
```

```

System.int64 GetMenux64(); 
```

#### Return Value

Menu handle for the main frame

Remarks

This method is only available through early binding and with 64-bit versions of the SOLIDWORKS software.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IFrame Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFrame.md)  
[IFrame Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFrame_members.md)  
[IFrame::GetMenu Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFrame~GetMenu.md)  
[IFrame::GetHWndx64 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFrame~GetHWndx64.md)  
[IFrame::GetHWnd Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFrame~GetHWnd.md)
