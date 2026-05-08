# Next Method (IEnumSketchSegments)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnumSketchSegments~Next`

Gets the next sketch segment in the sketch segments enumeration.
Gets the next sketch segment in the sketch segments enumeration.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub Next( _
   ByVal Celt As System.Integer, _
   ByRef Rgelt As SketchSegment, _
   ByRef PceltFetched As System.Integer _
) 
```

```

Dim instance As IEnumSketchSegments
Dim Celt As System.Integer
Dim Rgelt As SketchSegment
Dim PceltFetched As System.Integer
 
instance.Next(Celt, Rgelt, PceltFetched)
```

```

void Next( 
   System.int Celt,
   out SketchSegment Rgelt,
   out System.int PceltFetched
)
```

```

void Next( 
   System.int Celt,
   [Out] SketchSegment^ Rgelt,
   [Out] System.int PceltFetched
) 
```

#### Parameters

*Celt*
:   Number of sketch segments for the sketch segments enumeration

*Rgelt*
:   Pointer to an array of [sketch segments](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSegment.md) of size Celt

*PceltFetched*
:   Pointer to the number of sketch segments returned from the list;  this value can be less than celt if you ask for more sketch segments than exist, or it can be NULL if no more sketch segments exist

Remarks

For use in in-process DLLs only.

Example

[Select All Sketch Segments (C++)](Select_All_Sketch_Segments_Example_CPlusPlus_COM.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IEnumSketchSegments Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnumSketchSegments.md)  
[IEnumSketchSegments Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnumSketchSegments_members.md)
