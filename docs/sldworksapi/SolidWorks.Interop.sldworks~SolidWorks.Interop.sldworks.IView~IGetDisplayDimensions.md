# IGetDisplayDimensions Method (IView)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetDisplayDimensions`

Gets all of the display dimensions on this drawing view.
Gets all of the display dimensions on this drawing view.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IGetDisplayDimensions( _
   ByVal NumDisplayDim As System.Integer _
) As DisplayDimension
```

```

Dim instance As IView
Dim NumDisplayDim As System.Integer
Dim value As DisplayDimension
 
value = instance.IGetDisplayDimensions(NumDisplayDim)
```

```

DisplayDimension IGetDisplayDimensions( 
   System.int NumDisplayDim
)
```

```

DisplayDimension^ IGetDisplayDimensions( 
   System.int NumDisplayDim
) 
```

#### Parameters

*NumDisplayDim*
:   Total number of display dimensions on this drawing view

#### Return Value

- in-process, unmanaged C++: Pointer to an array of [display dimensions](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension.md)
- VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_methods.htm) for details about this type of method.

Remarks

Use this method to obtain the array of display dimensions all at once instead of calling [IView::GetFirstDisplayDimension5](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetFirstDisplayDimension5.md) and then repeatedly calling [IDisplayDimension::GetNext5](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~GetNext5.md) to obtain the remaining display dimensions on this drawing view.

Before calling this method, call [IView::GetDisplayDimensionCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetDisplayDimensionCount.md) to get the value for numDisplayDim.

**NOTE:** Display dimensions are not the same as [actual model dimensions](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension.md).

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.md)  
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.md)  
[IView::GetDisplayDimensions Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetDisplayDimensions.md)
