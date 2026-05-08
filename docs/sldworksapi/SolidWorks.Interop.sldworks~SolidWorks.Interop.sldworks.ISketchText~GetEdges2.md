# GetEdges2 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchText~GetEdges2`

Gets the edges for this sketch text.
Gets the edges for this sketch text.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetEdges2() As System.Object
```

```

Dim instance As ISketchText
Dim value As System.Object
 
value = instance.GetEdges2()
```

```

System.object GetEdges2()
```

```

System.Object^ GetEdges2(); 
```

#### Return Value

Array of [edges](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge.md)

Remarks

The difference between this method and the now obsolete ISketchText::GetEdges is this method also gets the edges of sketch text rendered with "stick" or single line fonts such as OLF SimpleSansOC.

The edges returned by this method are transient and should be regarded as read only. They can be used to obtain the underlying [ICurve](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve.md) objects, but should not be used for manipulation or to obtain any other objects. These pointers should not be saved; if they are needed again, they should be obtained at that time.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISketchText Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchText.md)  
[ISketchText Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchText_members.md)  
[ISketchText::EnumEdges Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchText~EnumEdges.md)
