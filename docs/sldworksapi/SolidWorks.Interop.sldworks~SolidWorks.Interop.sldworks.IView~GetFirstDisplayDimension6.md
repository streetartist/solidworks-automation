# GetFirstDisplayDimension6 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetFirstDisplayDimension6`

Gets the first display dimension in this drawing view.
Gets the first display dimension in this drawing view.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetFirstDisplayDimension6() As System.Object
```

```

Dim instance As IView
Dim value As System.Object
 
value = instance.GetFirstDisplayDimension6()
```

```

System.object GetFirstDisplayDimension6()
```

```

System.Object^ GetFirstDisplayDimension6(); 
```

Remarks

This method obsoletes IView::GetFirstDisplayDimension5 by supporting inactive sheets.

A SOLIDWORKS dimension can be displayed more than once. For example, the base-extrude dimension could be brought into three different views on a drawing. These three dimensions are referred to as display dimensions and are represented by the [IDisplayDimension](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension.md) object in the SOLIDWORKS API. The original base-extrude dimension is represented by the [IDimension](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension.md) object in the SOLIDWORKS API.

This method displays:

- dimensions on both the sheet and sheet format.
- suppressed dimensions.

Call [IDisplayDimension::GetNext5](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~GetNext5.md) to get the next display dimension on this drawing sheet.

Do not use [IAnnotation::Visible](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~Visible.md) property to modify this method's return value.

Example

[Get Dimension Values in Drawing (VBA)](Get_Dimension_Values_in_Drawing_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.md)  
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.md)  
[IView::GetDimensionCount4 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetDimensionCount4.md)  
[IView::GetDimensionDisplayInfo5 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetDimensionDisplayInfo5.md)  
[IView::GetDimensionDisplayInfoSize2 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetDimensionDisplayInfoSize2.md)  
[IView::GetDimensionDisplayString5 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetDimensionDisplayString5.md)  
[IView::GetDimensionIds4 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetDimensionIds4.md)  
[IView::GetDimensionInfo7 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetDimensionInfo7.md)  
[IView::GetDimensionString4 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetDimensionString4.md)  
[IView::GetDisplayDimensions Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetDisplayDimensions.md)  
[IView::ProjectedDimensions Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~ProjectedDimensions.md)
