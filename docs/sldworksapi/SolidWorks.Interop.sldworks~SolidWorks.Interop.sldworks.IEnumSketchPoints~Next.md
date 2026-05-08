# Next Method (IEnumSketchPoints)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnumSketchPoints~Next`

Gets the next sketch point in the sketch points enumeration.
Gets the next sketch point in the sketch points enumeration.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub Next( _
   ByVal Celt As System.Integer, _
   ByRef Rgelt As SketchPoint, _
   ByRef PceltFetched As System.Integer _
) 
```

```

Dim instance As IEnumSketchPoints
Dim Celt As System.Integer
Dim Rgelt As SketchPoint
Dim PceltFetched As System.Integer
 
instance.Next(Celt, Rgelt, PceltFetched)
```

```

void Next( 
   System.int Celt,
   out SketchPoint Rgelt,
   out System.int PceltFetched
)
```

```

void Next( 
   System.int Celt,
   [Out] SketchPoint^ Rgelt,
   [Out] System.int PceltFetched
) 
```

#### Parameters

*Celt*
:   Number of sketch points for the sketch points enumeration

*Rgelt*
:   Pointer to an array of [sketch points](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPoint.md) of size Celt

*PceltFetched*
:   Pointer to the number of sketch points returned from the list; this value can be less than celt if you ask for more sketch points than exist, or it can be NULL if no more sketch points exist

Remarks

For use in in-process DLLs only.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IEnumSketchPoints Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnumSketchPoints.md)  
[IEnumSketchPoints Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnumSketchPoints_members.md)
