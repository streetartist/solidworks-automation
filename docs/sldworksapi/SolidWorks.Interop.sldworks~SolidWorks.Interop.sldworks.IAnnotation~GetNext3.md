# GetNext3 Method (IAnnotation)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~GetNext3`

Gets the next annotation.
Gets the next annotation.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetNext3() As Annotation
```

```

Dim instance As IAnnotation
Dim value As Annotation
 
value = instance.GetNext3()
```

```

Annotation GetNext3()
```

```

Annotation^ GetNext3(); 
```

#### Return Value

[IAnnotation](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation.md)

Remarks

This method:

- retrieves all display dimensions, including suppressed, hidden, and dangling dimensions, on the sheet and on the sheet format if it is visible. See [ISheet::SheetFormatVisible](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet~SheetFormatVisible.md) for details.
- retrieves all instances of a dimension. For example, if a (4X) instance dimension is visible in the user interface, this method gets the 4X dimension and each of its four dimension instances.
- retrieves an annotation, even if it is on a layer that is not displayed.

A dimension is suppressed or hidden when you:

- specifically select a dimension and hide it.  
    
  - or -
- select a feature and hide all dimensions.

If you need to filter out suppressed or hidden dimensions, use [IAnnotation::Visible](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~Visible.md) to check the visibility status.

To get the first annotation on the sheet, call [IView::GetFirstAnnotation3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetFirstAnnotation3.md) before calling this method.

Example

[Get Display Dimensions, GTols, and Surface-finish Symbols (VBA)](Get_Display_Dimensions,_Gtols,_and_Surface-Finish_Symbols_Example_VB.htm)  
[Get Entities Attached to Cosmetic Thread (VBA)](Get_Entities_Attached_To_Cosmetic_Thread_Example_VB.htm)  
[Show Dimensions in Drawing Sheet (VBA)](Show_Dimensions_in_Drawing_Sheet_Example_VB.htm)  
[Get DimXpert Display Dimensions and Feature (C#)](Get_DimXpert_Display_Dimensions_and_Feature_Example_CSharp.htm)  
[Get DimXpert Display Dimensions and Feature (VB.NET)](Get_DimXpert_Display_Dimensions_and_Feature_Example_VBNET.htm)  
[Get DimXpert Display Dimensions and Feature (VBA)](Get_DimXpert_Display_Dimensions_and_Feature_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IAnnotation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation.md)  
[IAnnotation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation_members.md)  
[IView::GetFirstAnnotation3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetFirstAnnotation3.md)
