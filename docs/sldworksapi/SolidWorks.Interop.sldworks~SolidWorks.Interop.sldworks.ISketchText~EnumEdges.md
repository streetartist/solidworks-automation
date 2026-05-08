# EnumEdges Method (ISketchText)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchText~EnumEdges`

Gets the edges in this sketch text.
Gets the edges in this sketch text.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function EnumEdges() As EnumEdges
```

```

Dim instance As ISketchText
Dim value As EnumEdges
 
value = instance.EnumEdges()
```

```

EnumEdges EnumEdges()
```

```

EnumEdges^ EnumEdges(); 
```

#### Return Value

[Edges enumeration](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnumEdges.md)

Remarks

The edges returned by this method are transient and should be regarded as read only. They can be used to obtain the underlying [ICurve](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve.md) objects, but should not be used for manipulation or to obtain any other objects through them. These pointers should not be saved; if they are needed again, they should be obtained at that time.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISketchText Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchText.md)  
[ISketchText Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchText_members.md)  
[ISketchText::GetEdges Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchText~GetEdges.md)
