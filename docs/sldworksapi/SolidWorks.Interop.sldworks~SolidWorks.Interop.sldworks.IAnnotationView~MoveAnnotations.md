# MoveAnnotations Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotationView~MoveAnnotations`

Moves the specified annotations to this annotation view.
Moves the specified annotations to this annotation view.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function MoveAnnotations( _
   ByVal AnnotationsToMove As System.Object _
) As System.Boolean
```

```

Dim instance As IAnnotationView
Dim AnnotationsToMove As System.Object
Dim value As System.Boolean
 
value = instance.MoveAnnotations(AnnotationsToMove)
```

```

System.bool MoveAnnotations( 
   System.object AnnotationsToMove
)
```

```

System.bool MoveAnnotations( 
   System.Object^ AnnotationsToMove
) 
```

#### Parameters

*AnnotationsToMove*
:   Annotations to move

#### Return Value

True if the specified annotations are moved, false if not

Example

[Move Annotations to Notes Area Annotation View (C#)](Move_Annotations_to_First_Annotation_View_Example_CSharp.htm)  
[Move Annotations to Notes Area Annotation View (VB.NET)](Move_Annotations_to_First_Annotation_View_Example_VBNET.htm)  
[Move Annotations to Notes Area Annotation View (VBA)](Move_Annotations_to_First_Annotation_View_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IAnnotationView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotationView.md)  
[IAnnotationView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotationView_members.md)
