# GetFirstTableAnnotation2 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetFirstTableAnnotation2`

Gets the first table annotation in this view.
Gets the first table annotation in this view.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetFirstTableAnnotation2() As System.Object
```

```

Dim instance As IView
Dim value As System.Object
 
value = instance.GetFirstTableAnnotation2()
```

```

System.object GetFirstTableAnnotation2()
```

```

System.Object^ GetFirstTableAnnotation2(); 
```

#### Return Value

First [table annotation](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation.md)

Remarks

This method obsoletes IView::GetFirstTableAnnotation by supporting inactive sheets.

Example

[Get Table Annotation and Contents (VBA)](Get_Table_Annotation_and_Contents_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.md)  
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.md)  
[IView::GetTableAnnotations Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetTableAnnotations.md)  
[ITableAnnotation::GetNext Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~GetNext.md)
