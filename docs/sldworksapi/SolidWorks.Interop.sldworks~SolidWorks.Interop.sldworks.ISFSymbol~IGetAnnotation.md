# IGetAnnotation Method (ISFSymbol)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISFSymbol~IGetAnnotation`

Gets the annotation for this surface finish symbol.
Gets the annotation for this surface finish symbol.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IGetAnnotation() As Annotation
```

```

Dim instance As ISFSymbol
Dim value As Annotation
 
value = instance.IGetAnnotation()
```

```

Annotation IGetAnnotation()
```

```

Annotation^ IGetAnnotation(); 
```

#### Return Value

[Annotation](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation.md)

Remarks

This method gets the owning [IAnnotation](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation.md) object, which is a higher-level object that contains methods that are general to all types of annotations.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISFSymbol Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISFSymbol.md)  
[ISFSymbol Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISFSymbol_members.md)  
[ISFSymbol::GetAnnotation Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISFSymbol~GetAnnotation.md)
