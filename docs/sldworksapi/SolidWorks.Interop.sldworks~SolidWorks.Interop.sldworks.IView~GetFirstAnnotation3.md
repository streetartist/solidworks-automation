# GetFirstAnnotation3 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetFirstAnnotation3`

Gets the first annotation in this drawing view.
Gets the first annotation in this drawing view.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetFirstAnnotation3() As Annotation
```

```

Dim instance As IView
Dim value As Annotation
 
value = instance.GetFirstAnnotation3()
```

```

Annotation GetFirstAnnotation3()
```

```

Annotation^ GetFirstAnnotation3(); 
```

#### Return Value

First [annotation](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation.md) in the drawing view

Remarks

This method gets any display dimension, including suppressed, hidden, or dangling dimensions on the sheet and on the sheet format if it is visible. The sheet must be visible. See [ISheet::SheetFormatVisible](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet~SheetFormatVisible.md).

A dimension becomes suppressed or hidden when you specifically select a dimension and hide it or when you select a feature and say hide all dimensions. If you need to filter out these dimensions, you must use [IAnnotation::Visible](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~Visible.md) to check that status.

If the annotation is on a layer that is not shown, the annotation is still returned.

To get the next annotation, call [IAnnotation::GetNext3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~GetNext3.md).

Example

[Get Display Dimensions, GTols, and Surface-finish Symbols (VBA)](Get_Display_Dimensions,_Gtols,_and_Surface-Finish_Symbols_Example_VB.htm)  
[Get Entities Attached to Cosmetic Thread (VBA)](Get_Entities_Attached_To_Cosmetic_Thread_Example_VB.htm)  
[Show Dimensions in Drawing Sheet (VBA)](Show_Dimensions_in_Drawing_Sheet_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.md)  
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.md)  
[IView::GetAnnotations Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetAnnotations.md)  
[IView::IGetAnnotations Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetAnnotations.md)  
[IView::GetAnnotationCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetAnnotationCount.md)  
[IAnnotation::GetNext3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~GetNext3.md)  
[IView::GetAnnotationsByType Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetAnnotationsByType.md)
