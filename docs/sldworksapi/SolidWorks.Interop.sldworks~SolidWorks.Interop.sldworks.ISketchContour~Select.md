# Select Method (ISketchContour)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchContour~Select`

Obsolete. Superseded by ISketchContour::Select2.
Obsolete. Superseded by [ISketchContour::Select2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchContour~Select2.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function Select( _
   ByVal Append As System.Boolean, _
   ByVal Mark As System.Integer _
) As System.Boolean
```

```

Dim instance As ISketchContour
Dim Append As System.Boolean
Dim Mark As System.Integer
Dim value As System.Boolean
 
value = instance.Select(Append, Mark)
```

```

System.bool Select( 
   System.bool Append,
   System.int Mark
)
```

```

System.bool Select( 
   System.bool Append,
   System.int Mark
) 
```

#### Parameters

*Append*

*Mark*

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISketchContour Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchContour.md)  
[ISketchContour Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchContour_members.md)
