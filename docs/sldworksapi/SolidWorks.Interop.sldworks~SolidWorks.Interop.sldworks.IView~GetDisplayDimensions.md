# GetDisplayDimensions Method (IView)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetDisplayDimensions`

Gets all of the display dimension on this drawing view.
Gets all of the display dimension on this drawing view.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetDisplayDimensions() As System.Object
```

```

Dim instance As IView
Dim value As System.Object
 
value = instance.GetDisplayDimensions()
```

```

System.object GetDisplayDimensions()
```

```

System.Object^ GetDisplayDimensions(); 
```

#### Return Value

Array of [display dimensions](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension.md)

Remarks

Use this method to obtain the array of display dimensions all at once instead of calling [IView::GetFirstDisplayDimension5](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetFirstDisplayDimension5.md) and then repeatedly calling [IDisplayDimension::GetNext5](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~GetNext5.md) to obtain the remaining display dimensions on this drawing view.

**NOTE:** Display dimensions are not the same as [actual model dimensions](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension.md).

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
[IView::GetDisplayDimensionCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetDisplayDimensionCount.md)  
[IView::IGetDisplayDimensions Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetDisplayDimensions.md)
