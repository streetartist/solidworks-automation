# Next Method (IEnumSketchHatches)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnumSketchHatches~Next`

Gets the next sketch hatch in the sketch hatch enumeration.
Gets the next sketch hatch in the sketch hatch enumeration.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub Next( _
   ByVal Celt As System.Integer, _
   ByRef Rgelt As SketchHatch, _
   ByRef PceltFetched As System.Integer _
) 
```

```

Dim instance As IEnumSketchHatches
Dim Celt As System.Integer
Dim Rgelt As SketchHatch
Dim PceltFetched As System.Integer
 
instance.Next(Celt, Rgelt, PceltFetched)
```

```

void Next( 
   System.int Celt,
   out SketchHatch Rgelt,
   out System.int PceltFetched
)
```

```

void Next( 
   System.int Celt,
   [Out] SketchHatch^ Rgelt,
   [Out] System.int PceltFetched
) 
```

#### Parameters

*Celt*
:   Number of sketch hatches for this sketch hatch enumeration

*Rgelt*
:   Pointer to an array of [sketch hatches](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchHatch.md) of size Celt

*PceltFetched*
:   Pointer to the number of sketch hatches returned from the list; this value can be less than celt if you ask for more SketchHatch objects than exist, or it can be NULL if no more SketchHatch objects exist

Remarks

For use in in-process DLLs only.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IEnumSketchHatches Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnumSketchHatches.md)  
[IEnumSketchHatches Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnumSketchHatches_members.md)
