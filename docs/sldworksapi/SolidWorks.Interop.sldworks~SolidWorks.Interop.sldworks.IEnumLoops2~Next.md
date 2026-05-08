# Next Method (IEnumLoops2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnumLoops2~Next`

Gets the next loop in the loops enumeration.
Gets the next loop in the loops enumeration.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub Next( _
   ByVal Celt As System.Integer, _
   ByRef Rgelt As Loop2, _
   ByRef PceltFetched As System.Integer _
) 
```

```

Dim instance As IEnumLoops2
Dim Celt As System.Integer
Dim Rgelt As Loop2
Dim PceltFetched As System.Integer
 
instance.Next(Celt, Rgelt, PceltFetched)
```

```

void Next( 
   System.int Celt,
   out Loop2 Rgelt,
   out System.int PceltFetched
)
```

```

void Next( 
   System.int Celt,
   [Out] Loop2^ Rgelt,
   [Out] System.int PceltFetched
) 
```

#### Parameters

*Celt*
:   Number of loops for the loops enumeration

*Rgelt*
:   Pointer to an array of [loops](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoop2.md) of size Celt

*PceltFetched*
:   Pointer to the number of loops returned from the list; this value can be less than celt if you ask for more loops than exist, or it can be NULL if no more loops exist

Remarks

For use in in-process DLLs only.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IEnumLoops2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnumLoops2.md)  
[IEnumLoops2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnumLoops2_members.md)
