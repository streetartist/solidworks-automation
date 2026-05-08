# GetEllipseCount Method (IView)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetEllipseCount`

Gets the number of ellipses in the view.
Gets the number of ellipses in the view.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetEllipseCount() As System.Integer
```

```

Dim instance As IView
Dim value As System.Integer
 
value = instance.GetEllipseCount()
```

```

System.int GetEllipseCount()
```

```

System.int GetEllipseCount(); 
```

#### Return Value

Number of ellipses in the view

Remarks

Call this method before calling [IView::IGetEllipses5](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetEllipses5.md) to get the size of the array for that method.

Example

[Get Polylines Information (VBA)](Get_Polylines_Information_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.md)  
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.md)
