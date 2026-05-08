# GetDisplayDimensionCount Method (IView)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetDisplayDimensionCount`

Gets the number of display dimensions in this drawing view.
Gets the number of display dimensions in this drawing view.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetDisplayDimensionCount() As System.Integer
```

```

Dim instance As IView
Dim value As System.Integer
 
value = instance.GetDisplayDimensionCount()
```

```

System.int GetDisplayDimensionCount()
```

```

System.int GetDisplayDimensionCount(); 
```

#### Return Value

Number of display dimensions

Remarks

Call this method before calling [IView::IGetDisplayDimensions](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetDisplayDimensions.md) to determine the size of the array for that method.

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
[IView::GetDisplayDimensions Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetDisplayDimensions.md)
