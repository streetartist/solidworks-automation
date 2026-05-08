# CanShowInAnnotationView Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~CanShowInAnnotationView`

Gets whether this annotation can be shown in the specified annotation view.
Gets whether this annotation can be shown in the specified [annotation view](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotationView.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function CanShowInAnnotationView( _
   ByVal AnnotationViewName As System.String _
) As System.Boolean
```

```

Dim instance As IAnnotation
Dim AnnotationViewName As System.String
Dim value As System.Boolean
 
value = instance.CanShowInAnnotationView(AnnotationViewName)
```

```

System.bool CanShowInAnnotationView( 
   System.string AnnotationViewName
)
```

```

System.bool CanShowInAnnotationView( 
   System.String^ AnnotationViewName
) 
```

#### Parameters

*AnnotationViewName*
:   Name of annotation view in which to show this annotation (see **Remarks**)

#### Return Value

True if this annotation can be shown in the specified annotation view, false if not

Remarks

Use [IFeature::Name](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~Name.md) to get the name of the annotation view. See the examples for details.

Example

[Get Where Annotations Can Be Shown (C#)](Get_Where_Annotations_Can_Be_Shown_Example_CSharp.htm)  
[Get Where Annotations Can Be Shown (VB.NET)](Get_Where_Annotations_Can_Be_Shown_Example_VBNET.htm)  
[Get Where Annotations Can Be Shown (VBA)](Get_Where_Annotations_Can_Be_Shown_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IAnnotation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation.md)  
[IAnnotation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation_members.md)  
[IAnnotation::CanShowInMultipleAnnotationViews Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~CanShowInMultipleAnnotationViews.md)  
[IAnnotationView::Hide Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotationView~Hide.md)  
[IAnnotationView::IsShown Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotationView~IsShown.md)  
[IAnnotationView::Show Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotationView~Show.md)
