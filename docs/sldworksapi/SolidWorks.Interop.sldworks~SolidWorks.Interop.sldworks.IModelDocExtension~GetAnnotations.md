# GetAnnotations Method (IModelDocExtension)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetAnnotations`

Gets the annotations on this part.
Gets the annotations on this part.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetAnnotations() As System.Object
```

```

Dim instance As IModelDocExtension
Dim value As System.Object
 
value = instance.GetAnnotations()
```

```

System.object GetAnnotations()
```

```

System.Object^ GetAnnotations(); 
```

#### Return Value

Array of [annotations](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation.md)

Remarks

Example

[Get Annotations (VBA)](Get_Annotations_Example_VB.htm)  
[Get Annotations (VB.NET)](Get_Annotations_Example_VBNET.htm)  
[Get Annotations (C#)](Get_Annotations_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.md)  
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.md)  
[IModelDocExtension::GetAnnotationCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetAnnotationCount.md)  
[IModelDocExtension::IGetAnnotations Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~IGetAnnotations.md)  
[IView::GetAnnotations Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetAnnotations.md)  
[IModelDocExtension::GetAnnotationsByType Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetAnnotationsByType.md)
