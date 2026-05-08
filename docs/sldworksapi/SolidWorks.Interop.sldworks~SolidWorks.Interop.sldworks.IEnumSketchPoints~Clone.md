# Clone Method (IEnumSketchPoints)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnumSketchPoints~Clone`

Clones the sketch points enumeration.
Clones the sketch points enumeration.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub Clone( _
   ByRef Ppenum As EnumSketchPoints _
) 
```

```

Dim instance As IEnumSketchPoints
Dim Ppenum As EnumSketchPoints
 
instance.Clone(Ppenum)
```

```

void Clone( 
   out EnumSketchPoints Ppenum
)
```

```

void Clone( 
   [Out] EnumSketchPoints^ Ppenum
) 
```

#### Parameters

*Ppenum*
:   Pointer to the cloned [sketch points enumeration](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnumSketchPoints.md)

Remarks

For use in in-process DLLs only.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IEnumSketchPoints Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnumSketchPoints.md)  
[IEnumSketchPoints Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnumSketchPoints_members.md)
