# GetAnnotationsByType Method (IModelDocExtension)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetAnnotationsByType`

Gets the annotations of the specified type in this document.
Gets the annotations of the specified type in this document.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetAnnotationsByType( _
   ByVal Type As System.Integer _
) As System.Object
```

```

Dim instance As IModelDocExtension
Dim Type As System.Integer
Dim value As System.Object
 
value = instance.GetAnnotationsByType(Type)
```

```

System.object GetAnnotationsByType( 
   System.int Type
)
```

```

System.Object^ GetAnnotationsByType( 
   System.int Type
) 
```

#### Parameters

*Type*
:   Annotation type as defined by [swAnnotationType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swAnnotationType_e.html) (see **Remarks**)

#### Return Value

Array of [annotations](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation.md)

Remarks

This method does not support swAnnotationType\_e.swCThread for parts and assemblies, because in those models cosmetic threads are added as sub-features of holes, not annotations.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.md)  
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.md)  
[IModelDocExtension::GetAnnotations Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetAnnotations.md)  
[IModelDocExtension::GetAnnotationCount Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetAnnotationCount.md)  
[IView::GetAnnotationsByType Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetAnnotationsByType.md)
