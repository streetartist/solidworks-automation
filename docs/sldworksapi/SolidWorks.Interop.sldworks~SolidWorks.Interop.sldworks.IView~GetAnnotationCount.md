# GetAnnotationCount Method (IView)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetAnnotationCount`

Gets the number of annotations in this view.
Gets the number of annotations in this view.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetAnnotationCount() As System.Integer
```

```

Dim instance As IView
Dim value As System.Integer
 
value = instance.GetAnnotationCount()
```

```

System.int GetAnnotationCount()
```

```

System.int GetAnnotationCount(); 
```

#### Return Value

Number of annotations

Remarks

Call this method before [IView::GetAnnotations](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetAnnotations.md) to determine the size of the array for that method.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.md)  
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.md)  
[IView::GetAnnotations Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetAnnotations.md)
