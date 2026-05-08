# FrameLineStyle Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~FrameLineStyle`

Gets or sets the frame's line style for this annotation.
Gets or sets the frame's line style for this annotation.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property FrameLineStyle As System.Integer
```

```

Dim instance As IAnnotation
Dim value As System.Integer
 
instance.FrameLineStyle = value
 
value = instance.FrameLineStyle
```

```

System.int FrameLineStyle {get; set;}
```

```

property System.int FrameLineStyle {
   System.int get();
   void set (    System.int value);
}
```

#### Property Value

Frame's line style as defined by [swLineStyles\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swLineStyles_e.html)

Remarks

[IAnnotation::UseDocDispFrame](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~UseDocDispFrame.md) must be false for this property to have any effect.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IAnnotation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation.md)  
[IAnnotation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation_members.md)  
[IAnnotation::FrameThickness Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~FrameThickness.md)  
[IAnnotation::FrameThicknessCustom Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~FrameThicknessCustom.md)
