# IGetAnnotations Method (IModelDocExtension)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~IGetAnnotations`

Gets the annotations on this model.
Gets the annotations on this model.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IGetAnnotations( _
   ByVal NumAnnotations As System.Integer _
) As Annotation
```

```

Dim instance As IModelDocExtension
Dim NumAnnotations As System.Integer
Dim value As Annotation
 
value = instance.IGetAnnotations(NumAnnotations)
```

```

Annotation IGetAnnotations( 
   System.int NumAnnotations
)
```

```

Annotation^ IGetAnnotations( 
   System.int NumAnnotations
) 
```

#### Parameters

*NumAnnotations*
:   Number of annotations

#### Return Value

- in-process, unmanaged C++: Pointer to an array of [annotations](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation.md)

- VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

Remarks

Call [IModelDocExtension::GetAnnotationCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetAnnotations.md) before calling this method.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.md)  
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.md)  
[IModelDocExtension::GetAnnotations Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetAnnotations.md)
