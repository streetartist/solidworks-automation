# UnassignedView Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotationView~UnassignedView`

Gets whether this annotation view is assigned to a 3D View.
Gets whether this annotation view is assigned to a 3D View.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

ReadOnly Property UnassignedView As System.Boolean
```

```

Dim instance As IAnnotationView
Dim value As System.Boolean
 
value = instance.UnassignedView
```

```

System.bool UnassignedView {get;}
```

```

property System.bool UnassignedView {
   System.bool get();
}
```

#### Property Value

True if this annotation view is not assigned to a 3D View, false if it is

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
[IView3D Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView3D.md)  
[IAnnotationView::FlatPatternView Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotationView~FlatPatternView.md)
