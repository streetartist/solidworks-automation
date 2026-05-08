# GetDetailCircleCount2 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetDetailCircleCount2`

Gets the number of detail circles in the drawing view.
Gets the number of detail circles in the drawing view.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetDetailCircleCount2( _
   ByRef Size As System.Integer _
) As System.Integer
```

```

Dim instance As IView
Dim Size As System.Integer
Dim value As System.Integer
 
value = instance.GetDetailCircleCount2(Size)
```

```

System.int GetDetailCircleCount2( 
   out System.int Size
)
```

```

System.int GetDetailCircleCount2( 
   [Out] System.int Size
) 
```

#### Parameters

*Size*
:   Size, which includes a double for each detail circle; this new double contains the layer ID for the detail circle

#### Return Value

Number of detail circles in the drawing view

Remarks

Call this method before calling [IView::GetDetailCircles](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetDetailCircles.md) to get the size of the array for that method.

Example

[Get Detail Circle Information (VBA)](Get_Detail_Circle_Information_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.md)  
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.md)  
[IView::IGetDetail Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetDetail.md)  
[IView::IGetDetailCircleInfo2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetDetailCircleInfo2.md)  
[IView::IGetDetailCircleStrings Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetDetailCircleStrings.md)  
[IView::GetDetail Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetDetail.md)  
[IView::GetDetailCircleInfo2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetDetailCircleInfo2.md)  
[IView::GetDetailCircleStrings Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetDetailCircleStrings.md)  
[IView::GetDetailCircles Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetDetailCircles.md)
