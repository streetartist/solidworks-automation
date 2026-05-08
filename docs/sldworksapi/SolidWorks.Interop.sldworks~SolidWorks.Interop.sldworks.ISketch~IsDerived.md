# IsDerived Method (ISketch)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~IsDerived`

Gets whether a sketch is derived.
Gets whether a sketch is derived.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IsDerived() As System.Boolean
```

```

Dim instance As ISketch
Dim value As System.Boolean
 
value = instance.IsDerived()
```

```

System.bool IsDerived()
```

```

System.bool IsDerived(); 
```

#### Return Value

True if the sketch is derived, false if not

Example

[Create Derived or Underived Sketch (VB.NET)](Create_Derived_or_Underived_Sketch_Example_VBNET.htm)  
[Create Derived or Underived Sketch (VBA)](Create_Derived_or_Underived_Sketch_Example_VB.htm)  
[Create Derived or Underived Sketch (C#)](Create_Derived_or_Underived_Sketch_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISketch Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch.md)  
[ISketch Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch_members.md)  
[IModelDoc2::DeriveSketch Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~DeriveSketch.md)  
[IModelDoc2::UnderiveSketch Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~UnderiveSketch.md)
