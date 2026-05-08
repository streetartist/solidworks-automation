# GetGTolCount Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetGTolCount`

Gets the number of geometric tolerances in this drawing view.
Gets the number of geometric tolerances in this drawing view.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetGTolCount() As System.Integer
```

```

Dim instance As IView
Dim value As System.Integer
 
value = instance.GetGTolCount()
```

```

System.int GetGTolCount()
```

```

System.int GetGTolCount(); 
```

#### Return Value

Number of geometric tolerances

Remarks

Call this method before calling [IView::IGetGTols](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetGTols.md) to determine the size of the array for that method.

Example

[Get Annotations Arrays (C#)](Get_Annotations_Arrays_Example_CSharp.htm)  
[Get Annotations Arrays (VB.NET)](Get_Annotations_Arrays_Example_VBNET.htm)  
[Get Annotations Arrays (VBA)](Get_Annotations_Array_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.md)  
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.md)  
[IView::GetGTols Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetGTols.md)
