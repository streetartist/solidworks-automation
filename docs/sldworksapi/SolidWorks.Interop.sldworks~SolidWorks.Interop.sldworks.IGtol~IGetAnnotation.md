# IGetAnnotation Method (IGtol)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~IGetAnnotation`

Gets the annotation for this specific GTol.
Gets the annotation for this specific GTol.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IGetAnnotation() As Annotation
```

```

Dim instance As IGtol
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

Pointer to the [IAnnotation](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation.md) object

Remarks

The IAnnotation object is a higher-level object that contains methods that are available to all types of annotations.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IGtol Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol.md)  
[IGtol Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol_members.md)  
[IGtol::GetAnnotation Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~GetAnnotation.md)
