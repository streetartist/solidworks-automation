# SketchFillet2 Method (IModelDoc)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc~SketchFillet2`

Obsolete. Superseded by IModelDoc2::SketchFillet2.
Obsolete. Superseded by [IModelDoc2::SketchFillet2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~SketchFillet2.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function SketchFillet2( _
   ByVal Rad As System.Double, _
   ByVal ConstrainedCorners As System.Short _
) As System.Boolean
```

```

Dim instance As IModelDoc
Dim Rad As System.Double
Dim ConstrainedCorners As System.Short
Dim value As System.Boolean
 
value = instance.SketchFillet2(Rad, ConstrainedCorners)
```

```

System.bool SketchFillet2( 
   System.double Rad,
   System.short ConstrainedCorners
)
```

```

System.bool SketchFillet2( 
   System.double Rad,
   System.short ConstrainedCorners
) 
```

#### Parameters

*Rad*

*ConstrainedCorners*

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc.md)  
[IModelDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc_members.md)
