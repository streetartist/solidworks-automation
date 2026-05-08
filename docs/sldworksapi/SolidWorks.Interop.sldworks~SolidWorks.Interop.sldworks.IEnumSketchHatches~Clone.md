# Clone Method (IEnumSketchHatches)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnumSketchHatches~Clone`

Clones the sketch hatches enumeration.
Clones the sketch hatches enumeration.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub Clone( _
   ByRef Ppenum As EnumSketchHatches _
) 
```

```

Dim instance As IEnumSketchHatches
Dim Ppenum As EnumSketchHatches
 
instance.Clone(Ppenum)
```

```

void Clone( 
   out EnumSketchHatches Ppenum
)
```

```

void Clone( 
   [Out] EnumSketchHatches^ Ppenum
) 
```

#### Parameters

*Ppenum*
:   Pointer to the cloned sketch hatches enumeration

Remarks

For use in in-process DLLs only.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IEnumSketchHatches Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnumSketchHatches.md)  
[IEnumSketchHatches Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnumSketchHatches_members.md)
