# AttachAnnotation Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~AttachAnnotation`

Attaches an existing annotation to a drawing sheet or view.
Attaches an existing annotation to a drawing sheet or view.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function AttachAnnotation( _
   ByVal Option As System.Integer _
) As System.Boolean
```

```

Dim instance As IDrawingDoc
Dim Option As System.Integer
Dim value As System.Boolean
 
value = instance.AttachAnnotation(Option)
```

```

System.bool AttachAnnotation( 
   System.int Option
)
```

```

System.bool AttachAnnotation( 
   System.int Option
) 
```

#### Parameters

*Option*
:   Annotation attachment option as defined in [swAttachAnnotationOption\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swAttachAnnotationOption_e.html)

#### Return Value

True if attachment is successful, false if not

Remarks

To attach an annotation to a drawing view:

1. Multi-select the annotation and drawing view.
2. Call this method with Option set to swAttachAnnotationOption\_e.swAttachAnnotationOption\_View.

To attach an annotation to a drawing sheet:

1. Select the annotation.
2. Call this method with Option set to swAttachAnnotationOption\_e.swAttachAnnotationOption\_Sheet.

Example

[Attach Annotation (VBA)](Attach_Annotation_Example_VB.htm)  
[Attach Annotation (VB.NET)](Attach_Annotation_Example_VBNET.htm)  
[Attach Annotation (C#)](Attach_Annotation_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDrawingDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc.md)  
[IDrawingDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc_members.md)  
[IDrawingDoc::InsertModelAnnotations3 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~InsertModelAnnotations3.md)
