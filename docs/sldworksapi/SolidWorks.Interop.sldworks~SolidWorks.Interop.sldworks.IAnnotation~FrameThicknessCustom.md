# FrameThicknessCustom Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~FrameThicknessCustom`

Gets or sets the frame's line thickness for this annotation.
Gets or sets the frame's line thickness for this annotation.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property FrameThicknessCustom As System.Double
```

```

Dim instance As IAnnotation
Dim value As System.Double
 
instance.FrameThicknessCustom = value
 
value = instance.FrameThicknessCustom
```

```

System.double FrameThicknessCustom {get; set;}
```

```

property System.double FrameThicknessCustom {
   System.double get();
   void set (    System.double value);
}
```

#### Property Value

Value of frame's line thickness

Remarks

[IAnnotation::UseDocDispFrame](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~UseDocDispFrame.md) must be false for this property to have any effect.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IAnnotation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation.md)  
[IAnnotation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation_members.md)  
[IAnnotation::FrameLineStyle Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~FrameLineStyle.md)  
[IAnnotation::FrameThickness Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~FrameThickness.md)
