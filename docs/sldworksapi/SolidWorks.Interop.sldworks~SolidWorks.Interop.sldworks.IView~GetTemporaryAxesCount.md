# GetTemporaryAxesCount Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetTemporaryAxesCount`

Gets the number of temporary axes in this view.
Gets the number of temporary axes in this view.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetTemporaryAxesCount() As System.Integer
```

```

Dim instance As IView
Dim value As System.Integer
 
value = instance.GetTemporaryAxesCount()
```

```

System.int GetTemporaryAxesCount()
```

```

System.int GetTemporaryAxesCount(); 
```

#### Return Value

Number of temporary axes in this view

Remarks

Call this method before calling [IView::IGetTemporaryAxes](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetTemporaryAxes.md) to get the size of the array for that method.

Example

[Get Temporary Axes in Each Drawing View (VBA)](Get_Temporary_Axes_in_Each_Drawing_View_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.md)  
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.md)
