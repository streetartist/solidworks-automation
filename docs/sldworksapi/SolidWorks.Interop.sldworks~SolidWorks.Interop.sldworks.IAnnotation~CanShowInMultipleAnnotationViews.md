# CanShowInMultipleAnnotationViews Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~CanShowInMultipleAnnotationViews`

Gets whether this annotation can be shown in multiple annotation views.
Gets whether this annotation can be shown in multiple [annotation views.](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotationView.md)

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function CanShowInMultipleAnnotationViews() As System.Boolean
```

```

Dim instance As IAnnotation
Dim value As System.Boolean
 
value = instance.CanShowInMultipleAnnotationViews()
```

```

System.bool CanShowInMultipleAnnotationViews()
```

```

System.bool CanShowInMultipleAnnotationViews(); 
```

#### Return Value

True if this annotation can be shown in multiple annotation views, false if not

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
[IAnnotation::CanShowInAnnotationView Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~CanShowInAnnotationView.md)  
[IAnnotationView::Hide Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotationView~Hide.md)  
[IAnnotationView::IsShown Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotationView~IsShown.md)  
[IAnnotationView::Show Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotationView~Show.md)
