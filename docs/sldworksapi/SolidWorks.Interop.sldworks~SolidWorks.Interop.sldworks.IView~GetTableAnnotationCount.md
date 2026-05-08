# GetTableAnnotationCount Method (IView)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetTableAnnotationCount`

Gets the number of table annotations in this drawing view.
Gets the number of table annotations in this drawing view.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetTableAnnotationCount() As System.Integer
```

```

Dim instance As IView
Dim value As System.Integer
 
value = instance.GetTableAnnotationCount()
```

```

System.int GetTableAnnotationCount()
```

```

System.int GetTableAnnotationCount(); 
```

#### Return Value

Total number of table annotations on this drawing view

Remarks

Call this method before calling [IView::IGetTableAnnotations](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetTableAnnotations.md) to determine the size of the array for that method.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.md)  
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.md)  
[IView::GetTableAnnotations Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetTableAnnotations.md)
