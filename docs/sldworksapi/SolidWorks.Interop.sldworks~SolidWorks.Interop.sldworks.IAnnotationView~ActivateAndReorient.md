# ActivateAndReorient Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotationView~ActivateAndReorient`

Activates and reorients this annotation view.
Activates and reorients this annotation view.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function ActivateAndReorient() As System.Boolean
```

```

Dim instance As IAnnotationView
Dim value As System.Boolean
 
value = instance.ActivateAndReorient()
```

```

System.bool ActivateAndReorient()
```

```

System.bool ActivateAndReorient(); 
```

#### Return Value

True if the annotation view is activated and reoriented, false if not

Remarks

The annotation view is oriented normal to its plane.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IAnnotationView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotationView.md)  
[IAnnotationView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotationView_members.md)  
[IAnnotationView::Activate Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotationView~Activate.md)  
[IAnnotationView::Orient Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotationView~Orient.md)  
[IAnnotationView::Hide Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotationView~Hide.md)  
[IAnnotationView::Show Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotationView~Show.md)
