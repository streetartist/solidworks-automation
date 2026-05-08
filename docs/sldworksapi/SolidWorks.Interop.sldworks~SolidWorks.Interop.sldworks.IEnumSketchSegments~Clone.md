# Clone Method (IEnumSketchSegments)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnumSketchSegments~Clone`

Clones the sketch segments enumeration.
Clones the sketch segments enumeration.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub Clone( _
   ByRef Ppenum As EnumSketchSegments _
) 
```

```

Dim instance As IEnumSketchSegments
Dim Ppenum As EnumSketchSegments
 
instance.Clone(Ppenum)
```

```

void Clone( 
   out EnumSketchSegments Ppenum
)
```

```

void Clone( 
   [Out] EnumSketchSegments^ Ppenum
) 
```

#### Parameters

*Ppenum*
:   Pointer to the cloned [sketch segments enumeration](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnumSketchSegments.md)

Remarks

For use in in-process DLLs only.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IEnumSketchSegments Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnumSketchSegments.md)  
[IEnumSketchSegments Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnumSketchSegments_members.md)
