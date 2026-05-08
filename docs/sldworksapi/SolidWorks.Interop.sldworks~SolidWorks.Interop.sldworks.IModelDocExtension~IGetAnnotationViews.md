# IGetAnnotationViews Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~IGetAnnotationViews`

Gets the annotation views in this part or assembly document.
Gets the annotation views in this part or assembly document.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IGetAnnotationViews( _
   ByVal AnnotationViewCount As System.Integer _
) As AnnotationView
```

```

Dim instance As IModelDocExtension
Dim AnnotationViewCount As System.Integer
Dim value As AnnotationView
 
value = instance.IGetAnnotationViews(AnnotationViewCount)
```

```

AnnotationView IGetAnnotationViews( 
   System.int AnnotationViewCount
)
```

```

AnnotationView^ IGetAnnotationViews( 
   System.int AnnotationViewCount
) 
```

#### Parameters

*AnnotationViewCount*
:   Number of annotation views in this part or assembly document

#### Return Value

- in-process, unmanaged C++: Pointer to an array of [annotation views](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotationView.md)

- VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

Remarks

Before calling this method, call [IModelDocExtension::AnnotationViewCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~AnnotationViewCount.md) to get the value of AnnotationViewCount.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.md)  
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.md)  
[IModelDocExtension::AnnotationViews Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~AnnotationViews.md)
