# Next Method (IEnumBodies2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnumBodies2~Next`

Gets the next body in the bodies enumeration.
Gets the next body in the bodies enumeration.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub Next( _
   ByVal Celt As System.Integer, _
   ByRef Rgelt As Body2, _
   ByRef PceltFetched As System.Integer _
) 
```

```

Dim instance As IEnumBodies2
Dim Celt As System.Integer
Dim Rgelt As Body2
Dim PceltFetched As System.Integer
 
instance.Next(Celt, Rgelt, PceltFetched)
```

```

void Next( 
   System.int Celt,
   out Body2 Rgelt,
   out System.int PceltFetched
)
```

```

void Next( 
   System.int Celt,
   [Out] Body2^ Rgelt,
   [Out] System.int PceltFetched
) 
```

#### Parameters

*Celt*
:   Number of bodies for the bodies enumeration

*Rgelt*
:   Pointer to an array of [bodies](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.md) of size Celt

*PceltFetched*
:   Pointer to the number of bodies returned from the list; this value can be less than Celt if you request more bodies than exist, or it can be NULL if no more bodies exist

Remarks

For use in in-process DLLs only.

Example

[Enumerate Bodies (C++)](Enumerate_Bodies_Example_CPlusPlus_COM.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IEnumBodies2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnumBodies2.md)  
[IEnumBodies2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnumBodies2_members.md)
