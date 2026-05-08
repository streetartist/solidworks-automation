# IGetAnnotation Method (INote)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~IGetAnnotation`

Gets the annotation for this specific note.
Gets the annotation for this specific note.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IGetAnnotation() As Annotation
```

```

Dim instance As INote
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

This method obtains the owning [IAnnotation](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation.md) object for this [INote](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote.md) object. The IAnnotation object is a higher-level object that contains methods that are general to all types of annotations.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[INote Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote.md)  
[INote Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote_members.md)  
[INote::GetAnnotation Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~GetAnnotation.md)
