# Select2 Method (IAnnotation)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~Select2`

Obsolete. Superseded by IAnnotation::Select3.
Obsolete. Superseded by [IAnnotation::Select3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~Select3.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function Select2( _
   ByVal Append As System.Boolean, _
   ByVal Mark As System.Integer _
) As System.Boolean
```

```

Dim instance As IAnnotation
Dim Append As System.Boolean
Dim Mark As System.Integer
Dim value As System.Boolean
 
value = instance.Select2(Append, Mark)
```

```

System.bool Select2( 
   System.bool Append,
   System.int Mark
)
```

```

System.bool Select2( 
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

[IAnnotation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation.md)  
[IAnnotation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation_members.md)
