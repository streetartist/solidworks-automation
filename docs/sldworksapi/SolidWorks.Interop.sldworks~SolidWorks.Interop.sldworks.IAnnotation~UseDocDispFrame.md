# UseDocDispFrame Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~UseDocDispFrame`

Gets or sets whether to use the document's frame's line style and thickness or a specified line style and thickness for this annotation.
Gets or sets whether to use the document's frame's line style and thickness or a specified line style and thickness for this annotation.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property UseDocDispFrame As System.Boolean
```

```

Dim instance As IAnnotation
Dim value As System.Boolean
 
instance.UseDocDispFrame = value
 
value = instance.UseDocDispFrame
```

```

System.bool UseDocDispFrame {get; set;}
```

```

property System.bool UseDocDispFrame {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True to use the document's frame's line style and thickness, false to use a specified line style and thickness

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IAnnotation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation.md)  
[IAnnotation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation_members.md)  
[IAnnotation::FrameLineStyle Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~FrameLineStyle.md)  
[IAnnotation::FrameThickness Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~FrameThickness.md)  
[IAnnotation::FrameThicknessCustom Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~FrameThicknessCustom.md)
