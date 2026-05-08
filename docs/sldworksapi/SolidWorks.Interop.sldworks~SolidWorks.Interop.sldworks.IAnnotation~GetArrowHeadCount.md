# GetArrowHeadCount Method (IAnnotation)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~GetArrowHeadCount`

Gets the number of arrowheads on this symbol.
Gets the number of arrowheads on this symbol.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetArrowHeadCount() As System.Integer
```

```

Dim instance As IAnnotation
Dim value As System.Integer
 
value = instance.GetArrowHeadCount()
```

```

System.int GetArrowHeadCount()
```

```

System.int GetArrowHeadCount(); 
```

#### Return Value

Number of arrowheads on this annotation

Remarks

This method works with traditional leaders on annotations and [multijog leaders](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMultiJogLeader.md).

Call this method before calling [IAnnotation::GetArrowHeadSizeAtIndex](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~GetArrowHeadSizeAtIndex.md) to specify the annotation for which to get the arrow head size.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IAnnotation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation.md)  
[IAnnotation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation_members.md)  
[IAnnotation::SetArrowHeadSizeAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~SetArrowHeadSizeAtIndex.md)  
[IAnnotation::GetArrowHeadStyleAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~GetArrowHeadStyleAtIndex.md)  
[IAnnotation::SetArrowHeadStyleAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~SetArrowHeadStyleAtIndex.md)
