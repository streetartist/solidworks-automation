# Next Method (IEnumDisplayDimensions)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnumDisplayDimensions~Next`

Gets the next display dimension in the display dimensions enumeration.
Gets the next display dimension in the display dimensions enumeration.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub Next( _
   ByVal Celt As System.Integer, _
   ByRef Rgelt As DisplayDimension, _
   ByRef PceltFetched As System.Integer _
) 
```

```

Dim instance As IEnumDisplayDimensions
Dim Celt As System.Integer
Dim Rgelt As DisplayDimension
Dim PceltFetched As System.Integer
 
instance.Next(Celt, Rgelt, PceltFetched)
```

```

void Next( 
   System.int Celt,
   out DisplayDimension Rgelt,
   out System.int PceltFetched
)
```

```

void Next( 
   System.int Celt,
   [Out] DisplayDimension^ Rgelt,
   [Out] System.int PceltFetched
) 
```

#### Parameters

*Celt*
:   Number of display dimensions for the display dimension enumeration

*Rgelt*
:   Pointer to an array of [display dimensions](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension.md) in of size Celt

*PceltFetched*
:   Pointer to the number of display dimensions from the list; this value can be less than Celt if you ask for more display dimensions than exist, or it can be NULL if no more display dimensions exist

Remarks

For use in in-process DLLs only.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IEnumDisplayDimensions Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnumDisplayDimensions.md)  
[IEnumDisplayDimensions Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnumDisplayDimensions_members.md)
