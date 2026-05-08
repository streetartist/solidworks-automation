# GetGTols Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetGTols`

Gets all of the geometric tolerances on this drawing view.
Gets all of the geometric tolerances on this drawing view.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetGTols() As System.Object
```

```

Dim instance As IView
Dim value As System.Object
 
value = instance.GetGTols()
```

```

System.object GetGTols()
```

```

System.Object^ GetGTols(); 
```

#### Return Value

Array of [geometric tolerances](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol.md)

Remarks

Use this method to obtain the array of geometric tolerances all at once instead of calling [IView::GetFirstGTOL](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetFirstGTOL.md) and then repeatedly calling [IGtol::GetNextGTOL](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~GetNextGTOL.md) to obtain the remaining geometric tolerances in the drawing view.

Example

[Get Annotations Arrays (VBA)](Get_Annotations_Array_Example_VB.htm)  
[Get Annotations Arrays (VB.NET)](Get_Annotations_Arrays_Example_VBNET.htm)  
[Get Annotations Arrays (C#)](Get_Annotations_Arrays_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.md)  
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.md)  
[IView::GetGTolCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetGTolCount.md)  
[IView::IGetGTols Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetGTols.md)
