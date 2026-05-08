# IGetTableAnnotations Method (IView)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetTableAnnotations`

Gets all of the table annotations in this drawing view.
Gets all of the table annotations in this drawing view.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IGetTableAnnotations( _
   ByVal NumTableAnnotation As System.Integer _
) As TableAnnotation
```

```

Dim instance As IView
Dim NumTableAnnotation As System.Integer
Dim value As TableAnnotation
 
value = instance.IGetTableAnnotations(NumTableAnnotation)
```

```

TableAnnotation IGetTableAnnotations( 
   System.int NumTableAnnotation
)
```

```

TableAnnotation^ IGetTableAnnotations( 
   System.int NumTableAnnotation
) 
```

#### Parameters

*NumTableAnnotation*
:   Total number of table annotations in this drawing view

#### Return Value

- in-process, unmanaged C++: Pointer to an array of [table annotations](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation.md)
- VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_methods.htm) for details about this type of method.

Remarks

Use this method to obtain the array of table annotations all at once instead of calling [IView::GetFirstTableAnnotation](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetFirstTableAnnotation.md) and then repeatedly calling [ITableAnnotation::GetNext](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~GetNext.md) to obtain the table annotations in the drawing view.

Before calling this method, call [IView::GetTableAnnotationCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetTableAnnotationCount.md) to get the value for numTableAnnotations.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.md)  
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.md)  
[IView::GetTableAnnotations Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetTableAnnotations.md)
