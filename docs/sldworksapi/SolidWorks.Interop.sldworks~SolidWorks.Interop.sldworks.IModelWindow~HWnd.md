# HWnd Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelWindow~HWnd`

Gets the handle to this model window.
Gets the handle to this model window.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

ReadOnly Property HWnd As System.Integer
```

```

Dim instance As IModelWindow
Dim value As System.Integer
 
value = instance.HWnd
```

```

System.int HWnd {get;}
```

```

property System.int HWnd {
   System.int get();
}
```

#### Property Value

Handle for this model window

Remarks

If your application must be x64 compatible, then use [IModelWindow::HWndx64](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelWindow~HWndx64.md).

Example

[Switch Documents (C#)](Switch_Documents_Example_CSharp.htm)  
[Switch Documents (VB.NET)](Switch_Documents_Example_VBNET.htm)  
[Switch Documents (VBA)](Switch_Documents_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelWindow Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelWindow.md)  
[IModelWindow Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelWindow_members.md)
