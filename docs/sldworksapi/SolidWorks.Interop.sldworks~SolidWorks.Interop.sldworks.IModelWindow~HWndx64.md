# HWndx64 Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelWindow~HWndx64`

Gets the handle to this model window in 64-bit applications.
Gets the handle to this model window in 64-bit applications.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

ReadOnly Property HWndx64 As System.Long
```

```

Dim instance As IModelWindow
Dim value As System.Long
 
value = instance.HWndx64
```

```

System.long HWndx64 {get;}
```

```

property System.int64 HWndx64 {
   System.int64 get();
}
```

#### Property Value

Handle for this model window

Remarks

This property is only available through early binding and with 64-bit versions of the SOLIDWORKS software.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelWindow Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelWindow.md)  
[IModelWindow Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelWindow_members.md)  
[IModelWindow::HWnd Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelWindow~HWnd.md)
