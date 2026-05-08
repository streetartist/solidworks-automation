# Visible Property (IAnnotation)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~Visible`

Gets or sets the visibility state of this annotation.
Gets or sets the visibility state of this annotation.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property Visible As System.Integer
```

```

Dim instance As IAnnotation
Dim value As System.Integer
 
instance.Visible = value
 
value = instance.Visible
```

```

System.int Visible {get; set;}
```

```

property System.int Visible {
   System.int get();
   void set (    System.int value);
}
```

#### Property Value

Visibility state as defined in [swAnnotationVisibilityState\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swAnnotationVisibilityState_e.html)

Remarks

There are several reasons why an annotation might or might not be visible on the screen.

This property determines whether an annotation has been individually displayed or hidden if you selected and specifically hid the annotation or if you selected and specifically hid the dimensions of a feature. This property cannot determine whether an annotation is hidden if it is on a layer that is hidden (all annotations of this type are hidden) or if the feature that owns it is suppressed. Therefore, even though this method indicates that an annotation is visible, it might not necessarily be visible on the screen.

If an annotation's visibility is set to swAnnotationHalfHidden, then that annotation is in a half-hidden state, which is not a permanent state. For example, during a **Hide/Show Annotations** operation in a drawing, a half-hidden annotation is displayed in gray if the interactive user selects to show all annotations. Any annotation set to swAnnotationHalfHidden is hidden when the interactive user finishes using **Hide/Show Annotations**.

When you use this property to change the visibility of an annotation, you also cause changes to the visible model. To see those changes, redraw the graphics window using [IModelDoc2::GraphicsRedraw2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~GraphicsRedraw2.md).

Example

[Get Patterned Cosmetic Thread Annotations Data (C#)](Get_Patterned_Cosmetic_Thread_Annotations_Data_Example_CSharp.htm)  
[Get Patterned Cosmetic Thread Annotations Data (VB.NET)](Get_Patterned_Cosmetic_Thread_Annotations_Data_Example_VBNET.htm)  
[Get Patterned Cosmetic Thread Annotations Data (VBA)](Get_Patterned_Cosmetic_Thread_Annotations_Data_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IAnnotation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation.md)  
[IAnnotation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation_members.md)
