# GetTemporaryAxes Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetTemporaryAxes`

Gets the information of the temporary axes displayed in this view.
Gets the information of the temporary axes displayed in this view.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetTemporaryAxes() As System.Object
```

```

Dim instance As IView
Dim value As System.Object
 
value = instance.GetTemporaryAxes()
```

```

System.object GetTemporaryAxes()
```

```

System.Object^ GetTemporaryAxes(); 
```

#### Return Value

Array of double of the information about the temporary axes in this view (see **Remarks**)

Remarks

This array contains the start and end points, in that order, of temporary axes.

Example

[Get Temporary Axes in Each Drawing View (VBA)](Get_Temporary_Axes_in_Each_Drawing_View_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.md)  
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.md)  
[IView::GetTemporaryAxesCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetTemporaryAxesCount.md)  
[IView::IGetTemporaryAxes Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetTemporaryAxes.md)
